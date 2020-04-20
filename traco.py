import pdb #import pdb for debugging
import random
class Traco:
    # Élysson MR
    def __init__(self):
        self.cartas_do_jogo = []
        self.cartas_do_jogo.extend(self._criar_baralho())
        self.cartas_do_jogo.extend(self._criar_baralho())
        
        self.arquivo_morto_a = []
        self.arquivo_morto_a.extend(self._criar_arquivo_morto())
        
        self.arquivo_morto_b =[]
        self.arquivo_morto_b.extend(self._criar_arquivo_morto())

        self.lixo = []
        # self.lixo.extend(self._alimentar_lixo())


    def _criar_arquivo_morto(self):
        list_arquivo_morto = []
        # pdb.set_trace() #breakpoint

        for i in range(15):
            pos = self.indice_carta()          
            list_arquivo_morto.append(self.cartas_do_jogo[pos])
            self.deletar_carta(pos, 1)         
        return list_arquivo_morto 


    def alimentar_lixo(self, carta):
        # pdb.set_trace() #breakpoint  
        # print('Lixo antes ', carta)      
        self.lixo.append(carta)  
        # print('Lixo depois ', carta)            
        # return list_lixo

    def _criar_baralho(self):
        cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        naipes = ['C', 'E', 'O', 'P']

        list_baralho = []
        for carta in cartas:
            for naipe in naipes:
                list_baralho.append((carta, naipe))

        return list_baralho

    def indice_carta(self):
            carta = random.choice(self.cartas_do_jogo)
            _index = self.cartas_do_jogo.index(carta)
            return _index    

    def deletar_carta(self, pos, local):
        """
        Params: 
            pos = Positive integer
            local = Positive integer
                1 = cartas_do_jogo ==> Significa queserá exluída desse atributo.
                2 = arquivo_morto_a ==> Significa queserá exluída desse atributo.
                3 = arquivo_morto_b ==> Significa queserá exluída desse atributo.
        """
        if pos >= 0:
            if local == 1:
                del(self.cartas_do_jogo[pos])
            elif local == 2:
                del(self.arquivo_morto_a[pos])
            else:
                del(self.arquivo_morto_b[pos])                    
        #print(f'Removido o item da posição {pos}' \
        #f'. Agora temos {len(self.cartas_do_jogo)} cartas.')


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