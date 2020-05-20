import PySimpleGUI as sg
import random
from traco import Traco
from player import Player

naipes = ['C', 'E', 'O', 'P']
games_in_table = []

player1 = Player()
player2 = Player()
player3 = Player()
player4 = Player()

# PEGA UMA CARTA PARA JOGAR
# player1.catchCard(0)

# Descarta uma carta da sua mão.
player1.discard()

lixeira = player1.return_lixo()
print('------>',lixeira)

# Exclui as cartas da mão para simular a função player1.catchBag(1)
for c in range(len(player1.cards_in_hands)):

    player1.deletar_carta(0)
"""    print('Agora temos ', len(player1.cards_in_hands))
    if len(player1.cards_in_hands) > 0:
        print('Excluido: ', player1.cards_in_hands[0])"""

# Pega as cartas do arquivomorto a ou b.
player1.catchBag(1)

# Caso a última carta descartada pelo jogador anterior faça uma sequência
# com algum jogo nas suas mãos, ganhamos o direito de chamar essa função (É opcional)
player1.catchTrash(True)

# print('Descartado: ',player1.cards_in_hands[0])
# player1.discard()
# print('Lixo: ',traco.lixo)
# pos = player1.indice_carta(player1.cards_in_hands[6])




for j in naipes:
    games_in_table.append([player2.cards_in_hands[i] for i in range(len(player2.cards_in_hands)) if player2.cards_in_hands[i][1] == j])

games_in_table.append([(3, 'O'), (4, 'O'), (5, 'O')])

MAX_ROWS = len(games_in_table)
# [sg.Button(traco.lixo[i], size=(4, 2), pad=(0,0)) for i in range(len(traco.lixo))],]
layout = [[sg.Text('---------------------------------------------------- CARTAS NO LIXO ----------------------------------------------------'), sg.Text('', key='_OUTPUT_')],
          [sg.Button(player1.return_lixo(), size=(4, 2), pad=(0,0))]]
          

layout += [[sg.Text('---------------------------------------------------- JOGOS NA MESA ----------------------------------------------------'), sg.Text('', key='_OUTPUT_')],]


layout += [[sg.Button(games_in_table[i][j], size=(4, 2), key=(i,j), pad=(0,0)) for j in range(len(games_in_table[i]))] for i in range(MAX_ROWS)]

layout += [
            [sg.Text('---------------------------------------------------- CARTAS NA MÃO ----------------------------------------------------'), sg.Text('', key='_OUTPUT_')],
            [sg.Button(player1.cards_in_hands[i], size=(4, 2), pad=(0,0)) for i in range(len(player1.cards_in_hands)) if player1.cards_in_hands[i][1] == 'C'],
            [sg.Button(player1.cards_in_hands[i], size=(4, 2), pad=(0,0)) for i in range(len(player1.cards_in_hands)) if player1.cards_in_hands[i][1] == 'E'],
            [sg.Button(player1.cards_in_hands[i], size=(4, 2), pad=(0,0)) for i in range(len(player1.cards_in_hands)) if player1.cards_in_hands[i][1] == 'O'],
            [sg.Button(player1.cards_in_hands[i], size=(4, 2), pad=(0,0)) for i in range(len(player1.cards_in_hands)) if player1.cards_in_hands[i][1] == 'P'],
]

'''
layout.append([sg.Text('---------------------------------------------------- CARTAS NO LIXO ----------------------------------------------------'), sg.Text('', key='_OUTPUT_')],)
layout.append([sg.Button(cards_in_hands[i], size=(4, 2), pad=(0,0)) for i in range(len(cards_in_hands)) if cards_in_hands[i][1] == 'C'],)
'''

window = sg.Window('Jogando Biriba.', layout, size=(1165,600))

while True:
    event, values = window.read()
    print(event)
    if event in (None, 'Exit'):
        break
    # window[(row, col)].update('New text')   # To change a button's text, use this pattern
    # For this example, change the text of the button to the board's value and turn color black
    #window[event].update(board[event[0]][event[1]], button_color=('white','black'))
window.close()