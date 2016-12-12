import pygame

pygame.init()
ekraani_suurus = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Memory")

taust= pygame.image.load("pildid/taust.jpg")
pilt1 = pygame.image.load("pildid/pilt1.png")
pilt2 = pygame.image.load("pildid/pilt2.png")
pilt3 = pygame.image.load("pildid/pilt3.png")
pilt4 = pygame.image.load("pildid/pilt4.png")
pilt5 = pygame.image.load("pildid/pilt5.png")
pilt6 = pygame.image.load("pildid/pilt6.png")
pilt7 = pygame.image.load("pildid/pilt7.png")
pilt8 = pygame.image.load("pildid/pilt8.png")
pilt9 = pygame.image.load("pildid/pilt9.png")
pilt10 = pygame.image.load("pildid/pilt10.png")
pilt11 = pygame.image.load("pildid/pilt11.png")
pilt12 = pygame.image.load("pildid/pilt12.png")
pilt13 = pygame.image.load("pildid/pilt13.png")
pilt14 = pygame.image.load("pildid/pilt14.png")
pilt15 = pygame.image.load("pildid/pilt15.png")
pilt16 = pygame.image.load("pildid/pilt16.png")

ekraani_suurus.fill((0,0,0))
ekraani_suurus.blit(taust, (0, 0))
pygame.display.flip()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    
pygame.quit()