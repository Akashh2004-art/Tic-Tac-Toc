import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Colorful Tic Tac Toe")

        self.current_turn = 'X'  # X starts first
        self.board = [' ' for _ in range(9)]  # Single 3x3 board

        # Define colors for players
        self.colors = {
            'X': 'lightblue',
            'O': 'lightcoral',
            '': 'white'  # Default button color
        }

        # Create buttons for each cell in the grid
        self.buttons = [tk.Button(master, text=' ', font=("Helvetica", 20), width=5, height=2,
                            bg=self.colors[''], command=lambda i=i: self.make_move(i)) for i in range(9)]
        
        # Arrange buttons in a 3x3 grid
        for i, button in enumerate(self.buttons):
            row = i // 3
            col = i % 3
            button.grid(row=row, column=col, padx=5, pady=5)

        # Restart button
        self.restart_button = tk.Button(master, text="Restart", font=("Helvetica", 14), command=self.restart_game)
        self.restart_button.grid(row=3, column=0, columnspan=3, pady=10)

    def make_move(self, index):
        if self.board[index] == ' ':
            self.board[index] = self.current_turn
            self.buttons[index].config(text=self.current_turn, bg=self.colors[self.current_turn])
            if self.check_winner():
                self.display_winner()
            else:
                self.current_turn = 'O' if self.current_turn == 'X' else 'X'

    def check_winner(self):
        # Check rows, columns, and diagonals
        wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6)]
        
        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return True
        return False

    def display_winner(self):
        winner = self.current_turn
        for button in self.buttons:
            button.config(state='disabled')  # Disable buttons
        result_window = tk.Toplevel(self.master)
        result_window.title("Game Over")
        label = tk.Label(result_window, text=f"{winner} Wins!", font=("Helvetica", 24))
        label.pack(pady=20)
        button = tk.Button(result_window, text="Close", command=result_window.destroy)
        button.pack(pady=10)

    def restart_game(self):
        # Reset the game state
        self.current_turn = 'X'
        self.board = [' ' for _ in range(9)]
        for button in self.buttons:
            button.config(text=' ', bg=self.colors[''], state='normal')  # Reset button states

if __name__ == "__main__":
    root = tk.Tk()
    tic_tac_toe = TicTacToe(root)
    root.geometry("300x380")
    root.mainloop()
