import tkinter as tk
from tkinter import messagebox
import random

# Initialize scores
my_score = 0
comp_score = 0
draw = 0


def play_round(user_choice):
    global my_score, comp_score, draw
    choices = ['Rock', 'Paper', 'Scissors']
    comp_choice = random.choice(choices)

    if user_choice == comp_choice:
        result = "Game Draw"
        draw += 1
    elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
            (user_choice == 'Paper' and comp_choice == 'Rock') or \
            (user_choice == 'Scissors' and comp_choice == 'Paper'):
        result = "You Won!"
        my_score += 1
    else:
        result = "Computer Won"
        comp_score += 1

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {comp_choice}\nResult: {result}")
    score_label.config(text=f"Your Score: {my_score}\nComputer Score: {comp_score}\nDraws: {draw}")


def play_again():
    result = messagebox.askquestion("Play Again", "Do you want to play another round?")
    if result == 'yes':
        result_label.config(text="")
    else:
        messagebox.showinfo("Game Over",
                            f"Final Scores:\nYour Score: {my_score}\nComputer Score: {comp_score}\nDraws: {draw}")
        root.quit()


# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.attributes('-fullscreen', True)
root.configure(bg="#e0f7fa")

# Create and place widgets with enhanced styling
instructions = tk.Label(root, text="Welcome to Rock-Paper-Scissors!\n\n"
                                   "Instructions:\n"
                                   "1. Click 'Rock', 'Paper', or 'Scissors' to make your choice.\n"
                                   "2. The computer will make its choice randomly.\n"
                                   "3. The result will be displayed after each round.\n"
                                   "4. You will be asked if you want to play another round after each choice.\n"
                                   "5. Scores will be updated accordingly.\n"
                                   "6. Game ends when you choose not to play another round.\n"
                                   "Good luck and have fun!",
                        font=("Helvetica", 18), bg="#e0f7fa", fg="#00796b")
instructions.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky="nsew")

frame = tk.Frame(root, bg="#e0f7fa")
frame.grid(row=1, column=0, columnspan=3, pady=10)

# Style for buttons
button_style = {
    'font': ('Helvetica', 22),
    'bg': '#00796b',
    'fg': '#ffffff',
    'activebackground': '#004d40',
    'activeforeground': '#ffffff',
    'width': 12
}

rock_button = tk.Button(frame, text="Rock", command=lambda: [play_round('Rock'), play_again()], **button_style)
rock_button.grid(row=0, column=0, padx=20, pady=10)

paper_button = tk.Button(frame, text="Paper", command=lambda: [play_round('Paper'), play_again()], **button_style)
paper_button.grid(row=0, column=1, padx=20, pady=10)

scissors_button = tk.Button(frame, text="Scissors", command=lambda: [play_round('Scissors'), play_again()],
                            **button_style)
scissors_button.grid(row=0, column=2, padx=20, pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 18), bg="#e0f7fa", fg="#00796b")
result_label.grid(row=2, column=0, columnspan=3, pady=10, sticky="nsew")

score_label = tk.Label(root, text="Your Score: 0\nComputer Score: 0\nDraws: 0", font=("Helvetica", 18), bg="#e0f7fa",
                       fg="#00796b")
score_label.grid(row=3, column=0, columnspan=3, pady=10, sticky="nsew")

# Configure grid layout to expand and fill the screen
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Start the GUI event loop
root.mainloop()