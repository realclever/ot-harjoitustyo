import unittest
from services.cal_service import CalService


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.root = CalService()

    def test_set_total_func(self):
        self.root.set_total("0")
        self.assertEqual(self.root.current_value, "0")
        self.root.press(".")
        self.root.press("2")
        self.root.press("5")
        self.assertEqual(self.root.current_value, ".25")
        self.root.equals_btn_func()
        self.assertEqual(self.root.current_value, "0.25")

    def test_set_total_func_two(self):
        self.root.set_total("")
        self.root.press(".")
        self.root.equals_btn_func()
        self.assertEqual(self.root.current_value, "Syntax error")

    def test_set_total_func_three(self):
        self.root.set_total(".")
        self.assertEqual(self.root.current_value, ".")
        self.root.set_total("1")
        self.assertEqual(self.root.current_value, ".1")
        self.root.equals_btn_func()
        self.assertEqual(self.root.current_value, "0.1")

    def test_percent_func(self):
        self.root.current_value = "100"
        self.root.prct_btn_func()
        self.assertEqual(self.root.current_value, "1.0")

    def test_ac_func(self):
        self.root.current_value = "100"
        self.root.ac_btn_func()
        self.assertEqual(self.root.current_value, "0")

    def test_plusminus_func(self):
        self.root.current_value = "100"
        self.root.plusminus_btn_func()
        self.assertEqual(self.root.current_value, "-100")
        self.root.plusminus_btn_func()
        self.assertEqual(self.root.current_value, "100")
        self.root.ac_btn_func()
        self.assertEqual(self.root.current_value, "0")
        self.root.current_value = "1.1"
        self.assertEqual(self.root.current_value, "1.1")
        self.root.plusminus_btn_func()
        self.assertEqual(self.root.current_value, "-1.1")
        self.root.plusminus_btn_func()
        self.assertEqual(self.root.current_value, "1.1")

    def test_plusminus_func_two(self):
        self.root.current_value = "100"
        self.root.press("*")
        self.root.plusminus_btn_func()
        self.assertEqual(self.root.current_value, "Syntax error")

    def test_sqrt_func(self):
        self.root.current_value = "100"
        self.root.sqrt_btn_func()
        self.assertEqual(self.root.current_value, "10.0")

    def test_press_func(self):
        self.root.set_total("5")
        self.root.press("+")
        self.root.press(5)
        self.root.press("-")
        self.root.press(1)
        self.root.press("*")
        self.root.press(2)
        self.root.press("/")
        self.root.press(2)
        self.assertEqual(self.root.current_value, "5+5-1*2/2")
        self.root.equals_btn_func()
        self.assertEqual(self.root.current_value, "9.0")

    def test_operators(self):
        self.root.current_value = "10"
        self.root.press("+")
        self.root.press("-")
        self.root.press("5")
        self.root.equals_btn_func()
        self.assertEqual(self.root.secondary_value, "10+-5 =")
        self.assertEqual(self.root.current_value, "5")

    def test_del_func(self):
        self.root.current_value = "10"
        self.root.del_btn_func()
        self.assertEqual(self.root.current_value, "1")
        self.root.del_btn_func()
        self.assertEqual(self.root.current_value, "0")

    def test_del_func_two(self):
        self.root.current_value = "0"
        self.root.del_btn_func()
        self.assertEqual(self.root.current_value, "0")

    def test_facto_func(self):
        self.root.current_value = "5"
        self.root.facto_btn_func()
        self.assertEqual(self.root.current_value, "120")

    def test_facto_func_two(self):
        self.root.current_value = "5.0"
        self.root.facto_btn_func()
        self.assertEqual(self.root.current_value, "Syntax error")
        self.root.current_value = "5"
        self.root.facto_btn_func()
        self.assertEqual(self.root.current_value, "120")
        self.root.current_value = "-5"
        self.root.facto_btn_func()
        self.assertEqual(self.root.current_value, "Syntax error")

    def test_reci_func(self):
        self.root.current_value = "3"
        self.root.reci_btn_func()
        self.assertEqual(self.root.current_value, "0.333333")

    def test_reci_func_two(self):
        self.root.current_value = "0"
        self.root.reci_btn_func()
        self.assertEqual(self.root.current_value, "Syntax error")

    def test_sqrd_func(self):
        self.root.current_value = "10"
        self.root.sqrd_btn_func()
        self.assertEqual(self.root.current_value, "100")
        self.root.current_value = "-10"
        self.root.sqrd_btn_func()
        self.assertEqual(self.root.current_value, "-100")
        self.root.current_value = "0.5"
        self.root.sqrd_btn_func()
        self.assertEqual(self.root.current_value, "0.25")
        self.root.current_value = "-0.5"
        self.root.sqrd_btn_func()
        self.assertEqual(self.root.current_value, "-0.25")

    def test_sqrd_func_two(self):
        self.root.current_value = "10"
        self.root.press("*")
        self.root.sqrd_btn_func()
        self.assertEqual(self.root.current_value, "Syntax error")

    def test_equals_func(self):
        self.root.current_value = "10"
        self.root.press("-")
        self.root.press("5")
        self.root.equals_btn_func()
        self.assertEqual(self.root.current_value, "5")

    def test_equals_func_two(self):
        self.root.current_value = "10"
        self.root.press("/")
        self.root.press("0")
        self.root.equals_btn_func()
        self.assertEqual(self.root.current_value, "Syntax error")

    def test_secondline(self):
        self.root.current_value = "10"
        self.root.press("+")
        self.root.press("10")
        self.root.equals_btn_func()
        self.assertEqual(self.root.secondary_value, "10+10 =")
        self.root.ac_btn_func()
        self.assertEqual(self.root.secondary_value, "")

    def test_secondline_two(self):
        self.root.current_value = "10"
        self.root.press("+")
        self.root.press("10")
        self.root.equals_btn_func()
        self.assertEqual(self.root.secondary_value, "10+10 =")
        self.root.del_btn_func()
        self.assertEqual(self.root.secondary_value, "10+10 ")
        self.root.del_btn_func()
        self.assertEqual(self.root.secondary_value, "")

    def test_secondline_three(self):
        self.root.current_value = "10"
        self.root.press("/")
        self.root.press("0")
        self.root.equals_btn_func()
        self.assertEqual(self.root.current_value, "Syntax error")
        self.assertEqual(self.root.secondary_value, "")

    def test_call_buttons(self):
        self.root.numerical_values()
        self.root.equals_btn()
        self.root.plus_btn()
        self.root.minus_btn()
        self.root.multiplication_btn()
        self.root.division_btn()
        self.root.percent_btn()
        self.root.plusminus_btn()
        self.root.ac_btn()
        self.root.sqrt_btn()
        self.root.del_btn()
        self.root.sqrd_btn()
        self.root.reci_btn()
        self.root.facto_btn()

    if __name__ == "__main__":
        unittest.main()
