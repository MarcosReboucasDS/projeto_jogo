from Armas import Disparavel, Arma
from Golpes import Golpe
from typing import List

class Jogador:
    energia: float
    armas: List[Arma]

    def __init__(self):
        self.energia = 150
        self.armas: List[Arma] = []
    
    def __str__(self):
        return f'Energy: {self.energia: 2f}%'
    
    def atirar(self, d: Disparavel, j):
        d.disparar(j)
    
    def municiar(self, d: Disparavel):
        d.recarregar()

    def bater(self, j, golpe: Golpe = None, arma: Golpe = None):
        if golpe != None and arma == None:
            golpe.golpear(j)
        
        elif golpe == None and arma != None:
            arma.agredir(j)


    
    