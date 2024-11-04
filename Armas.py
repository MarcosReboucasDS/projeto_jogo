from abc import ABC
from FPS import Jogador

class Arma(ABC):
    destruicao: float

    #opcional
    def __init__(self, d: float):
        self.destruicao = d
    
    def agredir(self, j: Jogador):
        j.energia -= 5
    
    def __str__(self):
        return f'Destruição: {self.destruicao}'
    
class Faca(Arma):
    lamina: int

    def agredir(self, j: Jogador):
        if self.lamina > 0:
            self.lamina -= 1
            j.energia -= self.destruicao
        else:
            super().agredir(j)