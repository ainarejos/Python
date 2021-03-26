
bus=int(4000)
alumnos=int(input("Introuduce el numero de alumnos: "))
if alumnos >= 100:
    coste=int(alumnos*65)
    total=int(coste+bus)
    print(total)
elif alumnos >=50:
    coste=int(alumnos*70)
    total=int(coste+bus)
    print(total)
elif alumnos >=30:
    coste=int(alumnos*95)
    total=int(coste+bus)
    print(total)
elif alumnos > 0:
    coste = int(alumnos * 115)
    total = int(coste + bus)
    print(total)