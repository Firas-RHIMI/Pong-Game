import pygame

COLOR = (0, 0, 255)


class Border:
    def __init__(self, width, height, window_width):
        self.width = width
        self.height = height
        self.window_width = window_width
        self.left_limit = width
        self.right_limit = window_width - width
        self.up_limit = 0
        self.low_limit = height

    def draw(self, window):
        pygame.draw.rect(window, COLOR, [0, 0, self.width, self.height])
        pygame.draw.rect(window, COLOR, [self.window_width - self.width, 0, self.width, self.height])

