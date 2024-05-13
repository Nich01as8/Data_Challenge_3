#Definimos la clase de sistema estelar
class multiple_star_system:
    
    def __init__(self, star):
        self.star = star
    
    def mass_sorting(self): #Ordenar las estrellas por masa
        return sorted(self.star, key=lambda x: x.masa)
    
    def star_list(self): #Lista de estrellas con su nombre (en caso de coincidencias, se asigna una letra del alfabeto)
        ''' Con este codigo se asignaran letras del alfabeto para diferenciar las estrellas en caso de que tengan el mismo nombre,
        se considera que el alfabeto tiene 26 letras, por lo que si hay mas de 26 estrellas con el mismo nombre, 
        se asignara la letra'''
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        name_count = {}
        for star in self.star:
            if star.name in name_count:
                name_count[star.name] += 1
            else:
                name_count[star.name] = 1
        
        star_names = []
        for star in self.star:
            if name_count[star.name] > 1:
                star_names.append(star.name + alphabet[name_count[star.name] - 2])
                name_count[star.name] -= 1
            else:
                star_names.append(star.name)
        return star_names