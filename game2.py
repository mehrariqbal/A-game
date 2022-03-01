import pygame
import random
import math
from pygame import gfxdraw

# intialize the pygame 
pygame.init()

# creating screen
screen = pygame.display.set_mode((800,600))

# Game title
pygame.display.set_caption("bouncer")

# background
background = pygame.image.load('background.png')

# player image
plyrx=370
plyry=480
plyrx_chng = 0
plyry_chng = 0
def player(x,y):
    rect = pygame.Rect(x, y, 30, 30)
    gfxdraw.box(screen,rect,(70,30,255))

# points
px = random.randint(0,750)
py = random.randint(0,550)
def point(x,y):
    gfxdraw.filled_circle(screen,x,y,8,(0,255,0))
    
# balls
num = 20
x = []
y = []
r = [-3,3,-4,4,5,-5,6,-6,7,-7]
x_chng = []
y_chng = []
#color = []
for i in range(num):
    x.append(random.randint(20,760))
    y.append(random.randint(20,300))
    x_chng.append(random.choice(r))
    y_chng.append(random.choice(r))
    #color.append((random.randint(10,230),random.randint(10,230),random.randint(10,230)))
def balls(x,y): 
    gfxdraw.filled_circle(screen,x,y,15,(255,0,0))

#score
score_value = 0
txtx= 680
txty= 10
def Show_score(x,y,z):
    font = pygame.font.Font('freesansbold.ttf',z)
    score = font.render("score: " + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

# collision between balls
def collision (ix,iy,jx,jy):
    dis = math.sqrt((ix-jx)**2+(iy-jy)**2)
    if dis <=18:
        return True
    else:
        return False   

# collision betweens balls and player
def ball_player(plx,ply,bx,by):
    dis = math.sqrt((plx-bx)**2+(ply-by)**2)
    if dis <=25:
        return True
    else:
        return False 

# player getting point
def getting_point(plx,ply,px,py):
        dis = math.sqrt((plx-px)**2+(ply-py)**2)
        if dis <=30:
            return True
        else:
            return False 

# Game over
def game_over():
    for i in range(num):
        x_chng[i] = 0
        y_chng[i] = 0

# Game over txt
over_font = pygame.font.Font('freesansbold.ttf',70)
def game_over_txt():
    over_txt = over_font.render('GAME OVER',True,(255,255,255))
    screen.blit(over_txt,(190,200))                   

#loop counter
p = 0
r = 300
q = 0
 

running = True
while running:
    # screen filling with black color
    screen.fill((0,0,0))

    # setting the background
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # key inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                plyrx_chng = -4 
            if event.key == pygame.K_RIGHT:
                plyrx_chng = 4  
            if event.key == pygame.K_UP:
                plyry_chng = -4
            if event.key == pygame.K_DOWN:
                plyry_chng = 4   

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                plyrx_chng= 0 
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                plyry_chng = 0                    
    
    q += 1

    # player movement
    plyrx += plyrx_chng 
    plyry += plyry_chng
    
    if plyrx <= 0:
        plyrx = 0
    elif plyrx > 800-30:
        plyrx = 800-30
 
    if plyry<=0:
        plyry =0
    elif plyry > 600 - 30:
        plyry = 600 - 30                          

    # balls appearence
    if q <= r:
        p = 0
    elif q <= 2*r:
        p = 1
    elif q <= 3*r:
        p = 2
    elif q <= 4*r:
        p = 3
    elif q <= 5*r:
        p = 4
    elif q <= 6*r:
        p = 5
    elif q <= 7*r:
        p = 6  
    elif q <= 8*r:
        p = 7 
    elif q <= 9*r:
        p = 8
    elif q <= 10*r:
        p = 9
    elif q <= 11*r:
        p = 10
    elif q <= 12*r:
        p = 11                                         
    if p >=12:
        p = 12 
    # balls movement       
    for i in range(p+1):
        x[i] += x_chng[i]
        y[i] += y_chng[i]
        if x[i] >= 760 or x[i] <= 20: 
            x_chng[i] *= -1
        if y[i] >= 580 or y[i] <= 20:
            y_chng[i] *= -1

        # player and balls collision
        if ball_player(plyrx,plyry,x[i],y[i]): 
            game_over()
            game_over_txt()
            Show_score(275,270,70) 
            plyrx_chng *= 0
            plyry_chng *= 0
            q -= 1
            

        balls(x[i],y[i])     

    # collision
    for i in range(p+1):
        for j in range(i+1,p+1):
            col = collision(x[i],y[i],x[j],y[j])
            if col:
                i_chng_x = x_chng[i]
                i_chng_y = y_chng[i]
                j_chng_x = x_chng[j]
                j_chng_y = y_chng[j]
                x_chng[i], y_chng[i] = j_chng_x, j_chng_y
                x_chng[j], y_chng[j] = i_chng_x, i_chng_y

    # player getting point and point's replacemnt
    if getting_point(plyrx,plyry,px,py):
        px = random.randint(0,750)
        py = random.randint(0,550) 
        score_value += 1  
        q += 1       

    player(plyrx,plyry) 
    point(px,py) 
    Show_score(txtx,txty,25) 
         
    pygame.display.update()   

print(q)
