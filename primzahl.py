#primzahl
#Funktion: check if given number is prime

def isPrime(n):
# Logik einbauen
    if(n <= 0):
        return False
    for p in range(2,n):
        if(n % p == 0):
            return False

    return True

print("Primzahlen-Checker")
z = input("Bitte Zahl eingeben!")
z = int(z)

if(isPrime(z)):
    print("ist eine Primzahl")
else:
    print("ist keine Primzahl")
