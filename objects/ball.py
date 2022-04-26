import pygame
from random import random

VELOCITY_Y = 5
MAX_Y_VELOCITY = 15
RED = (255, 0, 0)
INCREASE_SPEED_FACTOR = 1.05


class Ball:
    def __init__(self, x, y, radius):
        self.reset_x = x
        self.reset_y = y
        self.radius = radius
        self.x = x
        self.y = y
        self.velocity_x = self.random_velocity_x()
        self.velocity_y = VELOCITY_Y

    @property
    def x_min(self):
        return self.x - self.radius

    @property
    def x_max(self):
        return self.x + self.radius

    @property
    def y_min(self):
        return self.y - self.radius

    @property
    def y_max(self):
        return self.y + self.radius

    def draw(self, window):
        pygame.draw.circle(window, RED, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def paddle_collision(self, paddle, border,  training=False):
        if ((paddle.y == 0) and (self.y_min <= paddle.size[1])) or \
                ((paddle.y > 0) and (self.y_max >= paddle.y)):
            if paddle.x <= self.x <= paddle.x_limit:
                if self.velocity_y < MAX_Y_VELOCITY:
                    self.velocity_y *= -INCREASE_SPEED_FACTOR
                else:
                    self.velocity_y *= -1
                deviation_factor = self.x - paddle.x_center
                self.update_velocity_x_post_paddle_collision(deviation_factor, border, paddle)
                if not training:
                    pygame.mixer.Sound.play(pygame.mixer.Sound("objects/collision_effect.wav"))
                paddle.nb_hits += 1
                if paddle.y == 0:
                    self.y = paddle.size[1] + self.radius
                else:
                    self.y = paddle.y - self.radius

    def update_velocity_x_post_paddle_collision(self, deviation_to_center, border, paddle):
        tan_max_angle = (border.window_width - paddle.size[0] / 2) / (border.height - paddle.size[1])
        self.velocity_x = tan_max_angle * deviation_to_center * abs(self.velocity_y) / (
                paddle.size[0] / 2)

    def border_collision(self, border):
        if self.y_min > border.up_limit and self.y_max < border.low_limit:
            if self.x_min <= border.left_limit:
                self.velocity_x *= -1
                self.x = border.left_limit + self.radius
            if self.x_max >= border.right_limit:
                self.velocity_x *= -1
                self.x = border.right_limit - self.radius

    def is_out_of_bounds_up(self):
        return self.y_min <= 0

    def is_out_of_bounds_down(self, limit_height):
        return self.y_max >= limit_height

    def is_out_of_bounds(self, limit_height):
        return self.is_out_of_bounds_up() or self.is_out_of_bounds_down(limit_height)

    def reset(self, limit_height, paddle_1, paddle_2):
        if self.is_out_of_bounds(limit_height):
            self.velocity_y = VELOCITY_Y
            self.velocity_x = self.random_velocity_x()
            self.x = self.reset_x
            self.y = self.reset_y
            paddle_1.reset()
            paddle_2.reset()
            return True

    @staticmethod
    def random_velocity_x():
        if random() < 0.4:
            return 1
        elif random() < 0.8:
            return -1
        else:
            return 0

    def distance_to_paddle(self, paddle):
        return (self.x - paddle.x_center) ** 2 + (self.y - paddle.y_limit) ** 2

    def interact_with_environment(self, paddle_1, paddle_2, border, training=False):
        self.move()
        self.paddle_collision(paddle_1, border, training)
        self.paddle_collision(paddle_2, border, training)
        self.border_collision(border)









