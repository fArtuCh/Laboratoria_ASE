import numpy as np
import random
import time

W={"A":0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}


def UZ(Droga,A,B,Wa):
    Droga[W[A]][W[B]] = Wa
    Droga[W[B]][W[A]] = Wa
    return Droga


Drogi= [     [0 , 9 , 9 , 9 , 9 , 9 , 9], #A
             [9 , 0 , 9 , 9 , 9 , 9 , 9],  #B
             [9 , 9 , 0 , 9 , 9 , 9 , 9],  #C
             [9 , 9 , 9 , 0 , 9 , 9 , 9],  #D
             [9 , 9 , 9 , 9 , 0 , 9 , 9], #E
             [9 , 9 , 9 , 9 , 9 , 0 , 9], #F
             [9 , 9 , 9 , 9 , 9 , 9 , 0]   #G
]

Wielkosc=len(W)
Drogi=UZ(Drogi,'A','C',1)
Drogi=UZ(Drogi,'A','D',2)
Drogi=UZ(Drogi,'C','B',2)
Drogi=UZ(Drogi,'C','D',1)
Drogi=UZ(Drogi,'C','E',3)
Drogi=UZ(Drogi,'F','E',2)
Drogi=UZ(Drogi,'B','F',3)
Drogi=UZ(Drogi,'D','G',1)
Drogi=UZ(Drogi,'G','F',1)
Wartosc_trasy=[]

Indeksy=['A','B','C','D','E','F','G']
S=[]                                            # WIERZCHOLKI PRZETWORZONE
Q={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}   # WIERZCHOLKI DO PRZETWORZENIA
D_W={'A':9,'B':9,'C':9,'D':9,'E':9,'F':9,'G':9} # Tymczasowe drogi

#--------POCZATEK----------#
D_W['A']=0
S.append(Q['A'])
Q.__delitem__('A')
#--------Koniec------------#

#-------PETLA--------------#
koniec=False;
while(koniec):

    #Droga z A Do Wszystkich
    for i in Indeksy:
        if(Drogi[W['A']][W[i]]!=9):
            D_W[i]=Drogi[W['A']][W[i]]


    # SZUKAMY NAJMNIEJSZEJ DROGI
    Najmniejszy_W='G'
    Wartosc=9

    for i in Indeksy:
        if (Q.__contains__(i)):
            if(D_W[i]<Wartosc):
                Wartosc=D_W[i]
                Najmniejszy_W=i



    print("NAJMNIEJSZA DROGA DO:")
    print(Najmniejszy_W)
    Q.__delitem__(Najmniejszy_W)
    print("WARTOSCI DROGI:")
    print (D_W)
    print("POZOSTALE WIERCHOLKI:")
    print (Q)
    koniec=True;

#-------PETLA-KONIEC---------#
















