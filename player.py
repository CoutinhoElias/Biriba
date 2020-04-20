from traco import Traco
import random
import pdb #import pdb for debugging

traco = Traco()

class Player:
    def __init__(self):
        self.cards_in_hands = []
        self.cards_in_hands.extend(self._cards_in_hands())


    def _cards_in_hands(self):
        list_cards_in_hands = []
        # pdb.set_trace() #breakpoint

        for i in range(15):
            self.catchCard(1)          
        return list_cards_in_hands 

        #for g in sorted(self.cards_in_hands, key=lambda k: (k[1], int(k[0]))):
        #    if g[1] == 'C':
        #        print(g[0], ' de COPAS', g)
        #    elif g[1] == 'E': 
        #        print(g[0], ' de ESPADA', g)   
        #    elif g[1] == 'O':
        #        print(g[0], ' de OURO', g)   
        #    elif g[1] == 'P':
        #        print(g[0], ' de PAUS', g)           

    def checkBag(self):
        catch_trash = False

    def catchCard(self, local):
        pos = traco.indice_carta()          
        self.cards_in_hands.append(traco.cartas_do_jogo[pos])
        traco.deletar_carta(pos, local)


    def catchTrash(self):
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
            traco.deletar_carta(pos, local)
        """     
        pos = self.indice_carta(self.cards_in_hands[0])
        print('Na função discard do player ', self.cards_in_hands[pos])
        excluir = self.cards_in_hands[pos]
        
        traco.alimentar_lixo(excluir)
        self.deletar_carta(pos)
        print('O jodador descartou.')

    def indice_carta(self, pos):
            _index = self.cards_in_hands.index(pos)
            return _index         

    def deletar_carta(self, pos):
        """
        Params: 
            pos = Positive integer
        """
        if pos >= 0:
            del(self.cards_in_hands[pos])                 
        print(f'Removido o item da posição {pos}' \
        f'. Agora temos {len(self.cards_in_hands)} cartas.')            


