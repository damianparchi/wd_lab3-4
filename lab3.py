#ZADANIE 1=================================
A=[1/x for x in range(1,11)]
B=[2**x for x in range(11)]
C=[x for x in B if x % 4 == 0]
print(A)
print(B)
print(C)
#ZADANIE 2=================================
lista=[
    [1,2,3,4],
    [4,5,6,7],
    [7,8,9,0],
    [1,2,3,4]
]

#ZADANIE 3==============

for row in lista:
    print(row)

    skroty={"PZU": "Państwowy zakład Ubezpieczeń",
            "ZUS": "Zakład Ubezpieczeń Społecznych",
                "PKO": "Powszechna Kasa Oszczędności"}
    odwrocone={value: key for key, value in skroty.items()}
    print("Oryginalny słownik")
    print(skroty)
    print("słownik odwrócony")
    print(odwrocone)

    produkt={"2 litry": "wody",
                "kilogram": "mąki",
                    "10 sztuk":"parówek",
                        "20 dekagramów":"ciastek"}
    odwrocone={value: key for key, value in produkt.items()}
    print("produkty")
    print(produkt)
    print("odwrocone")
    print(odwrocone)

    listanowa={value: key for key, value in produkt.items()}
    print(listanowa)


#zadanie 4===============
    def monotonicznosc_funkcji(a,x,b):
        y=a*x+b
        if(a>0):
            print("funkcja rosnaca")
            return a>0
        elif (a==0):
                print("funkcja stała")
        
        else:
            print("funkcja malejąca")
            return a<0

    print(monotonicznosc_funkcji(1,5,2))

#ZADANIE 5====================
def prostopadlosc_funkcji():
     y=a*x+b
# if(a1==a2): 
#     print("proste równoległe")
#     return a1=a2
#     elif(a1*a2==-1):
#         print("proste prostopadłe")
#         return a1*a2=-1
# print(prostopadlosc_funkcji(1,2,3))

def prostopadle_funkcji(a1,a2):
    if(a1==a2):
        return "rownolegle"
    elif(a1*a2 == -1):
        return "prostopadle"
print(prostopadle_funkcji(-1,1))
#ZADANIE 6 ==========================
import math
def rownanie_okregu(a,x,y,b):
    return math.sqrt((x-a)**2)+((y-b)**2)
print("okrag =", rownanie_okregu(2,3,2,5))


#ZADANIE 8==================
import math
def suma_ciagu(a1=1,r=1,ile=10):
    return print("suma = ",(a1+(ile-1)/2)*ile)
print(suma_ciagu())

#ADANIE 9=======================
def ciag(*liczby):
    if len(liczby)==0:
        return 0.0
    else:
        iloczyn=1
        for i in liczby:
            iloczyn*=i
        return iloczyn
print(ciag(1,2,3,4,5))


def to_lubie(**rzeczy):
    for cos in rzeczy:
        print("to jest ")
        print(cos)
        print("co lubie")
        print(rzeczy[cos])
to_lubie(slodycze="czekolada", rozrywka=["disco-polo","moda na sukces"])



listaZakupow = {'czekolada':5,'chleb':3,'maslo':2}
print(sum(listaZakupow.values()))

suma=0

#ZADANIE 10=================
def listaZakupow(** nazwa):
    suma=0
    for ile in nazwa:
      suma+=nazwa[ile]
print(suma)

  
print(listaZakupow(czekolada=10, chleb = 2,paczki =4))





       
      





    




