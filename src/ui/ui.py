from tkinter import Tk, Frame, Label, Button, SE
import math
from ast import literal_eval

def_f = ('Cambria', 11)


class UI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator application")
        self.root.configure(bg="#202020")
        self.root.resizable(False, False)

        self.current_value = "0"
        self.newnum = True

        self.create_ui()
        self.create_buttons()

    def buttons_space(self):
        buttons = Frame(master=self.root)
        buttons.pack(fill="both", expand=1, padx=5, pady=5)
        return buttons

    def screen_space(self):
        Frame(master=self.root).pack(
            fill="both", expand=1, padx=5, pady=5)

    def screen_line(self):
        line = Label(master=self.screen, text=self.current_value,
                     font=('Helvetica', 40), anchor=SE, bg="#202020")
        line.pack(
            fill="both", expand=1, padx=3, pady=50)
        return line

    def numerical_values(self):
        numbers_dict = {
            1: (3, 1), 2: (3, 2), 3: (3, 3), 4: (2, 1), 5: (2, 2), 6: (2, 3), 7: (1, 1), 8: (1, 2), 9: (1, 3), 0: (4, 1), '.': (4, 2)
        }

        for num, dic in numbers_dict.items():
            Button(master=self.buttons, text=num, bg="#3a3a3a", height=4, width=5, font=def_f,
                   command=lambda num=num: self.set_total(str(num))).grid(column=dic[1], row=dic[0])

    def plus_btn(self):
        Button(master=self.buttons, text="+", height=4, width=5,
               font=def_f, command=lambda: self.press("+")).grid(column=4, row=4)

    def minus_btn(self):
        Button(master=self.buttons, text="-", height=4, width=5,
               font=def_f, command=lambda: self.press("-")).grid(column=4, row=3)

    def multiplication_btn(self):
        Button(master=self.buttons, text="x",
               height=4, width=5, font=def_f, command=lambda: self.press("*")).grid(column=4, row=2)

    def division_btn(self):
        Button(master=self.buttons, text="÷",
               height=4, width=5, font=def_f, command=lambda: self.press("/")).grid(column=4, row=1)

    def sqrt_btn(self):
        Button(master=self.buttons, text="√",
               height=4, width=5, font=def_f, command=self.sqrt_btn_func).grid(column=4, row=0)

    def equals_btn(self):
        Button(master=self.buttons, text="=",
               height=4, width=5, font=def_f, command=self.equals_btn_func).grid(column=3, row=4)

    def percent_btn(self):
        Button(master=self.buttons, text="%",
               height=4, width=5, font=def_f, command=self.prct_btn_func).grid(column=3, row=0)

    def plusminus_btn(self):
        Button(master=self.buttons, text="+/-",
               height=4, width=5, font=def_f, command=self.plusminus_btn_func).grid(column=2, row=0)

    def ac_btn(self):
        Button(master=self.buttons, text="C",
               height=4, width=5, font=def_f,  command=self.ac_btn_func).grid(column=1, row=0)

    def ac_btn_func(self):
        self.current_value = "0"
        self.newnum = True
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
        self.current_value = str(eval(self.current_value))
        print("Yhtäkuin merkkiä painettu")
        self.update_values()

    def press(self, value):
        self.current_value += str(value)
        print("plus merkkiä painettu")
        self.update_values()

    def update_values(self):
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
        print("numeroa painettu")
        self.update_values()

    def create_ui(self):
        self.screen = self.screen_space()
        self.line = self.screen_line()
        self.buttons = self.buttons_space()

    def create_buttons(self):
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

    def start(self):
        self.root.mainloop()
