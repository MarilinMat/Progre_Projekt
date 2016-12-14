import random, pygame, sys, os
from pygame.locals import *

class lauamäng(object):
    def __init__(key):
        pygame.init()
        key.rida1 = 100
        key.rida2 = 210
        key.rida3 = 330
        key.rida4 = 450
        key.aken_laius = 900
        key.aken_kõrgus = 600
        key.kõik_pildid = 16 
        key.kaart_arv = 20
        key.paare = key.kaart_arv//2
        key.pildid = [] 
        key.kaardid = [] 
        key.kaardikaas = [] 
        key.paarid = [] 
        key.taustapilt = ''
        key.ekraan = pygame.display.set_mode((900,600))
        #key.font =''
        #key.clock = pygame.time
       
        for x in range(key.kõik_pildid):
            key.pildid.append(pygame.image.load(os.path.join('pildid/', 'pilt%d.png' % (x+1))))
        for x in range(key.kaart_arv):
            key.kaardikaas.append(pygame.image.load(os.path.join("pildid/kaart.jpg")))
       
        key.taustapilt = pygame.image.load(os.path.join('pildid/','taust.jpg'))
        key.pealkiripilt = pygame.image.load(os.path.join('pildid/','pealkiri1.png'))
        #key.font = pygame.font.SysFont('Constantia', 36)

    def uus_mängudata(key):
        del key.paarid[:]
        del key.kaardid[:]
        key.sega_kaardid()

    def sega_kaardid(key):
        random.shuffle(key.pildid)
        random.shuffle(key.pildid)
        
        for x in range(key.paare):
            key.kaardid.append(key.pildid[x])

        random.shuffle(key.kaardid)

        for x in range(key.paare, key.kaart_arv):
            key.kaardid.append(key.kaardid[x-(key.paare)])

        random.shuffle(key.kaardid)

    def mängusispilt(key):
        key.ekraan.blit(key.taustapilt,(0,0))
        #skoor = key.font.render('Arvamisi: %d' % int(arvamisi/2), True, (255,255,255))
        #key.ekraan.blit(skoor,(440,550))

    def leitud_paarid(key):
        return len(key.paarid)

    def kustuta_valitud(key):
        key.paarid.pop()

    def lisa_valitud(key, k_valik):
        key.paarid.append(k_valik)

    def on_paar(key, valik1, valik2):
        return (key.kaardid[valik1] == key.kaardid[valik2])

    def mängupilt(key):
        if(key.leitud_paarid() >= 1):
            
            laius = 100
            for row1 in range(0, 5):
                if(key.valitud_pilt(row1)):
                    key.ekraan.blit(key.kaardid[row1],(laius,key.rida1))
                else:
                    key.ekraan.blit(key.kaardikaas[row1],(laius,key.rida1))
                laius += 145

            laius = 100
            for row2 in range(5, 10):
                if(key.valitud_pilt(row2)):
                    key.ekraan.blit(key.kaardid[row2],(laius,key.rida2))
                else:
                    key.ekraan.blit(key.kaardikaas[row2],(laius,key.rida2))
                laius += 145

            laius = 100
            for row3 in range(10, 15):
                if(key.valitud_pilt(row3)):
                    key.ekraan.blit(key.kaardid[row3],(laius,key.rida3))
                else:
                    key.ekraan.blit(key.kaardikaas[row3],(laius,key.rida3))
                laius += 145
                
            laius = 100
            for row4 in range(15, 20):
                if(key.valitud_pilt(row4)):
                    key.ekraan.blit(key.kaardid[row4],(laius,key.rida4))
                else:
                    key.ekraan.blit(key.kaardikaas[row4],(laius,key.rida4))
                laius += 145

        else:
            laius = 100 ## print row 1
            for row1 in range(0, 5):
                key.ekraan.blit(key.kaardikaas[row1],(laius,key.rida1))
                laius += 145
             ## print row 2
            laius = 100
            for row2 in range(5, 10):
                key.ekraan.blit(key.kaardikaas[row2],(laius,key.rida2))
                laius += 145

            laius = 100 ## print row 3
            for row3 in range(10, 15):
                key.ekraan.blit(key.kaardikaas[row3],(laius,key.rida3))
                laius += 145

            laius = 100 ## print row 3
            for row4 in range(15, 20):
                key.ekraan.blit(key.kaardikaas[row4],(laius,key.rida4))
                laius += 145
                

    def valitud_pilt(key, kontrolli):
        for x in key.paarid:
            if(int(kontrolli) == int(x)):
                return True
        return False

    def mäng_läbi(key):
        inGame = False
        
        #arvamisi = int(arvamisi/2)
        #key.ekraan.blit(key.taust,(0,0))
        #skoor = key.font.render('Arvamisi: %d' % (arvamisi), True, (255,255,255))
        #jätka_mäng = key.font.render('Klikka kuskile',True, (255,255,255))
        #key.ekraan.blit(skoor,(230,35))
        #key.ekraan.blit(jätka_mäng,(90,515))
