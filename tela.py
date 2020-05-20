#!/usr/bin/env python
import PySimpleGUI as sg
import random
import string

"""
    Basic use of the Table Element
"""
##-----WINDOW AND LAYOUT---------------------------------##
naipes = ['C', 'E', 'O', 'P']
games_in_table = []
cards_in_hands = [(3, 'O'), (3, 'C'), (1, 'P'), (8, 'E'), 
                  (10, 'E'), (2, 'C'), (6, 'C'), (13, 'C'), 
                  (4, 'P'), (9, 'P'), (7, 'P'), (13, 'E'), 
                  (10, 'P'), (9, 'C'), (3, 'E')]

for j in naipes:
    games_in_table.append([cards_in_hands[i] for i in range(len(cards_in_hands)) if cards_in_hands[i][1] == j])


# *[[sg.Button(games_in_table[0][i]) for i in range(len(games_in_table))]], 
for i in range(len(games_in_table)):
    for j in range(len(games_in_table[i])):
        bt = sg.Button(games_in_table[i][j])
        print(games_in_table[i][j])



print('----', bt)

layout = [
           *[[sg.Button(games_in_table[i][j]) for i in range(len(games_in_table)) for j in range(len(games_in_table[i]))]],
        
            [sg.Text('-------- O For dentro de couchetes [] e SEM VIRGULA CRESCE PARA LADO -------------------'), sg.Text('', key='_OUTPUT_')],
           *[[sg.Button(games_in_table[3][k]) for k in range(len(games_in_table))]],
            [sg.Text('-------- O For fora do couchetes [] e COM VIRGULA CRESCE PARA BAIXO -------------------'), sg.Text('', key='_OUTPUT_')],
           *[[sg.Button(games_in_table[3][i]),] for i in range(len(games_in_table))],
            [sg.Text('---------------------------------------'), sg.Text('', key='_OUTPUT_')],           
           *[[sg.Button(games_in_table[3][i]),] for i in range(len(games_in_table))],
            [sg.Text('------------------TESTE RÁPIDO---------------------'), sg.Text('', key='_OUTPUT_')],           
  
            [sg.Text('---------------------------------------------------- CARTAS NA MÃO ----------------------------------------------------'), sg.Text('', key='_OUTPUT_')],
            [sg.Button(cards_in_hands[i]) for i in range(len(cards_in_hands)) if cards_in_hands[i][1] == 'C'],
            [sg.Button(cards_in_hands[i]) for i in range(len(cards_in_hands)) if cards_in_hands[i][1] == 'E'],
            [sg.Button(cards_in_hands[i]) for i in range(len(cards_in_hands)) if cards_in_hands[i][1] == 'O'],
            [sg.Button(cards_in_hands[i]) for i in range(len(cards_in_hands)) if cards_in_hands[i][1] == 'P'],
            
         ]
         

    
"""[sg.Frame(
                layout=[
                    [sg.Checkbox('Checkbox', size=(10,1)),  sg.Checkbox('My second checkbox!', default=True)],      
                    [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10,1)), sg.Radio('My second Radio!', "RADIO1")]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')]"""

# ------ Create Window ------
window = sg.Window('Biriba', layout,size=(1165,600))

#-----MAIN EVENT LOOP------------------------------------##
while True:
    event, values = window.read()
    print(event)
    if event is None:
        break
    if event in ['0','1','2','3','4','5','6','7','8','9']:
        pass
    if event in ['Escape:27','C','CE']: # 'Escape:27 for keyboard control
        pass
    if event in ['+','-','*','/']:
        pass
    if event == '=':
        pass
    if event == '.':
        pass
    if event == '%':
        pass