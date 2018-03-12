#Variable
a = 10
b = 20

aktion = input("Welche Funktion? +/-/*/:")
print("Funktion",aktion,"wird ausgefuehrt")


zahl = input("Zahl 1?")
zahl2 = input("Zahl 2 ?")



zahl = int(zahl)
zahl2 = int(zahl2)

summe = zahl+zahl2
differenz = zahl - zahl2
multiplikation = zahl*zahl2

if(aktion == ":"):
    if(zahl2 == 0):
        print("Division durch 0 nicht moeglich!")
    else:
        division = zahl/zahl
        print("Division von",zahl,":",zahl2,"=", division)

if (aktion == "+"):
    print("Summe von",zahl,"+",zahl2,"=", summe)
if (aktion == "-"):
    print("Differenz von",zahl,"-",zahl2,"=", differenz)
if (aktion == "*"):
    print("Multiplikation von",zahl,"*",zahl2,"=", multiplikation)
