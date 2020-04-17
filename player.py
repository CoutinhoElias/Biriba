"""

    Conhecido em alguns lugares como Biriba e emoutros como Buraco esse jogo émuito divertido.
    Pode ser jogado no mínimo com 2 jogadores e no máximo com 4.
    A maioria prefere jogocom 4 jogadores formando 2 times.

    Regras: 
    1 - Ganha se um jogador(Quando o jogo é individual) ou o time(Quando 4 jogadores formam dois times)
    somam mais pontos que os outros.
    2 - As cartas representam números de 1 a 13.
    2.1 Temos nesta sequencia letras representando números conforme abaixo:
        a) A letra "A" pode representar o número 1 e o número 14.
        b) A letra "J" chamada de "Valete" representa onúmero 11.
        c) A letra "Q" chamada de "Dama" ou "Rainha" representa o número 12. 
        d) A letra "K" chamada de "Rei" ou "Reis" representa o número 13.

    2.2 O número 2 pode servir como uma carta "coringa" desde que seja do mesmo nipe (Veja 2.3 abaixo).
        Chamamos o 2 de "Melé" quando ele está fora de sua posição original entre o 1 e o 3.
        A única carta que pode se repetir numa sequencia é o número 1 representado pela letra A.
        Portanto o número 2 (Melé) pode substituir uma carta faltantena sequencia masnão se repete,
        Caso a carta que o 2 apareça nas mãos do jogador ele subistitui o melé por esta carta e 
        realoca o melé para frente ou para traz.
        Exemplo:
        Temos as sequencias dispostas na mesa: 3, 4, 5, 2, 7 e puxamos a carta 6 no baralho
        Neste caso podemos colocar o 6 na posição correta e o 2 pode voltar para a sua 
        posição original ou pode servir de 8 e me permitir baixar mais cartas.


    2.3 Nipe é o nome do tipo de cartaque temos nas mãos, temos 4 tipos:
        Copas = CORAÇÃO VERMELHO.
        Espada = PRETO(Levemente semelhante a um coração rsrsrsrs).
        Ouro = LOSANGO VERMELHO.
        Paus = UMA ARVORE PRETA.

    3 - No fim de cada partida é feito a contabilidade:    
        a) Uma sequencia maior que 7 cartas e menor que 13 temos 200 pontos.
           Exemplos:
               Isso são 200 pontos: 1, 2, 3, 4, 5, 6, 7
               Isso são 200 pontos: 1, 2, 3, 4, 5, 6, 7, ..., 12
               Isso são 200 pontos: 6, 7, ..., 12
               Isso são 200 pontos: 2, 3, 4, 5, 6, 7, 8
        b) Uma sequencia de 7 cartas e um 2 fora de sua posição temos 100 pontos.
           Exemplos:
               Isso são 100 pontos: 3, 4, 2, 6, 7, 8, 9
               Isso são 100 pontos: 4, 5, 6, 7, ...,10, 2, 12       
        c) Uma sequencia de 13 cartas temos 500 pontos.
           Exemplo:
               Isso são 500 pontos: 1, 2, 3, 4, 5, 6, 7,...,13
     
        d) Uma sequencia de 13 cartas + número 1 temos 1000 pontos.
           Exemplo:
               Isso são 1000 pontos: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1
      
        soma-se os pontos feitos na mesa

    4 - Iniciando a partida:
            Definições:
                cards_in_hand = Cartas na mão.
                cards_in_trash = Lista de cartas que foram descartadas pelos jogadores.
                cards_dead = Lista com 30 cartas aleatórias que só deve ser retirada 15 por vez.
                    a) Podem ser retiradas 15 para mão de um usuário caso ele zere suas cartas da mão
                    contida em cards_in_hand.
                    b) Podem ser retirada 15 para a lista cards_in_table caso ela zere também.
****            cards_sequence_in_table = Lista de jogos baixados, essa definição tenho queperguntar meus 
                amigos de programação. Serão "n" sequências.   

                cards_in_table = Lista de cartas desconhecidas por todos os jogadores, essa lista é o
                resultado do baralho após a distribuição de cartas para as listas cards_in_hand e cards_dead

        Primeiro jogador em ação:
            A) Um jogador puxa uma carta do baralho que está na lista cards_in_table.
                Ações: 
                    Remove uma carta de cards_in_table e adiciona em cards_in_hand do jogador corrente.
                    O jogador escolhe umacarta de cards_in_hand para descartar, quando ele escolher 
                    removemos uma carta de cards_in_hand e adicionamos em cards_in_trash.
                    Quando isso ocorre é a vez do próximo jogador.

        Partindo do segundo jogador em ação:
            A) O jogador seguinte consulta essa carta em cards_in_trash jogada fora pelo jogador anterior.
            B) Verifica se essa carda em cards_in_trash faz sequência de 3 com as que ele possui.
                    Caso Verdadeiro: Deve ser consultado se o jogador deseja pegar as cartas de cards_in_trash.
                        Caso Verdadeiro: 
                            a) Deve ser jogado essa sequência em cards_sequence_in_table.
                            b) Ganha o direito de baixar cartas de cards_in_hand para cards_sequence_in_table
                               desde que formem sequencia de 3 cartas ou formem sequênciascom asquejá estão lá.
                        Caso falso:
                            a) Segue a partida usando as regras do primeiro jogador em ação.
                    Caso Falso: Segue a partida usando as regras do primeiro jogador em ação.           

            B) Um jogador puxa uma carta do baralho que está na lista cards_in_table.
                Ações: 
                    Remove uma carta de cards_in_table e adiciona em cards_in_hand do jogador corrente.
                    O jogador escolhe umacarta de cards_in_hand para descartar, quando ele escolher 
                    removemos uma carta de cards_in_hand e adicionamos em cards_in_trash.                    
                
                , essa lista é sempre
            alimentada pela lista cards_dead caso seja removida a última carta de 

"""
from traco import Traco
import random

