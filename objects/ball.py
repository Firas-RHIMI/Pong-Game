import pygame

VELOCITY_X = 0
VELOCITY_Y = 3
MAX_Y_VELOCITY = 9
RED = (255, 0, 0)
INCREASE_SPEED_FACTOR = 1.05


class Ball:
    def __init__(self, x, y, radius):
        self.reset_x = x
        self.reset_y = y
        self.x = x
        self.y = y
        self.velocity_x = VELOCITY_X
        self.velocity_y = VELOCITY_Y
        self.radius = radius

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

    def paddle_collision(self, paddle):
        if ((paddle.y == 0) and (self.y_min <= paddle.size[1])) or \
                ((paddle.y > 0) and (self.y_max >= paddle.y)):
            if paddle.x <= self.x <= paddle.x_limit:
                if self.velocity_y < MAX_Y_VELOCITY:
                    self.velocity_y *= -INCREASE_SPEED_FACTOR
                else:
                    self.velocity_y *= -1
                deviation_factor = self.x - paddle.x_center
                self.velocity_x = deviation_factor/10
                pygame.mixer.Sound.play(pygame.mixer.Sound("../objects/collision_effect.wav"))

    def border_collision(self, border):
        if self.y_min > border.up_limit and self.y_max < border.low_limit:
            if self.x_min <= border.left_limit or self.x_max >= border.right_limit:
                self.velocity_x *= -1

    def is_out_of_bounds_up(self):
        return self.y_min <= 0

    def is_out_of_bounds_down(self, limit_height):
        return self.y_max >= limit_height

    def is_out_of_bounds(self, limit_height):
        return self.is_out_of_bounds_up() or self.is_out_of_bounds_down(limit_height)

    def reset(self, limit_height):
        if self.is_out_of_bounds(limit_height):
            self.velocity_y = VELOCITY_Y
            self.velocity_x = VELOCITY_X
            self.x = self.reset_x
            self.y = self.reset_y
            return True
        return








