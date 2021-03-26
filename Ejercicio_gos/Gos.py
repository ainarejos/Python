class Gos:
    def __init__(self, energia, hambre, estado):
        self.energia=energia
        self.hambre=hambre
        self.estado=estado


    def menjar(self, cantidad):
        if self.estado=="famelec":
            self.hambre+=cantidad
            print("El perro ha comido, su nivel de hambre es: " + str(self.hambre))
        else:
            print("El perro no tiene hambre, su nivel de hambre es: " + str(self.hambre))

    def acariciar(self):
        self.estado="contento"
        print(self.estado)

    def jugar(self):
        if self.energia<2 & self.hambre<2:
            print("El perro esta cansado o tiene hambre")
        if self.estado=="contento":
            self.energia-=1
            self.hambre+=1
            print("El perro ha jugado, su hambre esta en: " + self.hambre + " y su energia se ha quedado en: " + self.energia)

    def Dormir(self, horas):
        if self.energia<2:
            self.energia+=horas;
            self.estado="famolenc"



