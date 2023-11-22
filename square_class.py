import pygame

# Class for a square in the game which could represent a part of the snake
# or food.
class Square():
    def __init__(self, pos):
        # Constructor
        self.pos = pos

    def move(self, changeX, changeY):
        # Moves the position of the square
        self.pos = [self.pos[0]+changeX, self.pos[1]+changeY]

    def changePos(self, pos):
        # Changes the position of the square
        self.pos = pos

    def draw(self, window, screen_width, screen_height, cols, rows, color):
        # Draws the square
        col_width = screen_width//cols
        row_width = screen_height//rows

        x = self.pos[0]
        y = self.pos[1]

        pygame.draw.rect(window, color, pygame.Rect(x*col_width, y*row_width,
                                                        col_width, row_width))
