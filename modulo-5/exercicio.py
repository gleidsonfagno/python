import math
from functools import reduce
emprestimos = []
with open(file='modulo-5\credito.csv', mode='r', encoding='utf8') as fp:
    fp.readline()  # cabeçalho
    linha = fp.readline()
    while linha:
        linha_emprestimo = {}
        linha_elementos = linha.strip().split(sep=',')
        linha_emprestimo['id_vendedor'] = linha_elementos[0]
        linha_emprestimo['valor_emprestimos'] = linha_elementos[1]
        linha_emprestimo['quantidade_emprestimos'] = linha_elementos[2]
        linha_emprestimo['data'] = linha_elementos[3]
        emprestimos.append(linha_emprestimo)
        linha = fp.readline()
for emprestimo in emprestimos:
    print(emprestimo)
print("\n")
"""
1. Função map
Aplique a função map na lista de emprestimos para extrair os valores da chave
valor_emprestimos na lista valor_emprestimos_lista . Faça também a conversão
de str para float .

"""
valor_emprestimos_lista = list(
    map(lambda x: float(x["valor_emprestimos"]), emprestimos))
print(f"O valor dos emprestimos sao {valor_emprestimos_lista}")
print("\n")

"""
2. Função filter
Aplique a função filter na lista de valor_emprestimos_lista
para filtrar apenas os valores
maiores que zero (os valores negativas são erros na base de dados).
Salve os valores na lista
valor_emprestimos_lista_filtrada .
"""
valor_emprestimos_lista_filtrada = list(
    filter(lambda x: x > 0, valor_emprestimos_lista))
print(f"Emprestimos maiores que zero {valor_emprestimos_lista_filtrada}")

"""
3. Função reduce
Com a nossa lista de valores de emprestimo pronta,
vamos extrair algumas métricas.
3.1. Função reduce para extrair a soma
Aplique a função reduce para somar os elementos da lista 
valor_emprestimos_lista_filtrada na variavel soma_valor_emprestimos.
"""

soma_valor_emprestimos = reduce(
    lambda x, y: x + y, valor_emprestimos_lista_filtrada)
print(soma_valor_emprestimos)
# Aplique a função reduce para extrair a média aritimética (mais informações aqui) dos elementos
# da lista valor_emprestimos_lista_filtrada na variavel
# media_valor_emprestimos .
media_valor_emprestimos = soma_valor_emprestimos / \
    len(valor_emprestimos_lista_filtrada)
print(media_valor_emprestimos)

# 3.3. (Desafio) Função reduce para extrair o desvio padrão
# Aplique a função reduce para extrair a média aritimética
# (mais informações aqui) dos elementos
# da lista valor_emprestimos_lista_filtrada na variavel
# desvio_padrao_valor_emprestimos .


media_valor_emprestimos = reduce(
    lambda x, y: x + y, valor_emprestimos_lista_filtrada) / len(valor_emprestimos_lista_filtrada)

desvio_padrao_valor_emprestimos = math.sqrt(
    reduce(lambda x, y: x + y, map(lambda x: (x - media_valor_emprestimos)
           ** 2, valor_emprestimos_lista_filtrada))
    / len(valor_emprestimos_lista_filtrada)
)
print(desvio_padrao_valor_emprestimos)
