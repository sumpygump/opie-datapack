"""Make the json files for wood_cutter recipes from which to which"""

import json

TARGET_DIR = "data/opie/recipe/crafting_shapeless"
ADVANCEMENT_DIR = "data/opie/advancement/recipes/decoration"

colors = [
    "white",
    "light_gray",
    "gray",
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "lime",
    "green",
    "cyan",
    "light_blue",
    "blue",
    "purple",
    "magenta",
    "pink",
]


def make_recipe(
    namespace,
    full_from,
    full_to,
    input_count=1,
    yield_count=1,
    from_tag=False,
    group=None,
):
    """Make a recipe file"""

    if from_tag:
        from_key = "tag"
    else:
        from_key = "item"

    recipe = {
        "type": "minecraft:crafting_shapeless",
        "ingredients": [
            {from_key: f"{namespace}:{full_from}"} for i in range(0, input_count)
        ],
        "result": {"count": yield_count, "id": f"{namespace}:{full_to}"},
    }

    if group:
        recipe["group"] = group

    filename = f"{TARGET_DIR}/{full_to}_from_{full_from}.json"
    print(filename)
    with open(filename, "w", encoding="utf-8") as f_d:
        json.dump(recipe, f_d, indent=2)


def make_recipe_advancement(full_from, full_to):
    """Make the recipe advancement"""
    obj = {
        "parent": "minecraft:recipes/root",
        "criteria": {
            f"has_{full_from}": {
                "conditions": {"items": [{"items": [f"minecraft:{full_from}"]}]},
                "trigger": "minecraft:inventory_changed",
            },
            "has_the_recipe": {
                "conditions": {
                    "recipe": f"opie:crafting_shapeless/{full_to}_from_{full_from}"
                },
                "trigger": "minecraft:recipe_unlocked",
            },
        },
        "requirements": [[f"has_{full_from}", "has_the_recipe"]],
        "rewards": {"recipes": [f"opie:crafting_shapeless/{full_to}_from_{full_from}"]},
    }
    filename = f"{ADVANCEMENT_DIR}/{full_to}_from_{full_from}.json"
    with open(filename, "w", encoding="utf-8") as f_d:
        json.dump(obj, f_d, indent=2)


def make_wool_recipe(color):
    """Make the recipe for wool from carpet"""
    make_recipe(
        "minecraft",
        f"{color}_carpet",
        f"{color}_wool",
        input_count=3,
        yield_count=2,
        group="wool",
    )


def make_wool_recipe_advancement(color):
    """Make the wool recipe advancement"""
    make_recipe_advancement(f"{color}_carpet", f"{color}_wool")


def make_string_recipe():
    """Make the recipe for string from wool"""

    make_recipe(
        "minecraft", "wool", "string", input_count=1, yield_count=4, from_tag=True
    )


def main():
    """Main function to generate the recipes"""
    for color in colors:
        # Three carpets of each color makes 2 wool of that color
        make_wool_recipe(color)
        make_wool_recipe_advancement(color)

    # One wool of any color makes 4 string
    make_string_recipe()


if __name__ == "__main__":
    main()
