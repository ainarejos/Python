from datetime import datetime

class Sobre:
    def __init__(self, nom, descripcio, preu):
        self.identificador=datetime.now()
        self.nom=nom
        self.descripcio=descripcio
        self.preu=preu
        self.cartes=[]

    def añadirCarta(self, carta):
        self.cartes.append(carta)

    def VeureCartesSobre(self):
        print("          (0 0)\n "
              " ---oOO-- (_) ----OOo---\n"
              "╔═════════════════════════╗\n"
              "║    Cartas del Sobre     ║\n"
              "╚═════════════════════════╝")
        print("---------------------------")
        for x in self.cartes:
            print(str(x.getNom()) + ", " + str(x.getTipus()) + ", " + str(x.getRaresa()))
        print("---------------------------")



