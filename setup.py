import pygame;
import random;
import math;
import myObjects;
import mazeGen;

pygame.init();

BLACK    = (   0,   0,   0);
WHITE    = ( 255, 255, 255);
GREEN    = (   0, 255,   0);
RED      = ( 255,   0,   0);
BLUE     = (   0,   0, 255);
#RANDOM_COLOR = (random.randint(0, 225), random.randint(0, 225), random.randint(0, 225));


pygame.display.set_caption("Tank Trouble Side");
surface = pygame.Surface((100, 100), pygame.SRCALPHA)
infoObject = pygame.display.Info();


marg = 10;
width = int(infoObject.current_w/2) - 2*marg;
height = int(infoObject.current_h - 80) - 2*marg;
print("width: ", width, " height: ", height);
numCells = 21;


m = myObjects.maze();
pts = m.generate(width, height, marg, numCells);
t = mazeGen.mazeGen(20, 20);
cellW = width/numCells;
cellH = height/numCells;


p1imgorig = pygame.image.load("red.png");
p2imgorig = pygame.image.load("blue.png");
p1im = pygame.image.load("red.png");
p2im = pygame.image.load("blue.png");
p1 = myObjects.player(p1im, 100, 100);
p2 = myObjects.player(p2im, 30, 30, -30, 2);


screen = pygame.display.set_mode([width, height]);
screen.fill(WHITE);
clock = pygame.time.Clock();
pygame.display.flip();
angle = 10;


cont = True;
while(cont):
    screen.fill(WHITE);

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cont = False;

        elif event.type == pygame.KEYDOWN:
            p1.buttonPress(event.key);
            if event.key == pygame.K_LEFT:
                rot = pygame.transform.rotate(p1imgorig, p1.ang);
                rotRect = rot.get_rect(center=[p1.x + 42/2, p1.y + 29/2]);
                p1im = rot;
            if event.key == pygame.K_RIGHT:
                rot = pygame.transform.rotate(p1imgorig, p1.ang);
                rotRect = rot.get_rect(center=[p1.x + 42/2, p1.y + 29/2]);
                p1im = rot;
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                p1.buttonRelease(event.key);
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                p1.buttonRelease(event.key);


    pygame.draw.rect(screen, BLACK, [marg, marg, width, height], 4);
    
#quotentaehashlashslash

    c = 0;
    for i in range(0, numCells**2):
        if t[int(c/numCells)][c%numCells]:
            r = pygame.draw.rect(screen, BLACK, [pts[i].x, pts[i].y, cellW, cellH]);
        else:
            r = pygame.draw.rect(screen, WHITE, [pts[i].x, pts[i].y, cellW, cellH], 1);
        c += 1;

    screen.blit(p1im, [p1.x, p1.y]);
    screen.blit(p2im, [p2.x, p2.y]);
    pygame.draw.ellipse(screen, BLUE, [p1.x + int(42/2) - 2, p1.y + int(29/2) - 2, 4, 4])
    pygame.draw.line(screen, RED, [p1.x, p1.y], [p1.x + 10*(p1.dp + 1)*math.cos(p1.ang), p1.y + 10*(p1.dp + 1)*math.sin(p1.ang)], 2);

    p1.update();
    #p2.update();
    pygame.display.flip();
pygame.quit()
