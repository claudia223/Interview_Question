import unittest
from distance import find_related_organizations
from levenshtein_alg import Levenshtein_alg
from cosine_sim_alg import Cosine_sim_alg
from hamming_alg import Hamming_alg
from fuzzy import Fuzzy
from dice import Dice

class TestRelatedOrganizations(unittest.TestCase):

    def test_basic_related_names(self):
        names = [
            "Caprice Holdings Ltd",
            "Caprice Holdings Ltd",
            "CAPRICE STREET Ltd",
            "THE NASHVILLE CORPORATION",
            "Soho House",
            "SOHO HOUSE LIMITED"
        ]
        expected = {
            ("Caprice Holdings Ltd", "Caprice Holdings Ltd"),
            ("Caprice Holdings Ltd", "CAPRICE STREET Ltd"),
            ("Soho House", "SOHO HOUSE LIMITED")
        }
        my_leveshtein = Levenshtein_alg()
        # my_cosine_sim = Cosine_sim_alg()
        my_hamming = Hamming_alg()
        my_fuzzy = Fuzzy()
        my_dice = Dice()

        for elem in [my_leveshtein, my_fuzzy, my_dice]:
            result = find_related_organizations(names, elem)
            self.assertEqual(result, expected)

    def test_similar_but_not_related_names(self):
        names = [
            "Soho House",
            "SOHO 12 House",
            "SOHO 15 HOUSE Lmt"
        ]
        expected = {
            ("Soho House", "SOHO 12 House"),
            ("Soho House", "SOHO 15 HOUSE Lmt"),
            ("SOHO 12 House", "SOHO 15 HOUSE Lmt")
        }

        my_leveshtein = Levenshtein_alg()
        # my_cosine_sim = Cosine_sim_alg()
        my_hamming = Hamming_alg()
        my_fuzzy = Fuzzy()
        my_dice = Dice()


        for elem in [my_leveshtein, my_fuzzy, my_dice]:
            result = find_related_organizations(names, elem)
            print(result)
            self.assertEqual(result, expected)

    def test_no_related_names(self):
        names = [
            "nhs",
            "hsn"
        ]
        expected = set()
        
        my_leveshtein = Levenshtein_alg()
        # my_cosine_sim = Cosine_sim_alg()
        my_hamming = Hamming_alg()
        my_fuzzy = Fuzzy()
        my_dice = Dice()

        for elem in [my_leveshtein, my_fuzzy, my_dice]:
            result = find_related_organizations(names, elem)
            print(result)
            self.assertEqual(result, expected)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
