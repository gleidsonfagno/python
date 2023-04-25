# 3. Estrutura repetição for / in
# 3.1. for / in
# Estrutura que permite a execução repetida de um bloco de código repetidas vezes.
# for variavel_temporaria in coleção:
#  <execute este código>


# 3.2. for / in / range
# Estrutura que permite a execução repetida de um bloco de código n vezes.
for valor in range(6):
 print(valor)

for n in range(0, 1):
     print(n)

soma = 0
for valor in range(0, 100000):
 soma = soma + valor
#  print(soma)
print(soma)

n = 0
for valor in range(5):
     n = n + valor
     print(n)
for contage in range(n):
     print(contage)


for multiplo_dois in range(2, 10, 4):
     print(multiplo_dois)
# 3.3. for / in / list
# Estrutura que permite a execução de um bloco de código para todos os elementos de uma lista.

frutas = ['maca', 'banana', 'laranja', 'uva', 'pera']
for fruta in frutas:
 print(fruta)

frase = 'Fala pessoal, meu nome é André Perez.'
for caracter in frase:
 if (caracter == 'A') | (caracter == 'z'):
  print(f"A letra '{caracter}' está presente na frase.")

# 3.4. for / in / dict
# Estrutura que permite a execução de um bloco de código para todos os elementos de um 
# dicionário.
credito = {'123': 750, '456': 812, '789': 980}

for chave, valor in credito.items():
 print(f'Para o documento {chave}, ' + 'o valor do escore de crédito é ' +  str(valor))
 print('\n')


for chave in credito.keys():
 print(chave)
 print(credito[chave])
 print(f'Para o documento {chave}, ' + 
'o valor do escore de crédito é .' + str(credito[chave]))
 print('\n')

for valor in credito.values():
 print(valor)
 print(f'O valor do escore de crédito é {valor}, ' +  'mas não temos mais as chaves :(.'
)
 print('\n')

#  3.5. break / continue
# Estrutura que permite a quebra ou o avanço de um laço de repetição.

for i in range(0, 10*10*10*10*10*10):
     print(f'o valor e {i}')
     if i == 10:
          break
print('\n')

numero = 3
if numero % 2 == 0:
 print(f'O numero {numero} é par')
else:
 print(f'O numero {numero} é impar')
print('\n')

numeros = [361, 553, 194, 13, 510, 33, 135]
for numero in numeros:
 if numero % 2 == 0:
     print(f'O numero {numero} é par')
     break
 else:
     print(f'O numero {numero} é impar')
print('\n')

numeros = [361, 553, 194, 13, 510, 33, 135]
for numero in numeros:
 if numero % 2 == 0:
     print(f'O numero {numero} é par')
     break
 else:
     continue
     print(f'O numero {numero} é impar')