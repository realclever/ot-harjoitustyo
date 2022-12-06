import unittest
from ui.ui import UI


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.root = UI()

    def test_set_total_func(self):
        self.root.current_value = "0"
        self.assertEqual(self.root.current_value, "0")
        self.root.set_total("3")
        self.assertEqual(self.root.current_value, "3")

    def test_percent_func(self):
        self.root.current_value = "100"
        self.assertEqual(self.root.current_value, "100")
        self.root.prct_btn_func()
        self.assertEqual(self.root.current_value, "1.0")

    def test_ac_func(self):
        self.root.current_value = "100"
        self.assertEqual(self.root.current_value, "100")
        self.root.ac_btn_func()
        self.assertEqual(self.root.current_value, "0")

    def test_plusminus_func(self):
        self.root.current_value = "100"
        self.assertEqual(self.root.current_value, "100")
        self.root.plusminus_btn_func()
        self.assertEqual(self.root.current_value, "-100.0")
        self.root.plusminus_btn_func()
        self.assertEqual(self.root.current_value, "100.0")

    def test_sqrt_func(self):
        self.root.current_value = "100"
        self.assertEqual(self.root.current_value, "100")
        self.root.sqrt_btn_func()
        self.assertEqual(self.root.current_value, "10.0")

    def test_press_func(self):
        self.root.current_value = "100"
        self.root.press("+")
        self.assertEqual(self.root.current_value, "100+")
        self.root.press("-")
        self.assertEqual(self.root.current_value, "100+-")
        # double operators +- needs to be fixed

    if __name__ == "__main__":
        unittest.main()
