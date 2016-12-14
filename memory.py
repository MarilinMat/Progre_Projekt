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