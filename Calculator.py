import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.display = tk.Entry(root, font=('Arial', 18), borderwidth=2, relief='ridge', justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.expression = ""

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0, 4)
        ]

        for button in buttons:
            if len(button) == 4:
                text, row, col, colspan = button
                button_widget = tk.Button(self.root, text=text, padx=20, pady=20, font=('Arial', 18),
                                         command=lambda t=text: self.on_button_click(t))
                button_widget.grid(row=row, column=col, columnspan=colspan, sticky='nsew')
            else:
                text, row, col = button
                button_widget = tk.Button(self.root, text=text, padx=20, pady=20, font=('Arial', 18),
                                         command=lambda t=text: self.on_button_click(t))
                button_widget.grid(row=row, column=col, sticky='nsew')

        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        if button_text == 'C':
            self.expression = ""
            self.display.delete(0, tk.END)
        elif button_text == '=':
            try:
                result = eval(self.expression)  
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)  
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, 'Error')
                self.expression = ""
        else:
            
            self.expression += button_text
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
