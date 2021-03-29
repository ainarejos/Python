class Gos:
    def __init__(self, energia, hambre, estado):
        self.energia=energia
        self.hambre=hambre
        self.estado=estado

    def menjar(self, cantidad):
        if (self.estado=="famolenc"):
            for x in range(cantidad):
                if self.hambre>0:
                    self.hambre=self.hambre-1
            print("El perro ha comido, su nivel de hambre es: " + str(self.hambre))
        else:
            print("El perro no tiene hambre, su nivel de hambre es: " + str(self.hambre))

    def acariciar(self):
        self.estado="contento"
        print("Perro acariciado")
        print("Estado del perro: " + self.estado)

    def jugar(self):
        if (self.energia<=2) | (self.hambre>=2) | (self.estado=="famolenc"):
            print("El perro no queire jugar")
        elif self.estado=="contento":
            self.energia-=1
            self.hambre+=1
            self.estado = "famolenc"
            print("El perro ha jugado, su hambre esta en: " + str(self.hambre) + " y su energia se ha quedado en: " + str(self.energia))

    def dormir(self, horas):
        if self.energia<=2:
            self.energia+=horas;
            self.estado="famolenc"
            print("El perro a domido: " + str(horas) + " horas, y su estado actual es: " + self.estado)
        else:
            print("El perro no puede dormir")



