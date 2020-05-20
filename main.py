import PySimpleGUI as sg
import random
from traco import Traco
from player import Player

import os
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")

naipes = ['C', 'E', 'O', 'P']

all_files = os.listdir(path)

images = []
for file in all_files:
    full_filename = os.path.join(path, file)
    
    if len(file) == 7:
        reverse_file = file[2] + str(file[:2])
        images.append({'file': reverse_file,'file_dir':full_filename})      
    else:
        reverse_file = file[1] + str(file[:1])
        images.append({'file': reverse_file,'file_dir':full_filename})


def img(pos):    
    for i in images:
        if pos == i['file']:
            return i['file_dir']

# sg.ChangeLookAndFeel('GreenTan')

player1 = Player()
player2 = Player()
player3 = Player()
player4 = Player()


# Descarta uma carta da sua mão.
# player1.discard()


# Caso a última carta descartada pelo jogador anterior faça uma sequência
# com algum jogo nas suas mãos, ganhamos o direito de chamar essa função (É opcional)
player1.catchTrash(True)


# ------------------------------------------------------------------------
# Esse código abaixo é usado meramente para ordenar as cartas na mesa
pos = 0
for i in sorted(player1.games_in_table, key=lambda k: (k[1], k[0])):
    old_pos = player1.games_in_table.index(i)
    player1.games_in_table.insert(pos,sorted(i, key=lambda k: (k[1], k[0])))
    pos += 1
    old_pos += 1
    if pos >= 0:
        del(player1.games_in_table[old_pos])

# ------------------------------------------------------------------------

# sorted(games_in_table[i], key=lambda k: (k[1], int(k[0])))

def choose_cards():
    player1.choose_cards.append(event)

baixar = []
def down_game(local):
    for i in player1.cards_in_hands[:]:
        if i in baixar:   
            player1.games_in_table.append(i)
            pos = player1.indice_carta(i)
            player1.deletar_carta(pos)


# Deve ser chamada no clique da carta
def vira_par(carta):
    anterior = []
    posterior = []
    entre = []


    if event[0] == 'cards_in_hands':
        baixar.append(event[1])    
        # print(f'O conteudo de baixar é {baixar}')

        card_anterior = carta[1][0]-2, carta[1][1]
        anterior.append(card_anterior)
        card_anterior = carta[1][0]-1, carta[1][1]
        anterior.append(card_anterior)

        card_entre = carta[1][0]-1, carta[1][1]
        entre.append(card_entre)
        card_entre = carta[1][0]+1, carta[1][1]
        entre.append(card_entre)

        card_posterior = carta[1][0]+1, carta[1][1]
        posterior.append(card_posterior)
        card_posterior = carta[1][0]+2, carta[1][1]
        posterior.append(card_posterior)

    #Representação das lists comprehensions abaixo
    #for x in anterior:
    #    if x in baixar:
    #        print(x)


    #print(f'O conteudo de anteior é {anterior}')
    if len([x for x in anterior if x in baixar]) >= 2:
        print(f'Deu certo! {event[1]} Formou jogo com: ', [x for x in anterior if x in baixar])
        window.Element('Baixar jogo').Update(visible=True)
        window.FindElement('Baixar jogo').Update(button_color=('black', 'yellow'))
        window.Element('_JOGOS NA MESA_').Update(visible=True)


    #print(f'O conteudo de entre é {entre}')
    if len([x for x in entre if x in baixar]) >= 2:
        print(f'Deu certo! {event[1]} Formou jogo com: ', [x for x in entre if x in baixar])
        window.Element('Baixar jogo').Update(visible=True)
        window.FindElement('Baixar jogo').Update(button_color=('black', 'yellow'))
        window.Element('_JOGOS NA MESA_').Update(visible=True)


    #print(f'O conteudo de posterior é {posterior}')
    if len([x for x in posterior if x in baixar]) >= 2:
        print(f'Deu certo! {event[1]} Formou jogo com: :', [x for x in posterior if x in baixar])
        window.Element('Baixar jogo').Update(visible=True)
        window.FindElement('Baixar jogo').Update(button_color=('black', 'yellow'))
        window.Element('_JOGOS NA MESA_').Update(visible=True)



