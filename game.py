import pygame
import os


class Game:
    def __init__(self, board, screen_size):
        self.screen = None
        self.images = None
        self.board = board
        self.screen_size = screen_size
        self.cell_size = self.screen_size[0] // self.board.get_size()[1], self.screen_size[1] // self.board.get_size()[0]
        self.load_images()

    def run(self):
        self.screen = pygame.display.set_mode(self.screen_size)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    right_click = pygame.mouse.get_pressed()[2]
                    self.handle_click(position, right_click)
            self.draw()
            pygame.display.flip()
            if self.board.get_won():
                print('won')
                running = False
        pygame.quit()

    def draw(self):
        top_left = (0, 0)
        for row in range(self.board.get_size()[0]):
            for col in range(self.board.get_size()[1]):
                image = self.images['empty-block']
                cell = self.board.get_cell((row, col))
                image = self.get_image(cell)
                self.screen.blit(image, top_left)
                top_left = top_left[0] + self.cell_size[0], top_left[1]
            top_left = 0, top_left[1] + self.cell_size[1]

    def load_images(self):
        self.images = {}
        for file_name in os.listdir("images"):
            if not file_name.endswith(".png"):
                continue
            image = pygame.image.load(r"images/" + file_name)
            image = pygame.transform.scale(image, self.cell_size)
            self.images[file_name.split('.')[0]] = image

    def get_image(self, cell):
        string = None
        if cell.get_clicked():
            string = 'bomb-at-clicked-block' if cell.get_has_bomb() else str(cell.get_numbers_around())
        else:
            string = 'flag' if cell.get_flagged() else 'empty-block'
        return self.images[string]

    def handle_click(self, position, right_click):
        if self.board.get_lost():
            return
        index = position[1] // self.cell_size[1], position[0] // self.cell_size[0]
        cell = self.board.get_cell(index)
        self.board.handle_click(cell, right_click)