<<<<<<< HEAD

    def valik(key,hiirx,hiiry):
        if((hiiry <= 190 ) and (hiiry >= 100)):
            if (hiirx >= 112) and (hiirx <= 227):
                if(key.valitud_pilt(0) == False):
                    return 0
            elif (hiirx >= 257) and (hiirx <=372):
                if(key.valitud_pilt(1) == False):
                     return 1
            elif (hiirx >= 402) and (hiirx <= 517):
                if(key.valitud_pilt(2) == False):
                    return 2
            elif (hiirx >= 547) and (hiirx <= 662):
                if (key.valitud_pilt(3) == False):
                    return 3
            elif (hiirx >= 692) and (hiirx <= 807):
                if (key.valitud_pilt(4) == False):
                    return 4

        elif((hiiry <= 310 ) and (hiiry >= 220)):
            if (hiirx >= 112) and (hiirx <= 227):
                if(key.valitud_pilt(5) == False):
                    return 5
            elif (hiirx >= 257) and (hiirx <=372):
                if(key.valitud_pilt(6) == False):
                     return 6
            elif (hiirx >= 402) and (hiirx <= 517):
                if(key.valitud_pilt(7) == False):
                    return 7
            elif (hiirx >= 547) and (hiirx <= 662):
                if (key.valitud_pilt(8) == False):
                    return 8
            elif (hiirx >= 692) and (hiirx <= 807):
                if (key.valitud_pilt(9) == False):
                    return 9

        elif((hiiry <= 430 ) and (hiiry >= 340)):
            if (hiirx >= 112) and (hiirx <= 227):
                if(key.valitud_pilt(10) == False):
                    return 10
            elif (hiirx >= 257) and (hiirx <=372):
                if(key.valitud_pilt(11) == False):
                     return 11
            elif (hiirx >= 402) and (hiirx <= 517):
                if(key.valitud_pilt(12) == False):
                    return 12
            elif (hiirx >= 547) and (hiirx <= 662):
                if (key.valitud_pilt(13) == False):
                    return 13
            elif (hiirx >= 692) and (hiirx <= 807):
                if (key.valitud_pilt(14) == False):
                    return 14

        elif((hiiry <= 550 ) and (hiiry >= 460)):
            if (hiirx >= 112) and (hiirx <= 227):
                if(key.valitud_pilt(15) == False):
                    return 15
            elif (hiirx >= 257) and (hiirx <=372):
                if(key.valitud_pilt(16) == False):
                     return 16
            elif (hiirx >= 402) and (hiirx <= 517):
                if(key.valitud_pilt(17) == False):
                    return 17
            elif (hiirx >= 547) and (hiirx <= 662):
                if (key.valitud_pilt(18) == False):
                    return 18
            elif (hiirx >= 692) and (hiirx <= 807):
                if (key.valitud_pilt(19) == False):
                    return 19

        return -1


    def valge_taust(key):
        key.ekraan.fill((255,255,255,255))

def main():
    
    inGame = False
    arvan, paar = 0, 0
    valik1, valik2 = -1, -1
    clock = pygame.time    
    mängulaud = lauamäng()
    os.environ["SDL_VIDEO_CENTERED"] = '1'
    ekraan = mängulaud.ekraan
    pygame.display.set_caption("Memory")
    mängulaud.sega_kaardid()

    while(not inGame):
        ekraan.blit(mängulaud.taustapilt,(0,0))
        ekraan.blit(mängulaud.pealkiripilt,(240,1))
        
        #while inGame:
            #DisplayIngameBackground(numGuesses, numPairs)
        
        if(paar < mängulaud.paare):
            if(mängulaud.leitud_paarid() < 1):
                mängulaud.mängupilt()
            elif(mängulaud.leitud_paarid() > 0):
                mängulaud.mängupilt()
                pygame.display.update()

                if (valik1 > -1) and (valik2 > -1):
                    clock.wait(750)
                    
                    for event in pygame.event.get():
                        if (event.type == MOUSEBUTTONUP):
                            continue

                    if (mängulaud.on_paar(valik1,valik2)):
                        paar += 1

                    else:
                        mängulaud.kustuta_valitud()
                        mängulaud.kustuta_valitud()

                    valik1 = -1
                    valik2 = -1

            for event in pygame.event.get():
                if ((event.type == QUIT) or event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()                

                if event.type == MOUSEMOTION :
                    hiirx, hiiry = event.pos

                elif event.type == MOUSEBUTTONUP:
                    hiirx, hiiry = event.pos

                    if (arvan % 2) == 0:
                        valik1 = mängulaud.valik(hiirx,hiiry)

                        if valik1 > -1 :
                            mängulaud.lisa_valitud(valik1)
                            arvan += 1
                    else:
                        valik2 = mängulaud.valik(hiirx,hiiry)

                        if valik2 > -1:
                            mängulaud.lisa_valitud(valik2)
                            arvan += 1
     
        else:
            mängulaud.mängupilt()
            pygame.display.update()
            inGame = mängulaud.mäng_läbi()
            mängulaud.valge_taust()
            mängulaud.uus_mängudata()
            arvan = 0
            paar = 0
        pygame.display.flip()
        clock.wait(70)
        


if __name__ == '__main__':
    main()
=======
        
>>>>>>> origin/master
