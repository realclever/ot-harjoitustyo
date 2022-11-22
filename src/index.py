from tkinter import *


class Calc:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator application")
        self.root.geometry("400x700")
        self.root.configure(bg="#202124")
        self.photo = PhotoImage(file='src/cal.png')
        self.root.iconphoto(False, self.photo)
        self.root.resizable(False, False)

        self.screen = self.screen_space()
        self.buttons = self.buttons_space()
        
        self.line = self.screen_line()

    def buttons_space(self):
        buttons = Frame(master=self.root).pack(fill="both", expand=1)
        return buttons

    def screen_space(self):
        screen = Frame(master=self.root, highlightbackground="#373b3e",
                       highlightthickness=2, height=150)
        screen.pack(fill="both", expand=1)
        return screen

    def screen_line(self):
        line = Label(self.screen, text="0").pack(
            fill="both", expand=1)
        return line

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    Calc().start()
