class mamiferos ():
    def __init__ (self,fur_color,number_eyes,has_tail,age,especie):
        self.fur_color = fur_color
        self.number_eyes = number_eyes
        self.has_tail = has_tail
        self.age = age
        self.especie = especie
    def print_atributes(self):
        print("Color de Piel ",self.number_eyes)
        print("Numero de Ojos ", self.number_eyes)
        print("Tiene cola? ", self.has_tail)
        print("Edad ", self.age)
        print("Especie ", self.especie)
        
        
if __name__ == "__main__":
    mamifero_generico = mamiferos("Marron",4,True,15,"Leon")
    mamifero_generico.print_atributes()
            