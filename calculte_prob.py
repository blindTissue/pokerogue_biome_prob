from map_prob import MAP_PROBS
from maps import BIOMES
import numpy as np
import itertools

BIOMES.remove("END")  # removed END biome since it is a special case


def get_combination_list(biomes: list):
    tot_len = len(biomes)
    out_list = []
    for i in range(1, tot_len + 1):
        out_list += list(itertools.combinations(biomes, i))
    return out_list


def calculate_transition_probabilities(transitions: dict) -> dict:

    biomes = list(transitions.keys())
    combination_list = get_combination_list(biomes)

    transition_probabilities = {}
    for biome in biomes:
        transition_probabilities[biome] = 0

    for combination in combination_list:
        init_prob = 1
        for next_biome, weight in transitions.items():
            if next_biome in combination:
                init_prob *= weight
            else:
                init_prob *= 1 - weight
        for biome in combination:
            transition_probabilities[biome] += init_prob / len(combination)

    eps = 1e-6
    assert abs(sum(transition_probabilities.values()) - 1) < eps, f"Sum of probabilities is not 1. Sum is {sum(transition_probabilities.values())}"
    return transition_probabilities


def create_transition_matrix():
    transition_matrix = np.zeros((len(BIOMES), len(BIOMES)))
    for i, biome in enumerate(BIOMES):
        transition_prob = calculate_transition_probabilities(MAP_PROBS[biome])
        for j, next_biome in enumerate(BIOMES):
            if next_biome in transition_prob:
                transition_matrix[i, j] = transition_prob[next_biome]
    return transition_matrix

def create_initial_state():
    initial_state = np.zeros(len(BIOMES))
    initial_state[BIOMES.index("TOWN")] = 1
    return initial_state

def calculate_expected_state_count(transition_matrix, initial_state, num_steps):
    state = initial_state

    matrix_sum = np.eye(len(BIOMES))
    for i in range(1, num_steps):
        matrix_sum += np.linalg.matrix_power(transition_matrix, i)
    expected_state_count = np.dot(state, matrix_sum)
    return expected_state_count

def print_expected_state_count(expected_state_count):
    out_dict = {}
    for i, biome in enumerate(BIOMES):
        out_dict[biome] = expected_state_count[i].round(3)
    # order and print
    out_dict = dict(sorted(out_dict.items(), key=lambda item: item[1], reverse=True))
    for key, value in out_dict.items():
        print(f"{key}: {value}")

def calculate_and_print_expected_state_count(transition_matrix, initial_state, num_steps):
    expected_state_count = calculate_expected_state_count(transition_matrix, initial_state, num_steps)
    print_expected_state_count(expected_state_count)

def classic_mode_expected_state_count(percentage=False):
    expected_state_count = calculate_expected_state_count(create_transition_matrix(), create_initial_state(), 19)
    expected_state_count = [x*10 for x in expected_state_count]
    if percentage:
        sum = np.sum(expected_state_count)
        expected_state_count = [x/sum for x in expected_state_count]
    print_expected_state_count(expected_state_count)




def find_convergence(transition_matrix):
    diff_threshold = 1e-6
    init = transition_matrix
    for i in range(1000):
        next = np.dot(init, transition_matrix)
        diff = np.linalg.norm(next - init)
        if diff < diff_threshold:
            print(f"Converged after {i} iterations")
            break
        init = next
    return init


# This is not equivalent to endless mode. Just stable state accoring to state transition matrix
def find_station_prob_after_convergence():
    transition_matrix = create_transition_matrix()
    converge = find_convergence(transition_matrix)
    init_mat = create_initial_state()
    station = np.dot(init_mat, converge)
    sum = np.sum(station)
    expected_state_count = [x / sum for x in station]
    print_expected_state_count(expected_state_count)

if __name__ == '__main__':
    print("Classic Mode Expected State Probs")
    classic_mode_expected_state_count(percentage=True) #set percentage to false to get the actual count. END is not included

    print("--------------------")
    print("Stable State Probs")
    find_station_prob_after_convergence()
    print("--------------------")


