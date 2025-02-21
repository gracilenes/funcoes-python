"""Crie uma função chamada idade_valida que verifica se a idade fornecida como argumento é um número inteiro válido entre 0 e 150."""

def idade_valida(idade):
    if isinstance(idade, int) and 0 <= idade <= 150:
        return True
    return False
print(idade_valida(25))  # Resultado: True
print(idade_valida(151))  # Resultado: False
print(idade_valida(-1))  # Resultado: False
print(idade_valida(100))  # Resultado: True
