# plik liczbyZespolone.py
import cmath
x=3
y=5
z= complex(x,y);
def czesc_Real():
    print("3+5j: ")
    print("Część rzeczywista liczby zespolonej: ",(z.real))
czesc_Real() 

def czesc_Imag():
    print("Część urojona liczby zespolonej: ",(z.imag)) 
czesc_Imag()



