from pygame_utils import *
from objects.agent import Agent
import neat
import pickle
pygame.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# Game Title
pygame.display.set_caption("Pong Game")


def run(config_file):
    replay = True
    while replay:
        is_two_player_mode, has_quit = start_screen(WINDOW)
        if has_quit:
            break
        else:
            is_playing = True
            clock, border, paddle_1, paddle_2, ball, score_1, score_2 = game_setup()
            if not is_two_player_mode:
                with open("best_agent.pickle", "rb") as f:
                    winner = pickle.load(f)

                config = neat.Config(neat.DefaultGenome,
                                     neat.DefaultReproduction,
                                     neat.DefaultSpeciesSet,
                                     neat.DefaultStagnation,
                                     config_file)
                ai_agent = Agent(winner, config, paddle_2)

            while is_playing:
                draw_frame(WINDOW, [border, paddle_1, paddle_2, ball, score_1, score_2])
                clock.tick(FPS)
                text_1 = "Player 1 won" if is_two_player_mode else "Player won"
                text_2 = "Player 2 won" if is_two_player_mode else "AI won"
                if score_1.is_winning_score():
                    display_winner(WINDOW, TITLE_SIZE, text_1, RED, (WIDTH // 2, 3 * HEIGHT // 4))
                    break

                if score_2.is_winning_score():
                    display_winner(WINDOW, TITLE_SIZE, text_2, RED, (WIDTH // 2, HEIGHT // 4))
                    break

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        is_playing = False
                        break

                keys = pygame.key.get_pressed()
                paddle_1.keyboard_interaction(keys, border, is_lower_paddle=True)
                if is_two_player_mode:
                    paddle_2.keyboard_interaction(keys, border, is_lower_paddle=False)
                else:
                    ai_agent_decision = ai_agent.get_agent_decision(ball, WIDTH, HEIGHT)
                    paddle_2.agent_interaction(ai_agent_decision, border, is_lower_paddle=False)

                ball.reset(HEIGHT, paddle_1, paddle_2)
                ball.interact_with_environment(paddle_1, paddle_2, border)
                score_1.update()
                score_2.update()
            if not is_playing:
                break

    pygame.quit()


if __name__ == "__main__":
    run("config.ini")
