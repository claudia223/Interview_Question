import Levenshtein

"""
Levenshtein or edit distance, measures the number of single-character edits (insertion, deletion, or substitutions)
needed to transform one string into another. It can be done using dynamic programming (as can be seen below),
however, for this example I have just called the library.

I have implemented a dynamic threshold, where some penalties were added. By looking at the example json file
provided some common problems were identified and reduced with the penalties.

Time complexity of Levenshtein O(n * m)

"""

class Levenshtein_alg:
    def __init__(self, base_threshold=10, length_penalty_factor=0.25):
        self.base_threshold = base_threshold 
        self.length_penalty_factor = length_penalty_factor


    def calculate_threshold(self, name1, name2):
        # Apply penalty to the base threshold if either word is small
        len_n1, len_n2 = len(name1), len(name2)
        if min(len_n1, len_n2) <= 3:
            adjusted_threshold = self.base_threshold * self.length_penalty_factor
        else:
            adjusted_threshold = self.base_threshold
        
        # Reduce threshold if words are of similar lengths
        length_difference = abs(len_n1 - len_n2)
        if length_difference <= 7:
            adjusted_threshold -= max(1, (7 - length_difference) * self.length_penalty_factor)
    
        return adjusted_threshold

    def is_similar_name(self, name1, name2):
        # Calculate the Levenshtein distance between the two names
        distance = Levenshtein.distance(name1.lower(), name2.lower())

        # Calculate the dynamic threshold based on the average length of names
        threshold = self.calculate_threshold(name1, name2)
        # Lower threshold values will consider strings with closer edit distance as similar

        return distance <= threshold


"""

def levenshtein_distance(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    
    # Create a matrix to store the distances
    matrix = [[0 for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]
    
    # Initialize the first row and column
    for i in range(len_str1 + 1):
        matrix[i][0] = i
    for j in range(len_str2 + 1):
        matrix[0][j] = j
        
    # Fill in the rest of the matrix
    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,         # Deletion
                matrix[i][j - 1] + 1,         # Insertion
                matrix[i - 1][j - 1] + cost   # Substitution
            )
    
    return matrix[len_str1][len_str2]

"""