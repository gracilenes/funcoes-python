"""Crie uma função chamada saudacao_personalizada que aceita um nome e um idioma como argumentos. O idioma é opcional e padrão para "inglês". 
A função deve retornar uma saudação no idioma especificado."""

def saudacao_personalizada(nome, idioma="inglês"):
    if idioma.lower() == "inglês":
        return f"Hello, {nome}!"
    elif idioma.lower() == "português":
        return f"Olá, {nome}!"
    elif idioma.lower() == "espanhol":
        return f"¡Hola, {nome}!"
    else:
        return f"Saudação não disponível em {idioma}. Olá, {nome}!"
print(saudacao_personalizada("João"))  # Saudação em inglês (padrão)
print(saudacao_personalizada("Maria", "português"))  # Saudação em português
print(saudacao_personalizada("Carlos", "espanhol"))  # Saudação em espanhol
print(saudacao_personalizada("Luisa", "francês"))  # Idioma não disponível
