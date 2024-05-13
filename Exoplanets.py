#Definimos la clase de exoplaneta
class exoplanet(planet):
    
    def __init__(self, host_star, masa, radio, semi_eje_mayor, inclinacion_orbital, excentricidad, argumento_periastron,
                 primer_metodo_descubrimiento, segundo_metodo_descubrimiento, num_stars):
        ''' Se reutilizan los metodos usados en la clase planetas y se agregan los metodos de descubrimiento y
        el numero de estrellas en el sistema'''
        super().__init__(host_star, masa, radio, semi_eje_mayor, inclinacion_orbital, excentricidad, argumento_periastron)
        self.primer_metodo_descubrimiento = primer_metodo_descubrimiento
        self.segundo_metodo_descubrimiento = segundo_metodo_descubrimiento
        self.num_stars = num_stars
    
    def first_method(self):
        impact_parameter = self.semi_eje_mayor * np.cos(self.inclinacion_orbital) * \
            ((1 - self.excentricidad**2) / self.host_star.radio * (1 + self.excentricidad * np.sin(self.argumento_periastron)))
        if impact_parameter < 1 and impact_parameter > 0:
            return "Transito"
        else:
            return self.primer_metodo_descubrimiento, impact_parameter
    
    def tatooine_lookalike(self):
        if self.num_stars >= 2:
            return "Tatooine Lookalike"