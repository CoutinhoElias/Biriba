import random
from traco import Traco
from player import Player

def main():
    # Cria otraço de baralho
    traco = Traco()
    traco.deletar_carta(6)

    # Cria a mão de baralho
    player1 = Player()
    player1.cards_in_hands()

    player2 = Player()
    player2.cards_in_hands()

    player3 = Player()
    player3.cards_in_hands()

    player4 = Player()
    player4.cards_in_hands()

    print('************* ',len(traco._criar_baralho()))
    


    #    print(F'Cartas de Gamer{j} ------------------------------------------' )
    #    for g in sorted(jogador, key=lambda k: (k[1], int(k[0]))):
    #        if g[1] == 'C':
    #            print(g[0], ' de COPAS', g)
    #        elif g[1] == 'E': 
    #            print(g[0], ' de ESPADA', g)   
    #        elif g[1] == 'O':
    #            print(g[0], ' de OURO', g)   
    #        elif g[1] == 'P':
    #            print(g[0], ' de PAUS', g)            
            

main()            

