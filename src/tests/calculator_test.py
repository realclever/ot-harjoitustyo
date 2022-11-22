import unittest
from index import Calc


class TestCalculator(unittest.TestCase):
    def setUp(self):
       self.root = Calc()

    def test_title_found(self):
        title = self.root.root.winfo_toplevel().title()
        expected = "Calculator application"
        self.assertEqual(title, expected)

    #Sovelluksessa ei vielä mitään merkityksellistä testattavaa     

if __name__ == "__main__":
    unittest.main()