def new_lay():
        # Deve verificar se a origem for maior que zero.
        # Verifique os parametros da função
        """
        Params: 
            pos = Positive integer
            local = Positive integer
                0 = cartas_do_jogo ==> Significa que será exluída desse atributo.
                1 = arquivo_morto_a ==> Significa que será exluída desse atributo.
                2 = arquivo_morto_b ==> Significa que será exluída desse atributo.
                3 = lixo ==> Significa que será exluída desse atributo.
        """

        col = []

        col.append([sg.Text('Cartas marcadas', font='Helvetica 10 bold'), sg.Text('', key='_CARTAS MARCADAS_2')])
        col.append([sg.Text(size=(50, 2), font=('Helvetica', 20), justification='center', key='_CARTAS NA MESA_')],)
        col.append([sg.Text('---------------------------------------------------- JOGOS NA MESA ----------------------------------------------------', visible=False, font='Helvetica 10 bold'), sg.Text('', key='_JOGOS NA MESA_')],)
        wid = []
        for i in range(len(sorted(player1.games_in_table))):
            # print(player1.games_in_table[i][1], player1.games_in_table[i][0])
            search =  str(player1.games_in_table[i][1]) + str(player1.games_in_table[i][0])
            wid.append(sg.Button('', button_color=('white', 'green'), image_filename=img(search), image_size=(100, 130), image_subsample=3, key=player1.games_in_table[i], size=(4, 2), pad=(0,0)),)            

        col.append(wid)

        # col += [[sg.Button(games_in_table[i][j], size=(4, 2), key=(i,j), pad=(0,0)) for j in range(len(games_in_table[i]))] for i in range(MAX_ROWS)]

        col.append([sg.Text('---------------------------------------------------- CARTAS NA MÃO ----------------------------------------------------', font='Helvetica 10 bold'), sg.Text('', key='_OUTPUT_')],)        

        for naipe in naipes:
            wid = []
            grupo_naipe = []
            for i in range(len(player1.cards_in_hands)):
                if naipe == player1.cards_in_hands[i][1]:
                    grupo_naipe.append(player1.cards_in_hands[i])
            
            for grupo in sorted(grupo_naipe):
                search = str(grupo[1]) + str(grupo[0])
                wid.append(sg.Button('', image_filename=img(search), image_size=(100, 130), image_subsample=3, key=('cards_in_hands', grupo), size=(4, 2), pad=(0,0)),)                   
            col.append(wid)

        # col.append([sg.Button('', image_filename=img('X15'), image_size=(100, 130), size=(10, 20), key=('add'), pad=(0,0))])
        if len(player1.return_lixo()) > 0:
            search = str(player1.return_lixo()[1]) + str(player1.return_lixo()[0])
        else:    
            search = None


        col2 = [[sg.Text('Funções e placar.', font='Helvetica 10 bold')],      
                [sg.Button('Puxar carta', size=(10, 3), font='Helvetica 10 bold')], 
                [sg.Button('Descartar', size=(10, 3), font='Helvetica 10 bold')], 
                [sg.Button('Baixar jogo', size=(10, 3), visible=False, font='Helvetica 10 bold')],
                [sg.Button('Pegar Morto', size=(10, 3), font='Helvetica 10 bold')],
                [sg.Button('Bater', size=(10, 3), font='Helvetica 10 bold')], 
                [sg.Button('Sair', size=(10, 3), font='Helvetica 10 bold')],
                [sg.Text('Cartas no Lixo', font='Helvetica 10 bold'), sg.Text('', key='_CARTAS NO LIXO_')],
                [sg.Button('', image_filename=img(search), 
                               image_size=(100, 130), 
                               image_subsample=3, 
                               key=player1.return_lixo(), 
                               size=(4, 2), pad=(0,0)),]]
        
        layout = [[
            sg.Column( col2, element_justification='Center' ), 
            sg.Column( col, size=(1100,900), scrollable=True, element_justification='Center' )
        ]]


        return layout

window = sg.Window('Jogando Biriba.', new_lay()).Finalize()
window.Maximize()

show_cards = False

while True:
    event, values = window.read()


    if event in (None, 'Exit'):
        break

   

    if event == 'Puxar carta':
        # Remove uma carta da mão e adiciona no lixo 
        player1.catchCard(0)
        
        window.Close()
        window = sg.Window('Jogando Biriba. Você descartou!', new_lay()).Finalize()

    if event == 'Descartar':
        # Remove uma carta da mão e adiciona no lixo 
        player1.discard()
        
        window.Close()
        window = sg.Window('Jogando Biriba. Você descartou!', new_lay()).Finalize()
    elif event == 'Pegar Morto':
        player1.catchBag(1)

        window.Close()
        window = sg.Window('Jogando Biriba. Você descartou!', new_lay()).Finalize() 


    elif event == 'Baixar jogo':
        down_game(1)
        window.Element('Baixar jogo').Update(visible=False)
        
        if len(player1.games_in_table)<=0:
            print('Sem nenhuma carta')
        else:
            print(f'Possui {len(player1.games_in_table)} cartas')
            show_cards = True        

        window.Close()
        window = sg.Window('Jogando Biriba. Você baixou jogo na mesa', new_lay()).Finalize()


    # Verifico se a lista games_in_table possui cartas, se positivo altero o conteúdo do sg.Text com
    # o event =  _CARTAS NA MESA_
    if show_cards:
        window['_CARTAS NA MESA_'].update(f'Ahhhhh baitola que tem  {len(player1.games_in_table)} cartas na mesa!') 


    elif event[0] == 1:
        try:
            card = int(event[0])
            choose_cards()
        except ValueError:
            print("Não é número")


    if event[0] == 'cards_in_hands':
        window.FindElement('Baixar jogo').Update(button_color=('black', 'yellow'))
        vira_par(event)


    elif event == 'Sair':
        window.Close()       

    # window[(row, col)].update('New text')   # To change a button's text, use this pattern
    # For this example, change the text of the button to the board's value and turn color black
    # window[event].update(board[event[0]][event[1]], button_color=('white','black'))
window.close()
