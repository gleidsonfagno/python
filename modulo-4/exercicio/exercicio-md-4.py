#  Exercícios
#  0. Preparação do ambiente
#  Neste exercício vamos trabalhar com os arquivos de csv e texto definidos abaixo. Execute cadauma das células de código para escrever os arquivos na sua máquina virtual.
#  carros.csv: arquivo csv com informações sobre carros (venda, manutenção, portas, etc.)

#  1. Funções para arquivo csv
#  Complete a função abaixo para extrair uma coluna do arquivo csv em uma lista. Os elementosdevem ter o tipo de dado correto.

def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int, tipo_dado: str):
    coluna = []
    
    with open(nome_arquivo, 'r', encoding='utf8') as arquivo:
        linhas = arquivo.readlines()
        
        for linha in linhas:
            elementos = linha.strip().split(',')
            dado = elementos[indice_coluna]
            
            if tipo_dado == 'str':
                coluna.append(dado)
            elif tipo_dado == 'int':
                coluna.append(int(dado))
            elif tipo_dado == 'float':
                coluna.append(float(dado))
            else:
                print("Tipo de dado inválido!")
                return None
    
    return coluna

# Teste da função
valor_venda = extrai_coluna_csv(nome_arquivo='./carros.csv', indice_coluna=1, tipo_dado='str')
print(valor_venda)


def extrai_linha_txt(nome_arquivo: str, numero_linha: int):
    palavras_linha = []
    
    with open(nome_arquivo, 'r', encoding='utf8') as arquivo:
        linhas = arquivo.readlines()
        
        if 1 <= numero_linha <= len(linhas):
            linha = linhas[numero_linha - 1].strip()
            palavras_linha = linha.split(' ')
    
    return palavras_linha

# Teste da função
linha10 = extrai_linha_txt(nome_arquivo='./musica.txt', numero_linha=10)
print(linha10)

