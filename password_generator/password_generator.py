import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    # Define the character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def on_generate_click(event=None):
    try:
        length = int(length_entry.get())
        if length < 8:
            messagebox.showwarning("Warning", "Password length should be at least 8 characters.")
        else:
            password = generate_password(length)
            password_label.config(text=f"Generated Password:\n{password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("600x400")
root.configure(bg="#fce4ec")  # Light pink background

# Create and place widgets
instructions = tk.Label(root, text="Enter the desired length of the password:", font=("Helvetica", 16), bg="#fce4ec", fg="#d32f2f")  # Dark red text
instructions.pack(pady=10)

length_entry = tk.Entry(root, font=("Helvetica", 16), width=10, bg="#ffffff", fg="#000000")  # White background with black text
length_entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=on_generate_click, font=("Helvetica", 16), bg="#e64a19", fg="#ffffff", activebackground="#d32f2f", activeforeground="#ffffff")  # Orange button
generate_button.pack(pady=20)

password_label = tk.Label(root, text="", font=("Helvetica", 24), bg="#fce4ec", fg="#d32f2f")  # Dark red text
password_label.pack(pady=20)

# Bind Enter key to the password generation function
root.bind('<Return>', on_generate_click)

# Start the GUI event loop
root.mainloop()