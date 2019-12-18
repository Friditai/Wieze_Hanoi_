# Gra "Wieże Hanoi" napisana w języku Python 3 z wykorzystaniem biblioteki PyGame

import sys, pygame


# inicjalizacja modułów

pygame.init()
pygame.mixer.init()

# stałe

WIDTHsc = 1280
HEIGHTsc = 720
FPS = 60
WIDTH_TOWER = 20
HEIGHT_TOWER = 100

# tytuł gry

GAME_TITLE = 'Wieże Hanoi'

# okno głowne
GAME_SURFACE = pygame.display.set_mode((WIDTHsc, HEIGHTsc))

# tytuł
pygame.display.set_caption('Wieże Hanoi')



# stałe dla kolorów
class Palette:
    def __init__(self):

        self.GREEN = (110, 111, 47)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BROWN = (139, 69, 19)
        self.GREY = (91, 93, 116)

# obiekt klasy Palette
col = Palette()

while True:


     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sys.exit(0)
           #kolor tla
        #GAME_SURFACE.fill(col.GREEN)
     tlo = pygame.image.load("tlo1m.png").convert()
        # pobieramy informacje o ekranie - tle
     screen = pygame.display.get_surface()

#wieże
     wieza1 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(310, 500, 15, 170))
     podstawa1 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(290, 670, 55, 10))
     wieza2 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(620, 500, 15, 170))
     podstawa2 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(600, 670, 55, 10))
     wieza3 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(930, 500, 15, 170))
     podstawa3 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(910, 670, 55, 10))

     # wymiary krążków
     g = 17  # grubość krążka
     d1 = 155  # długość krążka nr 1 - najdłuższego
     d2 = 135
     d3 = 115
     d4 = 95
     d5 = 75

     # krążki na 1 wieży - stan początkowy

     krazek1A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(240, 667, 155, 17))
     krazek2A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(250, 650, 135, 17))
     krazek3A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(260, 633, 115, 17))
     krazek4A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(270, 616, 95, 17))
     krazek5A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(280, 599, 75, 17))




        # przypisanie grafiki do określonego miejsca ekranu
     screen.blit(tlo, (0, 0))








     pygame.display.flip()
        #pygame.display.update()