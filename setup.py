import pygame;
pygame.init();

BLACK    = (   0,   0,   0);
WHITE    = ( 255, 255, 255);
GREEN    = (   0, 255,   0);
RED      = ( 255,   0,   0);
BLUE     = (   0,   0, 255);



pygame.display.set_caption("Tank Trouble Side");
infoObject = pygame.display.Info();
screen = pygame.display.set_mode((int(infoObject.current_w/2) - 100, infoObject.current_h));
screen.fill(WHITE);
clock = pygame.time.Clock();
pygame.display.flip();
cont = True;

while(cont):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cont = False;
    
    pygame.display.flip();


pygame.quit()
