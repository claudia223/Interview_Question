
"""
Simple algorithm, but not good because it does a char by char comparison, would be
useful if we had equal length strings.

"""


class Hamming_alg():

  def __init__(self, threshold=0.25):
      self.threshold = threshold

  def hamming_distance(self, name1, name2):
      distance = abs(len(name1) - len(name2))
      min_len = min(len(name1), len(name2))

      for i in range(min_len):
          if name1[i] != name2[i]:
              distance += 1

      return distance

  def is_similar_name(self, name1, name2):
      distance = self.hamming_distance(name1, name2)
      max_len = max(len(name1), len(name2))
      similarity_score = 1 - (distance / max_len)
      return similarity_score >= self.threshold