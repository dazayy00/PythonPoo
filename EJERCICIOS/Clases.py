class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f'Estas llamando desde un telefono : {self.modelo}')

    def colgar(self):
        print(f'Cortaste la llamada desde un telefono {self.modelo}')

celular1 = Celular("Apple", "Iphone 15", "40MP")
celular2 = Celular("Xiaomi", "Redmi 23", "15MP")

celular1.llamar()
celular2.colgar()
