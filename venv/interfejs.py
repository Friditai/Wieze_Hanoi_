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

# obiekt klasy Palette
col = Palette()

while True:


     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sys.exit(0)
           #kolor tla
        #GAME_SURFACE.fill(col.GREEN)
     tlo = pygame.image.load("IMG_2012png.png").convert()
        # pobieramy informacje o ekranie - tle
     screen = pygame.display.get_surface()

#wieże
     wieza1 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(310,500,15,170))
     wieza2 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(620, 500, 15, 170))
     wieza3 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(930, 500, 15, 170))




        # przypisanie grafiki do określonego miejsca ekranu
     screen.blit(tlo, (0, 0))








     pygame.display.flip()
        #pygame.display.update()