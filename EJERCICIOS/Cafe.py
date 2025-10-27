class Cafe():

    def que_soy(self):
        print("soy un Cafe")

class Te():

    def que_soy(self):
        print("soy un Te")

def definicion_bebida(bebida):
    bebida.que_soy()

definicion_bebida(Cafe())