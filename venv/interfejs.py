# Gra "Wieże Hanoi" napisana w języku Python 3 z wykorzystaniem biblioteki PyGame

import sys, pygame, time


# inicjalizacja modułów

pygame.init()
start_czasu = pygame.time.get_ticks()

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

muzyka = pygame.mixer.music.load("japansong.mp3")
pygame.mixer.music.play(-1)

nowy_czas = 0

class Czas:
    def __init__(self):
        self.start_czas = 0

    def start(self):
        self.start_czas = pygame.time.get_ticks()

    def obecny_czas(self):
        return (pygame.time.get_ticks() - self.start_czas)/1000


class Wyniki:
    def zapisz_wynik(self, current_score):
        plik = open("najlepsze_wyniki.txt", "w+")
        highscore = plik.read()
        highscore_in_no = float(highscore)
        if current_score < highscore_in_no:
            plik.write(str(current_score))
            highscore_in_no = current_score
            # use the highscore_in_no to print the highscore.
            plik.close()

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
        self.GREY5LIGHT = (111 + 50, 123 + 50, 126 + 50)
        self.GREY4LIGHT = (101 + 50, 113 + 50, 116 + 50)
        self.GREY3LIGHT = (91 + 50, 103 + 50, 106 + 50)
        self.GREY2LIGHT = (81 + 50, 93 + 50, 96 + 50)
        self.GREY1LIGHT = (71 + 50, 83 + 50, 86 + 50)

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
        textSurface = font.render(text, True, col.WHITE)
        return textSurface, textSurface.get_rect()

    def przycisk(self, pow, tekst, x, y, szer, wys, kolor_nieaktywny, kolor_aktywny, dzialanie=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + szer > mouse[0] > x and y + wys > mouse[1] > y:
            pygame.draw.rect(pow, kolor_aktywny, (x, y, szer, wys))
            if click[0] == 1 and dzialanie != None:
                if dzialanie == "gra":
                    cz.start()
                    cz.obecny_czas()
                    petla_gry()
                elif dzialanie == "wyjscie":
                    pygame.quit()
                    quit()
                elif dzialanie == "menu":

                    nap.zakryj_licznik()
                    zakrycie_poprzedniego = nap.zakryj(col.BLACK, 310 - 80, 545, 780, 200)
                    menu_glowne()
                    restart()

        else:
            pygame.draw.rect(pow, kolor_nieaktywny, (x, y, szer, wys))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = mn.text_objects(tekst, smallText)
        textRect.center = ((x + (szer / 2)), (y + (wys / 2)))
        pow.blit(textSurf, textRect)

    def wyswietl_menu(self):

        intro = True

        while intro:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            GAME_SURFACE.fill(col.GREEN2)
            graf = pygame.image.load("rys2.png")
            graf_dol = pygame.image.load("rys2dol.png")
            GAME_SURFACE.blit(graf, (5, 5))
            GAME_SURFACE.blit(graf_dol, (780, 320))
            largeText = pygame.font.Font('freesansbold.ttf', 60)
            TextSurf, TextRect = mn.text_objects("Towers of Hanoi", largeText)
            TextRect.center = ((1280/2), (100))
            GAME_SURFACE.blit(TextSurf, TextRect)
            #napis1 = nap.napisz("Nowa gra", col.WHITE, 1280/2 - 300, 720/3 - 20, 20)

            mn.przycisk(GAME_SURFACE, "Nowa gra", 490, 200, 300, 50, col.BLACK, col.GREEN, "gra")
            mn.przycisk(GAME_SURFACE, "Wyjście", 490, 300, 300, 50, col.BLACK, col.GREEN, "wyjscie")

            pygame.display.update()
            clock.tick(15)


    def wygrana_wyswietl(self):

        wygrana = True

        while wygrana:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            GAME_SURFACE.fill(col.GREEN2)
            graf = pygame.image.load("rys2.png")
            graf_dol = pygame.image.load("rys2dol.png")
            GAME_SURFACE.blit(graf, (5, 5))
            GAME_SURFACE.blit(graf_dol, (780, 320))
            largeText = pygame.font.Font('freesansbold.ttf', 60)
            TextSurf, TextRect = mn.text_objects("Gratulacje!", largeText)
            TextRect.center = ((1280/2), (100))
            GAME_SURFACE.blit(TextSurf, TextRect)

            mn.przycisk(GAME_SURFACE, "Nowa gra", 490, 400, 300, 50, col.BLACK, col.GREEN, "gra")
            mn.przycisk(GAME_SURFACE, "Wyjście", 490, 500, 300, 50, col.BLACK, col.GREEN, "wyjscie")

            pygame.display.update()
            clock.tick(15)
    def restart(self):
        gra = False
        licznik_ruchow = 0
        start_sek = 0


class Animacja_obrazu:

    def wyswietl_poczatkowe(self):

        #napisy
        nap.napisz("Aby wykonać ruch kliknij na wieżę, z której chcesz przenieść klocek, a następnie na wieżę docelową.", col.GREEN, 241, 7, 12)

        nap.napisz("31", col.WHITE, 590, 30, 50)


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


cz = Czas()

wyn = Wyniki()

#obiekt klasy Palette
col = Palette()

#obiekt klasy Napisy
nap = Napisy()

mn = Menu()

#obiekt klasy Animacja_obrazu
obraz = Animacja_obrazu()

def petla_gry():


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

    #obiekt klasy Animacja_obrazu
    obraz.wyswietl_poczatkowe()
    wygrana = False
    gra = True

    while gra:



         #zliczanie ruchów gracza
         licznik_ruchow = len(przelozenia) - 1

         #czas od startu gry
         start_sek = cz.obecny_czas()
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

         zegar = nap.napisz("{:0>2}".format(time_minuty) + ":" + "{:0>2}".format(time_sekund), col.WHITE, 240, 29, 50)

         mn.przycisk(tlo, "Menu", 15, 11, 60, 20, col.BLACK, col.GREEN, "menu")



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

                                kolor1 = col.GREY1
                                kolor2 = col.GREY2
                                kolor3 = col.GREY3
                                kolor4 = col.GREY4
                                kolor5 = col.GREY5

                                kolor1l = col.GREY1LIGHT
                                kolor2l = col.GREY2LIGHT
                                kolor3l = col.GREY3LIGHT
                                kolor4l = col.GREY4LIGHT
                                kolor5l = col.GREY5LIGHT

                                jaki_kolor = {75: kolor5, 95: kolor4, 115: kolor3, 135: kolor2, 155: kolor1}


                                jaki_kolorLIGHT = {75: kolor5l, 95: kolor4l, 115: kolor3l, 135: kolor2l, 155: kolor1l}



                                # wieża1
                                if 480 < clics[index_clics][1] < 729 and 217 < clics[index_clics][
                                    0] < 413:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 1
                                    z_a = True
                                    z_b = False
                                    z_c = False

                                    if len(pA)>0:
                                      poz1 = len(pA)
                                      dl1 = min(pA)
                                      w1 = 1
                                      kolor1l = jaki_kolorLIGHT.get(dl1)
                                      Narysuj_krazek(kolor1l, poz1, dl1, w1)

                                    if len(pB)>0:
                                      poz2 = len(pB)
                                      dl2 = min(pB)
                                      w2 = 2
                                      kolor2w = jaki_kolor.get(dl2)
                                      Narysuj_krazek(kolor2w, poz2, dl2, w2)


                                    if len(pC)>0:
                                      poz3 = len(pC)
                                      dl3 = min(pC)
                                      w3 = 3
                                      kolor3w = jaki_kolor.get(dl3)
                                      Narysuj_krazek(kolor3w, poz3, dl3, w3)







                                    # print("z_a = ", z_a)

                                    # wieża2
                                elif 480 < clics[index_clics][1] < 729 and 528 < clics[index_clics][
                                    0] < 728:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 2
                                    z_b = True
                                    z_a = False
                                    z_c = False

                                    if len(pB) > 0:
                                      poz2 = len(pB)
                                      dl2 = min(pB)
                                      w2 = 2
                                      kolor2l = jaki_kolorLIGHT.get(dl2)
                                      Narysuj_krazek(kolor2l, poz2, dl2, w2)

                                    if len(pC) > 0:
                                        poz3 = len(pC)
                                        dl3 = min(pC)
                                        w3 = 3
                                        kolor3w = jaki_kolor.get(dl3)
                                        Narysuj_krazek(kolor3w, poz3, dl3, w3)

                                    if len(pA) > 0:
                                      poz1 = len(pA)
                                      dl1 = min(pA)
                                      w1 = 1
                                      kolor1w = jaki_kolor.get(dl1)
                                      Narysuj_krazek(kolor1w, poz1, dl1, w1)







                                    # print("z_b = ", z_b)

                                    # wieża3
                                elif 480 < clics[index_clics][1] < 729 and 836 < clics[index_clics][
                                    0] < 1036:  # sprawdzenie czy mysz znajduje się pomiędzy danymi x obejmującymi wieżę 3
                                    z_c = True
                                    z_a = False
                                    z_b = False

                                    if len(pC) > 0:
                                      poz3 = len(pC)
                                      dl3 = min(pC)
                                      w3 = 3
                                      kolor3l = jaki_kolorLIGHT.get(dl3)
                                      Narysuj_krazek(kolor3l, poz3, dl3, w3)

                                    if len(pB) > 0:
                                      poz2 = len(pB)
                                      dl2 = min(pB)
                                      w2 = 2
                                      kolor2w = jaki_kolor.get(dl2)
                                      Narysuj_krazek(kolor2w, poz2, dl2, w2)

                                    if len(pA) > 0:
                                      poz1 = len(pA)
                                      dl1 = min(pA)
                                      w1 = 1
                                      kolor1w = jaki_kolor.get(dl1)
                                      Narysuj_krazek(kolor1w, poz1, dl1, w1)








                                    # print("z_c = ", z_c)

                                else:  # pole poza wieżami
                                    z_a = False
                                    z_b = False
                                    z_c = False

                                    if len(pC) > 0:
                                      poz3 = len(pC)
                                      dl3 = min(pC)
                                      w3 = 3
                                      kolor3w = jaki_kolor.get(dl3)
                                      Narysuj_krazek(kolor3w, poz3, dl3, w3)

                                    if len(pB) > 0:
                                      poz2 = len(pB)
                                      dl2 = min(pB)
                                      w2 = 2
                                      kolor2w = jaki_kolor.get(dl2)
                                      Narysuj_krazek(kolor2w, poz2, dl2, w2)

                                    if len(pA) > 0:
                                      poz1 = len(pA)
                                      dl1 = min(pA)
                                      w1 = 1
                                      kolor1w = jaki_kolor.get(dl1)
                                      Narysuj_krazek(kolor1w, poz1, dl1, w1)








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

                                 nap.zakryj(col.BLACK, 258, 694, 160, 15)


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

                                 nap.zakryj(col.BLACK, 258, 694, 160, 15)

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


                                 nap.zakryj(col.BLACK, 577, 694, 160, 15)





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



                                  nap.napisz("Tu nie ma krążków!", col.WHITE, 577, 694, 12)
                                  nap.zakryj(col.BLACK, 577, 694, 160, 15)


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

                                 nap.zakryj(col.BLACK, 897, 694, 160, 15)
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

                                 nap.zakryj(col.BLACK, 897, 694, 160, 15)
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
                        print("Wygrana!")
                        ekran_wygranej()



         nap.napisz("Wygrana!", col.WHITE, 180 - 1280/2, 80 - 720/2, 80)


         pygame.display.flip()
         pygame.display.update()




         pygame.display.flip()
         pygame.display.update()

def menu_glowne():
     mn.wyswietl_menu()

def ekran_wygranej():
    mn.wygrana_wyswietl()


menu_glowne()
petla_gry()