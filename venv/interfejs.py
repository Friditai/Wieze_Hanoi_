# Gra "Wieże Hanoi" napisana w języku Python 3 z wykorzystaniem biblioteki PyGame

import sys, pygame, time


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

clock = pygame.time.Clock()

#obraz tła - załadowanie obrazu do tła
tlo = pygame.image.load("nowetlo2.png").convert()





#stałe dla kolorów
class Palette:
    def __init__(self):

        self.GREEN = (160, 161, 97)
        self.GREEN2 = (62, 70, 37)
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

    def zakryj(self, kolor, x, y, szer, wys):
        kwadrat = pygame.draw.rect(tlo, kolor, pygame.Rect(x, y, szer, wys))

    def zakryj_licznik(self):
        nap.zakryj(col.BLACK, 1040, 29, 200, 50)


class Menu:

    def text_objects(self, text, font):
        textSurface = font.render(text, True, col.BLACK)
        return textSurface, textSurface.get_rect()

    def wyswietl_menu(self):

        intro = True

        while intro:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            GAME_SURFACE.fill(col.GREEN2)
            largeText = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = mn.text_objects("Towers of Hanoi", largeText)
            TextRect.center = ((1280/2 - 300), (720/3 - 20))
            GAME_SURFACE.blit(TextSurf, TextRect)
            #napis1 = nap.napisz("Nowa gra", col.WHITE, 1280/2 - 300, 720/3 - 20, 20)

            mouse = pygame.mouse.get_pos()

            # print(mouse)

            if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
                pygame.draw.rect(GAME_SURFACE, col.GREEN, (150, 450, 100, 50))
                pygame.draw.rect(GAME_SURFACE, col.GREEN, (550, 450, 100, 50))
            else:

                pygame.draw.rect(GAME_SURFACE, col.BLACK, (150, 450, 100, 50))
                pygame.draw.rect(GAME_SURFACE, col.BLACK, (550, 450, 100, 50))

            pygame.display.update()
            clock.tick(15)

