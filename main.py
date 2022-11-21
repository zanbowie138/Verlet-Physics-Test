import pygame;
import math;
import random

from pygame.locals import *
import utils
from sphere import Sphere
import manager

def update_fps():
	fps = f"FPS: {str(int(clock.get_fps()))}"
	return text_render(fps)

def text_render(string):
    return font.render(string, 1, pygame.Color("black"))
 
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)
 
gameOn = True
update_count = 0

spheres = []


while gameOn:
    clock.tick(60)
    update_count+=1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            gameOn = False

    keys = pygame.key.get_pressed()
    #if pygame.mouse.get_pressed():
    #    pass

    if len(spheres) < 200 and update_count%2 == 0:
        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        spheres.append(Sphere(update_count,[300.0,200.0],10, color))

    #Create background
    screen.fill((181,181,181))
    pygame.draw.circle(screen, (0,0,0), (400,300), 200)

    #Update fps
    screen.blit(update_fps(), (10,0))
    screen.blit(text_render(f"Frame #: {update_count}"), (10,30))

    #Update sphere
    manager.update(spheres,clock.get_time()/1000)

    for i, sphere in enumerate(spheres):
        pygame.draw.circle(screen, sphere.color,(sphere.getPositionX(),sphere.getPositionY()), sphere.size)
 
    # Update the display using flip
    pygame.display.flip()

pygame.quit()