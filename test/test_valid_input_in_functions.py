import unittest
from files.validate_input_in_functions import score_input


class MyTestCase1(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(score_input("Python test #1"), "Python test #1: 0")

    def test_score_input_test_score_valid(self):
        self.assertEqual(score_input("Python test #1", 50), "Python test #1: 50")
        self.assertEqual(score_input("Python test #2", 83), "Python test #2: 83")

    def test_score_input_test_score_below_range(self):
        self.assertEqual(score_input("Python test #3", -43), "Invalid test score, try again!")
        self.assertEqual(score_input("Python test #4", -1), "Invalid test score, try again!")

    def test_score_input_test_score_above_range(self):
        self.assertEqual(score_input("Python test #7", 101), "Invalid test score, try again!")
        self.assertEqual(score_input("Python test #7", 10534), "Invalid test score, try again!")

    def test_test_score_non_numeric(self):
        self.assertEqual(score_input("Python test #1", "me"), "Invalid test score, try again!")
        self.assertEqual(score_input("Python test #1", ";'."), "Invalid test score, try again!")

    def test_score_input_invalid_message(self):
        self.assertEqual(score_input("Python test #1", 98, "INVALID TEST SCORE!!!!"), "Python test #1: 98")
        self.assertEqual(score_input("Python test #5", 143, "INVALID TEST SCORE!!!!"), "INVALID TEST SCORE!!!!")


if __name__ == '__main__':
    unittest.main()
