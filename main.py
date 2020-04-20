import random
from traco import Traco
from player import Player

traco = Traco()

def main():
    # CRIA A MÃO DE BARALHO
    player1 = Player()
    player2 = Player()
    player3 = Player()
    player4 = Player()

    #print('O baralho inicializou com 104 cartas')
    #print('Distribuiu 60 cartas entre os jogadores')
    #print('Distribuiu 30 cartas entre os arquivos mortos')
    #print('Restam 14 cartas para iniciar o jogo')

    # PEGA UMA CARTA PARA JOGAR
    player1.catchCard(1)

    print('Descartado: ',player1.cards_in_hands[0])
    player1.discard()
    print('Lixo: ',traco.lixo)
 
main()            

