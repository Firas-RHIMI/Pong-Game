# Pong-Game
In this repo, a version of the famous Pong game is presented in Python code (using Pygame module).

### How to run the game ? 
-  #### The easy way (working)



The easiest way to run the game if you have python installed is to install the Pygame module and then run main.py : 
 ```
  $ pip install pygame
  $ python main.py
  ``` 
-  #### In a docker container (not working for me)
Another way would be to build a docker image using the Dockerfile and run a container. 
 ```
  $ docker build -t image_name .
  $ docker run --rm -it image_name
  ``` 
I tried this method but it seems not straightforward to run a Pygame GUI on a container as there are problems related to the display of the window (I tried many fixes but none allowed me to display the Pygame window) https://stackoverflow.com/questions/56668021/run-pygame-with-audio-in-docker-container

  




