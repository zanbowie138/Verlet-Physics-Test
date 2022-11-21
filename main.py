#Adapted from https://www.youtube.com/watch?v=lS_qeBy3aQI&ab_channel=Pezzza%27sWork
import pygame;
import math;
import random

from pygame.locals import *
import utils
from circle import Circle
import manager


def text_render(string):
    return font.render(string, 1, pygame.Color("black"))
def update_fps():
	fps = f"FPS: {str(int(clock.get_fps()))}"
	return text_render(fps)
 

#Pygame initial setup
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)
 
#Initialization
gameOn = True
update_count = 0
circles = []


#Configuration:
#SPHERE_SIZE determins the size of the circles spawned
#SPHERE_AMOUNT determines the the amount of circles that are spawned
#RATE decides how many frames pass between each spawn
SPHERE_SIZE = 10
SPHERE_AMOUNT = 200
RATE = 20

while gameOn:
    #Caps fps to 60
    clock.tick(60)

    #Updates frame count
    update_count+=1

    #Quits when exited
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            gameOn = False

    #Spawns circles that are randomly colored
    if len(circles) < SPHERE_AMOUNT and update_count % RATE == 0:
        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        circles.append(Circle(update_count,[300.0,200.0],10, color))

    #Create background
    screen.fill((181,181,181))
    pygame.draw.circle(screen, (0,0,0), (400,300), 200)

    #Update fps
    screen.blit(update_fps(), (10,0))
    screen.blit(text_render(f"Frame #: {update_count}"), (10,30))

    #Update circles
    manager.update(circles,clock.get_time()/1000)

    #Draws circles
    for circle in circles:
        pygame.draw.circle(screen, circle.color,(circle.getPositionX(),circle.getPositionY()), circle.size)
 
    # Update the display using flip
    pygame.display.flip()

pygame.quit()