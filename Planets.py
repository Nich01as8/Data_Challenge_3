#Definimos la clase de planeta
class planet:
    
    def __init__(self, host_star, masa, radio, semi_eje_mayor, inclinacion_orbital, excentricidad, argumento_periastron):
        self.host_star = host_star
        self.masa = masa
        self.radio = radio
        self.semi_eje_mayor = semi_eje_mayor
        self.inclinacion_orbital = inclinacion_orbital
        self.excentricidad = excentricidad
        self.argumento_periastron = argumento_periastron
        
    def keplerian_rotation(self): #Periodo de rotacion kepleriana
        return 2 * np.pi * np.sqrt(self.semi_eje_mayor**3 / (cte.G * self.host_star.masa))
    
    def orbital_period(self):
        return self.keplerian_rotation() * (1 - self.excentricidad**2) / (2 * np.pi)