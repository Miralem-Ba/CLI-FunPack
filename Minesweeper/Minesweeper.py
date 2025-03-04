import random
import tkinter as tk
from tkinter import messagebox

class Minesweeper:
    def __init__(self, master, size=10, mines=10):
        self.master = master
        self.size = size
        self.mines = mines
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.buttons = [[None for _ in range(size)] for _ in range(size)]
        self.revealed = [[False for _ in range(size)] for _ in range(size)]
        
        self.place_mines()
        self.calculate_numbers()
        self.create_widgets()
    
    def place_mines(self):
        positions = random.sample(range(self.size * self.size), self.mines)
        for pos in positions:
            row, col = divmod(pos, self.size)
            self.board[row][col] = -1
    
    def calculate_numbers(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == -1:
                    continue
                count = 0
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        r, c = row + i, col + j
                        if 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == -1:
                            count += 1
                self.board[row][col] = count
    
    def create_widgets(self):
        for row in range(self.size):
            for col in range(self.size):
                btn = tk.Button(self.master, width=3, height=1, command=lambda r=row, c=col: self.reveal(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn
    
    def reveal(self, row, col):
        if self.revealed[row][col]:
            return
        self.revealed[row][col] = True
        self.buttons[row][col].config(text=str(self.board[row][col]) if self.board[row][col] > 0 else '', state='disabled')
        
        if self.board[row][col] == -1:
            self.buttons[row][col].config(text='*', bg='red')
            messagebox.showinfo("Game Over", "You hit a mine!")
            self.master.quit()
        elif self.board[row][col] == 0:
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    r, c = row + i, col + j
                    if 0 <= r < self.size and 0 <= c < self.size:
                        self.reveal(r, c)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minesweeper")
    game = Minesweeper(root)
    root.mainloop()
