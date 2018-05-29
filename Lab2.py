import numpy as np
import random
import time

W={"A":0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}


def UZ(Droga,A,B,Wa):
    Droga[W[A]][W[B]] = Wa
    Droga[W[B]][W[A]] = Wa
    return Droga


Drogi= [     [0 , -1 , -1 , -1 , -1 , -1 , -1], #A
             [-1 , 0 , -1 , -1 , -1 , -1 , -1],  #B
             [-1 , -1 , 0 , -1 , -1 , -1 , -1],  #C
             [-1 , -1 , -1 , 0 , -1 , -1 , -1],  #D
             [-1 , -1 , -1 , -1 , 0 , -1 , -1], #E
             [-1 , -1 , -1 , -1 , -1 , 0 , -1], #F
             [-1 , -1 , -1 , -1 , -1 , -1 , 0]   #G
]


Drogi=UZ(Drogi,'A','C',1)
Drogi=UZ(Drogi,'A','D',2)
Drogi=UZ(Drogi,'C','B',3)
Drogi=UZ(Drogi,'C','D',1)
Drogi=UZ(Drogi,'C','E',3)
Drogi=UZ(Drogi,'F','E',2)
Drogi=UZ(Drogi,'B','F',3)
Drogi=UZ(Drogi,'D','G',1)
Drogi=UZ(Drogi,'G','F',1)

Indeksy=['A','B','C','D','E','F','G']
S=[]                                                    # WIERZCHOLKI PRZETWORZONE
Q={'A','B','C','D','E','F','G'}                         # WIERZCHOLKI DO PRZETWORZENIA
D_W={'A':-1,'B':-1,'C':-1,'D':-1,'E':-1,'F':-1,'G':-1}  # Tymczasowe drogi
Q.discard('A')
D_W['A']=0
S.append('A')
Najmniejszy_W='A'


for i in Indeksy:
    if (Drogi[W[Najmniejszy_W]][W[i]] > 0):
        if (D_W[i] > Drogi[W[Najmniejszy_W]][W[i]] or D_W[i] < 0):
            D_W[i] = Drogi[W[Najmniejszy_W]][W[i]]
#-------PETLA-------------#

while(len(Q)>0):

    # SZUKAMY NAJMNIEJSZEJ DROGI

    Wartosc=100
    Najmniejszy_TEMP='A' # tymczasowy by nie zmienial petli


    for i in Q:  # Dla wszystkich otaczajacych wierzcholkow
        if(Drogi[W[Najmniejszy_W]][W[i]]>0): # Sprawdz czy jest do nich polaczenie
                if(D_W[i]>Drogi[W[Najmniejszy_W]][W[i]] or D_W[i]<0):
                    D_W[i]=Drogi[W[Najmniejszy_W]][W[i]]+D_W[Najmniejszy_W]

                if(D_W[i]>0 and D_W[i]<Wartosc): # Jesli jest do niego polaczenie i ma najmniejsza wartosc z obecnych, przejdz do niego
                    Wartosc=D_W[i]
                    Najmniejszy_TEMP=i

    if(Najmniejszy_TEMP=='A'):
        S.append(Najmniejszy_W)
        Najmniejszy_W=Q.pop()

    else:
         Najmniejszy_W=Najmniejszy_TEMP
         S.append(Najmniejszy_W)  # dodaj wyszukany wierzcholek do nastepnego kroku
         Q.discard(Najmniejszy_W) # Usun wierzcholek ze swojej listy wiercholkow


    if(Najmniejszy_W=='F'):
        break



#-------PETLA-KONIEC---------#


print("Droga do F:")
print(S)
print("WARTOSCI DROGI:")
print (D_W)




















