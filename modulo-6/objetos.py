"""
Em programação orientada a objetos, um objeto é uma instância de uma classe. Um objeto é uma entidade que possui atributos (variáveis) e comportamentos (métodos) definidos pela classe da qual ele é uma instância.

Em Python, os objetos são criados a partir de classes. Cada objeto possui seu próprio conjunto de atributos e métodos, que podem ser diferentes dos atributos e métodos de outros objetos da mesma classe.

Para criar um objeto em Python, é necessário seguir os seguintes passos:

Definir a classe: Crie uma classe que define a estrutura e o comportamento do objeto. Os atributos são definidos no método especial __init__, e os métodos são definidos dentro da classe.

Instanciar o objeto: Crie uma instância da classe, chamando o nome da classe seguido de parênteses. Os argumentos necessários para inicializar os atributos da classe podem ser passados durante a criação do objeto.

Acessar atributos e chamar métodos: Uma vez que o objeto é criado, é possível acessar seus atributos e chamar seus métodos usando a notação de ponto (objeto.atributo e objeto.metodo()).

Aqui está um exemplo para ilustrar a criação e utilização de objetos em Python:

python
Copy code
"""


from time import sleep


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


# Instanciando objetos da classe Pessoa
pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)

# Acessando atributos e chamando métodos dos objetos
print(pessoa1.nome)  # Saída: João
print(pessoa2.idade)  # Saída: 30

pessoa1.saudacao()  # Saída: Olá, meu nome é João e tenho 25 anos.
pessoa2.saudacao()  # Saída: Olá, meu nome é Maria e tenho 30 anos.

"""
Neste exemplo, a classe Pessoa define objetos que representam pessoas. Cada objeto possui atributos nome e idade, e um método saudacao() que imprime uma saudação personalizada. Duas instâncias da classe Pessoa são criadas (pessoa1 e pessoa2), e é possível acessar seus atributos e chamar seus métodos conforme necessário.

Os objetos em Python permitem modelar o mundo real de forma mais precisa e modular, fornecendo uma abstração poderosa para trabalhar com dados e comportamentos relacionados.
"""

# Certamente! Aqui estão exemplos de código para demonstrar as operações de manipulação de objetos em Python:


class Pessoa:
    pass


# Criando um objeto da classe Pessoa
p1 = Pessoa()

# Atribuindo valores aos atributos do objeto
p1.nome = "João"
p1.idade = 30
p1.profissao = "Engenheiro"

# Acessando os atributos do objeto
print(p1.nome)        # Saída: João
print(p1.idade)       # Saída: 30
print(p1.profissao)   # Saída: Engenheiro


# Chamada de métodos:


class Calculadora:
    def somar(self, a, b):
        return a + b


# Criando um objeto da classe Calculadora
calc = Calculadora()

# Chamando o método somar do objeto
resultado = calc.somar(2, 3)
print(resultado)     # Saída: 5

# Comparação de objetos:


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Criando dois objetos da classe Ponto
p1 = Ponto(1, 2)
p2 = Ponto(3, 4)

# Comparando os objetos usando o operador de igualdade (==)
if p1 == p2:
    print("Os pontos são iguais")
else:
    print("Os pontos são diferentes")   # Saída: Os pontos são diferentes

# Iteração sobre objetos:


class ListaNumeros:
    def __init__(self, numeros):
        self.numeros = numeros

    def __iter__(self):
        return iter(self.numeros)


# Criando um objeto da classe ListaNumeros
lista = ListaNumeros([1, 2, 3, 4, 5])

# Iterando sobre os elementos do objeto
for numero in lista:
    print(numero)    # Saída: 1, 2, 3, 4, 5

# Esses são apenas exemplos básicos para ilustrar as operações de manipulação de objetos em Python. Lembre-se de que a implementação completa das classes e métodos dependerá das necessidades específicas do seu projeto.

tipos = [
    type(10),
    type(1.1),
    type('EBAC'),
    type(True),
    type(None),
    type([1, 2, 3]),
    type({1, 2, 3}),
    type({'janeiro': 1}),
    type(lambda x: x)
]
for tipo in tipos:
    print(tipo)


class ArquivoCSV(object):
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.conteudo = self._extrair_conteudo()
        self.colunas = self._extrair_nome_colunas()

    def _extrair_conteudo(self):
        conteudo = None
        with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:
            conteudo = arquivo.readlines()
        return conteudo

    def _extrair_nome_colunas(self):
        return self.conteudo[0].strip().split(sep=',')

    def extrair_coluna(self, indice_coluna: str):
        coluna = list()
        for linha in self.conteudo:
            conteudo_linha = linha.strip().split(sep=',')
            coluna.append(conteudo_linha[indice_coluna])
        coluna.pop(0)
        return coluna


arquivo_banco = ArquivoCSV(arquivo="modulo-6/banco.csv")

print(arquivo_banco.colunas)

# Extraindo a coluna de job
# job = arquivo_banco.extrair_coluna(indice_coluna=1)
# print(job)

# Extraindo a coluna de education
# education = arquivo_banco.extrair_coluna(indice_coluna=3)
# print(education)


# 4. Herança
# 4.1. Definição
# Uma especialização da classe.
"""
class NomeClasse(object):
 def __init__(self, params):...
class NomeClasseEspecializada(NomeClasse):
 def __init__(self, params):
 super().__init__(self, params)
 self.atributo3 = ...
self.atributo4 = ...
 def metodo3(self, params):
 ...
 def metodo4(self, params):
 ...
Repetindo a definição da classe Pessoa :
"""


class Pessoa(object):
    def __init__(self, nome: str, idade: int, documento: str = None):
        self.nome = nome
        self.idade = idade
        self.documento = documento

    def dormir(self, horas: int) -> None:
        for hora in range(1, horas+1):
            print(f'Dormindo por {hora} horas')
        sleep(1)

    def falar(self, texto: str) -> None:
        print(texto)

    def __str__(self) -> str:
        return f'{self.nome}, {self.idade} anos e ' + \
            f'documento numero {self.documento}'

# Criando a classe Universidade


class Universidade(object):
    def __init__(self, nome: str):
        self.nome = nome
# Especializando a classe Pessoa na classe Estudante :


class Estudante(Pessoa):
    def __init__(
        self,
        nome: str,
        idade: int,
        documento: str,
        universidade: Universidade
    ):
        super().__init__(nome=nome, idade=idade, documento=documento)
        self.universidade = universidade


# 4.2. Manipulação
usp = Universidade(
    nome='Universidade de São Paulo'
)

andre = Estudante(
 nome='Andre Perez',
 idade=30,
 documento='123',
 universidade=usp
)
print(andre)
print(andre.universidade.nome)