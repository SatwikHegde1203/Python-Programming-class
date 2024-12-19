import tkinter as tk
from tkinter import messagebox
from main import HorrorAdventureGame

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Horror Adventure Game")

        # Initialize the game logic
        self.game = HorrorAdventureGame()

        # Label to display the story text
        self.text_output = tk.Label(root, text="Welcome to the Horror Adventure Game!", font=("Helvetica", 14), wraplength=400)
        self.text_output.pack(pady=20)

        self.choice_buttons = []  # Holds all buttons for choices
        self.start_button = tk.Button(root, text="Start Game", font=("Helvetica", 12), command=self.start_game)
        self.start_button.pack(pady=10)

    def start_game(self):
        # Start the game and get the first outcome and choices
        outcome, choices = self.game.start_game()
        self.update_screen(outcome, choices)

        # Hide the Start button after game starts
        self.start_button.pack_forget()

    def update_screen(self, outcome, choices):
        # Update the text to reflect the current situation
        self.text_output.config(text=outcome)
        self.clear_buttons()

        # Create a button for each choice
        for idx, choice in enumerate(choices):
            button = tk.Button(self.root, text=choice, font=("Helvetica", 12), command=lambda c=choice: self.on_choice_made(c))
            button.pack(pady=5)

    def on_choice_made(self, choice):
        # Determine the corresponding game function based on the player's choice
        if choice == "Move toward the light":
            outcome, choices = self.game.move_toward_light()
        elif choice == "Stay in the dark room":
            outcome, choices = self.game.stay_in_dark_room()
        elif choice == "Enter the first door":
            outcome, choices = self.game.enter_first_door()
        elif choice == "Keep walking down the hallway":
            outcome, choices = self.game.keep_walking()
        elif choice == "Try to open the door":
            outcome, choices = self.game.try_open_door()
        elif choice == "Search for an escape route":
            outcome, choices = self.game.search_escape_route()
        elif choice == "Inspect the object":
            outcome, choices = self.game.inspect_object()
        elif choice == "Search for a key":
            outcome, choices = self.game.search_for_key()
        elif choice == "Confront the figure":
            outcome, choices = self.game.confront_figure()
        elif choice == "Turn around and run":
            outcome, choices = self.game.run_away()
        elif choice == "Touch the doll":
            outcome, choices = self.game.touch_doll()
        elif choice == "Leave the room":
            outcome, choices = self.game.leave_room()

        self.update_screen(outcome, choices)

    def clear_buttons(self):
        # Clear all the previous choice buttons from the screen
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button) and widget != self.start_button:
                widget.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    game_gui = GameGUI(root)
    root.geometry("600x250")
    root.mainloop()
