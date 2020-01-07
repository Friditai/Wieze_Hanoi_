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
        self.LIGHTBROWN = (180, 100, 50)
        self.LIGHTGREY = (131, 132, 156)

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

# funkcja rysująca krążki z użyciem grafiki
    '''def rysgraf(self):
        xpocz = 240
        roznicax = 10
        ypocz = 667
        roznicay = 17

        # opcjonalne grafiki krążków
        grafkr1 = pygame.image.load("klocek1.png").convert
        grafkr2 = pygame.image.load("klocek2.png").convert
        grafkr3 = pygame.image.load("klocek3.png").convert
        grafkr4 = pygame.image.load("klocek4.png").convert
        grafkr5 = pygame.image.load("klocek5.png").convert


        tlo.blit(grafkr5, (xpocz, ypocz))
        tlo.blit(grafkr4, (xpocz + roznicax, ypocz - roznicay))
        tlo.blit(grafkr3, (xpocz + 2*roznicax, ypocz - 2*roznicay))
        tlo.blit(grafkr2, (xpocz + 3*roznicax, ypocz - 3*roznicay))
        tlo.blit(grafkr1, (xpocz + 4*roznicax, ypocz - 4*roznicay))'''




class Krazek(Oblicz_wspolrzedne):
    def __init__(self, poziom, dlu, wieza):
        super().__init__(poziom, dlu, wieza)

    def rysuj(self):
        klocki = pygame.draw.rect(tlo, col.GREY, pygame.Rect(self.x, self.y, self.dlu, self.wys))


class Narysuj_krazek():
    def __init__(self, poziom, dlu, wieza):
     klasa_wspolrzedne = Oblicz_wspolrzedne(poziom, dlu, wieza)
     wspolrzedne = klasa_wspolrzedne.policz()
     krazek = klasa_wspolrzedne.rysuj()

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
            klocki = pygame.draw.rect(tlo, col.GREY, pygame.Rect(iksy[i], ygreki[i], dlulista[i], self.wys))

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
#poczatkowe = Ulozenie_planszy(1,75,1)


while True:

     #słownik przypisujący do nr klocka jego długość
     dictA = {5:75, 4:95, 3:115, 2:135, 1:155}
     #pA to lista odpowiadająca klockom na wieży a
     pA = [155, 135, 115, 95, 75]
     pB = []
     pC = []
     dysk = min(pA)
     poziom = 1



        #kolor tla
        #GAME_SURFACE.fill(col.GREEN)
        #załadowanie obrazu do tła
     tlo = pygame.image.load("tlo1m.png").convert()
        #pobieramy informacje o ekranie - tle
     screen = pygame.display.get_surface()


