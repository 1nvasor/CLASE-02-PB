from personaje import Personaje

class Mago(Personaje):

    def __init__(self, nombre, vida, nivel, mana, ap):
        super().__init__(nombre, vida, nivel)
        self.mana = mana
        self.ap = ap

    def atacar(self):
        print(f"{self.nombre} lanza un ataque magico")