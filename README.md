# Pong-Game
In this repo, a version of the famous Pong game is presented in Python code (using Pygame module).
### Game Description
The goal of the game is to score more goals than your opponent by moving your paddle. Two different modes are available:

1) **Two player mode** : In this mode, you can play vs your friend. Each of you will have his paddle to move and the corresponding keys on the keyboard. 

2) **Singe player mode** : In this mode you play vs an AI trained with an evolutionary algorithm called the NEAT algorithm. For the training, the neat-python library is used.
 If you are interested in the idea behind the algorithm or the implementation details, you can check the documentation and the papers linked to it here https://neat-python.readthedocs.io/en/latest/.


### How to run the game ? 
-  #### The easy way (working)



The easiest way to run the game if you have python installed is to install the Pygame module and the neat-python module (only necessary for the one player mode) and then run main.py : 
 ```
  $ pip install pygame
  $ pip install neat-python
  $ python main.py
  ``` 
If you want to train your own AI with the NEAT algorithm for this game, you can run train.py with the hyperparameters you want (check config.ini)
```
$ python train.py
  ``` 
Note that it can take some time to have a perfect AI agent trained. For this first version, the AI agent is far from being perfect but it detects the right direction most of the time.
-  #### In a docker container (not working for me)
Another way would be to build a docker image using the Dockerfile and run a container. 
 ```
  $ docker build -t image_name .
  $ docker run --rm -it image_name
  ``` 
I tried this method but it seems not straightforward to run a Pygame GUI on a container as there are problems related to the display of the window (I tried many fixes but none allowed me to display the Pygame window) https://stackoverflow.com/questions/56668021/run-pygame-with-audio-in-docker-container

  




