import tkinter as tk
from tkinter import messagebox
import random

def play(player_move):
    computer_move = random.choice(['Rock', 'Paper', 'Scissors'])
    result = determine_winner(player_move, computer_move)
    result_label.config(text=f"You chose {player_move}\nComputer chose {computer_move}\n{result}")

def determine_winner(player, computer):
    if player == computer:
        return "It's a Tie!"
    elif (player == "Rock" and computer == "Scissors") or (player == "Paper" and computer == "Rock") or (player == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "You Lose!"

def reset():
    result_label.config(text="")

def exit():
    window.quit()

window = tk.Tk()
window.title("Rock Paper Scissors")
window.config(bg="#E8F0F2")

title_label = tk.Label(window, text="Rock Paper Scissors", font=("Helvetica", 24, "bold"), bg="#E8F0F2", fg="#333")
title_label.pack(pady=20)

rock_button = tk.Button(window, text="Rock", font=("Helvetica", 14), width=12, bg="#FF5733", fg="white", command=lambda: play("Rock"))
paper_button = tk.Button(window, text="Paper", font=("Helvetica", 14), width=12, bg="#33FF57", fg="white", command=lambda: play("Paper"))
scissors_button = tk.Button(window, text="Scissors", font=("Helvetica", 14), width=12, bg="#3357FF", fg="white", command=lambda: play("Scissors"))

reset_button = tk.Button(window, text="Reset", font=("Helvetica", 14), width=12, bg="#FFC300", fg="white", command=reset)
exit_button = tk.Button(window, text="Exit", font=("Helvetica", 14), width=12, bg="#C70039", fg="white", command=exit)

result_label = tk.Label(window, text="", font=("Helvetica", 16), bg="#E8F0F2", fg="#333")

rock_button.pack(side=tk.LEFT, padx=10, pady=10)
paper_button.pack(side=tk.LEFT, padx=10, pady=10)
scissors_button.pack(side=tk.LEFT, padx=10, pady=10)
reset_button.pack(side=tk.LEFT, padx=10, pady=10)
exit_button.pack(side=tk.LEFT, padx=10, pady=10)
result_label.pack(pady=20)


window.mainloop()