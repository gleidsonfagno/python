# read para ler arquivos simples (ex: senhas, tokens, informacoes unicas)
with open('email.txt', 'r') as arquivo:
     email = arquivo.read()
     print(email)
     
# redline para arquivos maiores
with open("mensagem.txt", 'r', encoding='utf8') as arquivo:
     mensagem = arquivo.readlines() #le a primeira linha
     for linha in mensagem:
          if 'O faturamento desse mês foi de: R$15.000' in linha:
               print(linha)
               print(mensagem)
     # while mensagem:
     #           mensagem = arquivo.readline()
     #           print(mensagem)

with open('senha.txt', 'r') as arquivo:
     senha = arquivo.readlines()
     print(senha)

# substituir por completo o texto esta escrito
with open('senha.txt', 'w', encoding='utf8') as arquivo:
     arquivo.write('456789')

# aicionar informaco 
with open('email.txt', 'a', encoding='utf8') as arquivo:
     arquivo.write('\npythonfagnor@gmail.com')