class Animacja_obrazu:

    def wyswietl_poczatkowe(self):

        #napisy
        nap.napisz("Aby wykonać ruch kliknij na wiezę, z której chcesz przenieść klocek, a następnie na wieżę docelową.", col.GREEN, 241, 7, 12)

        nap.napisz("31", col.WHITE, 590, 30, 50)
        nap.napisz("Menu główne", col.WHITE, 11, 11, 16)

        # narysowanie wież i ich podstaw oraz zmiana ich koloru (podświetlenie) po najechaniu na nie myszką
        pozycja_kursora = pygame.mouse.get_pos()
        kolor_wiezy1 = col.BROWN
        kolor_wiezy2 = col.BROWN
        kolor_wiezy3 = col.BROWN

        print(pozycja_kursora)

        wieza1 = pygame.draw.rect(tlo, kolor_wiezy1, pygame.Rect(310, 500, 15, 170))  # wszystkie wieże bez podświetlenia
        podstawa1 = pygame.draw.rect(tlo, kolor_wiezy1, pygame.Rect(290, 670, 55, 10))
        wieza2 = pygame.draw.rect(tlo, kolor_wiezy2, pygame.Rect(620, 500, 15, 170))
        podstawa2 = pygame.draw.rect(tlo, kolor_wiezy2, pygame.Rect(600, 670, 55, 10))
        wieza3 = pygame.draw.rect(tlo, kolor_wiezy3, pygame.Rect(930, 500, 15, 170))
        podstawa3 = pygame.draw.rect(tlo,kolor_wiezy3, pygame.Rect(910, 670, 55, 10))

        if 217 < pozycja_kursora[0] < 413 and 480 < pozycja_kursora[1] < 729:

              # podświetlona wieża1
              kolor_wiezy1 = col.LIGHTBROWN
              wieza1 = pygame.draw.rect(tlo, kolor_wiezy1, pygame.Rect(310, 500, 15, 170))  # wszystkie wieże bez podświetlenia
              podstawa1 = pygame.draw.rect(tlo, kolor_wiezy1, pygame.Rect(290, 670, 55, 10))
              pygame.display.flip()
              pygame.display.update()

        elif 528 < pozycja_kursora[0] < 728 and 480 < pozycja_kursora[1] < 729:

              # podświetlona wieża2
              kolor_wiezy2 = col.LIGHTBROWN
              wieza2 = pygame.draw.rect(tlo, kolor_wiezy2, pygame.Rect(620, 500, 15, 170))
              podstawa2 = pygame.draw.rect(tlo, kolor_wiezy2, pygame.Rect(600, 670, 55, 10))
              pygame.display.flip()
              pygame.display.update()

        elif 836 < pozycja_kursora[0] < 1036 and 480 < pozycja_kursora[1] < 729:

             # podświetlona wieża3
              kolor_wiezy3 = col.LIGHTBROWN
              wieza3 = pygame.draw.rect(tlo, kolor_wiezy3, pygame.Rect(930, 500, 15, 170))
              podstawa3 = pygame.draw.rect(tlo, kolor_wiezy3, pygame.Rect(910, 670, 55, 10))
              pygame.display.flip()
              pygame.display.update()

        #krążki

        krazek5 = Narysuj_krazek(col.GREY5, 5, 75, 1)
        krazek4 = Narysuj_krazek(col.GREY4, 4, 95, 1)
        krazek3 = Narysuj_krazek(col.GREY3, 3, 115, 1)
        krazek2 = Narysuj_krazek(col.GREY2, 2, 135, 1)
        krazek1 = Narysuj_krazek(col.GREY1, 1, 155, 1)


    def wyswietl_ruch(self, dlugosc_krazka, poziom, wieza, poziom_st, wieza_st):


        kolor1 = col.GREY1
        kolor2 = col.GREY2
        kolor3 = col.GREY3
        kolor4 = col.GREY4
        kolor5 = col.GREY5

        jaki_kolor = {75: kolor5, 95: kolor4, 115: kolor3, 135: kolor2, 155: kolor1}
        kolor = jaki_kolor.get(dlugosc_krazka)

        nowy_krazek = Narysuj_krazek(kolor, poziom, dlugosc_krazka, wieza)

        zakrycie = Narysuj_krazek(col.BLACK, poziom_st, dlugosc_krazka, wieza_st)

        if wieza_st == 1:
            x_naprawy = 310
        elif wieza_st == 2:
            x_naprawy = 620
        else:
            x_naprawy = 930

        jakipoziom = {1: 667, 2: 650, 3: 633, 4: 616, 5: 599}
        y_naprawy = jakipoziom.get(poziom_st)
        naprawa_wiezy = pygame.draw.rect(tlo, col.BROWN, pygame.Rect(x_naprawy, y_naprawy, 15, 17))
        pygame.display.flip()
        pygame.display.update()


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


#obiekt klasy Palette
col = Palette()

#obiekt klasy Napisy
nap = Napisy()

mn = Menu()

mn.wyswietl_menu()

#obiekt klasy Animacja_obrazu
obraz = Animacja_obrazu()

#słownik przypisujący do nr klocka jego długość
dictA = {5:75, 4:95, 3:115, 2:135, 1:155}
#pA to lista odpowiadająca klockom na wieży a
pA = [155, 135, 115, 95, 75]
pB = []
pC = []
dysk = min(pA)
poziom = 1
wszystkie_ruchy = []
przelozenia = [0]
clics = []

#czas od startu gry



#obiekt klasy Animacja_obrazu
obraz.wyswietl_poczatkowe()
wygrana = False
gra = True

