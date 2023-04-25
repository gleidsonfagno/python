# Aula 1: Estrutura condicional if / else / elif
if True:
 print("Verdadeiro")
else:
 print("Falso")
# Exemplo: Código de segurança de um cartão de crédito
codigo_de_seguranca = '291'
codigo_de_seguranca_cadastro = '010'
pode_efetuar_pagamento = codigo_de_seguranca == codigo_de_seguranca_cadastro
print(pode_efetuar_pagamento)

# if pode_efetuar_pagamento:
#  print("Pagamento efetuado")
# else:
#  print("Erro: Código de segurança inválido")

# if codigo_de_seguranca == codigo_de_seguranca_cadastro:
#  print("Pagamento efetuado")
# else:
#  print("Erro: Código de segurança inválido")

# Exemplo: Código e senha de segurança de um cartão de crédito
codigo_de_seguranca = '852'
codigo_de_seguranca_cadastro = '852'
senha = '7783'
senha_cadastro = '7783'
# if (codigo_de_seguranca == codigo_de_seguranca_cadastro) & \
#  (senha == senha_cadastro):
#  print("Pagamento efetuado")
# else:
#  print("Erro: Pagamento não efetuado")

# if (codigo_de_seguranca != codigo_de_seguranca_cadastro) | \
#  (senha != senha_cadastro):
#  print("Erro: Pagamento não efetuado")
# else:
#  print("Pagamento efetuado")


# 1.2. if / elif / else
# Podemos também avaliar múltipla condições.
if (codigo_de_seguranca == codigo_de_seguranca_cadastro) & \
 (senha == senha_cadastro):
 print("Pagamento efetuado")
elif (codigo_de_seguranca != codigo_de_seguranca_cadastro) & \
 (senha == senha_cadastro):
 print("Erro: Código de segurança inválido")
elif (codigo_de_seguranca == codigo_de_seguranca_cadastro) & \
 (senha != senha_cadastro):
 print("Erro: Senha inválida inválida")
else:
 print("Erro: Código de segurança e senha inválidos")


s = '23'
sc = '23'
cli = 'fagno'
clic = 'fagno'
if (s == sc)  & (cli == clic):
 print("aprovado")
elif(s == sc ) & (cli != clic):
     print("cliente invalido")
elif(s != sc ) & (cli == clic):
     print("senha invalida")
else:
     print("tudo errado")