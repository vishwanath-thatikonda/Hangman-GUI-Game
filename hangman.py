import pygame
import random
import os
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman game")

# button variables
RADIUS = 20
GAP = 15
letters = []
start_x = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
start_y = 400
for i in range(26):
    x = start_x + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
    y = start_y + (i // 13) * (RADIUS * 2 + GAP)
    letters.append([x,y])



# setting colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

hangman_status = 4

# loading images
images = []
for i in range(7):
    image = pygame.image.load(os.path.join("hangman" + str(i) + ".png"))
    images.append(image)

clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE)
    # draw the buttons
    for letter in letters:
        x, y = letter
        pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
    win.blit(images[hangman_status], (100,100))
    pygame.display.update()
    
    
# setup game loop
while run:
    clock.tick(FPS)
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()