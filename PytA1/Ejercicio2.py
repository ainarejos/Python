a= int(input("Introduduze un valor: "))
b= int(input("Introduze un segundo valor: "))
print("-------------------------------")
print("Opciones")
print("-------------------------------")
print("[A]- suma\n[B]- Resta\n[C]- Multiplicación\n[D]- división")
pregunta= input("Introduze la operación que se quiere realizar: ")
if pregunta == "A":
    suma=a+b;
    print(suma)
if pregunta == "B":
    resta=a-b;
    print(resta)
if pregunta == "C":
    mult=a*b;
    print(mult)
if pregunta == "D":
    div=a/b;
    print(div)