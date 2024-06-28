from maps import BIOMES
from map_prob import MAP_PROBS

def check_for_state_names():
    biomes = set(BIOMES)
    map_biomes = set(MAP_PROBS.keys())
    map_biomes.add("END") #since END is a special case
    assert biomes == map_biomes, f"Biomes in maps.py and map_prob.py do not match. {biomes.difference(map_biomes)}"
    print("Biomes match")

def check_for_state_weight_counts():
    num_weights_1 = 0
    num_weights_half = 0
    num_weights_third = 0
    num_weights_quarter = 0

    for biome in MAP_PROBS:
        for connection in MAP_PROBS[biome]:
            if MAP_PROBS[biome][connection] == 1:
                num_weights_1 += 1
            elif MAP_PROBS[biome][connection] == 0.5:
                num_weights_half += 1
            elif MAP_PROBS[biome][connection] == 0.25:
                num_weights_quarter += 1
            elif MAP_PROBS[biome][connection] == 1/3:
                num_weights_third += 1
            else:
                print("ERROR")
    print("Number of weights of 1: ", num_weights_1)
    print("Number of weights of 0.5: ", num_weights_half)
    print("Number of weights of 0.25: ", num_weights_quarter)
    print("Number of weights of 1/3: ", num_weights_third)

    assert num_weights_half == 1, f"Number of weights of 0.5 is {num_weights_half}, should be 1"
    assert num_weights_quarter == 4, f"Number of weights of 0.25 is {num_weights_quarter}, should be 4"
    assert num_weights_third == 5, f"Number of weights of 1/3 is {num_weights_third}, should be 5"

def check_destination_names():
    for biome, dest in MAP_PROBS.items():
        for destination in dest:
            assert destination in BIOMES, f"Destination {destination} in {biome} not in BIOMES"
    print("All destinations are in BIOMES")


if __name__ == '__main__':
    check_for_state_names()
    check_for_state_weight_counts()
    check_destination_names()
    print("All checks passed")