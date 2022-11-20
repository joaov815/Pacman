import pygame

from colors import YELLOW, BLACK
from game_element import GameElement


class Pacman(GameElement):
    def __init__(self, size):
        self.column = 1
        self.line = 1

        self.center_x = 400
        self.center_y = 300

        self.size = size
        self.radius = self.size // 2  # 13

        self.vel_x = 0
        self.vel_y = 0
        self.key_pressed = None

    def calculate_rules(self, scenario):
        if scenario.approved_move(self.column + self.vel_x, self.line + self.vel_y):
            self.column += self.vel_x
            self.line += self.vel_y

            self.center_x = self.column * self.size + self.radius
            self.center_y = self.line * self.size + self.radius

    def draw(self, _screen):
        # Body
        pygame.draw.circle(_screen, YELLOW, (self.center_x, self.center_y), self.radius)

        # Mouth
        pygame.draw.polygon(_screen, BLACK, [
            (self.center_x, self.center_y),
            (self.center_x + self.radius, self.center_y),
            (self.center_x + self.radius, self.center_y - self.radius)
        ])

        # Eye
        pygame.draw.circle(_screen, BLACK,
                           [int(self.center_x + self.radius / 5), int(self.center_y - self.radius * 0.6)], 3)

    def process_events(self, events):
        # Capture events
        for event in events:
            if event.type == pygame.KEYDOWN and self.key_pressed is None:
                if event.key == pygame.K_RIGHT:
                    self.vel_x = 1
                elif event.key == pygame.K_LEFT:
                    self.vel_x = -1
                elif event.key == pygame.K_UP:
                    self.vel_y = -1
                elif event.key == pygame.K_DOWN:
                    self.vel_y = 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.vel_x = 0
                elif event.key == pygame.K_LEFT:
                    self.vel_x = 0
                elif event.key == pygame.K_UP:
                    self.vel_y = 0
                elif event.key == pygame.K_DOWN:
                    self.vel_y = 0

    # def process_mouse_events(self, events):
    #     for event in events:
    #         if event.type == pygame.MOUSEMOTION:
    #             mouse_x, mouse_y = event.pos
    #
    #             self.column = (mouse_x - self.center_x) / 100
    #             self.line = (mouse_y - self.center_y) / 100
