"""Make the json files for wood_cutter recipes from which to which"""

import json

TARGET_DIR = "data/opie/recipes/crafting_shapeless"

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
    namespace, full_from, full_to, input_count=1, yield_count=1, from_tag=False
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
        "result": {"count": yield_count, "item": f"{namespace}:{full_to}"},
    }
    filename = f"{TARGET_DIR}/{full_to}_from_{full_from}.json"
    print(filename)
    with open(filename, "w", encoding="utf-8") as f_d:
        json.dump(recipe, f_d, indent=2)


def make_wool_recipe(color):
    """Make the recipe for wool from carpet"""
    make_recipe(
        "minecraft", f"{color}_carpet", f"{color}_wool", input_count=3, yield_count=2
    )


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

    # One wool of any color makes 4 string
    make_string_recipe()


if __name__ == "__main__":
    main()
