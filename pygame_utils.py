import pygame
from constants import *
from objects.border import Border
from objects.paddle import Paddle
from objects.ball import Ball
from objects.score import Score
import random


def draw_court(window):
    window.fill(BLACK)


def display_winner(window, size, text, color, location):
    text = pygame.font.SysFont("comicsans", size).render(text, 1, color)
    window.blit(text, text.get_rect(center=location))
    pygame.display.update()
    pygame.time.wait(2000)


def draw_frame(window, objects):
    draw_court(window)
    for element in objects:
        element.draw(window)
    pygame.display.update()


def random_ball_position_training():
    height = HEIGHT - 2 * PADDLE_SIZE[1]
    width = random.randrange(WIDTH//2 - WIDTH // 4, WIDTH // 2 + WIDTH // 4)
    return width, height


def game_setup(training=False):
    clock = pygame.time.Clock()
    border = Border(BORDER_WIDTH, HEIGHT, WIDTH)
    paddle_1 = Paddle(WIDTH // 2 - PADDLE_SIZE[0] // 2, HEIGHT - PADDLE_SIZE[1], PADDLE_SIZE)
    paddle_2 = Paddle(WIDTH // 2 - PADDLE_SIZE[0] // 2, 0, PADDLE_SIZE)
    if training:
        width, height = random_ball_position_training()
        ball = Ball(width, height, BALL_RADIUS)
        ball.velocity_y = - ball.velocity_y
    else:
        ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)
    score_1 = Score(paddle_1, ball, border, hits_score=training)
    score_2 = Score(paddle_2, ball, border, hits_score=training)
    return clock, border, paddle_1, paddle_2, ball, score_1, score_2


def start_screen(window):
    game_started = False
    has_quit = False
    is_two_player_mode = False
    while not game_started and not has_quit:
        window.fill(BLACK)
        title = pygame.font.SysFont("comicsans", TITLE_SIZE).render("PONG GAME", 1, RED)
        description1 = pygame.font.SysFont("comicsans", DESCRIPTION_SIZE).render(
            "First player to reach 5 points win",
            1, BLUE)
        description2 = pygame.font.SysFont("comicsans", DESCRIPTION_SIZE).render(
            "use arrows to move player1, Q and D to move player2",
            1, BLUE)
        one_player_mode = pygame.font.SysFont("comicsans", SUB_TITLE_SIZE).render(
            "Press 1 to play against AI", 1, WHITE)
        two_player_mode = pygame.font.SysFont("comicsans", SUB_TITLE_SIZE).render(
            "Press 2 to play against a friend", 1, WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                has_quit = True
                break
            key = pygame.key.get_pressed()
            if key[pygame.K_2]:
                game_started = True
                is_two_player_mode = True
            elif key[pygame.K_1]:
                game_started = True
            window.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 10)))
            window.blit(description1, description1.get_rect(center=(WIDTH // 2, HEIGHT // 4)))
            window.blit(description2, description2.get_rect(center=(WIDTH // 2, HEIGHT // 3)))
            window.blit(one_player_mode, one_player_mode.get_rect(center=(WIDTH // 2, 2 * HEIGHT // 3)))
            window.blit(two_player_mode, two_player_mode.get_rect(center=(WIDTH // 2, 3 * HEIGHT // 4)))
            pygame.display.update()
    return is_two_player_mode, has_quit
