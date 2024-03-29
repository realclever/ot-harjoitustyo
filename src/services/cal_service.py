from tkinter import Tk, Frame, Label, Button, SE
import math
from ast import literal_eval


font = ('Helvetica', 13, 'bold')
font2 = ('Helvetica', 39, 'bold')
font3 = ('Helvetica', 22, 'bold')
style = {'height': 4, 'width': 10, 'borderwidth': 0,
         'fg': "#FFF", 'bg': "#323232", 'highlightbackground': "#202124"}
style2 = {'height': 4, 'width': 10, 'borderwidth': 0,
          'fg': "#FFF", 'bg': "#3a3a3a", 'highlightbackground': "#202124"}


class CalService:
    def __init__(self):
        """
        Constructor that creates the calculator including components and styling.
        """
        self.root = Tk()
        self.root.title("Calculator app")
        self.root.configure(bg="#202124")
        self.root.resizable(False, False)

        self.current_value = "0"
        self.secondary_value = ""
        self.newnum = True

        self.iniate_screen_components()

    def buttons_space(self):
        """
        Creates frame (space) for buttons and returns it.

        Returns:
         Buttons space component
        """
        buttons = Frame(master=self.root, bg="#202124",
                        highlightbackground="#202124", relief="raised")
        buttons.pack(fill="both", expand=1, padx=1, pady=1)
        return buttons

    def screen_space(self):
        """
        Creates frame (space) for main screen.
        """
        Frame(master=self.root, highlightbackground="#202124").pack(
            fill="both", expand=1)

    def screen_line(self):
        """
        Creates label for line where the calculations/outcome takes place.

        Returns:
         Calculations line component
        """
        line = Label(master=self.screen_space(), text=self.current_value,
                     font=font2, anchor=SE, fg="#e7eaed", bg="#202124")
        line.pack(
            fill="both", expand=1, padx=10, pady=55)

        return line

    def secondary_screen_line(self):
        """
        Creates secondary label for line where the calculations take place.

        Returns:
         Calculations line component
        """
        secondline = Label(master=self.screen_space(), text=self.secondary_value,
                           font=font3, anchor=SE, fg="#969ba1", bg="#202124")
        secondline.pack(
            fill="both", expand=1, padx=10, pady=23)

        return secondline

    def numerical_values(self):
        """
        Creates numerical buttons 0-9 and "." and inserts them in their respective places.
        """
        numbers_dict = {
            1: (4, 1), 2: (4, 2), 3: (4, 3), 4: (3, 1), 5: (3, 2),
            6: (3, 3), 7: (2, 1), 8: (2, 2), 9: (2, 3), 0: (5, 2), '.': (5, 3)
        }

        for num, dic in numbers_dict.items():
            Button(master=self.buttons, text=num, **style2, font=font,
                   command=lambda num=num: self.set_total(str(num))).grid(column=dic[1], row=dic[0])

    def plus_btn(self):
        """
        Creates plus button.
        """
        Button(master=self.buttons, text="+", **style, font=font,
               command=lambda: self.press("+")).grid(column=4, row=4)

    def minus_btn(self):
        """
        Creates minus button.
        """
        Button(master=self.buttons, text="-", **style, font=font,
               command=lambda: self.press("-")).grid(column=4, row=3)

    def multiplication_btn(self):
        """
        Creates multiplication button.
        """
        Button(master=self.buttons, text="\u00D7",
               **style, font=font, command=lambda: self.press("*")).grid(column=4, row=2)

    def division_btn(self):
        """
        Creates division button.
        """
        Button(master=self.buttons, text="÷",
               **style, font=font, command=lambda: self.press("/")).grid(column=4, row=1)

    def sqrt_btn(self):
        """
        Creates square root button.
        """
        Button(master=self.buttons, text="√",
               **style, font=font, command=self.sqrt_btn_func).grid(column=3, row=0)

    def equals_btn(self):
        """
        Creates equals button.
        """
        Button(master=self.buttons, text="=",
               **style, font=font, command=self.equals_btn_func).grid(column=4, row=5)

    def percent_btn(self):
        """
        Creates percentage button.
        """
        Button(master=self.buttons, text="%",
               **style, font=font, command=self.prct_btn_func).grid(column=2, row=0)

    def plusminus_btn(self):
        """
        Creates plus-minus button.
        """
        Button(master=self.buttons, text="+/-",
               **style2, font=font, command=self.plusminus_btn_func).grid(column=1, row=5)

    def ac_btn(self):
        """
        Creates clear button.
        """
        Button(master=self.buttons, text="C",
               **style, font=font,  command=self.ac_btn_func).grid(column=1, row=0)

    def del_btn(self):
        """
        Creates delete button.
        """
        Button(master=self.buttons, text="\u232b",
               **style, font=font, command=self.del_btn_func).grid(column=4, row=0)

    def sqrd_btn(self):
        """
        Creates squared button.
        """
        Button(master=self.buttons, text="x\u00b2",
               **style, font=font,  command=self.sqrd_btn_func).grid(column=3, row=1)

    def reci_btn(self):
        """
        Creates reciprocal button.
        """
        Button(master=self.buttons, text="x\u207B" "\u00B9",
               **style, font=font,  command=self.reci_btn_func).grid(column=2, row=1)

    def facto_btn(self):
        """
        Creates factorial button.
        """
        Button(master=self.buttons, text="x!",
               **style, font=font,  command=self.facto_btn_func).grid(column=1, row=1)

    def set_total(self, value):
        """
        Helper to set and check the initial character of the calculations line.

        Args:
            value: Pressed value
        """
        if self.current_value == "0":
            self.current_value = f'{value}'
        else:
            self.current_value = f'{self.current_value}{value}'

        self.update_values()
        self.update_second_values()

    def update_values(self):
        """
        Updates the line value for calculations.
        """
        self.line.config(text=self.current_value[:16])

    def update_second_values(self):
        """
        Updates the secondary line value for calculations.
        """
        self.secondline.config(text=self.secondary_value[:16])

    def ac_btn_func(self):
        """
        Resets calculation lines to "0" and "".
        """
        self.current_value = "0"
        self.secondary_value = ""
        self.newnum = True
        self.update_values()
        self.update_second_values()

    def del_btn_func(self):
        """
        Removes the last of character of string, until it equals "0".
        """
        self.current_value = self.current_value[:-1]
        self.secondary_value = self.secondary_value[:-1]
        if self.current_value == "":
            self.newnum = True
            self.current_value = "0"
            self.secondary_value = ""
        self.update_values()
        self.update_second_values()

    def sqrt_btn_func(self):
        """
        Square root button logic.
        """
        try:
            self.secondary_value = ""
            self.secondary_value = '√' + self.current_value + self.secondary_value
        except (ValueError, ArithmeticError, SyntaxError):
            self.current_value = "Syntax error"
            self.secondary_value = ""
        finally:
            self.current_value = str(
                math.sqrt((float(self.current_value))))[:8]
            self.update_values()
            self.update_second_values()

    def prct_btn_func(self):
        """
        Percentage button logic.
        """
        try:
            self.secondary_value = ""
            self.secondary_value = self.current_value + self.secondary_value + '%'
        except (ValueError, ArithmeticError, SyntaxError):
            self.current_value = "Syntax error"
            self.secondary_value = ""
        finally:
            self.current_value = str(literal_eval(self.current_value)/100)[:8]
            self.update_values()
            self.update_second_values()

    def plusminus_btn_func(self):
        """
        Plus-minus button logic.
        """
        try:
            if self.current_value.lstrip('-+').isdigit():
                self.current_value = str(-(int(self.current_value)))[:8]
            else:
                self.current_value = str(-(float(self.current_value)))[:8]
        except (ValueError, ArithmeticError, SyntaxError):
            self.current_value = "Syntax error"
            self.secondary_value = ""
        finally:
            self.update_values()

    def equals_btn_func(self):
        """
        Equals button logic. If calculation is incorrect,
        sets currrent value as "Syntax error" and clears the secondary line.
        """
        self.secondary_value = self.current_value
        self.update_second_values()
        try:
            self.current_value = str(eval(f'{self.current_value}'))[:8]
            self.secondary_value = self.secondary_value + ' ='
        except (ValueError, ArithmeticError, SyntaxError):
            self.current_value = "Syntax error"
            self.secondary_value = ""
        finally:
            self.update_values()
            self.update_second_values()

    def reci_btn_func(self):
        """
        Reciprocal button logic. Uses inner helper function to calculate reciprocal value.
        If calculation is incorrect, sets currrent value as "Syntax error".
        """
        def reciprocal(value):
            """
            Helper function to calculate reciprocal value.

            Returns:
                Reciprolcal value
            """
            return 1.0 / value
        try:
            self.secondary_value = ""
            self.secondary_value = self.current_value + \
                self.secondary_value + "\u207B" "\u00B9"
            self.current_value = str(reciprocal(
                (float(self.current_value))))[:8]
        except (ValueError, ArithmeticError, SyntaxError):
            self.current_value = "Syntax error"
            self.secondary_value = ""
        finally:
            self.update_values()
            self.update_second_values()

    def facto_btn_func(self):
        """
        Factorial button logic.
        If calculation is incorrect, sets value as "Syntax error", using non-negative integers.
        """
        try:
            self.secondary_value = ""
            self.secondary_value = self.current_value + self.secondary_value + '!'
            self.current_value = str(literal_eval(
                str(math.factorial(int(self.current_value)))))[:8]
        except (ValueError, ArithmeticError, SyntaxError):
            self.current_value = "Syntax error"
            self.secondary_value = ""
        finally:
            self.update_values()
            self.update_second_values()

    def sqrd_btn_func(self):
        """
        Squared button logic.
        """
        try:
            self.secondary_value = ""
            self.secondary_value = self.current_value + self.secondary_value + '²'
            self.current_value = str(eval(f'{self.current_value}**2'))[:6]
        except (ValueError, ArithmeticError, SyntaxError):
            self.current_value = "Syntax error"
            self.secondary_value = ""
        finally:
            self.update_values()
            self.update_second_values()

    def press(self, value):
        """
        Logic for pressing operators.

        Args:
            value: Pressed button.
        """
        if self.current_value == "0":
            self.current_value = f'{value}'
        else:
            self.current_value = f'{self.current_value}{value}'

        self.update_values()
        self.update_second_values()

    def iniate_screen_components(self):
        """
        Iniates screenlines and buttons
        """
        self.secondline = self.secondary_screen_line()
        self.line = self.screen_line()
        self.buttons = self.buttons_space()


cal_service = CalService()
