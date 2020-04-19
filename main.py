import random
from traco import Traco
from player import Player

# traco = Traco()

def main():
    # CRIA A MÃO DE BARALHO
    player1 = Player()
    player2 = Player()
    player3 = Player()
    player4 = Player()

    print('O baralho inicializou com 104 cartas')
    print('Distribuiu 60 cartas entre os jogadores')
    print('Distribuiu 30 cartas entre os arquivos mortos')
    print('Restam 14 cartas para iniciar o jogo')

    # PEGA UMA CARTA PARA JOGAR
    player1.catchCard('Puxar a carta para mão', 1)      

"""
    Usar essas mensagens onde bem desejar

    # print(f'Distribuído 15 cartas e restaram {len(traco.cartas_do_jogo)} na mesa')
    # print(f'O arquivo morto 1 possui {len(traco.arquivo_morto_a)} cartas')
    # print(f'O arquivo morto 2 possui {len(traco.arquivo_morto_b)} cartas')    
"""
     
main()            

