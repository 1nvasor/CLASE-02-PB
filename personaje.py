class Personaje:

    def __init__(self, nombre, vida, nivel):
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel

    def atacar(self):
        print(f"{self.nombre} realiza un ataque")

    def recibir_damage(self, damage):
        self.vida -= damage

        if self.vida < 0:
            self.vida = 0

        print(f"{self.nombre} recibio {damage} de daño")
        print(f"vida actual: {self.vida}")

    def mostar_infor (self):
        print(f"Nombre: {self.nombre}")
        print(f"Vida: {self.vida}")
        print(f"Nivel: {self.nivel}")
# clase Personaje