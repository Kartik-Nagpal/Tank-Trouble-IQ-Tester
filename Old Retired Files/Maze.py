import pygame;
import random;


class Point():
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def x(self):
        return self.x;

    def y(self):
        return self.y;



class maze(pygame.sprite.Sprite):
    size = 1;
    
    def __init__(self):
        print("Maze Being Generated");
        

    def generate(self, w, h, m):
        body = [];
        body.append(Point(0 + m, 0 + m));
        body.append(Point(w - 2*m, h - 2*m));

        #for

        return body;