#narysowanie wież i ich podstaw
     pozycja_kursora = pygame.mouse.get_pos()

     if 217 < pozycja_kursora[0] < 413 and 480 < pozycja_kursora[1] < 729:

         wieza1_podswietlenie = pygame.draw.rect(tlo, col.LIGHTBROWN, pygame.Rect(310, 500, 15, 170))
         podstawa1_podswietlenie = pygame.draw.rect(tlo, col.LIGHTBROWN, pygame.Rect(290, 670, 55, 10))
         wieza2 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(620, 500, 15, 170))
         podstawa2 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(600, 670, 55, 10))
         wieza3 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(930, 500, 15, 170))
         podstawa3 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(910, 670, 55, 10))

     elif 528 < pozycja_kursora[0] < 728 and 480 < pozycja_kursora[1] < 729:

         wieza2_podswietlenie = pygame.draw.rect(tlo, col.LIGHTBROWN, pygame.Rect(620, 500, 15, 170))
         podstawa2_podswietlenie = pygame.draw.rect(tlo, col.LIGHTBROWN, pygame.Rect(600, 670, 55, 10))
         wieza1 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(310, 500, 15, 170))
         podstawa1 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(290, 670, 55, 10))
         wieza3 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(930, 500, 15, 170))
         podstawa3 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(910, 670, 55, 10))

     elif 836 < pozycja_kursora[0] < 1036 and 480 < pozycja_kursora[1] < 729:

         wieza3_podswietlenie = pygame.draw.rect(tlo, col.LIGHTBROWN, pygame.Rect(930, 500, 15, 170))
         podstawa3_podswietlenie = pygame.draw.rect(tlo, col.LIGHTBROWN, pygame.Rect(910, 670, 55, 10))
         wieza1 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(310, 500, 15, 170))
         podstawa1 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(290, 670, 55, 10))
         wieza2 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(620, 500, 15, 170))
         podstawa2 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(600, 670, 55, 10))

     else:

         wieza1 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(310, 500, 15, 170))
         podstawa1 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(290, 670, 55, 10))
         wieza2 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(620, 500, 15, 170))
         podstawa2 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(600, 670, 55, 10))
         wieza3 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(930, 500, 15, 170))
         podstawa3 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(910, 670, 55, 10))

     # krążki na 1 wieży

     '''krazek = [1,2,3,4,5]
     

     for key, value in dictA.items():

        krazek[key-1] = Narysuj_krazek(key,value,1)'''


     krazek1 = Narysuj_krazek(1, 155, 1)
     krazek2 = Narysuj_krazek(2, 135, 1)
     krazek3 = Narysuj_krazek(3, 115, 1)
     krazek4 = Narysuj_krazek(4, 95, 1)
     krazek5 = Narysuj_krazek(5, 75, 1)

     listakraz = [krazek1, krazek2, krazek3, krazek4, krazek5]


     #poczatkowe.rysujplansze()





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
                #klik_mysz = pygame.mouse.get_pressed()
                #print(pozycja_kursora)
                #print(klik_mysz)

                #kliknięcie lewego przycisku myszy - wybór wieży, z której przenosimy krążek
                if event.button == 1:
                #if klik_mysz == (1, 0, 0):
                    print("lewy")
                    if 480 < pozycja_kursora[1] < 729:  #sprawdzenie czy mysz znajduje się pomiędzy danymi y obejmującymi wysokość wszystkich trzech wież

                        #wieża1
                        if 217 < pozycja_kursora[0] < 413:  #sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 1
                            dysk = min(pA)  #aktualny krążek to element najmniejszy z listy pA równy długości najmniejszego krążka
                                    #usunięcie ostatniego elementu z listy pA
                            print("wieza 1")


                        #wieża2
                        elif 528 < pozycja_kursora[0] < 728:  #sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 2
                            print("wieza 2")
                            dysk = min(pB)
                            pB.pop()

                        #wieża3
                        elif 836 < pozycja_kursora[0] < 1036:  ##sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 3
                            print("wieza 3")
                            dysk = min(pC)
                            pC.pop()


                #if klik_mysz == (0, 0, 1):
                #kliknięcie prawego przycisku myszy - wybór docelowej wieży, na którą przenosimy krążek z poprzednio wybranej wieży
                if event.button == 3:
                    print("prawy")
                    if 480 < pozycja_kursora[1] < 729:  #sprawdzenie czy mysz znajduje się pomiędzy danymi y obejmującymi wysokość wszystkich trzech wież

                        #wieża1
                        if 217 < pozycja_kursora[0] < 413:  #sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 1
                            dysk = min(pA)
                            wieza = 1                       #przypisanie do zmiennej "wieża" aktualny nr wieży
                            if (len(pA) > 0 and dysk < pA[-1]) or pA == []: #sprawdzenie czy jeśli na liście (wieży) są już elementy (krążki) czy aktualnie -
                                                                            # - przenoszony krążek = "dysk"  jest mniejszy od ostatniego krążka lub czy lista jest pusta
                                poziom = len(pA) + 1                        #przypisanie zmiennej "poziom", która jest piętrem, na którym ma się znależć krążek wartości o 1 -
                                                                             # - większej od ilości krążków na docelowej wieży
                                pA.append(dysk)                             # dołączenie do listy (wieży) aktualnie przenoszonego elementu (krążka) = "dysku"
                                print("wieza 1")

                        #wieża2
                        elif 528 < pozycja_kursora[0] < 728:  #sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 2
                            dysk = min(pA)
                            wieza = 2
                            if (len(pB) > 0 and dysk < pB[-1]) or pB == []:
                                poziom = len(pB) + 1

                                print("kwadrat")
                                pA.pop()
                                pB.append(dysk)
                                print("wieza 2")

                        #wieża3
                        elif 836 < pozycja_kursora[0] < 1036:  #sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 3
                            dysk = min(pA)
                            wieza = 3
                            if (len(pC) > 0 and dysk < pC[-1]) or pC == []:
                                poziom = len(pC) + 1
                                pC.append(dysk)

                                print("wieza 3")
                print(pA, pB, pC)
            pygame.display.update()





  # przypisanie grafiki do określonego miejsca ekranu
     screen.blit(tlo, (0, 0))








     pygame.display.flip()
     pygame.display.update()