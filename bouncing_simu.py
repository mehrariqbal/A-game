import pygame
import random
import math
from pygame import gfxdraw

# intialize the pygame 
pygame.init()

# creating screen
screen = pygame.display.set_mode((800,600))

# Game title
pygame.display.set_caption("collision")

# background
background = pygame.image.load('background.png')

# balls
x = []
y = []
r = [-3,3,-4,4,5,-5]
x_chng = []
y_chng = []
g = 1
#color = []
for i in range(50):
    x.append(random.randint(20,760))
    y.append(random.randint(20,300))
    x_chng.append(random.choice(r))
    y_chng.append(random.choice(r))
    #color.append((random.randint(10,230),random.randint(10,230),random.randint(10,230)))
def balls(x,y):    
    gfxdraw.filled_circle(screen,x,y,15,(0,255,0))

# collision between balls
def collision (ix,iy,jx,jy):
    dis = math.sqrt((ix-jx)**2+(iy-jy)**2)
    if dis <=18:
        return True
    else:
        return False    

running = True
while running:
    # screen filling with black color
    screen.fill((0,0,0))

    # setting the background
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # balls movement
    for i in range(6):
        balls(x[i],y[i])
        y_chng[i] += g
        x[i] += x_chng[i]
        y[i] += y_chng[i]
        if x[i] >= 760 or x[i] <= 20: 
            x_chng[i] *= -1
        if y[i] >= 580: #or y[i] <= 20:
            y_chng[i] *= -1
            y[i] = 580
        if y_chng[i] == 0 and y[i] == 580:
            if x_chng[i] <0:
                x_chng[i] +=1
            elif x_chng[i] >0:
                x_chng[i] -= 1
            else:
                x[i] = x[i]     

    # collision
    for i in range(6):
        for j in range(i+1,6):
            col = collision(x[i],y[i],x[j],y[j])
            if col:
                i_chng_x = x_chng[i]
                i_chng_y = y_chng[i]
                j_chng_x = x_chng[j]
                j_chng_y = y_chng[j]
                x_chng[i], y_chng[i] = j_chng_x, j_chng_y
                x_chng[j], y_chng[j] = i_chng_x, i_chng_y
        
    

    pygame.display.update()        