#38. Create a class CalculatorApp that uses tkinter to create a simple calculator GUI.
import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.result_var = tk.StringVar()  

        self.result_display = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 24), justify='right')
        self.result_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            if button == '=':
                tk.Button(self.root, text=button, command=self.calculate, height=2, width=5, font=("Arial", 18)).grid(row=row_val, column=col_val, padx=5, pady=5)
            elif button == 'C':
                tk.Button(self.root, text=button, command=self.clear, height=2, width=5, font=("Arial", 18)).grid(row=row_val, column=col_val, padx=5, pady=5)
            else:
                tk.Button(self.root, text=button, command=lambda b=button: self.append_to_expression(b), height=2, width=5, font=("Arial", 18)).grid(row=row_val, column=col_val, padx=5, pady=5)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def append_to_expression(self, value):
        current_expression = self.result_var.get() 
        current_expression += value  
        self.result_var.set(current_expression)  

    def calculate(self):
        try:
            expression = self.result_var.get()  
            result = eval(expression)  
            self.result_var.set(result) 
        except Exception as e:
            self.result_var.set("Error")  

    def clear(self):
        self.result_var.set("")  

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

