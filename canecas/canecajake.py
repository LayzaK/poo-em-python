from .classe_caneca import *

class CanecaJake(Caneca):
    def __init__(self):
        super().__init__('Jake', 'Laranja', 'cachorro')

    def extra(self):
        caneca_som = 'Olá eu sou o Jake!'
        print(caneca_som)
