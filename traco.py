import pdb #import pdb for debugging
import random
class Traco:
    # Élysson MR
    def __init__(self):
        self.cartas_do_jogo = [] # Lista de tuplas
        self.cartas_do_jogo.extend(self._criar_baralho())
        self.cartas_do_jogo.extend(self._criar_baralho())
        
        self.arquivo_morto_a = [] # Lista de tuplas
        self.arquivo_morto_a.extend(self._criar_arquivo_morto())
        
        self.arquivo_morto_b =[] # Lista de tuplas
        self.arquivo_morto_b.extend(self._criar_arquivo_morto())

        self.lixo = [] # Lista de tuplas

        self.table = [] # Lista de listas de tuplas


    def _criar_arquivo_morto(self):
        list_arquivo_morto = []
        # pdb.set_trace() #breakpoint

        for i in range(15):
            pos = self.indice_carta()          
            list_arquivo_morto.append(self.cartas_do_jogo[pos])
            self.deletar_carta(pos, 0)         
        return list_arquivo_morto 


    def alimentar_lixo(self, carta):    
        self.lixo.append(carta) 
        # print('Na lixeira temos as cartas: ', self.lixo)


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
                0 = cartas_do_jogo ==> Significa que será exluída desse atributo.
                1 = arquivo_morto_a ==> Significa que será exluída desse atributo.
                2 = arquivo_morto_b ==> Significa que será exluída desse atributo.
                3 = lixo ==> Significa que será exluída desse atributo.
                
        """
        if pos >= 0:
            if local == 0:
                del(self.cartas_do_jogo[pos])
            elif local == 1:
                del(self.arquivo_morto_a[pos])
            elif local == 2:
                del(self.arquivo_morto_b[pos]) 
            elif local == 3:
                del(self.lixo[pos])  
   