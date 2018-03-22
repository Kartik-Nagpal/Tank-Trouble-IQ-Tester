import Pygame;
import random;

class player(pygame.sprite.Sprite):
    x = 0;
    y = 0;
    dx = 0;
    dy = 0;
    size = 1;
    body[] = nul;

    def __init__(self, color):
        print("Player Made");


    def move():
        x += dx;
        y += dy;

    def buttonPress(dirt, val):
        if dirt == "x":
            dx += val;
        elif dirt == "y":
            dy += val;
        else:
            print("why dafaq, did you give me: " + x);

    def buttonRelease(dirt):
        if dirt == "x":
            dx = 0;
        elif dirt == "y":
            dy = 0;
        else:
            print("why dafaq, did you give me: " + x);
