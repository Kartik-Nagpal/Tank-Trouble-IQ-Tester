import pygame;
import random;
import math;
import os;

class Point():
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def x(self):
        return self.x;

    def y(self):
        return self.y;

    def __str__(self):
        return str(self.x) + str(self.y);



class maze(pygame.sprite.Sprite):
    size = 1;
    
    def __init__(self):
        print("Maze Being Generated");
        

    def generate(self, w, h, m, n):
        body = [];

        cellW = w/n;
        cellH = h/n;
        cx = 0;
        cy = 0;
        for i in range(0, n):
            for j in range(0, n):
                body.append(Point(cellW*cx + m, cellH*cy + m));
                cx += 1;
            cx = 0;
            cy += 1;
       return body;


class player(pygame.sprite.Sprite):

    def __init__(self, im, px=0, py=0, angle=0, v=0):
        super().__init__();
        self.x = px;
        self.y = py;
        self.ang = angle;
        self.dp = v;
        self.img = im;
        print("Player Made");


    def update(self):
        self.x += self.dp * -math.cos(self.ang);
        self.y += self.dp * math.sin(self.ang);
        #print("UPDATE: X=", self.x, " Y=", self.y);

    def buttonPress(self, key, val=1):
        if key == pygame.K_UP or key == pygame.K_w:
            self.dp += val;
        elif key == pygame.K_DOWN or key == pygame.K_s:
            self.dp -= val;
        elif key == pygame.K_LEFT or key == pygame.K_a:
            self.ang += 10;
        elif key == pygame.K_RIGHT or key == pygame.K_d:
            self.ang -= 10;
        else:
            print("why dafaq, did you give me: " + str(key));

    def buttonRelease(self, key):
        if key == pygame.K_UP or key == pygame.K_w or key == pygame.K_DOWN or key == pygame.K_s:
            #self.dp = 0;
            print();
        elif key == pygame.K_LEFT or key == pygame.K_RIGHT or key == pygame.K_a or key == pygame.K_d:
            #don't do it
            print();
        else:
            print("why dafaq, did you give me: " + str(key));
