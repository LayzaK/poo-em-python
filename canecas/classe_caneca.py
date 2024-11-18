class Caneca:
    def __init__(self, nome, cor, formato):
        self.nome = nome
        self.cor = cor
        self.formato = formato

    def informações_caneca(self):
       print(f'Nome: {self.nome}') 
       print(f'Cor: {self.cor}')
       print(f'Formato: {self.formato}')

    def encher(self):
        caneca_cheia = 'Enchi de café'
        return caneca_cheia
    
    def vazia(self):
        caneca_vazia = 'Tomei tudo'
        return caneca_vazia
    