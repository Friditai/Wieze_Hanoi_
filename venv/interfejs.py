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

#klasa robocza do obliczeń wspołrzędnych lewego górnego rogu krążka na ekranie, przy danym poziomie, długości krążka i danej wieży
class Oblicz_wspolrzedne:

    def __init__(self, poziom, dlu, wieza):
        self.x = 0
        self.y = 0
        self.wys = 17
        self.dlu = dlu
        self.poziom = poziom
        self.wieza = wieza


    def policz(self):
        #wx to współrzędne iksowe danej wieży
        if self.wieza == 1:
         wx = 310
        elif self.wieza == 2:
         wx = 620
        else:
         wx = 930
        jakipoziom = { 1:667,2:650,3:633,4:616,5:599}
        y = jakipoziom.get(self.poziom)
        x = wx-(self.dlu/2)+7.5
        self.x = x
        self.y = y

    def rysuj(self):
            klocki = pygame.draw.rect(tlo, col.GREY, pygame.Rect(self.x, self.y, self.dlu, self.wys))




class Krazek(Oblicz_wspolrzedne):
    def __init__(self, poziom, dlu, wieza):
        super().__init__(poziom, dlu, wieza)

    def rysuj(self):
        klocki = pygame.draw.rect(tlo, col.GREY, pygame.Rect(self.x, self.y, self.dlu, self.wys))



class Ulozenie_planszy(Krazek):


    def __init__(self, poziom, dlu, wieza):
        super().__init__(poziom, dlu, wieza)


    def rysujplansze(self):

        #lista = [krazek1A, krazek2A, krazek3A, krazek4A, krazek5A]

        #dlugosci klocków
        dlulista = []
        self.dlu = 75
        dlulista.append(self.dlu)
        for s in range(5):
            self.dlu+=20
            dlulista.append(self.dlu)

        #współrzędne iksowe klockow w stanie początkowym

        iksy = []
        self.x = 280
        iksy.append(self.x)
        for i in range(5):
            self.x-=10
            iksy.append(self.x)

        #współrzędne ygrekowe klocków w stanie początkowym
        ygreki = []
        self.y = 599
        ygreki.append(self.y)
        for i in range(5):
            self.y+=17
            ygreki.append(self.y)


        #rysowanie planszy pięciu klocków
        for i in range(5):
            klocki = pygame.draw.rect(tlo, col.GREY, pygame.Rect(iksy[i], ygreki[i], dlulista[i], self.wys  ))

 #metoda przekładająca krążek z jednej wieży na drugą, przy czym jeśli: skad = 1 -> z wieży 1, skad = 2 -> z wieży 2, skad = 3 -> z wieży ,
 #   analogicznie jeśli: dokad = 1 -> na wieżę 1 itd.
    # dysk - aktualnie przekładany dysk

        """krazek1A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(240, 667, 155, 17))
        krazek2A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(250, 650, 135, 17))
        krazek3A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(260, 633, 115, 17))
        krazek4A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(270, 616, 95, 17))
        krazek5A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(280, 599, 75, 17))"""


# obiekt klasy Palette
col = Palette()
poczatkowe = Ulozenie_planszy(1,75,1)


while True:

    # lista odpowiadająca klockom na wieży a
     pA = [1, 2, 3, 4, 5]
     pB = []
     pC = []















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


     poczatkowe.rysujplansze()





     # krążki na 1 wieży - stan początkowy

     #krazek1A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(240, 667, 155, 17))
     #krazek2A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(250, 650, 135, 17))
     #krazek3A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(260, 633, 115, 17))
     #krazek4A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(270, 616, 95, 17))
     #krazek5A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(280, 599, 75, 17))

     #sterowanie
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                # obsługa kursora
                pozycja_kursora = pygame.mouse.get_pos()
                klik_mysz = pygame.mouse.get_pressed()
                print(pozycja_kursora)
                print(klik_mysz)
                if klik_mysz == (1, 0, 0):
                    print("lewy")
                    if 480 < pozycja_kursora[1] < 729:
                        if 217 < pozycja_kursora[0] < 413:  # wieża1
                            dysk = max(pA)  # aktualny krążek
                            pA.pop()
                            print("wieza 1")
                        elif 528 < pozycja_kursora[0] < 728:  # wieża2
                            print("wieza 2")
                            dysk = max(pB)
                            pB.pop()
                        elif 836 < pozycja_kursora[0] < 1036:  # wieża3
                            print("wieza 3")
                            dysk = max(pC)
                            pC.pop()

                if klik_mysz == (0, 0, 1):
                    print("prawy")
                    if 480 < pozycja_kursora[1] < 729:
                        if 217 < pozycja_kursora[0] < 413:  # wieża1
                            dysk = max(pA)
                            if (len(pA) > 0 and dysk > pA[-1]) or pA == []:
                                poziom = len(pA) + 1
                                pA.append(dysk)

                                print("wieza 1")
                        elif 528 < pozycja_kursora[0] < 728:  # wieża2
                            dysk = max(pA)
                            if (len(pB) > 0 and dysk > pB[-1]) or pB == []:
                                poziom = len(pB) + 1
                                print("kwadrat")

                                klasa_wspolrzedne = Oblicz_wspolrzedne(1, 75, 2)
                                wspolrzedne = klasa_wspolrzedne.policz()
                                krazek = klasa_wspolrzedne.rysuj()

                                #cos = pygame.draw.rect(tlo, col.GREY, pygame.Rect(590, 667, 75, 17))

                                pB.append(dysk)
                                print("wieza 2")

                        elif 836 < pozycja_kursora[0] < 1036:  # wieża3
                            dysk = max(pA)
                            if (len(pC) > 0 and dysk > pC[-1]) or pC == []:
                                poziom = len(pC) + 1
                                pC.append(dysk)
                                print("wieza 3")







  # przypisanie grafiki do określonego miejsca ekranu
     screen.blit(tlo, (0, 0))








     pygame.display.flip()
     pygame.display.update()