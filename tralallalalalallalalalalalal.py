import pygame
pygame.init()
ekraani_suurus = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Memory")
taust = pygame.image.load("pildid/tasutaks.jpg")
#ekraani_pind.fill(taust,(0,0))
pygame.display.blit(taust, (0,0))
#pygame.display.flip()
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
pygame.quit()