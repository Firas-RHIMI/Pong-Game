import pygame

VELOCITY = 5
WHITE = (255, 255, 255)


class Paddle:
    def __init__(self, x, y, size):
        self.reset_x = x
        self.reset_y = y
        self.x = x
        self.y = y
        self.velocity = VELOCITY
        self.size = size
        self.score = 0
        self.nb_hits = 0

    @property
    def x_center(self):
        return (2 * self.x + self.size[0]) // 2

    @property
    def y_limit(self):
        if self.y == 0:
            return self.size[1]
        else:
            return self.y

    @property
    def x_limit(self):
        return self.x + self.size[0]

    def draw(self, window):
        pygame.draw.rect(window, WHITE,
                         [self.x, self.y, self.size[0], self.size[1]])

    def move(self, right=True):
        if right:
            self.x += VELOCITY
        else:
            self.x -= VELOCITY

    def reset(self):
        self.x = self.reset_x
        self.y = self.reset_y

    def keyboard_interaction(self, keys, border, is_lower_paddle=True):
        if is_lower_paddle:
            if keys[pygame.K_LEFT] and self.x > border.left_limit:
                self.move(right=False)
            if keys[pygame.K_RIGHT] and self.x_limit < border.right_limit:
                self.move(right=True)
        else:
            if keys[pygame.K_q] and self.x > border.left_limit:
                self.move(right=False)
            if keys[pygame.K_d] and self.x_limit < border.right_limit:
                self.move(right=True)

    def agent_interaction(self, agent_decision, border, is_lower_paddle):
        if is_lower_paddle:
            if agent_decision == "left" and self.x > border.left_limit:
                self.move(right=False)
            if agent_decision == "right" and self.x_limit < border.right_limit:
                self.move(right=True)
        else:
            if agent_decision == "right" and self.x > border.left_limit:
                self.move(right=False)
            if agent_decision == "left" and self.x_limit < border.right_limit:
                self.move(right=True)






