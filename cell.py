class Cell:
    def __init__(self, has_bomb):
        self.numbers_around = None
        self.neighbors = None
        self.has_bomb = has_bomb
        self.clicked = False
        self.flagged = False

    def get_has_bomb(self):
        return self.has_bomb

    def get_clicked(self):
        return self.clicked

    def get_flagged(self):
        return self.flagged

    def get_numbers_around(self):
        return self.numbers_around

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors
        self.set_numbers_around()

    def set_numbers_around(self):
        self.numbers_around = 0
        for cell in self.neighbors:
            if cell.get_has_bomb():
                self.numbers_around += 1

    def toggle_flag(self):
        self.flagged = not self.flagged

    def click(self):
        self.clicked = True

    def get_neighbors(self):
        return self.neighbors
