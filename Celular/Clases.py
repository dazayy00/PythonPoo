class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

celular1 = Celular("Apple", "Iphone 15", "40MP")
celular2 = Celular("Xiaomi", "Redmi 23", "15MP")

print(celular1.marca)
print(celular2.marca)
