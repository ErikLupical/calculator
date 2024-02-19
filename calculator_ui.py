from tkinter import *
from math import *


class CalculatorUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.handler = Handler(self)
        self.buttons_list = [
            "7", "8", "9", "(", ") ", "del", "clr",
            "4", "5", "6", "^", "√", "▲", "▼",
            "1", "2", "3", "*", "/", "e", "log",
            ".", "0", "%", "+", "-", "π", "="
        ]
        self.expression = ''
        self.answer = ''

    def set_viewer(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        expression_display = Label(self.root, text=self.expression, padx=5, pady=5, anchor="w")
        expression_display.grid(row=0, column=0, columnspan=7, sticky='nsew')

        answer_display = Label(self.root, text=self.answer, padx=5, pady=5, anchor="e")
        answer_display.grid(row=1, column=0, columnspan=7, sticky='nsew')

        button_objects = []
        rows, cols = 4, 7

        for i in range(rows):
            for j in range(cols):
                index = i * cols + j
                if index < len(self.buttons_list):
                    button_text = self.buttons_list[index]
                    button = Button(self.root, text=button_text,
                                    command=lambda text=button_text: self.handler.handle_click(text))
                    button.grid(row=i+2, column=j, sticky='nsew')
                    button_objects.append(button)

        for i in range(rows+2):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(cols):
            self.root.grid_columnconfigure(i, weight=1)

    def view(self):
        self.root.mainloop()


class Handler:
    def __init__(self, ui):
        self.ui = ui
        self.memory = [["", ""], ["1+1", "2"], ["2+2", "4"]]
        self.memory_index = 0
        self.ui.expression = self.memory[self.memory_index][0]
        self.ui.answer = self.memory[self.memory_index][1]

    def handle_click(self, button_text):
        if button_text == "▲" or button_text == "▼":
            if button_text == "▲":
                if self.memory_index < len(self.memory)-1:
                    self.memory_index += 1
            elif button_text == "▼":
                if self.memory_index > 0:
                    self.memory_index -= 1

        elif button_text == "=":
            self.memory[self.memory_index][1] = calculate(self.memory[self.memory_index][0])
            self.memory = self.memory[self.memory_index:]
            self.memory_index = 0

        elif button_text == "clr":
            if self.memory[0] != ["", ""]:
                self.memory = [["", ""]] + self.memory
            self.memory_index = 0

        else:
            if button_text != "clr":
                if button_text == "del":
                    self.memory[self.memory_index][0] = self.memory[self.memory_index][0][:-1]
                elif button_text == "^":
                    self.memory[self.memory_index][0] += "**"
                elif button_text == "√":
                    self.memory[self.memory_index][0] += " sqrt("
                elif button_text == "log":
                    self.memory[self.memory_index][0] += " log("
                elif button_text == "π":
                    self.memory[self.memory_index][0] += " pi"
                elif button_text == "e":
                    self.memory[self.memory_index][0] += " e"
                else:
                    self.memory[self.memory_index][0] += button_text

                self.memory[self.memory_index][1] = ""
                self.memory = self.memory[self.memory_index:]
                self.memory_index = 0

        self.ui.expression = self.memory[self.memory_index][0]
        self.ui.answer = self.memory[self.memory_index][1]
        self.ui.set_viewer()


def calculate(expression):
    try:
        answer = eval(expression)
        return str(answer)
    except Exception as e:
        return "syntax error"
