import numpy as np
import random
import timeit as T
import time
random.seed()

def sortuj_babelkowo(Lista):
    wielkosc=len(Lista)
    flaga=True
    for i in range(wielkosc-1):
        if(Lista[wielkosc-1-i]<Lista[wielkosc-i-2]):
            temp=Lista[wielkosc-i-1]
            temp2=Lista[wielkosc-i-2]
            Lista[wielkosc - i-1]=temp2
            Lista[wielkosc - i - 2]=temp
            flaga=False
            break;
    return Lista,flaga


def sortuj_zamiana(Lista2):
    wielkosc=len(Lista2)
    flaga=False
    najmniejszy_element=0
    aktualny_indeks=0;
    iterator=0;
    cos=True


    while(flaga==False):

        if (aktualny_indeks == wielkosc - 1):
            break

        if(Lista2[aktualny_indeks]>najmniejszy_element):
            iterator=aktualny_indeks
            while(cos):
                if(Lista2[iterator]==najmniejszy_element):
                    cos=False
                else:
                    iterator+=1
                    if(iterator==wielkosc-1):
                        cos=False
                        najmniejszy_element+=1

            cos=True
            temp1 = Lista2[aktualny_indeks]
            temp2 = Lista2[iterator]

            Lista2[aktualny_indeks]=temp2
            Lista2[iterator]=temp1


        else:
            if(aktualny_indeks<wielkosc):
                aktualny_indeks+=1
            else:
                break

        if(najmniejszy_element==9):
            flaga=True


    return Lista2,flaga




ilosc_elementow=200
random.randint(0,9)
Lista=np.arange(0,ilosc_elementow,1)
for i in range (ilosc_elementow):
    Lista[i]=random.randint(0,9);

Lista2=Lista.copy()
Lista3=Lista.copy()
Lista4=Lista.copy()
czy_koniec=False;
ile_razy=0

Pocz=time.clock()
while(czy_koniec==False):
    [Lista,czy_koniec]=sortuj_babelkowo(Lista)
    ile_razy+=1
Kon=time.clock()
print("Ile nawrotow:")
print(ile_razy)
print("Czas dla babelkowego:")
print (Kon-Pocz)
Pocz=time.clock()
Lista2=sortuj_zamiana(Lista2);
Kon=time.clock()
print("Czas dla zamiany:")
print (Kon-Pocz)

def sortuj_brytyjcycy(P1,P2):
    wielkosc=len(Lista3)
    if(P1>=0 and P1+1<P2):
        Piwo=P1;
        Lewy=P1+1;
        Prawy=P2;
        while(Lewy!=Prawy ):
            if(Lista3[Lewy]>=Lista3[Piwo]):
                if (Lista3[Prawy] < Lista3[Piwo]):
                    if(Prawy>=Lewy):
                        temp=Lista3[Prawy]
                        Lista3[Prawy]=Lista3[Lewy]
                        Lista3[Lewy]=temp
                    else:
                        break
                else:
                    if (Prawy >0):
                         Prawy-=1
                    else:
                         break
            else :
                Lewy+=1


        temp2 = Lista3[Piwo]
        Lista3[Piwo] = Lista3[Lewy - 1]
        Lista3[Lewy - 1] = temp2

        if(Piwo<Lewy):
            sortuj_brytyjcycy(Piwo,Lewy)
        if(Prawy!=wielkosc-1):
            sortuj_brytyjcycy(Prawy,wielkosc-1)
        return
    return

Pocz=time.clock()
sortuj_brytyjcycy(0,len(Lista3)-1)
Kon=time.clock()
print("Quick sort:")
print (Kon-Pocz)
