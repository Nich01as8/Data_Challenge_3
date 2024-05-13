#Definimos la clase de estrella
class star:
    
    def __init__(self, nombre, masa, radio, temperatura_superficial, distancia, movimiento, movimiento_propio):
        self.nombre = nombre
        self.masa = masa
        self.radio = radio
        self.temperatura_superficial = temperatura_superficial
        self.distancia = distancia
        self.movimiento = movimiento
        self.movimiento_propio = movimiento_propio
    
    def luminosity(self): #Luminosidad de una estrella
        return 4 * np.pi *self.radio**2 * cte.sigma * self.temperatura_superficial**4
    
    def main_sequence_luminosity(self): #Luminosidad de una estrella en la secuencia principal
        return cte.L_sun * (self.masa/cte.M_sun)**3.5
    
    def main_sequence_age(self):
        return 10**10 * (self.masa/cte.M_sun)**(-2.5)