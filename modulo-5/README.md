
# 1. Função lambda
1.1. Definição
Função anônima (sem nome) com bloco de código super enxuto e
que pode ser salva em uma
variável. Em geral é utilizada com outros métodos funcionais
como map , filter , e reduce .
variavel = lambda params: expressão
Exemplo: Função lambda para extrair provedor de e-mail.


dobro = lambda x: x * 2
resultado = dobro(5)
print(resultado)  # Saída: 10

# map() é uma função embutida em Python que permite aplicar uma função a cada
elemento de um iterável (como uma lista, tupla, etc.)
e retorna um novo iterador contendo os resultados.

A sintaxe básica da função map() é a seguinte:

map(funcao, iteravel)

numeros = [1, 2, 3, 4, 5]
dobro = map(lambda x: x * 2, numeros)
resultado = list(dobro)
print(resultado)  # Saída: [2, 4, 6, 8, 10]

# filter() é uma função embutida em Python que permite filtrar
elementos de um iterável (como uma lista, tupla, etc.)
com base em uma determinada condição.
Ela retorna um iterador contendo apenas os elementos que atendem à
condição especificada.

A sintaxe básica da função filter() é a seguinte:

filter(funcao, iteravel)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filter(lambda x: x % 2 == 0, numeros)
resultado = list(pares)
print(resultado)  # Saída: [2, 4, 6, 8, 10]
