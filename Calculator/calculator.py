import tkinter as tk
from tkinter import messagebox
import math


def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        elif operation == 'sqrt':
            if num1 < 0:
                messagebox.showerror("Error", "Cannot calculate the square root of a negative number.")
                return
            result = math.sqrt(num1)
        elif operation == '^':
            result = math.pow(num1, num2)
        elif operation == '%':
            result = (num1 * num2) / 100
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


# Create the main window
root = tk.Tk()
root.title("Enhanced Calculator")
root.geometry("500x400")
root.configure(bg="#b3e5fc")  # Light blue background color

# Create and place widgets
instructions = tk.Label(root, text="Enter two numbers and choose an operation:", font=("Helvetica", 16), bg="#b3e5fc",
                        fg="#0277bd")  # Darker blue text
instructions.pack(pady=10)

frame = tk.Frame(root, bg="#b3e5fc")
frame.pack(pady=10)

label_num1 = tk.Label(frame, text="Number 1:", font=("Helvetica", 14), bg="#b3e5fc", fg="#01579b")  # Blue text
label_num1.grid(row=0, column=0, padx=10, pady=5)

entry_num1 = tk.Entry(frame, font=("Helvetica", 14), bg="#ffffff", fg="#000000")  # White background with black text
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(frame, text="Number 2:", font=("Helvetica", 14), bg="#b3e5fc", fg="#01579b")  # Blue text
label_num2.grid(row=1, column=0, padx=10, pady=5)

entry_num2 = tk.Entry(frame, font=("Helvetica", 14), bg="#ffffff", fg="#000000")  # White background with black text
entry_num2.grid(row=1, column=1, padx=10, pady=5)

operation_var = tk.StringVar(value='+')

frame_operations = tk.Frame(root, bg="#b3e5fc")
frame_operations.pack(pady=10)

label_operation = tk.Label(frame_operations, text="Operation:", font=("Helvetica", 14), bg="#b3e5fc",
                           fg="#01579b")  # Blue text
label_operation.grid(row=0, column=0, padx=10, pady=5)

operation_buttons = {
    '+': tk.Radiobutton(frame_operations, text='+', variable=operation_var, value='+', font=("Helvetica", 14),
                        bg="#b3e5fc", fg="#000000", selectcolor="#90caf9"),  # Light blue selection
    '-': tk.Radiobutton(frame_operations, text='-', variable=operation_var, value='-', font=("Helvetica", 14),
                        bg="#b3e5fc", fg="#000000", selectcolor="#90caf9"),
    '': tk.Radiobutton(frame_operations, text='', variable=operation_var, value='*', font=("Helvetica", 14),
                       bg="#b3e5fc", fg="#000000", selectcolor="#90caf9"),
    '/': tk.Radiobutton(frame_operations, text='/', variable=operation_var, value='/', font=("Helvetica", 14),
                        bg="#b3e5fc", fg="#000000", selectcolor="#90caf9"),
    'sqrt': tk.Radiobutton(frame_operations, text='√', variable=operation_var, value='sqrt', font=("Helvetica", 14),
                           bg="#b3e5fc", fg="#000000", selectcolor="#90caf9"),
    '^': tk.Radiobutton(frame_operations, text='^', variable=operation_var, value='^', font=("Helvetica", 14),
                        bg="#b3e5fc", fg="#000000", selectcolor="#90caf9"),
    '%': tk.Radiobutton(frame_operations, text='%', variable=operation_var, value='%', font=("Helvetica", 14),
                        bg="#b3e5fc", fg="#000000", selectcolor="#90caf9")
}

for i, button in enumerate(operation_buttons.values()):
    button.grid(row=0, column=i + 1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate, font=("Helvetica", 16), bg="#0288d1",
                             fg="#ffffff", activebackground="#0277bd", activeforeground="#ffffff")  # Blue button
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=("Helvetica", 16), bg="#b3e5fc", fg="#01579b")  # Blue text
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()