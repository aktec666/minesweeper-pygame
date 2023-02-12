from cell import Cell
from random import random


class Board:
    def __init__(self, size, prob):
        self.board = None
        self.size = size
        self.prob = prob
        self.lost = False
        self.won = False
        self.numbers_click = 0
        self.numbers_none_bombs = 0
        self.set_board()

    def set_board(self):
        self.board = []
        for row in range(self.size[0]):
            row = []
            for col in range(self.size[1]):
                has_bomb = random() < self.prob
                if not has_bomb:
                    self.numbers_none_bombs += 1
                cell = Cell(has_bomb)
                row.append(cell)
            self.board.append(row)
        self.set_neighbors()

    def set_neighbors(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                cell = self.get_cell((row, col))
                neighbors = self.get_list_of_neighbors((row, col))
                cell.set_neighbors(neighbors)

    def get_list_of_neighbors(self, index):
        neighbors = []
        for row in range(index[0] - 1, index[0] + 2):
            for col in range(index[1] - 1, index[1] +2):
                out_of_bounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]
                same = row == index[0] and col == index[1]
                if same or out_of_bounds:
                    continue
                neighbors.append(self.get_cell((row, col)))
        return neighbors

    def get_size(self):
        return self.size

    def get_cell(self, index):
        return self.board[index[0]][index[1]]

    def handle_click(self, cell, right_click):
        if cell.get_clicked() or (not right_click and cell.get_flagged()):
            return
        elif right_click:
            cell.toggle_flag()
            return
        cell.click()
        if cell.get_has_bomb():
            self.lost = True
            return
        self.numbers_click += 1
        if cell.get_numbers_around() != 0:
            return
        for neighbor in cell.get_neighbors():
            if not neighbor.get_has_bomb() and not neighbor.get_clicked():
                self.handle_click(neighbor, False)
                neighbor.click()

    def get_won(self):
        return self.numbers_none_bombs == self.numbers_click

    def get_lost(self):
        return self.lost
