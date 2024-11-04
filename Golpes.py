from FPS import Jogador
from abc import ABC, abstractmethod #que que isso veyr preciso pesquisar

class Golpe(ABC):
    @abstractmethod
    def golpear(self, j: Jogador):
        pass #ele literalmente passa?

class Soco(Golpe):
    def golpear(self, j: Jogador):
       j.energia -= 1

class Chute(Golpe):
    def golpear(self, j: Jogador):
       j.energia -= 2
