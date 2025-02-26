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
    
    