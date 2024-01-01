from tkinter import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("580x630+100+200")
        self.root.resizable(False, False)
        self.root.configure(bg="#17161b")

        self.equation = ""
        self.create_gui()

    def create_gui(self):
        self.label_result = Label(self.root, width=25, height=2, text="", font=("arial", 30))
        self.label_result.pack()

        buttons = [
            ("C", 10, 130, self.clear),
            ("/", 150, 130, lambda: self.show("/")),
            ("%", 290, 130, lambda: self.show("%")),
            ("*", 430, 130, lambda: self.show("*")),

            ("7", 10, 230, lambda: self.show("7")),
            ("8", 150, 230, lambda: self.show("8")),
            ("9", 290, 230, lambda: self.show("9")),
            ("-", 430, 230, lambda: self.show("-")),

            ("6", 10, 330, lambda: self.show("6")),
            ("5", 150, 330, lambda: self.show("5")),
            ("4", 290, 330, lambda: self.show("4")),
            ("+", 430, 330, lambda: self.show("+")),

            ("3", 10, 430, lambda: self.show("3")),
            ("2", 150, 430, lambda: self.show("2")),
            ("1", 290, 430, lambda: self.show("1")),
            ("0", 10, 544, lambda: self.show("0")),

            (".", 290, 544, lambda: self.show(".")),
            ("=", 430, 430, self.calculate)
        ]

        for (text, x, y, command) in buttons:
            Button(self.root, text=text, width=4, height=1, font=("arial", 30, "bold"), bd=1,
                   fg="#fff", bg="#2a2d36", command=command).place(x=x, y=y)

    def show(self, value):
        if value == "=":
            try:
                result = str(eval(self.equation))
                self.label_result.config(text=result[:18])  # Limit result length for display
                self.equation = result
            except ZeroDivisionError:
                self.label_result.config(text="Cannot divide by zero")
            except Exception as e:
                self.label_result.config(text=f"Error: {str(e)}")
        else:
            self.equation += value
            self.label_result.config(text=self.equation)

    def clear(self):
        self.equation = ""
        self.label_result.config(text=self.equation)

    def calculate(self):
        self.show("=")

if __name__ == "__main__":
    root = Tk()
    Calculator(root)
    root.mainloop()
