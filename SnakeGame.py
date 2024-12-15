#That code's game provided by book writen by Marcin Moskala 12.12.2024
import pygame
from random import randint
pygame.init()
cube_size = 25
cubes_num = 20
width = cube_size * cubes_num
screen = pygame.display.set_mode((width, width))
pygame.display.set_caption("Snake Game")
screen.fill((255, 255, 255))
pygame.display.update()

class Direction:
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return isinstance(other, Position) and self.x == other.x and self.y == other.y
    def __str__(self):
        return f"({self.x}, {self.y})"
    __repr__ = __str__


INITIAL_SNAKE = [Position(1, 2), Position(2, 2), Position(3, 2)]
INITIAL_DIRECTION = Direction.RIGHT

class GameState:
    def __init__(self, snake=None, direction=None, food=None, field_size=cubes_num):
        self.field_size = field_size
        self.snake = snake if snake else INITIAL_SNAKE[:]
        self.direction = direction if direction else INITIAL_DIRECTION
        self.food = food
        self.initial_position()

    def next_head_position(self, direction):
        pos = self.snake[-1]
        if direction == Direction.UP:
            return Position(pos.x, (pos.y - 1) % self.field_size)
        elif direction == Direction.DOWN:
            return Position(pos.x, (pos.y + 1) % self.field_size)
        elif direction == Direction.RIGHT:
            return Position((pos.x + 1) % self.field_size, pos.y)
        elif direction == Direction.LEFT:
            return Position((pos.x - 1) % self.field_size, pos.y)
    def initial_position(self):
        self.snake = INITIAL_SNAKE[:]
        self.direction = INITIAL_DIRECTION
        self.set_random_food_position()

    def step_move_snake(self):
        new_head = self.next_head_position(self.direction)
        if new_head in self.snake:  # Collision with itself
            self.initial_position()
            return
        self.snake.append(new_head)
        if new_head == self.food:  # Eating food
            self.set_random_food_position()
        else:
            self.snake.pop(0)
    def set_random_food_position(self):
        self.food = Position(randint(0, self.field_size - 1), randint(0, self.field_size - 1))
        while True:
            self.food = Position(randint(0, self.field_size - 1), randint(0, self.field_size - 1))
            if self.food not in self.snake:
                break

    def turn(self, direction):
        if self.can_turn(direction):
            self.direction = direction

    def can_turn(self, direction):
        new_head = self.next_head_position(direction)
        return new_head != self.snake[-2]

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

state = GameState()
clock = pygame.time.Clock()
while True:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                state.turn(Direction.LEFT)

            elif event.key == pygame.K_RIGHT:
                state.turn(Direction.RIGHT)

            elif event.key == pygame.K_UP:
                state.turn(Direction.UP)

            elif event.key == pygame.K_DOWN:
                state.turn(Direction.DOWN)

    state.step_move_snake()
    draw(state.snake, state.food)
