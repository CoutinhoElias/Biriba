import random
from traco import Traco
from player import Player

# print('O baralho inicializou com 104 cartas')
# print('Distribuiu 60 cartas entre os jogadores')
# print('Distribuiu 30 cartas entre os arquivos mortos')
# print('Restam 14 cartas para iniciar o jogo')

def main():
    # CRIA A MÃO DE BARALHO PARA CADA JOGADOR
    player1 = Player()
    player2 = Player()
    player3 = Player()
    player4 = Player()


    # PEGA UMA CARTA PARA JOGAR
    # player1.catchCard(0)

    # Descarta uma carta da sua mão.
    player1.discard()

    # Exclui as cartas da mão para simular a função player1.catchBag(1)
    for c in range(len(player1.cards_in_hands)):

        player1.deletar_carta(0)
        print('Agora temos ', len(player1.cards_in_hands))
        if len(player1.cards_in_hands) > 0:
            print('Excluido: ', player1.cards_in_hands[0])

    # Pega as cartas do arquivomorto a ou b.
    player1.catchBag(1)

    # Caso a última carta descartada pelo jogador anterior faça uma sequência
    # com algum jogo nas suas mãos, ganhamos o direito de chamar essa função (É opcional)
    player1.catchTrash(True)

    # print('Descartado: ',player1.cards_in_hands[0])
    # player1.discard()
    # print('Lixo: ',traco.lixo)
    # pos = player1.indice_carta(player1.cards_in_hands[6])
 
main()            

