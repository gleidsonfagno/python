# 2. Estrutura condicional try /except / finally
# 2.1. Exceção
# Exceções são erros que podem acontecer durante a execução do nosso código. 
# Exemplo: Erro de operações numéricas impossíveis
preco = 132.85
pessoas = 0
# valor_por_pessoa = preco / pessoas
# nome = 'Andre Perez'
# idade = True
# apresentacao = 'Fala pessoal, meu nome é ' + nome + \
# ' e eu tenho ' + idade + ' anos'
# anos = [2019, 2020, 2021]
# no_atual = anos[3]

cursos = {
 'python': {
'nome': 'Python para Análise de Dados', 'duracao': 2.5
 },
 'sql': {
'nome': 'SQL para Análise de Dados', 'duracao': 2
 }
}
# curso_atual = cursos['analista']


# 2.2. try / except
# Estrutura para tratar exceções
preco = 132.85
pessoas = 2
try:
 valor_por_pessoa = preco / pessoas
 print(valor_por_pessoa)
except ZeroDivisionError:
 print('Número de pessoas inválido. ' + \
'Espera-se um valor maior que 0 e obteve-se um valor igual a ' + \
str(pessoas)
)
anos = [2019, 2020, 2021]
try:
 ano_atual = anos[3]
 print(ano_atual)
except Exception:
 print('Lista de anos é menor que o valor escolhido. ' + \
'Espera-se um valor entre 0 e ' + \
str(len(anos) - 1)
)


anos = [2019, 2020, 2021]
try:
 ano_atual = anos[3]
 print(ano_atual)
except Exception as exc:
 print('Descrição da exceção: ' + str(exc))
 print('Tipo da exceção: ' + str(type(exc)))
 print('Lista de anos é menor que o valor escolhido. ' + \
'Espera-se um valor entre 0 e ' + \
str(len(anos) - 1)
)

anos = [2019, 2020, 2021]
try:
 ano_atual = anos[3]
 print(ano_atual)
except IndexError:
 print('Lista de anos é menor que o valor escolhido. ' + \
'Espera-se um valor entre 0 e ' + \
str(len(anos) - 1)
)
except Exception as exc:
 print(exc)
 print('Erro genérico')

#  2.3. try / except / finally
nome = 'Andre Perez'
idade = 19
try:
 apresentacao = 'Fala pessoal, meu nome é ' + nome + \
' e eu tenho ' + idade + ' anos'
 print(apresentacao)
except TypeError:
 idade = str(idade)
finally:
 print('Segunda chance')
 apresentacao = 'Fala pessoal, meu nome é ' + nome + \
' e eu tenho ' + idade + ' anos'
 print(apresentacao)
