#Definimos la clase de sistema planetario
class planetary_system(planet):
    
    def __init__(self, planet):
        self.planet = planet
    
    def planet_list(self):
        return len(self.planet) 

    def ordered_planets(self):
        return sorted(self.planet, key=lambda x: x.semi_eje_mayor)