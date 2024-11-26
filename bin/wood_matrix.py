"""Make the json files for wood_cutter recipes from which to which"""

import json

TARGET_DIR = "data/opie/recipe/wood_cutter"

wood_types = [
    "acacia",
    "bamboo",
    "birch",
    "cherry",
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
        "hanging_sign",
        "trapdoor",
    ],
    "stairs": ["planks", "slab"],
    "slab": ["planks", "stairs"],
}

log_types = {
    "acacia",
    "birch",
    "cherry",
    "dark_oak",
    "jungle",
    "mangrove",
    "oak",
    "spruce",
}

to_sticks = [
    "boats",
    "hanging_signs",
    "planks",
    "signs",
    "wooden_buttons",
    "wooden_doors",
    ("opie", "wooden_fence_gates"),
    "wooden_fences",
    "wooden_pressure_plates",
    "wooden_slabs",
    "wooden_stairs",
    "wooden_trapdoors",
]


def make_wood_recipe(wood_type, from_, to_, count=1, from_tag=False):
    """Make a recipe file"""
    make_recipe(
        "minecraft",
        f"{wood_type}_{from_}",
        f"{wood_type}_{to_}",
        count=count,
        from_tag=from_tag,
    )


def make_stick_recipe(wood_type, from_, count=2, from_tag=False):
    """Make a recipe file"""
    make_recipe("minecraft", f"{wood_type}_{from_}", "stick", count, from_tag=from_tag)


def make_recipe(namespace, full_from, full_to, count=1, from_tag=False):
    """Make a recipe file"""

    if full_to in ["crimson_boat", "warped_boat"]:
        # These don't exist
        return

    if full_to == "bamboo_boat":
        full_to = "bamboo_raft"

    if from_tag:
        from_key = "tag"
    else:
        from_key = "item"

    recipe = {
        "type": "minecraft:stonecutting",
        "ingredient": {from_key: f"{namespace}:{full_from}"},
        "result": {
            "id": f"minecraft:{full_to}",
            "count": count,
        },
    }
    filename = f"{TARGET_DIR}/{full_to}_from_{full_from}.json"
    print(filename)
    with open(filename, "w", encoding="utf-8") as f_d:
        json.dump(recipe, f_d, indent=2)


def main():
    """Main function to generate recipes for all types and items"""
    for wood_type in wood_types:
        for from_, to_items in item_map.items():
            for item in to_items:
                make_wood_recipe(wood_type, from_, item)

    # Make stick recipes for this wood type
    for item in to_sticks:
        namespace = "minecraft"
        if isinstance(item, tuple):
            namespace, item = item
        make_recipe(namespace, item, "stick", count=2, from_tag=True)

    # Make wood recipes for each log type
    for wood_type in log_types:
        make_wood_recipe(wood_type, "logs", "planks", count=4, from_tag=True)
        make_stick_recipe(wood_type, "logs", count=8, from_tag=True)

    # Make sticks from ladders
    make_recipe("minecraft", "ladder", "stick", count=6)


if __name__ == "__main__":
    main()
