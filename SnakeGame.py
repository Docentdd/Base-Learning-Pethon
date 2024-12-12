#That code's game provided by book writen by Marcin Moskala 12.12.2024
import pygame
pygame.init()
cube_size = 25
cubes_num = 20
width = cube_size * cubes_num
screen = pygame.display.set_mode((width, width))
pygame.display.set_caption("Snale Game")
screen.fill((255, 255, 255))
pygame.display.update()

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return isinstance(other, Position) and self.x == other.x and self.y == other.y
    def __str__(self):
        return f"({self.x}, {self.y})"
    __repr__ = __str__

class GameState:
    def __init__(self, snake, direction, food, field_size):
        self.snake = snake
        self.direction = direction
        self.food = food
        self.field_size = field_size

    def next_head(self, direction):
        pos = self.snake[-1]
        if direction == Direction.UP:
            return(pos.x, pos.y - 1)
        if direction == Direction.DOWN:
            return(pos.x, pos.y + 1)
        if direction == Direction.LEFT:
            return(pos.x - 1, pos.y)
        if direction == Direction.RIGHT:
            return(pos.x, pos.y + 1)
    def step(self):
        new_head = self.next_head(self.direction)
        self.snake.append(new_head)
        self.snake = self.snake[:-1]


class Direction:
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

def draw_snake(snake):
    for part in snake:
        draw_snake_part(part)


def draw_snake_part(pos):
    position = (pos.x * cube_size, pos.y * cube_size, cube_size, cube_size)
    pygame.draw.rect(screen, (0, 255, 0), position)


def draw_food(pos):
    radius = cube_size /2
    position = (pos.x * cube_size + radius, pos.y * cube_size + radius)
    pygame.draw.circle(screen, (0, 0, 0), position, radius)

def draw(snake, food):
    screen.fill((255, 255, 255))
    draw_snake(snake)
    draw_food(food)
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
