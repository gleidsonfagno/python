# 3. Dicionários
# 3.1. Motivação
# Para se conectar a uma rede wi-fi, você precisa de duas informações: o nome da rede e a 
# senha de acesso. Quando você vai acessar uma nova rede, você encontra uma lista de redes 
# disponíveis:
wifi_disponiveis = ['rede1', 'cnx_cnx', 'uai-fi', 'r3d3']
# print(wifi_disponiveis)

# definicoes

brasil = {'capital': 'Brasília', 'idioma': 'Português', 'populacao': 210}
# print(brasil)
# print(type(brasil))

carro = {
 'marca': 'Volkswagen',
 'modelo': 'Polo',
 'ano': 2021,
 'ano': 2004
}
# print(carro)

# Podemos criar dicionários compostos:
cadastro = {
     'fagno':{
          'nome': 'gleidson fagno',
          'ano_nascimeto': 1992,
          'pais':{
               'pai': {
                    'nome': 'joao pedro',
                    'ano_nascimento': 1971
               },
               'mae':{
                    'nome': 'marinete da conceicao',
                    'ano_nascimento': 1973
               },
          }
     }
}
# print(cadastro)
dados = cadastro ['fagno']['pais']['mae']['ano_nascimento']
# print(dados)

# 3.3. Operações
credito ={
     '123': 750,
     '789': 980
}

# Elementos são acessados pela sua chave.
score_123 = credito['123']
score_789 = credito['789']
print(score_123)
print(score_789)

# Elementos são atualizados pela sua chave
credito['123'] = 435
# print(credito)

# Para adicionar um novo elemento, basta criar um novo elemento chave-valor:
credito['456'] = 1000
# print(credito)

# 3.4. Métodos
# São métodos nativos do Python que nos ajudam a trabalhar no dia a dia com dicionários.

artigo = dict(
 titulo='Modulo 02 | Python: Estruturas de Dados',
 corpo='Topicos, Aulas, Listas, Conjuntos, Dicionários, ...',
 total_caracteres=1530
)
# adicionar/atualizar um elemento pelo chave-valor: dict.update(dict)
# print(artigo)
artigo.update({'total_caracteres': 7850})
# print(artigo)
artigo['total_caracteres'] = 7850

# remover um elemento pelo chave: dict.pop(key)
# print(artigo)
# total_caracteres = artigo.pop('total_caracteres')
# print(artigo)

# 3.5. Conversão
# Podemos converter as chaves e os items de um dicionário em uma lista

chaves = list(artigo.keys())
print(chaves)
print(type(chaves))


valores = list(artigo.values())
print(valores)
print(type(valores))

wifi_disponiveis = []
rede = {'nome': 'rede1', 'senha': 'cnx_cnx'}
wifi_disponiveis.append(rede)
rede = {'nome': 'uai-fi', 'senha': 'r3d3'}
wifi_disponiveis.append(rede)

print(wifi_disponiveis)
