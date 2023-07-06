"""Make the json files from which to which"""

import json

wood_types = [
    "acacia",
    "birch",
    "crimson",
    "dark_oak",
    "jungle",
    "mangrove",
    "oak",
    "spruce",
    "warped",
]

item_map = {
    "planks": [
        "stairs",
        "slab",
        "boat",
        "button",
        "door",
        "fence",
        "fence_gate",
        "pressure_plate",
        "sign",
        "trapdoor",
    ],
    "stairs": ["planks", "slab"],
    "slab": ["planks", "stairs"],
}

log_types = {
    "acacia",
    "birch",
    "dark_oak",
    "jungle",
    "mangrove",
    "oak",
    "spruce",
}

to_sticks = [
    "boat",
    "button",
    "door",
    "fence",
    "fence_gate",
    "planks",
    "pressure_plate",
    "sign",
    "slab",
    "stairs",
    "trapdoor",
]


def make_wood_recipe(wood_type, from_, to, count=1):
    """Make a recipe file"""
    make_recipe(
        "minecraft",
        "{}_{}".format(wood_type, from_),
        "{}_{}".format(wood_type, to),
        count=count,
    )


def make_stick_recipe(wood_type, from_, count=2):
    """Make a recipe file"""
    make_recipe("minecraft", "{}_{}".format(wood_type, from_), "stick", count)


def make_recipe(namespace, full_from, full_to, count=1):
    """Make a recipe file"""

    if full_to in ["crimson_boat", "warped_boat"]:
        # These don't exist
        return

    recipe = {
        "type": "minecraft:stonecutting",
        "count": count,
        "ingredient": {"item": "{}:{}".format(namespace, full_from)},
        "result": "{}:{}".format(namespace, full_to),
    }
    filename = "{}_from_{}.json".format(full_to, full_from)
    print(filename)
    with open(filename, "w", encoding="utf-8") as f_d:
        json.dump(recipe, f_d, indent=2)


def main():
    """Main function to generate recipes for all types and items"""
    for wood_type in wood_types:
        for from_, to_items in item_map.items():
            for item in to_items:
                make_wood_recipe(wood_type, from_, item)
        for item in to_sticks:
            make_stick_recipe(wood_type, item)
    for wood_type in log_types:
        make_wood_recipe(wood_type, "log", "planks", count=4)
        make_stick_recipe(wood_type, "log", count=8)


if __name__ == "__main__":
    main()
