from pygame_utils import *
from objects.agent import Agent
import pygame
import neat
import pickle

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# Game Title
pygame.display.set_caption("Pong Game")


def eval_genomes(genomes, config):
    # each genome is competing against the others in the same generation
    for genome_id, genome in genomes:
        genome.fitness = 0

    for genome_id, genome in genomes:
        for genome_id_, genome_ in genomes:
            if genome_id_ != genome_id:
                is_playing = True
                clock, border, paddle_1, paddle_2, ball, score_1, score_2 = game_setup(training=True)
                neat_agent = Agent(genome, config, paddle_2)
                opponent = Agent(genome_, config, paddle_1)
                while is_playing:
                    draw_frame(WINDOW, [border, paddle_1, paddle_2, ball, score_1, score_2])
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            quit()

                    neat_agent_decision = neat_agent.get_agent_decision(ball, WIDTH, HEIGHT)
                    opponent_decision = opponent.get_agent_decision(ball, WIDTH, HEIGHT)
                    # penalize staying in the middle
                    if neat_agent_decision is None:
                        neat_agent.penalize_fitness(PENALIZATION_FITNESS_VALUE)
                    paddle_1.agent_interaction(opponent_decision, border, is_lower_paddle=True)
                    paddle_2.agent_interaction(neat_agent_decision, border, is_lower_paddle=False)

                    is_goal_scored = ball.reset(HEIGHT, paddle_1, paddle_2)
                    if is_goal_scored or paddle_1.nb_hits > MAX_HITS_TRAINING:
                        neat_agent.update_fitness()
                        opponent.update_fitness()
                        is_playing = False

                    ball.interact_with_environment(paddle_1, paddle_2, border, training=True)
                    score_1.update()
                    score_2.update()


def train(config_file, eval_criterion, nb_generations):
    config = neat.Config(neat.DefaultGenome,
                         neat.DefaultReproduction,
                         neat.DefaultSpeciesSet,
                         neat.DefaultStagnation,
                         config_file)

    # initial population
    p = neat.Population(config)

    # Terminal Stats and checkpoints
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_criterion, nb_generations)
    # serialize best agent
    with open("best_agent.pickle", "wb") as f:
        pickle.dump(winner, f)


if __name__ == "__main__":
    train("config.ini", eval_genomes, NB_GENERATIONS)
