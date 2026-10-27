import random
import tkinter as tk
from tkinter import messagebox


class RockPaperScissorsApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Rock Paper Scissors Game")
    self.root.geometry("400x450")
    self.root.config(bg="#f4f6f9")

    self.choices = ["Rock", "Paper", "Scissors"]
    self.user_score = 0
    self.computer_score = 0

    # Title
    self.title_label = tk.Label(
        root,
        text="Rock Paper Scissors",
        font=("Helvetica", 18, "bold"),
        bg="#f4f6f9",
        fg="#2c3e50",
    )
    self.title_label.pack(pady=15)

    # Scoreboard
    self.score_label = tk.Label(
        root,
        text="Player: 0  |  Computer: 0",
        font=("Helvetica", 12, "bold"),
        bg="#f4f6f9",
        fg="#34495e",
    )
    self.score_label.pack(pady=5)

    # Status / Result Display
    self.result_label = tk.Label(
        root,
        text="Choose your move!",
        font=("Helvetica", 12),
        bg="#ffffff",
        relief="groove",
        width=30,
        height=3,
    )
    self.result_label.pack(pady=20)

    # Buttons Frame
    btn_frame = tk.Frame(root, bg="#f4f6f9")
    btn_frame.pack(pady=10)

    # Rock, Paper, Scissors Buttons
    tk.Button(
        btn_frame,
        text="🪨 Rock",
        font=("Helvetica", 12, "bold"),
        width=10,
        bg="#e74c3c",
        fg="white",
        command=lambda: self.play("Rock"),
    ).grid(row=0, column=0, padx=5, pady=5)

    tk.Button(
        btn_frame,
        text="📄 Paper",
        font=("Helvetica", 12, "bold"),
        width=10,
        bg="#3498db",
        fg="white",
        command=lambda: self.play("Paper"),
    ).grid(row=0, column=1, padx=5, pady=5)

    tk.Button(
        btn_frame,
        text="✂️ Scissors",
        font=("Helvetica", 12, "bold"),
        width=10,
        bg="#2ecc71",
        fg="white",
        command=lambda: self.play("Scissors"),
    ).grid(row=0, column=2, padx=5, pady=5)

    # Reset Button
    tk.Button(
        root,
        text="Reset Game",
        font=("Helvetica", 10),
        command=self.reset_game,
        bg="#95a5a6",
        fg="white",
    ).pack(pady=15)

  def play(self, user_choice):
    computer_choice = random.choice(self.choices)

    if user_choice == computer_choice:
      result = f"It's a Tie!\nBoth chose {user_choice}."
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
      result = (
          f"You Win! 🎉\n{user_choice} beats {computer_choice}."
      )
      self.user_score += 1
    else:
      result = f"Computer Wins! 🤖\n{computer_choice} beats {user_choice}."
      self.computer_score += 1

    self.result_label.config(text=result)
    self.score_label.config(
        text=f"Player: {self.user_score}  |  Computer: {self.computer_score}"
    )

  def reset_game(self):
    self.user_score = 0
    self.computer_score = 0
    self.score_label.config(text="Player: 0  |  Computer: 0")
    self.result_label.config(text="Game Reset! Choose your move.")


if __name__ == "__main__":
  root = tk.Tk()
  app = RockPaperScissorsApp(root)
  root.mainloop()