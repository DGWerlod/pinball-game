import pygame, constants, math
from logic import collisions
from img import images
from objects.rect import Rect
from objects.flipper import Flipper
from objects.ball import Ball

# Window will spawn in exact center
import os
from win32api import GetSystemMetrics
windowX = GetSystemMetrics(0)/2 - constants.gameW/2
windowY = GetSystemMetrics(1)/2 - constants.gameH/2
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (windowX, windowY)

# If ya don't boop
# angle = -90 + 2*(n-90)
# speed = 0.8v

# If ya boop
# angle =
# speed = 1.6v

from pygame.locals import NOFRAME, DOUBLEBUF
# flags = DOUBLEBUF

pygame.init()

# pygame.FULLSCREEN
ctx = pygame.display.set_mode((constants.gameW,constants.gameH), NOFRAME | DOUBLEBUF)
# ctx = pygame.display.set_mode((constants.gameW,constants.gameH), flags)

ctx.set_alpha(None)
pygame.display.set_caption("Pinball")
clock = pygame.time.Clock()

def listen(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    return running

def main():

    # pygame.mixer.music.play()

    running = True
    score = 0

    daBall = Ball(50,50,20,(234,206,205))

    leftX = -15 + constants.gameW/2-45
    rightX = 15 + constants.gameW/2+45 + 2*35

    daFlip = Flipper(leftX,550,90,20,math.pi/6,(0,0,255))
    daFlip2 = Flipper(rightX,550,90,20,5*math.pi/6,(0,128,255))

    midline = Rect(199,0,2,600,(0,0,0))

    while running:
        running = listen(running)
        # Reset BG
        ctx.fill((255,0,0))

        midline.go(ctx)
        daBall.go(ctx)
        daFlip.go(ctx)
        daFlip2.go(ctx)

        score = score + 100

        # Debug
        fps = constants.muli["15"].render(str(round(clock.get_fps(),1)),True,constants.black)
        ctx.blit(fps,(15,15))

        # Update Window
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

main()
# if game_over:
#myimage=PhotoImage(file='Gameover.gif')
#canvas.create_image(0,0,anchor=NW,image=myimage)
#text_rect = text.get_rect()
    #    text_x = screen.get_width() / 2 - text_rect.width / 2
        #text_y = screen.get_height() / 2 - text_rect.height / 2
    #    screen.blit(text, [text_x, text_y])
