pA = [1, 2, 3, 4, 5]

pB = []
pC = []

C = pA

wygrana = pA
dysk = max(pA)
print(pA, pB, pC)
liczba_ruch = 0

while pA != pB:


            przelozenie = input("Podaj skąd dokąd przełożyć dysk: \n")

            if przelozenie == 'ab':
                dysk = max(pA)
                if (len(pB) > 0 and dysk > pB[-1]) or pB == []:
                 pB.append(dysk)
                 #pB[0] = dysk
                 #pA[-1] = 0
                 pA.pop()



            if przelozenie == 'ac':
                dysk = max(pA)
                if (len(pC) > 0 and dysk > pC[-1]) or pC == []:
                 pC.append(dysk)
                 #pC[0] = dysk
                 #pA[-1] = 0
                 pA.pop()


            if przelozenie == 'ba':
                dysk = max(pB)
                if (len(pA) > 0 and dysk > pA[-1]) or pA == []:
                 pA.append(dysk)
                 pB.pop()


            if przelozenie == 'bc':
                dysk = max(pB)
                if (len(pC) > 0 and dysk > pC[-1]) or pC == []:
                 pC.append(dysk)
                 pB.pop()


            if przelozenie == 'ca':
                dysk = max(pC)
                if (len(pA) > 0 and dysk > pA[-1]) or pA == []:
                 pA.append(dysk)
                 pC.pop()

            if przelozenie == 'cb':
                dysk = max(pC)
                if (len(pB) > 0 and dysk > pB[-1]) or pB == []:
                 pB.append(dysk)
                 pC.pop()





            liczba_ruch +=1
            print(pA, pB, pC)


print("Wygrana!")
print("Liczba ruchów: ", liczba_ruch)