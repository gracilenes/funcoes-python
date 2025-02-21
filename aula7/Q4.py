"""Escreva uma função potencia que aceita uma base e um expoente (com expoente padrão igual a 2) e retorna a base elevada ao expoente."""

def potencia(base, expoente=2):
    return base ** expoente
print(potencia(3))        # 3 elevado a 2, resultado: 9
print(potencia(4, 3))     # 4 elevado a 3, resultado: 64
print(potencia(5, 0))     # 5 elevado a 0, resultado: 1
