from Golpes import *
from FPS import *
from Armas import *

if __name__ == "__main__":
    j1 = Jogador()
    j2 = Jogador()
    print(j1)
    print(j2)
    r1 = Revolver()
    j1.armas(j1.armas[0], j2)
    print(j1)
    print(j2)

    j1.bater(j2, arma=j1.armas[0])
    print(j1)
    print(j2)