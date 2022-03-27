import time
import pygame, random

pygame.init()

win=pygame.display.set_mode((700, 700))
pygame.display.set_caption('Space Dodge')

menu=True
run=False
plyr=pygame.image.load('Assets/pixil-frame-0.png')
plyr=pygame.transform.scale(plyr, (100, 100))
asteroid1=pygame.image.load('Assets/Asteroid.png')
asteroid1=pygame.transform.scale(asteroid1, (120, 120))
asteroid2=pygame.image.load('Assets/Asteroid.png')
asteroid2=pygame.transform.scale(asteroid2, (120, 120))
asteroid3=pygame.image.load('Assets/Asteroid.png')
asteroid3=pygame.transform.scale(asteroid1, (120, 120))
asteroid4=pygame.image.load('Assets/Asteroid.png')
asteroid4=pygame.transform.scale(asteroid2, (120, 120))
logo=pygame.image.load('Assets/MCTOWELL.png')


background=pygame.image.load('Assets/Space_background.png')
px=350
py=350
bx, by = px, py
bulletspeed=15
ex, ey= random.randrange(0, 700), -100
ex2, ey2= random.randrange(0, 700), -100
ex3, ey3= random.randrange(0, 700), -100
ex4, ey4= random.randrange(0, 700), -100
xvel=10
yvel=10
cx, cy=random.randrange(10, 690), -10
fallspeed=10
health=500
score=0
death=False
clock=pygame.time.Clock()
    
def game_over_text():
        text=pygame.font.Font('Fonts/Pixel.ttf', 60)
        text_surface=text.render("Game Over", True, (0, 255, 255))
        win.blit(text_surface, (275, 300))
def game_over_text2():
        text=pygame.font.Font('Fonts/Pixel.ttf', 60)
        text_surface=text.render("(Click to replay)", True, (0, 255, 255))
        win.blit(text_surface, (275, 370))

def menutext1():
        text=pygame.font.Font('Fonts/Pixel.ttf', 60)
        text_surface=text.render("Space Dodge", True, (0, 255, 255))
        win.blit(text_surface, (200, 200))
def menutext2():
        text=pygame.font.Font('Fonts/Pixel.ttf', 60)
        text_surface=text.render("(Click to play)", True, (0, 255, 255))
        win.blit(text_surface, (200, 270))
def scoretext():
        text=pygame.font.Font('Fonts/Pixel.ttf', 60)
        text_surface=text.render("Score :"+ str(score), 1, (0, 255, 255))
        win.blit(text_surface, (10, 50))
    


    
    
while menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu=False
            pygame.quit()
    
    win.fill((255, 255, 255))
    win.blit(background, (0, 0))
    win.blit(logo, (-100, 250))
    menutext1()
    menutext2()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            menu=False
            run=True
    
    pygame.display.update()
    clock.tick(60)

    
     
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
    
    win.blit(background, (0, 0))
    win.blit(asteroid1, (ex, ey))
    win.blit(asteroid2, (ex2, ey2))
    win.blit(asteroid3, (ex3, ey3))
    win.blit(asteroid4, (ex4, ey4))
    win.blit(plyr, (px, py))
    
    
    key=pygame.key.get_pressed()

    pygame.draw.rect(win, (255, 0, 0), (10, 100, 250, 10))
    pygame.draw.rect(win, (0, 255, 0), (10, 100, (health//2), 10))

    ey+=fallspeed
    ey2+=fallspeed + random.randrange(0, 6)
    ey3+=fallspeed + random.randrange(0, 6)
    ey4+=fallspeed + random.randrange(0, 6)

    pcollide=plyr.get_rect(center=(px, py))
    ecollide1=asteroid1.get_rect(center=(ex, ey))
    ecollide2=asteroid2.get_rect(center=(ex2, ey2))
    ecollide3=asteroid1.get_rect(center=(ex3, ey3))
    ecollide4=asteroid2.get_rect(center=(ex4, ey4))
    ccollide=asteroid2.get_rect(center=(cx,cy))
    if pcollide.colliderect(ecollide1) or pcollide.colliderect(ecollide2) or pcollide.colliderect(ecollide3) or pcollide.colliderect(ecollide4):
        health -=3.5
        
    if health <= 0:
        game_over_text()
        run=False
        
    
    scoretext()
    
    if key[pygame.K_d]:
        px += xvel
    if key[pygame.K_a]:
        px -= xvel
    if key[pygame.K_s]:
        py += yvel
    if key[pygame.K_w]:
        py -= yvel

    cy += fallspeed

    if px <= 0:
        px=0
    if px >= 600:
        px=600
    if py <= 0:
        py=0
    if py >= 600:
        py =600

    if ey >= 750:
        ex=random.randrange(0, 700)
        ey=-100
    if ey2 >= 750:
        score += 1
        ex2=random.randrange(0, 700)
        ey2=-100
    if ey3 >= 750:
        score +=1
        ex3=random.randrange(0, 700)
        ey3=-100
    if ey4 >= 750:
        ex4=random.randrange(0, 700)
        ey4=-100

    if cy >= 750:
        cx=random.randrange(0, 700)
        cy=-100
    
    pygame.display.update()
    clock.tick(60)

time.sleep(3)
pygame.quit()