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

#tytuł gry

GAME_TITLE = 'Wieże Hanoi'

#okno głowne
GAME_SURFACE = pygame.display.set_mode((WIDTHsc, HEIGHTsc))

#tytuł
pygame.display.set_caption('Wieże Hanoi')



#stałe dla kolorów
class Palette:
    def __init__(self):

        self.GREEN = (160, 161, 97)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BROWN = (69, 49, 19)
        self.GREY5 = (111, 123, 126)
        self.GREY4 = (101, 113, 116)
        self.GREY3 = (91, 103, 106)
        self.GREY2 = (81, 93, 96)
        self.GREY1 = (71, 83, 86)
        self.LIGHTBROWN = (190, 110, 60)
        self.LIGHTGREY = (131, 132, 156)

class Napisy:
    def napisz(self, tekst, kolor, x, y, rozmiar):
        czcionka = pygame.font.SysFont("Arial", rozmiar)
        rend = czcionka.render(tekst, 1, kolor)
        tlo.blit(rend, (x, y))

#class Obsluga_myszy:


'''class Przyciski:
    def dodaj_przycisk(self, ekran, kolor_tla, kolor_tekstu, tekst, x, y, szer, wys):
        przycisk = pygame.draw.rect(ekran, kolor_tla, pygame.Rect(x, y, szer, wys))
        nap.napisz(tekst, kolor_tekstu, x, y, 30)


class Wyswietl_menu:
    def wyswietl(self):
        if aktualny_ekran == "menu":
            GAME_SURFACE.fill(col.GREEN)
            screen1 = pygame.display.get_surface()
            przyc.dodaj_przycisk(screen1, col.BLACK, col.WHITE, "Nowa gra", 300 - WIDTHsc/2, 100, 300, 80)'''


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

    def rysuj(self, kolor):
            klocki = pygame.draw.rect(tlo, kolor, pygame.Rect(self.x, self.y, self.dlu, self.wys))

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
    def __init__(self, kolor, poziom, dlu, wieza):
     klasa_wspolrzedne = Oblicz_wspolrzedne(poziom, dlu, wieza)
     wspolrzedne = klasa_wspolrzedne.policz()
     krazek = klasa_wspolrzedne.rysuj(kolor)

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
 #analogicznie jeśli: dokad = 1 -> na wieżę 1 itd.
    #dysk - aktualnie przekładany dysk

        """krazek1A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(240, 667, 155, 17))
        krazek2A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(250, 650, 135, 17))
        krazek3A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(260, 633, 115, 17))
        krazek4A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(270, 616, 95, 17))
        krazek5A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(280, 599, 75, 17))"""


#obiekt klasy Palette
col = Palette()

#obiekt klasy Napisy
nap = Napisy()

#obiekt klasy Przyciski
#przyc = Przyciski()

#obiekt klasy Wyswietl_menu
#menu = Wyswietl_menu()
#słownik przypisujący do nr klocka jego długość
dictA = {5:75, 4:95, 3:115, 2:135, 1:155}
#pA to lista odpowiadająca klockom na wieży a
pA = [155, 135, 115, 95, 75]
pB = []
pC = []
dysk = min(pA)
poziom = 1
ruch = []
wszystkie_ruchy = []
przechowalnia = []
z_a = False
z_b = False
z_c = False
na_a = False
na_b = False
na_c = False
clics = []

'''if len(clics)!=0:
    for index_clicks in range(len(clics)):
        if index_clics % 2 ==0: #dla elementów zagnieżdżonej listy "clics" o indeksach parzystych, reprezentujących pozycję myszy po kliknięciu
            klikniecie = "podnies"   #w celu podniesienia klocka z wieży
            print("Kliknięcie w pętli 1: ", klikniecie)

                #wieża1
            if 480 < clicks[index_clicks][1] < 729 and 217 < clicks[index_clicks][0] < 413: #sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 1
                z_a = True

                #wieża2
            elif 480 < clicks[index_clicks][1] < 729 and 528 < clicks[index_clicks][0] < 728: #sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 2
                z_b = True

                #wieża3
            elif 480 < clicks[index_clicks][1] < 729 and 836 < clicks[index_clicks][0] < 1036: #sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 3
                z_c = True

        else: #dla elementów zagnieżdżonej listy "clics" o indeksach nieparzystych, reprezentujących pozycję myszy po kliknięciu
            klikniecie = "poloz"  #w celu położenia klocka na wieżę
            print("Kliknięcie w pętli 2: ", klikniecie)

            # wieża1
            if 480 < clicks[index_clicks][1] < 729 and 217 < clicks[index_clicks][0] < 413:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 1
                na_a = True

                # wieża2
            elif 480 < clicks[index_clicks][1] < 729 and 528 < clicks[index_clicks][0] < 728:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 2
                na_b = True

                # wieża3
            elif 480 < clicks[index_clicks][1] < 729 and 836 < clicks[index_clicks][0] < 1036:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 3
                na_c = True'''

