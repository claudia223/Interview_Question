import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

"""
FuzzyWuzzy primarily relies on the Levenshtein distance, along with some other algorithms,
to calculate similarity scores between strings. It gives a score of certainty.

In this case I have used, partial_ratio for substring matching. However, using this sometimes led to mistakes
because words like "limited" were weighted too much. This could be fixed with pre-processing.

"""

class Fuzzy:
  def __init__(self,threshold=60):
    self.threshold = threshold

  def is_similar_name(self, name1, name2):
    # Calculate the Levenshtein distance between the two names
    ratio = fuzz.partial_ratio(name1.lower(), name2.lower())

    len_n1, len_n2 = len(name1), len(name2)
    if min(len_n1, len_n2) <= 3:
        ratio = 50

    return ratio >= self.threshold