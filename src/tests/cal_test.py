import unittest
from ui.cal_ui import UI

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.root = UI()

    def test_set_total_func(self):
        self.root.current_value = "0"
        self.assertEqual(self.root.current_value, "0")
        self.root.set_total("3")
        self.assertEqual(self.root.current_value, "3")

    def test_set_total_func_two(self):
        self.root.set_total("0")
        self.assertEqual(self.root.current_value, "0")
        self.root.press(".")
        self.root.press("2")
        self.root.press("5")
        self.assertEqual(self.root.current_value, "0.25")    

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
        self.assertEqual(self.root.current_value, "-100.0")
        self.root.plusminus_btn_func()
        self.assertEqual(self.root.current_value, "100.0")

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
        self.assertEqual(self.root.current_value, "10+-")
        #double operators +- needs to be fixed

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

    def test_facto_func(self):
        self.root.current_value = "5.0"
        self.root.facto_btn_func()
        self.assertEqual(self.root.current_value, "Syntax error")

    def test_reci_func(self):
        self.root.current_value = "3"
        self.root.reci_btn_func()
        self.assertEqual(self.root.current_value, "0.3333333333333333")

    def test_reci_func_two(self):
        self.root.current_value = "0"
        self.root.reci_btn_func()
        self.assertEqual(self.root.current_value, "Syntax error")

    def test_sqrd_func(self):
        self.root.current_value = "10"
        self.root.sqrd_btn_func()
        self.assertEqual(self.root.current_value, "100.0")  

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


    if __name__ == "__main__":
        unittest.main()
