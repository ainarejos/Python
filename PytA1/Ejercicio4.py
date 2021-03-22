from random import randint
x = randint(0,10)
a= int(input("Introduce un numero entre el 0 y el 10: "))
if x == a:
    print("Has acertado!!!!")
else:
    print("No has adivinado el numero, el numero era: " + str(x))