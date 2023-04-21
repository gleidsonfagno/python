# 2. Conjuntos 
# 2.1. Motivação
# Você trabalha como analista de dados de mídias sociais e precisa descobrir todas as hashtags
# que alcançaram o top trending do Twitter durante uma semana. Você já conseguiu as hashtags
# por dia da semana:

hashtags_seg = ['#tiago', '#joao', '#bbb']
hashtags_ter = ['#sarah', '#bbb', '#fiuk']
hashtags_qua = ['#gil', '#thelma', '#lourdes']
hashtags_qui = ['#rafa', '#fora', '#danilo']
hashtags_sex = ['#juliete', '#arthur', '#bbb']
# hashtags_semana = hashtags_seg + hashtags_ter + hashtags_qua + hashtags_qui +  hashtags_sex

# remover lista repetidas usa o set
hashtags_semana = list(set(hashtags_seg + hashtags_ter + hashtags_qua + hashtags_qui +  hashtags_sex))
print(hashtags_semana)
print(len(hashtags_semana))
# print(type(hashtags_semana))



# 2.4. Métodos
# São métodos nativos do Python que nos ajudam a trabalhar no dia a dia com conjuntos.
cursos = {'Exatas', 'Humanas', 'Biológicas'}
print(cursos)
# inserir um elemento no conjunto: set.add(val)
cursos.add('Saúde')
print(cursos)
# remover um elemento no conjunto: set.remove(val)
cursos.remove('Saúde')
print(cursos)