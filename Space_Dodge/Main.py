import time
import pygame, random
pygame.mixer.pre_init(44100, -16, 2, 512)

pygame.init()

win=pygame.display.set_mode((700, 700))
pygame.display.set_caption('Space Dodge')

game=True
menu=True
run=False
plyr=pygame.image.load('Assets/Spaceship.png')
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

music=pygame.mixer.music.load('Music/Space Music.ogg')
pygame.mixer.music.play(-1)

gameoversound=pygame.mixer.Sound('Music/GameOver.wav')
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
gameover=False
help=pygame.Surface((50, 50))
hx, hy =random.randrange(0, 700), -100
clock=pygame.time.Clock()
    
def game_over_text():
        text=pygame.font.Font('Fonts/Pixel.ttf', 60)
        text_surface=text.render("Game Over", True, (0, 255, 255))
        win.blit(text_surface, (250, 300))
def game_over_text2():
        text=pygame.font.Font('Fonts/Pixel.ttf', 60)
        text_surface=text.render("(Click Space to replay)", True, (0, 255, 255))
        win.blit(text_surface, (125, 370))

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
            
    
    win.blit(background, (0, 0))
    win.blit(asteroid1, (ex, ey))
    win.blit(asteroid2, (ex2, ey2))
    win.blit(asteroid3, (ex3, ey3))
    win.blit(asteroid4, (ex4, ey4))
    win.blit(help, (hx, hy))
    help.fill((200, 200, 30))
    win.blit(plyr, (px, py))
    
    
    key=pygame.key.get_pressed()

    pygame.draw.rect(win, (255, 0, 0), (10, 100, 250, 10))
    pygame.draw.rect(win, (0, 255, 0), (10, 100, (health//2), 10))

    if health >= 500:
        health=500
    if health <=0:
        health=0
    
    if health !=0:

        ey+=fallspeed + random.randrange(0, 6)
        ey2+=fallspeed + random.randrange(0, 6)
        ey3+=fallspeed +random.randrange(0, 6)
        ey4+=fallspeed +random.randrange(0, 6)

    pcollide=plyr.get_rect(center=(px, py))
    ecollide1=asteroid1.get_rect(center=(ex, ey))
    ecollide2=asteroid2.get_rect(center=(ex2, ey2))
    ecollide3=asteroid1.get_rect(center=(ex3, ey3))
    ecollide4=asteroid2.get_rect(center=(ex4, ey4))
    hcollide=help.get_rect(center=(hx,hy))
    if pcollide.colliderect(ecollide1) or pcollide.colliderect(ecollide2) or pcollide.colliderect(ecollide3) or pcollide.colliderect(ecollide4):
        health -=3.5

    if pcollide.colliderect(hcollide):
        health += 3.5    
    if health <= 0:
        gameover = True

    if gameover == True:
        gameoversound.play()
        game_over_text()
        game_over_text2()
        xvel=0
        yvel=0
        fallspeed=0
        
        
        
    
    scoretext()
    
    if key[pygame.K_d] and xvel  >0:
        px += xvel
    if key[pygame.K_a] and xvel > 0:
        px -= xvel
    if key[pygame.K_s] and yvel >0:
        py += yvel
    if key[pygame.K_w] and yvel >0:
        py -= yvel
    
    
    if event.type == pygame.KEYDOWN and gameover== True:
        if event.key == pygame.K_SPACE:
            health =500
            px=350
            py=350
            ex, ey= random.randrange(0, 700), -100
            ex2, ey2= random.randrange(0, 700), -100
            ex3, ey3= random.randrange(0, 700), -100
            ex4, ey4= random.randrange(0, 700), -100
            gameover= False
            score=0
            fallspeed=10
            xvel, yvel =10, 10
        
    hy += fallspeed

    if health == 0:
        fallspeed=0

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

    if hy >= 750:
        hx=random.randrange(0, 700) 
        hy=-100
    
    if key[pygame.K_m]:
        pygame.mixer.music.fadeout(0)
    if key[pygame.K_p]:
        pygame.mixer.music.play(-1)

    pygame.display.update()
    clock.tick(60)

