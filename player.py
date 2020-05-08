from traco import Traco
import random
# import pdb #import pdb for debugging
# pdb.set_trace() #breakpoint

traco = Traco()

class Player:
    def __init__(self):
        self.cards_in_hands = []
        self.cards_in_hands.extend(self._cards_in_hands())

    # From traco.cartas_do_jogo to player.cards_in_hands
    def _cards_in_hands(self):
        list_cards_in_hands = []

        for i in range(15):
            carta = random.choice(traco.cartas_do_jogo)
            _index = traco.cartas_do_jogo.index(carta)

            self.cards_in_hands.append(traco.cartas_do_jogo[_index])
            traco.deletar_carta(_index, 0)         
        return list_cards_in_hands 
         

    def checkBag(self):
        catch_trash = False

    # From traco.arquivo_morto_? to player.cards_in_hands
    def catchBag(self, local):
        if len(self.cards_in_hands) == 0:

            if len(traco.arquivo_morto_a) > 0:
                print('Batido! Vou pegar o morto')

                for i in range(len(traco.arquivo_morto_a)):
                    carta = random.choice(traco.arquivo_morto_a)
                    _index = traco.arquivo_morto_a.index(carta)

                    self.cards_in_hands.append(traco.arquivo_morto_a[_index])
                    traco.deletar_carta(_index, 1)

                # print(f'Agora o arquivo morto A possui {len(traco.arquivo_morto_a)} cartas')
                # print(f'Agora eu possuo {len(self.cards_in_hands)} cartas na mão')

            elif len(traco.arquivo_morto_b) > 0: 
                print('Batido! Vou pegar o morto')

                for i in range(len(traco.arquivo_morto_b)):
                    carta = random.choice(traco.arquivo_morto_b)
                    _index = traco.arquivo_morto_b.index(carta)

                    self.cards_in_hands.append(traco.arquivo_morto_b[_index])
                    traco.deletar_carta(_index, 2)  

                # print(f'Agora o arquivo morto B possui {len(traco.arquivo_morto_b)} cartas')
                # print(f'Agora eu possuo {len(self.cards_in_hands)} cartas na mão')                                     

        else:
            print(f'Ainda possuo {len(self.cards_in_hands)} cartas na mão!')    


    def catchCard(self, local):
        pos = traco.indice_carta()          
        self.cards_in_hands.append(traco.cartas_do_jogo[pos])
        traco.deletar_carta(pos, local)


    def catchTrash(self, par):
        print('O jogador pegou o BAG')
        if par == True:         
        
            print('Opa! Peguei o Lixo!')

            for i in range(len(traco.lixo)):
                carta = random.choice(traco.lixo)
                _index = traco.lixo.index(carta)

                self.cards_in_hands.append(traco.lixo[_index])
                traco.deletar_carta(_index, 3)        

        self.sortCards()


    def sortCards(self):
        print('O jogador ordenou suas cartas.')

        pos = 0
        for i in sorted(self.cards_in_hands, key=lambda k: (k[1], int(k[0]))):
            old_pos = self.cards_in_hands.index(i)
            # print('Old_pos antes ', old_pos)

            self.cards_in_hands.insert(pos,i)
            pos += 1
            old_pos += 1
            self.deletar_carta(old_pos)

        # print('Cartas na mão Depois', self.cards_in_hands)    

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
        # carta meramente para escolher aleatório
        carta = random.choice(self.cards_in_hands)
        # pos deve ser passada por parametro ao chamar a função discard no main.
        pos = self.indice_carta(carta)

    
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
        """print(f'Removido o item da posição {pos}' \
        f'. Agora temos {len(self.cards_in_hands)} cartas.')"""

    def return_lixo(self):
        # print('-----------------')
        lixeira = traco.lixo[0]
        # print(lixeira)
        return lixeira
