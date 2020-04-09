#ZADANIE 1================
plik = open("zad2.py","r")
wiersze = plik.readlines()
#ZADANIE 2================
with open("zad2.py","r") as plik:
    for linia in plik:
        print(linia,end="")

print("\n")

plik.close()

print(wiersze)
print("\n")
#ZADANIE 3============================
with open("dozad3.py","r+") as plik:
    for linia in plik:
        print(linia,end="")

print("\n")


#ZADANIE 4=======================================================
class NaZakupy():
    nazwa_produktu = "bułka" 
    ilosc = 4
    jednostka_miary = "gram" 
    cena_jed = 1
    def __init__ (self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed


wyswietl_produkt = NaZakupy('chleb', "1", " bochenek" , 3)
ile_produktu = NaZakupy('chleb', "1", " bochenek" , 3)
ile_kosztuje = NaZakupy('ziemniak', 3, " kg" , 2)


print(wyswietl_produkt.nazwa_produktu)

print(ile_produktu.ilosc + ile_produktu.jednostka_miary)

print(ile_kosztuje.ilosc * ile_kosztuje.cena_jed)



    






        
         
        
