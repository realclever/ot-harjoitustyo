from tkinter import *

default_font = ('Cambria', 14)


class main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator application")
        self.root.configure(bg="#202020")
        self.photo = PhotoImage(file='src/cal.png')
        self.root.iconphoto(False, self.photo)
        self.root.resizable(False, False)
        self.current_value = ""

        self.screen = self.screen_space()
        self.line = self.screen_line()
        self.buttons = self.buttons_space()

        self.numerical_values()
        self.equals_button()
        self.plus_button()
        self.minus_button()
        self.multiplication_button()
        self.division_button()
        self.percentage_button()
        self.plusminus_button()
        self.ac_button()

    def buttons_space(self):
        buttons = Frame(master=self.root)
        buttons.pack(fill="both", expand=1, padx=5, pady=5)
        return buttons

    def screen_space(self):
        screen = Frame(master=self.root).pack(
            fill="both", expand=1, padx=5, pady=5)
        return screen

    def screen_line(self):
        line = Label(master=self.screen, text=self.current_value,
                     font=('Helvetica', 40), anchor=SE, bg="#202020", borderwidth=0, relief="groove")
        line.pack(
            fill="both", expand=1, padx=3, pady=50)
        return line

    def numerical_values(self):
        numbers_dict = {
            1: (3, 1), 2: (3, 2), 3: (3, 3), 4: (2, 1), 5: (2, 2), 6: (2, 3), 7: (1, 1), 8: (1, 2), 9: (1, 3), 0: (4, 1), '.': (4, 2)
        }
        for number, dict in numbers_dict.items():
            Button(master=self.buttons, text=number, bg="#3a3a3a", height=4, width=5, font=default_font,
                   command=lambda num=number: self.set_total(str(num))).grid(column=dict[1], row=dict[0])

    def set_total(self, value):
        self.current_value += value
        self.line.config(text=self.current_value)

    def equals_button(self):
        Button(master=self.buttons, text="=",
               height=4, width=5, font=default_font, command=NONE).grid(column=3, row=4)

    def plus_button(self):
        Button(master=self.buttons, text="+",
               height=9, width=5, font=default_font, command=NONE).grid(column=4, row=3, rowspan=2)

    def minus_button(self):
        Button(master=self.buttons, text="-",
               height=4, width=5, font=default_font, command=NONE).grid(column=4, row=2)

    def multiplication_button(self):
        Button(master=self.buttons, text="x",
               height=4, width=5, font=default_font, command=NONE).grid(column=4, row=1)

    def division_button(self):
        Button(master=self.buttons, text="÷",
               height=4, width=5, font=default_font, command=NONE).grid(column=4, row=0)

    def percentage_button(self):
        Button(master=self.buttons, text="%",
               height=4, width=5, font=default_font, command=NONE).grid(column=3, row=0)

    def plusminus_button(self):
        Button(master=self.buttons, text="±",
               height=4, width=5, font=default_font, command=NONE).grid(column=2, row=0)

    def ac_button(self):
        Button(master=self.buttons, text="AC",
               height=4, width=5, font=default_font, command=NONE).grid(column=1, row=0)

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    main().start()
