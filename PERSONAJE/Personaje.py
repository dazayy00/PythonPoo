class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("Fuerza : ", self.fuerza)
        print("Inteligencia", self.inteligencia)
        print("Defensa : ", self.defensa)
        print("Vida : ", self.vida)

    def subirniv(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa +defensa

    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, " Ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "Ha realizado", daño, "puntos de daño a ", enemigo.nombre)
        if enemigo.esta_vivo():
            print("la vida de ", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

    def get_fuerza(self):
        return self.fuerza
    
    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("Error, has introducido un numero negativo")
        else:
            self.fuerza = fuerza

#mi_personaje = Personaje("Dazayy", 80, 70, 80, 70)
#mi_enemigo = Personaje("Downzayy", 70, 45, 20, 100)
#mi_personaje.atributos()
#mi_personaje.subirniv(2, 4, 3)
#mi_personaje.set_fuerza(5)
#mi_personaje.atributos()
#print(mi_personaje.estar_vivo())
#mi_personaje.morir()
#print(mi_personaje.daño(mi_enemigo))
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.atributos()
#print(mi_personaje.get_fuerza())

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elije un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10 "))
        if opcion == 1:
            self.espada = 1
        elif opcion == 2:
            self.espada = 1
        else:
            print("Numero de arma incorrecto")

    def atributos(self):
        super().atributos()
        print("Espada: ", self.espada)

    def daño(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa

#guts = Guerrero("guts", 90, 60, 90, 65, 5)
#print(guts.estar_vivo())
#guts.cambiar_arma()
#guts.atributos()
#print(guts.espada)

class Mago(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("Libro: ", self.libro)

    def daño(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
    
#goku = Personaje("Dazayy", 20, 15, 10, 100)
#guts = Guerrero("Guts", 20, 15, 10, 100, 5)
#vanessa = Mago("Vanessa", 20, 15, 10, 100, 5)

#goku.atacar(guts)
#guts.atacar(vanessa)
#vanessa.atacar(goku)

#goku.atributos()
#guts.atributos()
#vanessa.atributos()

personaje_1 = Guerrero("Guts", 40, 12, 89, 80, 5)
personaje_2 = Mago("Vanessa", 55, 20, 78, 80, 5)

def combate(jugador_1, jugador_2):
    turno = 0 
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTURNO", turno)
        print("\n Accion de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        print("\n Accion de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")

combate(personaje_1, personaje_2)