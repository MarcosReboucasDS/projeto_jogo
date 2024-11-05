from abc import *
from Golpes import Soco
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

class Disparavel(metaclass= ABCMeta):
    @abstractmethod
    def disparar(self):
        pass

    @abstractmethod
    def recarregar(self):
        pass

class Revolver(Arma, Disparavel):
    cartuchos: int

    def __init__(self):
        super().__init__(20)
        self.cartucho = 6

    def disparar(self, j: Jogador):
        if self.cartucho > 0:
            self.cartucho -= 1
            j.energia -= self.destruicao
    
    def recarregar(self):
        self.cartucho = 6

class Soco_Ingles(Soco, Faca):
    def golpear(self, j):
        super().agredir()
        super().golpear()


class Lanca_chamas(Arma, Disparavel):
    gas: float

    def __init__(self):
        super().__init__(30)
        self.gas = 100

    def disparar(self, j: Jogador):
        if self.gas > 0:
            self.gas -= 5.5
            j.energia -= self.destruicao
    
    def recarregar(self):
        self.gas = 100
    