class Player:

    def cards_in_hands(self):
        traco = Traco()
        # traco.deletar_carta(6)
        # lista_carta = traco._criar_baralho()
        # print(lista_carta)

        list_cards_in_hands = []

        for i in range(15):
            carta = random.choice(traco._criar_baralho())
            pos = traco._criar_baralho().index(carta)
            list_cards_in_hands.append(carta)
            traco.deletar_carta(pos)  

        print(f'Para esse jogador temos {len(list_cards_in_hands)} cartas.')     

    def checkBag(self):
        catch_trash = False

    def catchCard(self, card):
        """
            Quando um jogador pega a carta do baralho na mesa deve seguir estas lógicas: 

            1 - Organizar as cartas na mão. "self.sortCards()"
            2 - Verificar se pode contribuir com o jogo baixado na mesa.
            2.1 Caso verdade ele decide se deve ou não baixar essas cartas:
            2.1.1 SIM, ele escolhe que cartas devem ser baixadas. "FUNÇÃO NÃO MONTADA"
            2.1.2 NÃO, ele chama a função de descarte. "self.destarte()"
            3 - Verificar se deseja baixar jogo montadona mão
            3.1 Caso verdade ele decide se deve ou não baixar esse jogo:
            3.1.1 SIM, ele escolhe que cartas devem ser baixadas. "FUNÇÃO NÃO MONTADA"
            3.1.2 NÃO, ele chama a função de descarte. "self.destarte()"
        """
        print(f'O jogador pegou a carta "{card}" do baralho')
        self.sortCards()

    def catchTrash(self):
        """
            Esta função se for executada deve remover todas as cartas da lista "cards_in_trash" 
            e adicionar em "cards_in_hand" do jogador da jogada atual.
        """
        print('O jogador pegou o BAG')
        self.sortCards()

    def sortCards(self):
        """
            Quando o jogador ordenar as cartas ele escolhe uma das que possui em mãos para descartar,
            assim o próximo jogador pode usar ou não a função catchTrash().
        """
        print('O jogador ordenou suas cartas.')
        self.chooseDiscard()

    def chooseDiscard(self):
        """
            O descarte remove uma carta da lista "cards_in_hand" e adiciona esta carta 
            na lista cards_in_trash, esta por sua vez pode ser capturada pelo próximo jogador usando
            a função catchTrash().
            Isso me obriga a criar uma função para o jogador robô escolher a melhor carta 
            para o próximo jogador não conseguir pegar.     
        """
        print('O jogador escolheu a carta do descarte')
        self.discard()

    def discard(self):
        """
            Essa função remove uma carta da lista "cards_in_hand" e adiciona esta carta 
            na lista cards_in_trash.        
        """
        """
            Quando o jogador descartar não pode chamar a função chooseDiscard, 
            isso causa um Loop infinito.
        """        
        print('O jodador descartou.')


