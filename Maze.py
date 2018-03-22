import Pygame;
import random;

class maze(pygame.sprite.Sprite):
    size = 1;
    body[] = nul;

    def __init__(self, color):
        print("Maze Being Generated");


    def generate(w, h, m):
        body[0] = (0 + m, 0 + m);
        body[1] = (w - m, 0 + m);
        body[2] = (w - m, h - m);
        body[3] = (0 + m, h - m);
        #for
