"""
No Python, uma classe é uma estrutura que define um tipo de objeto. É uma maneira de criar um "molde" para objetos que compartilham características semelhantes. As classes definem atributos e métodos que descrevem o comportamento e as propriedades dos objetos.

Para criar uma classe em Python, você pode usar a palavra-chave class, seguida pelo nome da classe. Aqui está um exemplo básico de uma classe em Python:
"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


# Criando um objeto da classe Pessoa
pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("gleidson", 21)

# Chamando o método saudacao do objeto
pessoa1.saudacao()
pessoa2.saudacao()
"""
Neste exemplo, temos uma classe chamada "Pessoa" que tem dois atributos: "nome" e "idade". O método __init__ é um método especial chamado de construtor, responsável por inicializar os atributos da classe. O método saudacao é um método da classe que imprime uma saudação usando os atributos.

Para criar objetos da classe, basta chamar o nome da classe seguido de parênteses, como em pessoa1 = Pessoa("João", 25). Em seguida, você pode acessar os atributos e chamar os métodos do objeto, como em pessoa1.saudacao().

As classes em Python são fundamentais para a programação orientada a objetos, permitindo a criação de estruturas complexas e organizadas. Elas facilitam a reutilização de código, encapsulamento de dados e abstração de comportamentos. Além disso, Python também suporta herança, polimorfismo e outros conceitos avançados da orientação a objetos.

"""


class Pessoa:
    def __init__(self, nome, idade, cpf, cidade):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cidade = cidade

    def saudacao(self):
        print(f"ola {self.nome}, seu CPF: {self.cpf}, {self.cidade}")


usuario1 = Pessoa("fagno", 21, "053-312-823-00", "atamira")

usuario1.saudacao()
