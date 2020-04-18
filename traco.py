import pdb #import pdb for debugging
class Traco:
    # Élysson MR
    def __init__(self):
        self.cartas_do_jogo = []
        self.cartas_do_jogo.extend(self._criar_baralho())
        self.cartas_do_jogo.extend(self._criar_baralho())

        print(f'Na classe Traco possui {len(self.cartas_do_jogo)} cartas')

    def _criar_baralho(self):
        cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        naipes = ['C', 'E', 'O', 'P']

        list_baralho = []
        for carta in cartas:
            for naipe in naipes:
                list_baralho.append((carta, naipe))

        return list_baralho

    def deletar_carta(self, pos):
        if pos > len(self.cartas_do_jogo):
            # pdb.set_trace() #breakpoint
            print('**********   Esse indice não existe   **********')
        if pos >= 0:
            del(self.cartas_do_jogo[pos])
        print(f'Removido o item da posição {pos}. Agora temos {len(self.cartas_do_jogo)} cartas.')


# traco = Traco()
# traco.deletar_carta(6)

#class Traco:
#    def __init__(self, ):
#        self.cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#        self.nipes = ['C', 'E', 'O',  'P']
#        self.gamer1 = []
#        self.gamer2 = []
#        self.gamer3 = []
#        self.gamer4 = []
#
#
#    def create_deck(self):
#        self.deck = [(carta, nipe) for nipe in self.nipes for carta in self.cartas]
#        print('Na classe Traco na função "deck" o deck está com ', len(self.deck))
#        # self.create_card_gamer()
#
#    def del_card_deck(self, pos):
#        if pos >= 0:
#            del(self.deck[pos])
#        print('Na classe Traco depois da função "deleta" o deck está com ', len(self.deck))
#
#    def create_card_gamer(self):
#
#        jogadores = [gamer1, gamer2, gamer3, gamer4]
#
#        # random.choice(baralho)
#        # preenchendo cartas do jogador e removendo do baralho
#        j = 0
#        #for jogador in jogadores:
#        #    j += 1
#        #    for i in range(15):
#        #        carta = random.choice(self.deck)
#        #        pos = deck.index(carta)
#        #        jogador.append(carta)
#        #        del(baralho[pos])        