'''if a == True and b == True:
    if
    przelozenie = "ab"
    przelozenie = "ba"
if a == True and c == True:
    przelozenie = "ac"
    przelozenie = "ca"
if b == True and c == True:
    przelozenie = "bc"
    przelozenie = "cb"'''

while True:

     #screen1 = pygame.display.get_surface()
     #aktualny_ekran = "menu"
     #menu.wyswietl()

        #kolor tla
        #GAME_SURFACE.fill(col.GREEN)
        #załadowanie obrazu do tła
     tlo = pygame.image.load("tlo1m.png").convert()
        #pobieramy informacje o ekranie - tle
     screen = pygame.display.get_surface()

#napisy
     nap.napisz("Kliknij lewy przycisk myszy nad wieżą, z której chcesz przenieść klocek", col.GREY3, 141, 15, 12)
     nap.napisz("Kliknij prawy przycisk myszy nad więżą, na którą chcesz przenieść klocek", col.GREY3, 141, 40, 12)
     nap.napisz("31", col.WHITE, 590, 30, 72)
     nap.napisz("Menu główne", col.WHITE, 11, 11, 16)

#narysowanie wież i ich podstaw oraz zmiana ich koloru (podświetlenie) po najechaniu na nie myszką
     pozycja_kursora = pygame.mouse.get_pos()
     #print(pozycja_kursora)

     if 217 < pozycja_kursora[0] < 413 and 480 < pozycja_kursora[1] < 729:

         wieza1_podswietlenie = pygame.draw.rect(tlo, col.LIGHTBROWN, pygame.Rect(310, 500, 15, 170)) #podświetlona wieża1
         podstawa1_podswietlenie = pygame.draw.rect(tlo, col.LIGHTBROWN, pygame.Rect(290, 670, 55, 10))
         wieza2 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(620, 500, 15, 170))
         podstawa2 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(600, 670, 55, 10))
         wieza3 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(930, 500, 15, 170))
         podstawa3 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(910, 670, 55, 10))

     elif 528 < pozycja_kursora[0] < 728 and 480 < pozycja_kursora[1] < 729:

         wieza2_podswietlenie = pygame.draw.rect(tlo, col.LIGHTBROWN, pygame.Rect(620, 500, 15, 170)) #podświetlona wieża2
         podstawa2_podswietlenie = pygame.draw.rect(tlo, col.LIGHTBROWN, pygame.Rect(600, 670, 55, 10))
         wieza1 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(310, 500, 15, 170))
         podstawa1 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(290, 670, 55, 10))
         wieza3 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(930, 500, 15, 170))
         podstawa3 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(910, 670, 55, 10))

     elif 836 < pozycja_kursora[0] < 1036 and 480 < pozycja_kursora[1] < 729:

         wieza3_podswietlenie = pygame.draw.rect(tlo, col.LIGHTBROWN, pygame.Rect(930, 500, 15, 170)) #podświetlona wieża3
         podstawa3_podswietlenie = pygame.draw.rect(tlo, col.LIGHTBROWN, pygame.Rect(910, 670, 55, 10))
         wieza1 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(310, 500, 15, 170))
         podstawa1 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(290, 670, 55, 10))
         wieza2 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(620, 500, 15, 170))
         podstawa2 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(600, 670, 55, 10))

     else:

         wieza1 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(310, 500, 15, 170))        #wszystkie wieże bez podświetlenia
         podstawa1 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(290, 670, 55, 10))
         wieza2 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(620, 500, 15, 170))
         podstawa2 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(600, 670, 55, 10))
         wieza3 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(930, 500, 15, 170))
         podstawa3 = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(910, 670, 55, 10))

     # krążki na 1 wieży

     '''krazek = [1,2,3,4,5]
     for key, value in dictA.items():

        krazek[key-1] = Narysuj_krazek(key,value,1)'''

     krazek1 = Narysuj_krazek(col.GREY1, 1, 155, 1)
     krazek2 = Narysuj_krazek(col.GREY2, 2, 135, 1)
     krazek3 = Narysuj_krazek(col.GREY3, 3, 115, 1)
     krazek4 = Narysuj_krazek(col.GREY4, 4, 95, 1)
     krazek5 = Narysuj_krazek(col.GREY5, 5, 75, 1)

     listakraz = [krazek1, krazek2, krazek3, krazek4, krazek5]


     #poczatkowe.rysujplansze()

     # krążki na 1 wieży - stan początkowy
     #krazek1A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(240, 667, 155, 17))
     #krazek2A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(250, 650, 135, 17))
     #krazek3A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(260, 633, 115, 17))
     #krazek4A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(270, 616, 95, 17))
     #krazek5A = pygame.draw.rect(tlo, col.GREY, pygame.Rect(280, 599, 75, 17))

     if len(clics) != 0:
         for index_clics in range(len(clics)):
             if index_clics % 2 == 0:  # dla elementów zagnieżdżonej listy "clics" o indeksach parzystych, reprezentujących pozycję myszy po kliknięciu
                 klikniecie = "podnies"  # w celu podniesienia klocka z wieży
                 print("Kliknięcie w pętli 1: ", klikniecie)

                 # wieża1
                 if 480 < clics[index_clics][1] < 729 and 217 < clics[index_clics][0] < 413:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 1
                     z_a = True

                     # wieża2
                 elif 480 < clics[index_clics][1] < 729 and 528 < clics[index_clics][0] < 728:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 2
                     z_b = True

                     # wieża3
                 elif 480 < clics[index_clics][1] < 729 and 836 < clics[index_clics][0] < 1036:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 3
                     z_c = True

             else:  # dla elementów zagnieżdżonej listy "clics" o indeksach nieparzystych, reprezentujących pozycję myszy po kliknięciu
                 klikniecie = "poloz"  # w celu położenia klocka na wieżę
                 print("Kliknięcie w pętli 2: ", klikniecie)

                 # wieża1
                 if 480 < clics[index_clics][1] < 729 and 217 < clics[index_clics][0] < 413:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 1
                     na_a = True

                     # wieża2
                 elif 480 < clics[index_clics][1] < 729 and 528 < clics[index_clics][0] < 728:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 2
                     na_b = True

                     # wieża3
                 elif 480 < clics[index_clics][1] < 729 and 836 < clics[index_clics][0] < 1036:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 3
                     na_c = True

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
                clics.append(pozycja_kursora)

            #if klik_mysz == (1, 0, 0):


                '''print("lewy")
                if 480 < pozycja_kursora[1] < 729:  #sprawdzenie czy mysz znajduje się pomiędzy danymi y obejmującymi wysokość wszystkich trzech wież

                    #wieża1
                    if 217 < pozycja_kursora[0] < 413:  #sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 1
                          #aktualny krążek to element najmniejszy z listy pA równy długości najmniejszego krążka
                                #usunięcie ostatniego elementu z listy pA
                        print("wieza 1")


                        a = True
                        ruch.append("a")
                        clics.append(pozycja_kursora)
                        else:
                            nap.napisz("Tu nie ma krążków!", col.WHITE, 258, 694, 12)

                    #wieża2
                    elif 528 < pozycja_kursora[0] < 728:  #sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 2
                        print("wieza 2")

                        b = True
                        ruch.append("b")
                        clics.append(pozycja_kursora)
                        else:
                            nap.napisz("Tu nie ma krążków!", col.WHITE, 577, 694, 12)

                    #wieża3
                    elif 836 < pozycja_kursora[0] < 1036:  ##sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 3
                        print("wieza 3")

                        c = True
                        ruch.append("c")
                        clics.append(pozycja_kursora)'''

                            #nap.napisz("Tu nie ma krążków!", col.WHITE, 897, 694, 12)


            '''#if klik_mysz == (0, 0, 1):
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
                            pA.append(dysk)
                            ruch.append("a")                                            # dołączenie do listy (wieży) aktualnie przenoszonego elementu (krążka) = "dysku"
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
                            ruch.append("b")
                            print("wieza 2")

                    #wieża3
                    elif 836 < pozycja_kursora[0] < 1036:  #sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 3
                        dysk = min(pA)
                        wieza = 3
                        if (len(pC) > 0 and dysk < pC[-1]) or pC == []:
                            poziom = len(pC) + 1
                            pA.pop()
                            pC.append(dysk)
                            ruch.append("c")
                            print("wieza 3")'''

            print(pA, pB, pC)
            print(ruch)
            if len(ruch) == 2:

                 wszystkie_ruchy.append(ruch)
                 del ruch[0:2]

            print(wszystkie_ruchy)
            print("z_a = ", z_a, " z_b = ", z_b, " z_c = ", z_c)


        print("clics: ", clics)
        #print("Klikniecie: ", klikniecie)

        pygame.display.update()



  # przypisanie grafiki do określonego miejsca ekranu
     screen.blit(tlo, (0, 0))
     pygame.display.flip()
     pygame.display.update()