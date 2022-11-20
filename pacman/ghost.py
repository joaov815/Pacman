import pygame.draw
import directions
import random

from game_element import GameElement
from colors import WHITE, BLACK


class Ghost(GameElement):
    def __init__(self, color, size):
        self.column = 6
        self.line = 2
        self.color = color
        self.size = size
        self.slice = self.size // 8
        self.vel = 1
        self.direction = directions.DOWN

    def process_events(self, events):
        pass

    def calculate_rules(self, scenario):
        available_directions = scenario.get_available_moves_list((self.column, self.line))

        if len(available_directions) >= 3 or self.direction not in available_directions:
            self.direction = random.choice(available_directions)

        if self.direction == directions.UP:
            self.line -= self.vel
        elif self.direction == directions.DOWN:
            self.line += self.vel
        elif self.direction == directions.RIGHT:
            self.column += self.vel
        elif self.direction == directions.LEFT:
            self.column -= self.vel

    def draw(self, screen):
        top_left_x = self.column * self.size
        top_left_y = self.line * self.size

        self.draw_body(screen, top_left_x, top_left_y)
        self.draw_eyes(screen, top_left_x, top_left_y)

    def draw_body(self, screen, top_left_x, top_left_y):
        outline = [
            (top_left_x, top_left_y + self.size),
            (top_left_x + self.slice, top_left_y + 2 * self.slice),
            (top_left_x + 2 * self.slice, top_left_y + self.slice // 2),
            (top_left_x + 3 * self.slice, top_left_y),
            (top_left_x + 5 * self.slice, top_left_y),
            (top_left_x + 6 * self.slice, top_left_y + self.slice // 2),
            (top_left_x + 7 * self.slice, top_left_y + 2 * self.slice),
            (top_left_x + self.size, top_left_y + self.size),
        ]

        pygame.draw.polygon(screen, self.color, outline, 0)

    def draw_eyes(self, screen, top_left_x, top_left_y):
        external_radius = self.slice
        internal_radius = self.slice // 2

        left_center_x = int(top_left_x + self.slice * 2.5)
        right_center_x = int(top_left_x + self.slice * 5.5)

        center_y = int(top_left_y + self.slice * 2.5)

        # Left
        pygame.draw.circle(screen, WHITE, (left_center_x, center_y), external_radius)
        pygame.draw.circle(screen, BLACK, (left_center_x, center_y), internal_radius)

        # Right
        pygame.draw.circle(screen, WHITE, (right_center_x, center_y), external_radius)
        pygame.draw.circle(screen, BLACK, (right_center_x, center_y), internal_radius)
