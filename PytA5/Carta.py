class Carta:
    def __init__(self,  nom, tipus, raresa, atac, defensa, vida, passiva):
        self.nom=nom
        self.tipus=tipus
        self.raresa=raresa
        self.atac=atac
        self.defensa=defensa
        self.vida=vida
        self.passiva=passiva

    def getNom(self):
            return self.nom
    def getTipus(self):
            return self.tipus
    def getRaresa(self):
            return self.raresa
    def getAtac(self):
            return self.atac
    def getDefensa(self):
            return self.defensa
    def getVida(self):
            return self.vida
    def getPassiva(self):
            return self.passiva