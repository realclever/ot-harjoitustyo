from tkinter import Tk, Frame, Label, Button, SE
import math
from ast import literal_eval

font = ('Helvetica', 13)
style = {'height': 4, 'width': 10, 'borderwidth': 0,
         'fg': "#FFFFFF", 'bg': "#323232", 'highlightbackground': "#000000"}
style2 = {'height': 4, 'width': 10, 'borderwidth': 0,
          'fg': "#FFFFFF", 'bg': "#3a3a3a", 'highlightbackground': "#000000"}


class UI:
    def __init__(self):
        """
        Constructor that creates the calculator including components and styling.
        """
        self.root = Tk()
        self.root.title("Calculator application")
        self.root.configure(bg="#000000")
        self.root.resizable(False, False)

        self.current_value = "0"
        self.newnum = True

        self.create_ui()
        self.create_buttons()

    def buttons_space(self):
        """
        Creates frame (space) for buttons and returns it.

        Returns:
         Buttons space component
        """
        buttons = Frame(master=self.root, bg="#000000",
                        highlightbackground="#000000", relief="raised")
        buttons.pack(fill="both", expand=1, padx=1, pady=1)
        return buttons

    def screen_space(self):
        """
        Creates frame (space) for whole screen.
        """
        Frame(master=self.root, highlightbackground="#000000").pack(
            fill="both", expand=1)

    def screen_line(self):
        """
        Creates label for line where the calculations take place.

        Returns:
         Calculations line component
        """
        line = Label(master=self.screen, text=self.current_value,
                     font=('Helvetica', 40), anchor=SE, fg="#FFFFFF", bg="#000000")
        line.pack(
            fill="both", expand=1, padx=3, pady=75)

        return line

    def numerical_values(self):
        """
        Creates numerical buttons 0-9 and "." and inserts them in their respective places.
        """
        numbers_dict = {
            1: (4, 1), 2: (4, 2), 3: (4, 3), 4: (3, 1), 5: (3, 2), 6: (3, 3), 7: (2, 1), 8: (2, 2), 9: (2, 3), 0: (5, 2), '.': (5, 3)
        }

        for num, dic in numbers_dict.items():
            Button(master=self.buttons, text=num, **style2, font=font,
                   command=lambda num=num: self.set_total(str(num))).grid(column=dic[1], row=dic[0])

    def plus_btn(self):
        """
        Creates plus button.
        """
        Button(master=self.buttons, text="+", **style, font=font,
               command=lambda: self.press(" + ")).grid(column=4, row=4)

    def minus_btn(self):
        """
        Creates minus button.
        """
        Button(master=self.buttons, text="-", **style, font=font,
               command=lambda: self.press(" - ")).grid(column=4, row=3)

    def multiplication_btn(self):
        """
        Creates multiplication button.
        """
        Button(master=self.buttons, text="\u00D7",
               **style, font=font, command=lambda: self.press(" * ")).grid(column=4, row=2)

    def division_btn(self):
        """
        Creates division button.
        """
        Button(master=self.buttons, text="÷",
               **style, font=font, command=lambda: self.press(" / ")).grid(column=4, row=1)

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
        Button(master=self.buttons, text="x\u00b2",
               **style, font=font,  command=self.sqrd_btn_func).grid(column=3, row=1)

    def reci_btn(self):
        Button(master=self.buttons, text="1/x",
               **style, font=font,  command=self.reci_btn_func).grid(column=2, row=1)

    def facto_btn(self):
        Button(master=self.buttons, text="x!",
               **style, font=font,  command=self.facto_btn_func).grid(column=1, row=1)

    def ac_btn_func(self):
        """
        Resets calculations line to 0
        """
        self.current_value = "0"
        self.newnum = True
        self.update_values()

    def del_btn_func(self):
        """
        Removes the last of character of string, until it equals 0
        """
        self.current_value = self.current_value[:-1]
        if self.current_value == "":
            self.newnum = True
            self.current_value = "0"
        self.update_values()

    def sqrt_btn_func(self):
        self.current_value = str(math.sqrt((float(self.current_value))))
        self.update_values()

    def prct_btn_func(self):
        self.current_value = str(literal_eval(self.current_value)/100)
        self.update_values()

    def plusminus_btn_func(self):
        self.current_value = str(-(float(self.current_value)))
        self.update_values()

    def equals_btn_func(self):
        try:
            self.current_value = str(eval(self.current_value))
            self.update_values()
        except ZeroDivisionError:
            self.current_value = "Syntax error"
        finally:
            self.update_values()

    def reci_btn_func(self):
        def reciprocal(value):
            return 1.0 / value
        try:
            self.current_value = str(reciprocal((float(self.current_value))))
            self.update_values()
        except ZeroDivisionError:
            self.current_value = "Syntax error"
        finally:
            self.update_values()

    def facto_btn_func(self):
        """
        Generates UI components screen, buttons and line for calculations.
        """
        try:
            self.current_value = str(literal_eval(
                str(math.factorial(int(self.current_value)))))
            self.update_values()
        except ValueError:
            self.current_value = "Syntax error"
        finally:
            self.update_values()

    def sqrd_btn_func(self):
        self.current_value = str(math.pow(float(self.current_value), 2))
        self.update_values()

    def press(self, operator):
        self.current_value += str(operator)
        self.update_values()

    def update_values(self):
        """
        Updates the line value for calculations.
        """
        self.line.config(text=self.current_value)

    def set_total(self, value):
        if self.newnum:
            self.current_value = str(value)
            self.newnum = False
        else:
            if str(value) == ".":
                if str(value) in self.current_value:
                    return
            self.current_value = self.current_value + str(value)
        self.update_values()

    def create_ui(self):
        """
        Generates UI components screen, buttons and line for calculations.
        """
        self.screen = self.screen_space()
        self.line = self.screen_line()
        self.buttons = self.buttons_space()

    def create_buttons(self):
        """
        Generates all the buttons.
        """
        self.numerical_values()
        self.equals_btn()
        self.plus_btn()
        self.minus_btn()
        self.multiplication_btn()
        self.division_btn()
        self.percent_btn()
        self.plusminus_btn()
        self.ac_btn()
        self.sqrt_btn()
        self.del_btn()
        self.sqrd_btn()
        self.reci_btn()
        self.facto_btn()


    def start(self):
        """
        Starts the UI.
        """
        self.root.mainloop()
