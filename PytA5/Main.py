from PytA5.Sobre import Sobre
from PytA5.Carta import Carta
c1 = Carta("Hechicero", "Mago", "super rara", 5, 4, 2, "Cura a los compañeros cercanos")
c2 = Carta("Guardian", "Tanque", "rara", 6, 8, 10, "Crea un campo en el que los aliados reciben escudos")
s1 = Sobre("El sobre tenebroso", "Es un sobre que es tenebroso", 5)
s1.añadirCarta(c1)
s1.añadirCarta(c2)
s1.VeureCartesSobre()

