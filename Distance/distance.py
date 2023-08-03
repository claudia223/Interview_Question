import json
from levenshtein_alg import Levenshtein_alg
from cosine_sim_alg import Cosine_sim_alg
from hamming_alg import Hamming_alg
from dice import Dice

def find_related_organizations(names_list, algorithm):
    related_pairs = set()


    # Iterate through each pair of names in the list
    for i in range(len(names_list)):
        for j in range(i + 1, len(names_list)):
            name1 = names_list[i]
            name2 = names_list[j]

            if algorithm.is_similar_name(name1, name2):
                # If the names are considered related, add them to the set of related pairs
                related_pairs.add((name1, name2))
    return related_pairs


def main():
    # Load the JSON file containing the list of names
    with open("../org_names.json", "r") as file:
        data = json.load(file)
    
    my_leveshtein = Levenshtein_alg()
    # my_cosine_sim = Cosine_sim_alg()
    my_hamming = Hamming_alg()
    my_dice = Dice()

    # Call the function with the sample data
    output = find_related_organizations(data, algorithm=my_dice)
    print(output)
    print(len(output))


if __name__ == "__main__":
    main()