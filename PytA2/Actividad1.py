inicial = int(100)

cantidad= int(input("Cuanta viña quiere el cliente: "))
tipo=input("Tipo A o B: ")
numero=int(input("1 o 2: "))
if (tipo == "A") & (numero == 1):
    total=int(inicial+20)
    resultado=int(total*cantidad)
    print(resultado)
elif (tipo == "A") & (numero == 2):
    total=int(inicial+30)
    resultado=int(total*cantidad)
    print(resultado)
elif (tipo == "B") & (numero == 1):
    total=int(inicial-30)
    resultado=int(total*cantidad)
    print(resultado)
elif (tipo == "B") & (numero == 2):
    total=int(inicial-50)
    resultado=int(total*cantidad)
    print(resultado)


