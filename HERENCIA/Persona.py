class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Hola cabeza de bola")


class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f'mi habilidad es {self.habilidad}')


class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        print (f'hola, soy {self.nombre}, y trabajo en {self.empresa}')
        self.mostrar_habilidad()

roberto = EmpleadoArtista("roberto", 23, "Mexicano", "Cantar", 10000, "hybe")

roberto.presentarse()