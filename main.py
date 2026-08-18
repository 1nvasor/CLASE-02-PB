from jugador import Jugador
from mago import Mago


#Método principal

def main():

    nuevo_jugador = Jugador(1, "Vicente")

    nuevo_mago = Mago("Veigar", 800, 15, 300,265)

    nuevo_jugador.crear_personajes(nuevo_mago)

    nuevo_mago.atacar()

if __name__ == "__main__":
    main()