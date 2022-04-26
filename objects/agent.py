import neat


class Agent:
    def __init__(self, genome, config, paddle):
        self.genome = genome
        self.paddle = paddle
        self.is_lower_paddle = paddle.y > 0
        self.config = config
        self.neuralNetwork = neat.nn.FeedForwardNetwork.create(genome, config)

    def get_agent_input(self, ball, width, height):
        paddle_x = self.paddle.x_center
        paddle_y = self.paddle.y
        ball_vy_sign = abs(ball.velocity_y) / ball.velocity_y
        ball_x = ball_vy_sign * abs(ball.x - paddle_x) / width
        ball_y = abs(ball.y - paddle_y) / height
        return paddle_x / width, ball_x, ball_y

    def get_agent_decision(self, ball, width, height):
        prediction = self.neuralNetwork.activate(self.get_agent_input(ball, width, height))
        max_prediction = prediction.index(max(prediction))
        if max_prediction == 1:
            if self.is_lower_paddle:
                return "right"
            else:
                return "left"
        elif max_prediction == 2:
            if self.is_lower_paddle:
                return "left"
            else:
                return "right"

    def update_fitness(self):
        self.genome.fitness += self.paddle.nb_hits

    def penalize_fitness(self, value):
        self.genome.fitness -= value




