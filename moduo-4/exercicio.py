# mode
# r lritura 
# a append / incrementa
# w escrita
# x criar arquivos
# R+ leitura mais escrita

# abrir arquivo
arquivo = open('moduo-4\exercicio.txt', mode='r', encoding='utf8' )

print(arquivo.readable()) # veificar o statatus o retono dele se ele pode ser lido
print(arquivo.readline())
print(arquivo.read())


lista = arquivo.readline()
print(lista)
arquivo.close()

