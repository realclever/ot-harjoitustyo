import unittest
from index import *


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.root = main()

    def test_title_found(self):
        title = self.root.root.winfo_toplevel().title()
        expected = "Calculator application"
        self.assertEqual(title, expected)

    # def test_number_button(self):


if __name__ == "__main__":
    unittest.main()
