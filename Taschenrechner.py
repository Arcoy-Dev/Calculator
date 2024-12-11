from pydoc import replace

import msvcrt
def addieren(x,y): return x+y

def subtrahieren (x,y): return x-y

def multiplizieren (x,y): return x*y

def dividieren(x, y):
    if y != 0:
        return x / y
    else:
        return "Fehler: Division durch 0!"


print("Taschenrechner by Arcoy Version 1.0")
while True:
    try:
        Zahl1=float(input("Zahl1:"))
        Zahl2=float(input("Zahl2:"))
        break
    except ValueError: print("Bitte machen sie eine gültige Eingabe")
x = Zahl1
y = Zahl2
while True:
     print("Wähle einen Operator aus:")
     print("1.Addieren ")
     print("2.Subtrahieren ")
     print("3.Multiplizierem")
     print("4.Dividieren")
     wahl = input("1/2/3/4:")
     if wahl in ["1","2","3","4",]: break

     else: print("ungültige Ausgabe")

if wahl == "1": Ergebnis = addieren(x,y)
elif wahl == "2": Ergebnis = subtrahieren(x,y)
elif wahl == "3":Ergebnis = multiplizieren(x,y)
elif wahl == "4": Ergebnis = dividieren(x, y)
else: Ergebnis= "Ungültige Auswahl bitte wählen sie 1/2/3/4"
print(Ergebnis)

print("Zum beenden beliebige Taste drücken")
msvcrt.getch()