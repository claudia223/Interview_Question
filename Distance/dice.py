
"""

The test for nhs hsn doesn't pass, as the characters are too similar.

"""


class Dice:

  def __init__(self, threshold=0.5):
      self.threshold = threshold

  
  @staticmethod
  def preprocess_text(text):
      # Preprocess text by removing special characters and lowercasing
      return text.lower().replace(".", "").replace(",", "").replace("limited", "").replace("ltd", "").strip()

  def is_similar_name(self, s1, s2):
      s1 = self.preprocess_text(s1)
      s2 = self.preprocess_text(s2)

      if not len(s1) or not len(s2):
          return 0.0
      if len(s1) == 1:
          s1 = s1 + u'.'
      if len(s2) == 1:
          s2 = s2 + u'.'

      # Two sets of bigrams for the two strings.
      a = [s1[i:i + 2] for i in range(len(s1) - 1)]
      b = [s2[i:i + 2] for i in range(len(s2) - 1)]

      # Count the number of bigrams in common.
      overlap = len(set(a) & set(b))
      dice_coeff = (2.0 * overlap) / (len(a) + len(b))

      print(dice_coeff, s1, s2)

      return self.threshold <= dice_coeff