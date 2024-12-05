# print()
print("Olá, mundo!")

# len()
texto = "Python"
print(len(texto))  # Saída: 6

# input()
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

# range()
for i in range(5):
    print(i)  # Saída: 0, 1, 2, 3, 4

# sum(), max() e min()
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)  # Saída: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

# Parâmetros em Funções
def saudacao(nome):
    print("Olá," + nome)
saudacao("Maria")

def saudacao(nome, sexo):
    if sexo == 'f':
        print(f"Olá, senhora {nome}!")
    elif sexo == 'm':
        print(f"Olá, senhor {nome}!")        
    else:
        print(f"Olá, {nome}!")

saudacao('José', 'm')

# Retornos em Funções
def soma(a, b):
    resultado = a + b
    return resultado

resultado_soma = soma(3, 5)
print(resultado_soma)  # Saída: 8

def saudacao(nome):
    print(f"Olá, {nome}!")
    # Sem instrução return

resultado = saudacao("Maria")
print(resultado)  # Saída: None

# Tipagem Opcional
resultado_soma1 = soma(3, 5)
resultado_soma2 = soma("Olá, ", "Mundo!")
print(resultado_soma1)  # Saída: 8
print(resultado_soma2)  # Saída: Olá, Mundo!

# Declaração de Tipos em Parâmetros
def soma(a: int, b: int) -> int:
    resultado = a + b
    return resultado

def saudacao(nome: str) -> str:
    return "Olá, " + nome

# Tipos Compostos e Anotações Avançadas
from typing import List, Dict, Tuple

def processa_dados(dados: List[str]) -> Dict[str, int]:
    resultado: Dict[str, int] = {}
    for item in dados:
        resultado[item] = len(item)
    return resultado

# Escopo Local e Escopo Global em Python
# 1. Escopo Local: 
# O escopo local refere-se às variáveis que são definidas dentro de uma função.
# Essas variáveis só são acessíveis dentro da função em que foram criadas.
# Quando a função termina de ser executada, as variáveis locais deixam de existir.
# Se tentarmos acessar uma variável local fora da função, ocorrerá um erro de "NameError".

def minha_funcao():
    x = 10  # Variável local, só visível dentro da função
    print(x)
minha_funcao() # Saída: 10
print(x) # Erro: NameError: name 'x' is not defined

# Escopo Global: 
# O escopo global refere-se às variáveis que são definidas fora de qualquer função ou bloco de código.
# Essas variáveis são acessíveis em todo o programa, em qualquer função.
# Variáveis globais podem ser lidas (usadas) em uma função sem a necessidade de declará-las novamente, mas para modificá-las, é preciso usar a palavra-chave "global" para informar ao Python que queremos modificar a variável global e não criar uma variável local com o mesmo nome.

x = 10  # Variável global

def minha_funcao():
    print(x)  # Variável global acessível dentro da função

minha_funcao()  # Saída: 10

def altera_variavel_global():
    global x
    x = 20  # Modificando a variável global
    print(x)

altera_variavel_global()  # Saída: 20
print(x)  # Saída: 20 (variável global foi modificada)

# Encadeamento de Escopos (Closure):
# Python também permite a criação de funções dentro de funções, o que gera uma estrutura de escopos encadeados. 
# Nesse caso, a função interna (função aninhada) tem acesso ao escopo local da função externa (função pai).

def funcao_pai():
    x = 10

    def funcao_filha():
        print(x)  # A função filha pode acessar a variável x da função pai

    funcao_filha()

funcao_pai()  # Saída: 10
