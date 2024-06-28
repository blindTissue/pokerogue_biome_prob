MAP_PROBS = {
    "TOWN": {
        "PLAINS": 1
    },
    "PLAINS": {
        "GRASS": 1,
        "METROPOLIS": 1,
        "LAKE": 1
    },
    "GRASS": {
        "TALL_GRASS": 1
    },
    "TALL_GRASS": {
        "FOREST": 1,
        "CAVE": 1,
    },
    "METROPOLIS": {
        "SLUM": 1,
    },
    "FOREST": {
        "MEADOW": 1,
        "JUNGLE": 1,
    },
    "SEA": {
        "SEABED": 1,
        "ICE_CAVE": 1
    },
    "SWAMP": {
        "TALL_GRASS": 1,
        "GRAVEYARD": 1
    },
    "BEACH": {
        "SEA": 1,
        "ISLAND": 0.25
    },
    "LAKE": {
        "BEACH": 1,
        "SWAMP": 1,
        "CONSTRUCTION_SITE": 1
    },
    "SEABED": {
        "CAVE": 1,
        "VOLCANO": 1/4
    },
    "MOUNTAIN": {
        "VOLCANO": 1,
        "WASTELAND": 1/3
    },
    "BADLANDS": {
        "MOUNTAIN": 1,
        "DESERT": 1
    },
    "CAVE": {
        "LAKE": 1,
        "BADLANDS": 1
    },
    "DESERT": {
        "RUINS": 1,
    },
    "ICE_CAVE": {
        "SNOWY_FOREST": 1
    },
    "MEADOW": {
        "PLAINS": 1,
        "FAIRY_CAVE": .5
    },
    "POWER_PLANT": {
        "FACTORY": 1
    },
    "VOLCANO": {
        "BEACH": 1,
        "ICE_CAVE": 1/4
    },
    "GRAVEYARD": {
        "ABYSS": 1
    },
    "DOJO": {
        "PLAINS": 1,
        "TEMPLE": 1/3
    },
    "FACTORY": {
        "PLAINS": 1,
        "LABORATORY": 0.25
    },
    "RUINS": {
        "FOREST": 1,
    },
    "WASTELAND": {
        "BADLANDS": 1,
    },
    "ABYSS": {
        "CAVE": 1,
        "SPACE": 1/3,
        "WASTELAND": 1/3
    },
    "SPACE": {
        "RUINS": 1
    },
    "CONSTRUCTION_SITE": {
        "POWER_PLANT": 1,
        "DOJO": 1
    },
    "JUNGLE": {
        "TEMPLE": 1
    },
    "FAIRY_CAVE": {
        "ICE_CAVE": 1,
        "SPACE": 1/3
    },
    "TEMPLE": {
        "SWAMP": 1,
        "RUINS": 1
    },
    "SLUM": {
        "CONSTRUCTION_SITE": 1
    },
    "SNOWY_FOREST": {
        "LAKE": 1
    },
    "ISLAND": {
        "SEA": 1
    },
    "LABORATORY": {
        "CONSTRUCTION_SITE": 1
    },
}

