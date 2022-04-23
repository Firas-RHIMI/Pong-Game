import pygame
from objects.border import Border
from objects.paddle import Paddle
from objects.ball import Ball
from objects.score import Score
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 620
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
BORDER_WIDTH = 20
PADDLE_SIZE = (100, 10)
BALL_RADIUS = 8
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 255, 255)
FPS = 60
TITLE_SIZE = 40
SUB_TITLE_SIZE = 20
DESCRIPTION_SIZE = 15

# Game Title
pygame.display.set_caption("Pong Game")


def draw_court(window):
    window.fill(BLACK)


def draw_frame(window, objects):
    draw_court(window)
    for element in objects:
        element.draw(window)
    pygame.display.update()


def start_screen():
    game_started = False
    has_quit = False
    is_two_player_mode = False
    while not game_started and not has_quit:
        WINDOW.fill(BLACK)
        title = pygame.font.SysFont("comicsans", TITLE_SIZE).render("PONG GAME", 1, RED)
        description1 = pygame.font.SysFont("comicsans", DESCRIPTION_SIZE).render(
            "First player to reach 3 points win",
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
            WINDOW.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 10)))
            WINDOW.blit(description1, description1.get_rect(center=(WIDTH // 2, HEIGHT // 4)))
            WINDOW.blit(description2, description2.get_rect(center=(WIDTH // 2, HEIGHT // 3)))
            WINDOW.blit(one_player_mode, one_player_mode.get_rect(center=(WIDTH // 2, 2 * HEIGHT // 3)))
            WINDOW.blit(two_player_mode, two_player_mode.get_rect(center=(WIDTH // 2, 3 * HEIGHT // 4)))
            pygame.display.update()
    return is_two_player_mode, has_quit


def run():
    replay = True
    while replay:
        is_two_player_mode, has_quit = start_screen()
        if has_quit:
            break
        elif is_two_player_mode:
            is_playing = True
            clock = pygame.time.Clock()
            border = Border(BORDER_WIDTH, HEIGHT, WIDTH)
            paddle_1 = Paddle(WIDTH // 2 - PADDLE_SIZE[0] // 2, HEIGHT - PADDLE_SIZE[1], PADDLE_SIZE)
            paddle_2 = Paddle(WIDTH // 2 - PADDLE_SIZE[0] // 2, 0, PADDLE_SIZE)
            ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)
            score_1 = Score(paddle_1, ball, border)
            score_2 = Score(paddle_2, ball, border)
            while is_playing:
                draw_frame(WINDOW, [border, paddle_1, paddle_2, ball, score_1, score_2])
                clock.tick(FPS)

                if score_1.is_winning_score():
                    text = pygame.font.SysFont("comicsans", TITLE_SIZE).render("Player 1 won", 1, RED)
                    WINDOW.blit(text, text.get_rect(center=(WIDTH // 2, 3 * HEIGHT // 4)))
                    pygame.display.update()
                    break

                if score_2.is_winning_score():
                    text = pygame.font.SysFont("comicsans", TITLE_SIZE).render("Player 2 won", 1, RED)
                    WINDOW.blit(text, text.get_rect(center=(WIDTH // 2, HEIGHT // 4)))
                    pygame.display.update()
                    break

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        is_playing = False
                        break
                keys = pygame.key.get_pressed()
                paddle_1.keyboard_interaction(keys, border, is_lower_paddle=True)
                paddle_2.keyboard_interaction(keys, border, is_lower_paddle=False)
                ball.move()
                ball.paddle_collision(paddle_1)
                ball.paddle_collision(paddle_2)
                ball.border_collision(border)
                score_1.update()
                score_2.update()

                is_goal_scored = ball.reset(HEIGHT)
                if is_goal_scored:
                    paddle_1.reset()
                    paddle_2.reset()

            if not is_playing:
                break

    pygame.quit()


if __name__ == "__main__":
    run()
