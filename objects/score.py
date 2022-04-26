import pygame

WHITE = (255, 255, 255)
TEXT_SIZE = 30
WINNING_SCORE = 5


class Score:
    def __init__(self, paddle, ball, border, hits_score=False):
        self.value = 0
        self.paddle = paddle
        self.ball = ball
        self.is_lower_paddle = self.paddle.y > 0
        self.border = border
        self.window_height = border.height
        self.hits_score = hits_score

    def update(self):
        if (not self.is_lower_paddle and self.ball.is_out_of_bounds_down(self.window_height)) or \
                (self.is_lower_paddle and self.ball.is_out_of_bounds_up()):
            self.value += 1

    def draw(self, window):
        if self.is_lower_paddle:
            text_position = (self.border.right_limit, 3 * self.window_height // 4)
        else:
            text_position = (self.border.right_limit, self.window_height // 4)
        if self.hits_score:
            window.blit(pygame.font.SysFont("comicsans", TEXT_SIZE).render(f"{self.paddle.nb_hits}", 1, WHITE),
                        text_position)
        else:
            window.blit(pygame.font.SysFont("comicsans", TEXT_SIZE).render(f"{self.value}", 1, WHITE),
                        text_position)

    def is_winning_score(self):
        return self.value == WINNING_SCORE

    def reset(self):
        self.value = 0