while gra:

     licznik_ruchow = len(przelozenia) - 1
     start_sek = pygame.time.get_ticks() / 1000
     time_minuty = int(start_sek // 60)
     time_sekund = int(start_sek % 60)
     z_a = False
     z_b = False
     z_c = False
     na_a = False
     na_b = False
     na_c = False
     len(clics) == 2

     #pobieramy informacje o ekranie
     screen = pygame.display.get_surface()
     screen.blit(tlo, (0, 0))

     #wyświetlenie licznika ruchów
     nap.napisz(str(licznik_ruchow), col.WHITE, 1040, 29, 50)

     zakrycie_zegara = nap.zakryj(col.BLACK, 210, 29, 180, 50)
     pygame.display.flip()
     pygame.display.update()
     zegar = nap.napisz(str(time_minuty)+":"+str(time_sekund), col.WHITE, 240, 29, 50)

     pygame.display.flip()
     pygame.display.update()

     #sterowanie
     for event in pygame.event.get():


        if event.type == pygame.QUIT:
            sys.exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:

            # obsługa kursora
            pozycja_kursora = pygame.mouse.get_pos()
            przycisk = pygame.mouse.get_pressed()

            #print(pozycja_kursora)


            #kliknięcie lewego przycisku myszy - dodanie aktualnej pozycji kursora do listy "pozycja_kursora"

            if event.button == 1:
                clics.append(pozycja_kursora)


                if len(clics) != 0:

                    if len(clics)==4:
                        clics[0] = clics[2]
                        clics[1] = clics[3]
                        del clics[2:]

                    for index_clics in range(len(clics)):



                        if index_clics % 2 == 0:  # dla elementów zagnieżdżonej listy "clics" o indeksach parzystych, reprezentujących pozycję myszy po kliknięciu
                            klikniecie = "podnies"  # w celu podniesienia klocka z wieży
                            print("Kliknięcie w pętli 1: ", klikniecie)


                            # wieża1
                            if 480 < clics[index_clics][1] < 729 and 217 < clics[index_clics][
                                0] < 413:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 1
                                z_a = True
                                z_b = False
                                z_c = False

                                # print("z_a = ", z_a)

                                # wieża2
                            elif 480 < clics[index_clics][1] < 729 and 528 < clics[index_clics][
                                0] < 728:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 2
                                z_b = True
                                z_a = False
                                z_c = False

                                # print("z_b = ", z_b)

                                # wieża3
                            elif 480 < clics[index_clics][1] < 729 and 836 < clics[index_clics][
                                0] < 1036:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 3
                                z_c = True
                                z_a = False
                                z_b = False

                                # print("z_c = ", z_c)

                            else:  # pole poza wieżami
                                z_a = False
                                z_b = False
                                z_c = False


                        else:  # dla elementów zagnieżdżonej listy "clics" o indeksach nieparzystych, reprezentujących pozycję myszy po kliknięciu
                            klikniecie = "poloz"  # w celu położenia klocka na wieżę
                            print("Kliknięcie w pętli 2: ", klikniecie)


                            # wieża1
                            if 480 < clics[index_clics][1] < 729 and 217 < clics[index_clics][
                                0] < 413:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 1
                                na_a = True
                                na_b = False
                                na_c = False


                                # print("na_a = ", na_a)

                                # wieża2
                            elif 480 < clics[index_clics][1] < 729 and 528 < clics[index_clics][
                                0] < 728:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 2
                                na_b = True
                                na_a = False
                                na_c = False


                                # print("na_b = ", na_b)

                                # wieża3
                            elif 480 < clics[index_clics][1] < 729 and 836 < clics[index_clics][
                                0] < 1036:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 3
                                na_c = True
                                na_a = False
                                na_b = False


                                # print("na_c = ", na_c)

                            else:  # pole poza wieżami
                                na_c = False
                                na_a = False
                                na_b = False


                        # przełożenia klocka z jednej wieży na drugą w zależności od wartości zmiennych wygenerowanych na podstawie kliknięć gracza
                        if z_a == True and na_b == True:

                            if len(pA)==0:
                             nap.napisz("Tu nie ma krążków!", col.WHITE, 258, 694, 12)

                            else:

                             print("Przelozenie ab")


                             dysk = min(pA)
                             if len(pA) > 0 and ((len(pB) > 0 and dysk < pB[-1]) or pB == []):

                                if przelozenia[-1] != "ab":
                                     nap.zakryj_licznik()
                                     przelozenia.append("ab")

                                poziom = len(pB) + 1
                                poziom_stary = len(pA)
                                pB.append(dysk)
                                pA.pop()
                                wieza = 2
                                wieza_stara = 1


                                obraz.wyswietl_ruch(dysk, poziom, wieza, poziom_stary, wieza_stara)
                                print("poziom: ", poziom)


                        elif z_a == True and na_c == True:

                            if len(pA)==0:
                             nap.napisz("Tu nie ma krążków!", col.WHITE, 258, 694, 12)

                            else:

                             print("Przełożenie ac")



                             dysk = min(pA)
                             if len(pA) > 0 and ((len(pC) > 0 and dysk < pC[-1]) or pC == []):

                                if przelozenia[-1] != "ac":
                                   nap.zakryj_licznik()
                                   przelozenia.append("ac")

                                poziom = len(pC) + 1
                                poziom_stary = len(pA)
                                pC.append(dysk)
                                pA.pop()
                                wieza = 3
                                wieza_stara = 1
                                obraz.wyswietl_ruch(dysk, poziom, wieza, poziom_stary, wieza_stara)


                        elif z_b == True and na_a == True:

                            if len(pB)==0:
                             nap.napisz("Tu nie ma krążków!", col.WHITE, 577, 694, 12)

                            else:

                             print("Przelozenie ba")


                             dysk = min(pB)
                             if len(pB) > 0 and ((len(pA) > 0 and dysk < pA[-1]) or pA == []):

                                if przelozenia[-1] != "ba":
                                    nap.zakryj_licznik()
                                    przelozenia.append("ba")

                                poziom = len(pA) + 1
                                poziom_stary = len(pB)
                                pA.append(dysk)
                                pB.pop()
                                wieza = 1
                                wieza_stara = 2
                                obraz.wyswietl_ruch(dysk, poziom, wieza, poziom_stary, wieza_stara)

                        elif z_b == True and na_c == True:

                            if len(pB)==0:

                              nap.zakryj(col.BLACK, 577, 694, 80, 12)

                              nap.napisz("Tu nie ma krążków!", col.WHITE, 577, 694, 12)


                            else:

                             print("Przelozenie bc")


                             dysk = min(pB)
                             if len(pB) > 0 and ((len(pC) > 0 and dysk < pC[-1]) or pC == []):

                                if przelozenia[-1] != "bc":
                                    nap.zakryj_licznik()
                                    przelozenia.append("bc")

                                poziom = len(pC) + 1
                                poziom_stary = len(pB)
                                pC.append(dysk)
                                pB.pop()
                                wieza = 3
                                wieza_stara = 2
                                obraz.wyswietl_ruch(dysk, poziom, wieza, poziom_stary, wieza_stara)

                        elif z_c == True and na_a == True:

                            if len(pC)==0:
                             nap.napisz("Tu nie ma krążków!", col.WHITE, 897, 694, 12)

                             nap.zakryj(col.BLACK, 897, 694, 12, 80)
                            else:
                             print("Przelozenie ca")


                             dysk = min(pC)
                             if len(pC) > 0 and ((len(pA) > 0 and dysk < pA[-1]) or pA == []):

                                if przelozenia[-1] != "ca":
                                    nap.zakryj_licznik()
                                    przelozenia.append("ca")

                                poziom = len(pA) + 1
                                poziom_stary = len(pC)
                                pA.append(dysk)
                                pC.pop()
                                wieza = 1
                                wieza_stara = 3
                                obraz.wyswietl_ruch(dysk, poziom, wieza, poziom_stary, wieza_stara)

                        elif z_c == True and na_b == True:

                            if len(pC)==0:
                             nap.napisz("Tu nie ma krążków!", col.WHITE, 897, 694, 12)

                             nap.zakryj(col.BLACK, 897, 694, 12, 80)
                            else:

                             print("Przelozenie cb")


                             dysk = min(pC)
                             if len(pC) > 0 and ((len(pB) > 0 and dysk < pB[-1]) or pB == []):

                                if przelozenia[-1] != "cb":
                                    nap.zakryj_licznik()
                                    przelozenia.append("cb")

                                poziom = len(pB) + 1
                                poziom_stary = len(pC)
                                pB.append(dysk)
                                pC.pop()
                                wieza = 2
                                wieza_stara = 3
                                obraz.wyswietl_ruch(dysk, poziom, wieza, poziom_stary, wieza_stara)

                        na_a = False
                        na_b = False
                        na_c = False

                print("clics: ", clics)
                print("Przełożenia: ", przelozenia)
                print("Stan wież Hanoi: ", pA, pB, pC)
                if pA == pB:

                    wygrana = True
                    seconds_survived = (pygame.time.get_ticks() - start_sec) /1000
                    print("Wygrana!")



     nap.napisz("Wygrana!", col.WHITE, 180 - 1280/2, 80 - 720/2, 80)

     '''stop_sek = pygame.time.get_ticks() / 1000
     time_minuty = int(stop_sek // 60)
     time_sekund = int(stop_sek % 60)'''

     pygame.display.flip()
     pygame.display.update()