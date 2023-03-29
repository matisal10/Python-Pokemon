import time
import numpy as np
import sys

def imprimir(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class pokemon:
    def __init__(self, nombre, tipos, movimientos, EVs, puntos_de_salud='================'):
        self.nombre = nombre
        self.tipos = tipos
        self.movimientos = movimientos
        self.ataque = EVs['ataque']
        self.defensa = EVs['defensa']
        self.puntos_de_salud = puntos_de_salud
        self.barras = 20

    def impresa(self, Pokemon2):
        print('---BATALLA DE POKEMON---')
        print(f"\n{self.nombre}")
        print("tipo:", self.tipos)
        print("ataque:", self.ataque)
        print("defensa:", self.defensa)
        print("Nv.:", 3*(1+np.mean([self.ataque,self.defensa])))
        print("\nVS")
        print(f"\n{Pokemon2.nombre}")
        print("tipo:", Pokemon2.tipos)
        print("ataque:", Pokemon2.ataque)
        print("defensa:", Pokemon2.defensa)
        print("Nv.:", 3 * (1 + np.mean([Pokemon2.ataque, Pokemon2.defensa])))
        print("\nVS")
        time.sleep(2)

    def lucha(self,Pokemon2):
        version = ['fuego', 'agua', 'planta']
        for i, k in enumerate(version):
            if self.tipos == k:
                if Pokemon2.tipos == k:
                    cadena1Ataque = '\nNo es muy efectivo...'
                    cadena2Ataque = '\nNo es muy efectivo...'

                if Pokemon2.tipos == version[(i+1)%3]:
                    Pokemon2.ataque *= 2
                    Pokemon2.defensa *= 2
                    self.ataque /= 2
                    self.defensa /= 2
                    cadena1Ataque = '\nNo es muy efectivo...'
                    cadena2Ataque = '\nEs muy Eficaz!'

                if Pokemon2.tipos == version[(i+2)%3]:
                    self.ataque *= 2
                    self.defensa *= 2
                    Pokemon2.ataque /= 2
                    Pokemon2.defensa /= 2
                    cadena1Ataque = '\nEs muy Eficaz!'
                    cadena2Ataque = '\nNo es muy efectivo...'

        while (self.barras > 0) and (Pokemon2.barras > 0):
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
            print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}")

            print(f"adelante {self.nombre}")
            for i, x in enumerate(self.movimientos):
                print(f"{i+1}.",x)
            index = int(input("elige un movimiento: "))
            imprimir(f'\n{self.nombre} uso {self.movimientos[index-1]}!')
            time.sleep(1)
            imprimir(cadena1Ataque)
            Pokemon2.barras -= self.ataque
            Pokemon2.puntos_de_salud = ""

            for j in range (int(Pokemon2.barras +.1*Pokemon2.defensa)):
                Pokemon2.puntos_de_salud += "="

            time.sleep(1)
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
            print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}")
            time.sleep(5)

            if Pokemon2.barras <=0:
                imprimir("\n..." + Pokemon2.nombre + " Se debilito.\n")
                break

            print(f"adelante {Pokemon2.nombre}")
            for i, x in enumerate(Pokemon2.movimientos):
                print(f"{i + 1}.", x)
            index = int(input("elige un movimiento: "))
            imprimir(f'\n{Pokemon2.nombre} uso {Pokemon2.movimientos[index - 1]}!')
            time.sleep(1)
            imprimir(cadena2Ataque)

            self.barras -= Pokemon2.ataque
            self.puntos_de_salud = ""

            for j in range(int(self.barras + .1 * self.defensa)):
                self.puntos_de_salud += "="

            time.sleep(1)
            print(f"\n{self.nombre}\t\tPS\t{self.puntos_de_salud}")
            print(f"\n{Pokemon2.nombre}\t\tPS\t{Pokemon2.puntos_de_salud}")
            time.sleep(5)

            if Pokemon2.barras <= 0:
                imprimir("\n..." + self.nombre + " Se debilito.")
                break

        self.impresa(Pokemon2)

        money = np.random.choice(5000)
        imprimir(f"\n el oponente te pago ${money} \n")


if __name__ == '__main__':
    Charizard = pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'],
                        {'ataque': 12, 'defensa': 8})
    Blastoise = pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],
                        {'ataque': 10, 'defensa': 10})
    Venusaur = pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],
                       {'ataque': 8, 'defensa': 12})

    Charmander = pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],
                         {'ataque': 4, 'defensa': 2})
    Squirtle = pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'], {'ATTACK': 3, 'DEFENSE': 3})
    Bulbasaur = pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],
                        {'ataque': 2, 'defensa': 4})

    Charmeleon = pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],
                         {'ataque': 6, 'defensa': 5})
    Wartortle = pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],
                        {'ataque': 5, 'defensa': 5})
    Ivysaur = pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],
                      {'ataque': 4, 'defensa': 6})
    Venusaur.lucha(Blastoise)