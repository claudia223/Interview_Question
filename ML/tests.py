import unittest
from clustering import find_related_pairs as clust
from pretrained_nlp import find_related_pairs as nlp

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
            ('SOHO HOUSE LIMITED', 'Soho House'),
            ('CAPRICE STREET Ltd', 'Caprice Holdings Ltd')
        }


        result1 = clust(names)
        result2 = nlp(names)

        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)

    def test_similar_but_not_related_names(self):
        names = [
            "Soho House",
            "SOHO 12 House",
            "SOHO 15 HOUSE Lmt"
        ]
        expected = {
            ('SOHO 12 House', 'Soho House'),
            ('SOHO 15 HOUSE Lmt', 'Soho House'),
            ("SOHO 12 House", "SOHO 15 HOUSE Lmt")
        }

        result1 = clust(names)
        result2 = nlp(names)
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)

    def test_no_related_names(self):
        names = [
            "nhs",
            "hsn"
        ]
        expected = set()
        
        result1 = clust(names)
        result2 = nlp(names)
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
