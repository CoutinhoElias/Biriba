import PySimpleGUI as sg
import random
from traco import Traco
from player import Player

# sg.ChangeLookAndFeel('GreenTan')

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


# ------------------------------------------------------------------------
# Esse código abaixo é usado meramente para ordenar as cartas na mesa

games_in_table = []
games_in_table.append(sorted([(13, 'O'), (4, 'O'), (5, 'O')]))
games_in_table.append([(12, 'E'), (9, 'E'), (6, 'E'), (5, 'E'), (6, 'E'), (7, 'E')])
games_in_table.append([(12, 'C'), (9, 'C'), (6, 'C')])
games_in_table.append([(12, 'P'), (9, 'P'), (3, 'P'), (6, 'P'), (3, 'P')])

pos = 0
for i in sorted(games_in_table, key=lambda k: (k[1], k[0])):
    old_pos = games_in_table.index(i)
    # print('Old_pos antes ', old_pos)

    games_in_table.insert(pos,sorted(i, key=lambda k: (k[1], k[0])))
    pos += 1
    old_pos += 1
    if pos >= 0:
        del(games_in_table[old_pos])

# ------------------------------------------------------------------------

# sorted(games_in_table[i], key=lambda k: (k[1], int(k[0])))





MAX_ROWS = len(games_in_table)

C1 = '/home/elias/Downloads/Python/Scripts/Biriba/img/1C.png'
C2 = '/home/elias/Downloads/Python/Scripts/Biriba/img/2C.png'
C3 = '/home/elias/Downloads/Python/Scripts/Biriba/img/3C.png'
C4 = '/home/elias/Downloads/Python/Scripts/Biriba/img/4C.png'
C5 = '/home/elias/Downloads/Python/Scripts/Biriba/img/5C.png'
C6 = '/home/elias/Downloads/Python/Scripts/Biriba/img/6C.png'
C7 = '/home/elias/Downloads/Python/Scripts/Biriba/img/7C.png'
C8 = '/home/elias/Downloads/Python/Scripts/Biriba/img/8C.png'
C9 = '/home/elias/Downloads/Python/Scripts/Biriba/img/9C.png'
C10 = '/home/elias/Downloads/Python/Scripts/Biriba/img/10C.png'
C11 = '/home/elias/Downloads/Python/Scripts/Biriba/img/11C.png'
C12 = '/home/elias/Downloads/Python/Scripts/Biriba/img/12C.png'
C13 = '/home/elias/Downloads/Python/Scripts/Biriba/img/13C.png'


E1 = '/home/elias/Downloads/Python/Scripts/Biriba/img/1E.png'
E2 = '/home/elias/Downloads/Python/Scripts/Biriba/img/2E.png'
E3 = '/home/elias/Downloads/Python/Scripts/Biriba/img/3E.png'
E4 = '/home/elias/Downloads/Python/Scripts/Biriba/img/4E.png'
E5 = '/home/elias/Downloads/Python/Scripts/Biriba/img/5E.png'
E6 = '/home/elias/Downloads/Python/Scripts/Biriba/img/6E.png'
E7 = '/home/elias/Downloads/Python/Scripts/Biriba/img/7E.png'
E8 = '/home/elias/Downloads/Python/Scripts/Biriba/img/8E.png'
E9 = '/home/elias/Downloads/Python/Scripts/Biriba/img/9E.png'
E11 = '/home/elias/Downloads/Python/Scripts/Biriba/img/11E.png'
E10 = '/home/elias/Downloads/Python/Scripts/Biriba/img/10E.png'
E12 = '/home/elias/Downloads/Python/Scripts/Biriba/img/12E.png'
E13 = '/home/elias/Downloads/Python/Scripts/Biriba/img/13E.png'


O1 = '/home/elias/Downloads/Python/Scripts/Biriba/img/1O.png'
O2 = '/home/elias/Downloads/Python/Scripts/Biriba/img/2O.png'
O3 = '/home/elias/Downloads/Python/Scripts/Biriba/img/3O.png'
O4 = '/home/elias/Downloads/Python/Scripts/Biriba/img/4O.png'
O5 = '/home/elias/Downloads/Python/Scripts/Biriba/img/5O.png'
O6 = '/home/elias/Downloads/Python/Scripts/Biriba/img/6O.png'
O7 = '/home/elias/Downloads/Python/Scripts/Biriba/img/7O.png'
O8 = '/home/elias/Downloads/Python/Scripts/Biriba/img/8O.png'
O9 = '/home/elias/Downloads/Python/Scripts/Biriba/img/9O.png'
O11 = '/home/elias/Downloads/Python/Scripts/Biriba/img/11O.png'
O10 = '/home/elias/Downloads/Python/Scripts/Biriba/img/10O.png'
O12 = '/home/elias/Downloads/Python/Scripts/Biriba/img/12O.png'
O13 = '/home/elias/Downloads/Python/Scripts/Biriba/img/13O.png'


