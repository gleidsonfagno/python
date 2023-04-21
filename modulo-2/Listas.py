# 1. Listas

dia_11_saldo_inicial = 1000

dia_11_transacao_1 = 243
dia_11_transacao_2 = -798.58
dia_11_transacao_3 = 427.12
dia_11_transacao_4 = -10.91

dia_11_saldo_final = dia_11_saldo_inicial + \
dia_11_transacao_1 + \
dia_11_transacao_2 + \
dia_11_transacao_3 + \
dia_11_transacao_4
print(dia_11_saldo_final)
# 1.2. Definição
# Armazenam sequências mutáveis e ordenadas de valores. São do tipo list
usuario_web = [
 'André Perez',
 'andre.perez',
 'andre123',
 'andre.perez@gmail.com'
]
print(usuario_web)
print(type(usuario_web))

idade = 20
saldo_em_conta = 723.15
usuario_loggedin = True
usuario_web = [
 'André Perez',
 idade,
 'andre.perez',
 'andre123',
 'andre.perez@gmail.com',
 saldo_em_conta,
 usuario_loggedin
]
print(usuario_web)
print(type(usuario_web))
# 1.3. Operações
# As operações da estrutura do tipo list são:
# + (concatenação).
# Exemplo: Fabricantes de hardware mobile
fabricantes_mobile_china = ['xiaomi', 'huawei']
fabricantes_mobile_eua = ['apple', 'motorola']
fabricantes_mobile = fabricantes_mobile_china + fabricantes_mobile_eua
print(fabricantes_mobile_china)
print(fabricantes_mobile_eua)
print(fabricantes_mobile)

print(f'0: {fabricantes_mobile[2:len(fabricantes_mobile)]}')
fabricantes_mobile[2] = 'nokia'
print(fabricantes_mobile)

# 1.4. Métodos
# São métodos nativos do Python que nos ajudam a trabalhar no dia a dia com listas.
juros = [0.05, 0.07, 0.02, 0.04, 0.08]
print(juros)
#  inserir um elemento sem substituir: list.insert(index, val)
juros.insert(0, 0.10)
print(juros)

#  inserir um elemento no fim da lista: list.append(val)
juros.append(0.09)
print(juros)

#  remover um elemento pelo valor: list.remove(val)
juros.remove(0.1)
print(juros)


# remover um elemento pelo índice: list.pop(val)
terceiro_juros = juros.pop(2)
print(terceiro_juros)

# 1.5. Conversão
# Podemos converter alguns tipos de variáveis em listas, como strings.

email = 'andre.perez@gmail.com'
caracteres_email = list(email)
print(email)
print(caracteres_email)

dia_11_saldo_inicial = 1000
dia_11_transacoes = []
dia_11_transacoes.append(243)
dia_11_transacoes.append(-798.58)
dia_11_transacoes.append(427.12)
dia_11_transacoes.append(-10.91)
print(dia_11_transacoes)

dia_11_saldo_final = dia_11_saldo_inicial + \
dia_11_transacoes[0] + \
dia_11_transacoes[1] + \
dia_11_transacoes[2] + \
dia_11_transacoes[3]
print(dia_11_saldo_final)