import unittest
from files.string_functions import multiply_string


class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual(multiply_string("Jack",5), "JackJackJackJackJack")


if __name__ == '__main__':
    unittest.main()
