class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print("Estudiando...")
     
nombre = input("digame su nombre: ")
edad = input("digame su edad: ")
grado = input("digame su grado: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      Datos del estidiante \n
      nombre: {estudiante.nombre} \n
      edad: {estudiante.edad} \n
      grado: {estudiante.grado} \n

    """)

while True:
    estudiar = input()
    if(estudiar.lower() == "estudiar"):
        estudiante.estudiar()
