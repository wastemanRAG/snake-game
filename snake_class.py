import pygame
from square_class import Square

# Class for the snake
class Snake():
    def __init__(self, front):
        # Constructor
        self.front = Square(front)
        self.body = [self.front]
        self.last_move = (0, 0)
        self.removed_pos = [front[0]-1, front[1]]

    def addPiece(self):
        # Adds one square to the length of the snake
        temp_sq = Square(self.removed_pos)
        self.body.append(temp_sq)

    def move(self):
        # Changes a few variables of this class(instance/object) to imitate
        # the snake moving.
        temp = self.front.pos
        temp2 = []

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.last_move != (0, 1):
                self.last_move = (0, -1)

        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.last_move != (0, -1):
                self.last_move = (0, 1)

        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.last_move != (1, 0):
                self.last_move = (-1, 0)

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.last_move != (-1, 0):
                self.last_move = (1, 0)

        if self.last_move != (0, 0):
            self.front.move(self.last_move[0], self.last_move[1])

            for i in range(1, len(self.body)):
                temp2 = self.body[i].pos
                self.body[i].changePos(temp)
                temp = temp2.copy()
            self.removed_pos = temp

            return True
        else: return False

    def collision(self, apples, cols, rows):
        # Checks if the snake is on an apple or if the snake has hit the edges.
        for i in range(len(apples)):
            if self.front.pos == apples[i].pos:
                self.addPiece()
                del apples[i]
                return 1

        if self.front.pos[0] >= cols or self.front.pos[0] < 0 \
            or self.front.pos[1] >= rows \
            or self.front.pos[1] < 0:
                return 0

        elif self.front.pos in [x.pos for x in self.body[1:]]:
            return 0


    def draw(self, window, screen_width, screen_height, cols, rows, snake_color):
        # Draws the snake
        for sq in self.body:
            sq.draw(window, screen_width, screen_height, cols, rows, snake_color)

        col_width = screen_width//cols
        row_width = screen_height//rows

        front_pos = self.front.pos
        radius = 4

        if self.last_move == (0, 0):
            tempX = (front_pos[0]+1)*col_width - radius
            tempY = round((front_pos[1]+0.5)*row_width)

            pygame.draw.circle(window, (0, 0, 0), (tempX, tempY - radius - 1),
                                                                        radius)
            pygame.draw.circle(window, (0, 0, 0), (tempX, tempY + radius + 1),
                                                                        radius)

        elif self.last_move[0] == 0:
            if self.last_move[1] == 1:
                tempX = (front_pos[0]+0.5)*col_width
                tempY = round((front_pos[1]+1)*row_width) - radius
            else:
                tempX = (front_pos[0]+0.5)*col_width
                tempY = round(front_pos[1]*row_width)  + radius

            pygame.draw.circle(window, (0, 0, 0), (tempX - radius - 1, tempY),
                                                                        radius)
            pygame.draw.circle(window, (0, 0, 0), (tempX + radius + 1, tempY),
                                                                        radius)

        else:
            if self.last_move[0] == 1:
                tempX = (front_pos[0]+1)*col_width - radius
                tempY = round((front_pos[1]+0.5)*row_width)
            else:
                tempX = front_pos[0]*col_width + radius
                tempY = round((front_pos[1]+0.5)*row_width)

            pygame.draw.circle(window, (0, 0, 0), (tempX, tempY - radius - 1),
                                                                        radius)
            pygame.draw.circle(window, (0, 0, 0), (tempX, tempY + radius + 1),
                                                                        radius)
