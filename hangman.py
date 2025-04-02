import pygame
import os
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 500
FPS = 60

# setting up fonts
FONT = pygame.font.SysFont("comicsans", 30)


# setting colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman game")

# button variables
RADIUS = 20
GAP = 15
A = 65
letters = []
start_x = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
start_y = 400
for i in range(26):
    x = start_x + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
    y = start_y + (i // 13) * (RADIUS * 2 + GAP)
    letters.append([x,y, chr(A + i),True])

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
        x, y, ltr,visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

    win.blit(images[hangman_status], (100,100))
    pygame.display.update()
    
    
# setup game loop
while run:
    clock.tick(FPS)
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, my = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr,visible = letter
                if visible:
                    dis = math.sqrt((x - m_x) ** 2 + (y - my) ** 2)
                    if dis < RADIUS:
                        letter[3] = False


pygame.quit()