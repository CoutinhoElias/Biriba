# Criei uma lista de coisas
z = ['A', 'B', 'C', 'D']

print(z)
# Resultado ['A', 'B', 'C', 'D']
# -----------------------------------------------------------------------------------------

# Mostrar somente parte de uma lista baseando nas suas posições.
# O uso do sinal negativo é se referindo aos ultimos, no exemplo abaixo os dois últimos:

print(z[-2:])
# Resultado ['C', 'D']
# -----------------------------------------------------------------------------------------

# Quero adicionar um elemento em determinada posição da lista.
z.insert(3, 'why')
print(z)
# Resultado ['A', 'B', 'C', 'why', 'D']

# Observe que quando adicionei oelemento 'why' na posição 3 e mandei imprimir ele mostrou
# depoisdo A, B e C, isso dá uma falsa impressão que está na posição 4, mas ele está realmente 
# na posição 3, pois na programação independente da linguagem tudo começa do ZERO, ou seja,

# Elementos: 'A', 'B', 'C', 'D', 'F', 'G', ... n  
# Posição:    0,   1,   2,   3,   4,   5, ... n


