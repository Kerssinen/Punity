import pygame
import random

naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Piirtäminen")
viholliskuvat = ["lato.jpeg", "vihollinen.jpg"]


def piirraKuva(kuvatiedosto, x, y):
    naytto.blit(kuvatiedosto, (x, y))

def piirtaminen(naytto, hahmot, viholliset):
    naytto.fill((0, 0, 0))
    for hahmo in hahmot:
        if hahmo[3] == True:
            kuva = pygame.image.load(hahmo[0]).convert()
            naytto.blit(kuva, (hahmo[1], hahmo[2]))
    for vihollinen in viholliset:
        if vihollinen[3]:
            kuva = pygame.image.load(vihollinen[0]).convert()
            naytto.blit(kuva, (vihollinen[1], vihollinen[2]))
    pygame.display.flip()

def kontrolli(hahmot, viholliset, tapahtuma):
    for vihollinen in viholliset:
        if vihollinen[1] == hahmot[0][1] and vihollinen[2] == hahmot[0][2]:
            del hahmot[0]
    if tapahtuma.type == pygame.KEYDOWN:
        if tapahtuma.key == pygame.K_SPACE:
            for hahmo in hahmot:
                hahmo[3] = True
            for vihollinen in viholliset:
                vihollinen[3] = True
        elif tapahtuma.key == pygame.K_RIGHT:
            päähahmo = hahmot[0]
            if rajat([päähahmo[1] + 10, päähahmo[2]]):
                päähahmo[1] += 10
        elif tapahtuma.key == pygame.K_LEFT:
            päähahmo = hahmot[0]
            if rajat([päähahmo[1] - 10, päähahmo[2]]):
                päähahmo[1] -= 10
        elif tapahtuma.key == pygame.K_UP:
            päähahmo = hahmot[0]
            if rajat([päähahmo[1], päähahmo[2] - 10]):
                päähahmo[2] -= 10
        elif tapahtuma.key == pygame.K_DOWN:
            päähahmo = hahmot[0]
            if rajat([päähahmo[1], päähahmo[2] + 10]):
                päähahmo[2] += 10

    if vihollinen[2] > 400:
        vihollinen[2] = 0
        vihollinen[1] = random.randint(0, 600)
        vihollinen[0] = viholliskuvat[random.randint(0, len(viholliskuvat) - 1)]
    else:
        vihollinen[2] += 10

def rajat(suunta):
    return suunta[0] > 0 and suunta[0] < 640 - 16 and suunta[1] > 0 and suunta[1] < 400 - 16

def main():
    hahmo = ["heart.png", 100, 100, False]
    viholliset = [["vihollinen.jpg", 200, 200, False]]
    hahmot = [hahmo]
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, viholliset, tapahtuma)
        piirtaminen(naytto, hahmot, viholliset)


main()