P1 = '/home/elias/Downloads/Python/Scripts/Biriba/img/1P.png'
P2 = '/home/elias/Downloads/Python/Scripts/Biriba/img/2P.png'
P3 = '/home/elias/Downloads/Python/Scripts/Biriba/img/3P.png'
P4 = '/home/elias/Downloads/Python/Scripts/Biriba/img/4P.png'
P5 = '/home/elias/Downloads/Python/Scripts/Biriba/img/5P.png'
P6 = '/home/elias/Downloads/Python/Scripts/Biriba/img/6P.png'
P7 = '/home/elias/Downloads/Python/Scripts/Biriba/img/7P.png'
P8 = '/home/elias/Downloads/Python/Scripts/Biriba/img/8P.png'
P9 = '/home/elias/Downloads/Python/Scripts/Biriba/img/9P.png'
P11 = '/home/elias/Downloads/Python/Scripts/Biriba/img/11P.png'
P10 = '/home/elias/Downloads/Python/Scripts/Biriba/img/10P.png'
P12 = '/home/elias/Downloads/Python/Scripts/Biriba/img/12P.png'
P13 = '/home/elias/Downloads/Python/Scripts/Biriba/img/13P.png'


layout = [[sg.Text('---------------------------------------------------- CARTAS NO LIXO ----------------------------------------------------'), sg.Text('', key='_OUTPUT_')],]

image_file = f'/home/elias/Downloads/Python/Scripts/Biriba/img/{str(player1.return_lixo()[0]) + str(player1.return_lixo()[1])}.png'

layout += [[sg.Button('', image_filename=image_file, image_size=(25, 40), image_subsample=3, key='Next', size=(4, 2), pad=(0,0)),]]        

layout.append([sg.Text('---------------------------------------------------- JOGOS NA MESA ----------------------------------------------------'), sg.Text('', key='_OUTPUT_')],)        
for i in range(len(sorted(games_in_table))):
    wid = []
    
    for j in range(len(sorted(games_in_table[i], key=lambda k: (k[1], int(k[0]))))):
        image_file = f'/home/elias/Downloads/Python/Scripts/Biriba/img/{str(games_in_table[i][j][0]) + str(games_in_table[i][j][1])}.png'
        # wid.append(sg.Button('', image_filename=image_file, image_size=(25, 40), image_subsample=3, key=(f'({i}, {j})'), size=(4, 2), pad=(0,0)),)
        wid.append(sg.Button(games_in_table[i][j], key=(f'({i}, {j})'), size=(4, 2), pad=(0,0)),)
        # wid.append(sg.Button('', image_filename=image_file, image_size=(25, 40), image_subsample=3, key='Next', size=(4, 2), pad=(0,0)),)
    layout.append(wid)

# layout += [[sg.Button(games_in_table[i][j], size=(4, 2), key=(i,j), pad=(0,0)) for j in range(len(games_in_table[i]))] for i in range(MAX_ROWS)]

"""layout += [
            [sg.Text('---------------------------------------------------- CARTAS NA MÃO ----------------------------------------------------'), sg.Text('', key='_OUTPUT_')],
            [sg.Button(player1.cards_in_hands[i], size=(4, 2), pad=(0,0)) for i in range(len(player1.cards_in_hands)) if player1.cards_in_hands[i][1] == 'C'],
            [sg.Button(player1.cards_in_hands[i], size=(4, 2), pad=(0,0)) for i in range(len(player1.cards_in_hands)) if player1.cards_in_hands[i][1] == 'E'],
            [sg.Button(player1.cards_in_hands[i], size=(4, 2), pad=(0,0)) for i in range(len(player1.cards_in_hands)) if player1.cards_in_hands[i][1] == 'O'],
            [sg.Button(player1.cards_in_hands[i], size=(4, 2), pad=(0,0)) for i in range(len(player1.cards_in_hands)) if player1.cards_in_hands[i][1] == 'P'],
            
            
]"""

layout.append([sg.Text('---------------------------------------------------- CARTAS NA MÃO ----------------------------------------------------'), sg.Text('', key='_OUTPUT_')],)        

wid = []
for i in range(len(player1.cards_in_hands)):
    image_file = f'/home/elias/Downloads/Python/Scripts/Biriba/img/{str(player1.cards_in_hands[i][0]) + str(player1.cards_in_hands[i][1])}.png'
    wid.append(sg.Button('', image_filename=image_file, image_size=(25, 40), image_subsample=3, key=(f'({i}, {j})'), size=(4, 2), pad=(0,0)),)
    # wid.append(sg.Button('', image_filename=image_file, image_size=(25, 40), image_subsample=3, key='Next', size=(4, 2), pad=(0,0)),)

layout.append(wid)



"""
# NÃO EXCLUIR DE FORMA ALGUMA


layout.append([sg.Text('---------------------------------------------------- USANDO O FOR ----------------------------------------------------'), sg.Text('', key='_OUTPUT_')],)        
for i in range(len(games_in_table)):
    wid = []
    for j in range(len(games_in_table[i])):
        image_file = f'/home/elias/Downloads/Python/Scripts/Biriba/img/{str(games_in_table[i][j][0]) + str(games_in_table[i][j][1])}.png'
        wid.append(sg.Button('', image_filename=image_file, image_size=(25, 40), image_subsample=3, key=(f'({i}, {j})'), size=(4, 2), pad=(0,0)),)
        # wid.append(sg.Button('', image_filename=image_file, image_size=(25, 40), image_subsample=3, key='Next', size=(4, 2), pad=(0,0)),)
    layout.append(wid)
"""

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