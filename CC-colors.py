import pygame
from pygame.locals import *
from sys import exit

pygame.init ()

#let's define our variables
R = 0
G = 0
B = 0

display = pygame.display.set_mode((640, 480), 0, 32)

#MAIN LOOP GOES HERE
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
	pressedKeys = pygame.key.get_pressed()

	if pressedKeys[K_LEFT]:
		R -= 1
	elif pressedKeys[K_RIGHT]:
		R += 1
	if pressedKeys[K_UP]:
		G -=1
	elif pressedKeys[K_DOWN]:
		G += 1
	if pressedKeys[K_w]:
		B -= 1
	elif pressedKeys[K_s]:
		B +=1

	#we need to check that our r, g, b would not go below zero or above 255

	if R < 0:
		R = 0
	elif R > 255:
		R = 255
	if G < 0:
		G = 0
	elif G > 255:
		G = 255	
	if B < 0:
		B = 0
	elif B > 255:
		B = 255

	display.fill ((R, G, B))
	pygame.display.update()


