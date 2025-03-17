"""
Arquivo: erros_comuns.py
Este arquivo contém exemplos de erros comuns em Python, com explicações para cada um.
"""

# SyntaxError: Erro de sintaxe
# Ocorre quando há um erro na escrita do código.
# Exemplo (remova o comentário para ver o erro):
# print("Hello World"  # Parêntese não fechado causa erro

# IndexError: Erro de indexação
# Ocorre quando tentamos acessar um índice inexistente em uma sequência.
lista = [1, 2, 3]
# print(lista[5])  # Erro: Índice 5 não existe na lista

# ModuleNotFoundError: Erro de módulo não encontrado
# Ocorre quando tentamos importar um módulo que não está instalado no ambiente.
# import nonexistent_module  # Erro: módulo não encontrado

# NameError: Erro de nome
# Ocorre quando tentamos usar uma variável que não foi definida.
# print(x)  # Erro: x não foi definido antes de ser usado

# ValueError: Erro de valor
# Ocorre quando passamos um valor inválido para uma função ou conversão.
# numero = int("abc")  # Erro: 'abc' não pode ser convertido para int

# KeyError: Erro de chave
# Ocorre quando tentamos acessar uma chave inexistente em um dicionário.
dicionario = {"nome": "Nicolas", "idade": 25}
# print(dicionario["endereco"])  # Erro: chave 'endereco' não existe

# TypeError: Erro de tipo
# Ocorre quando tentamos realizar uma operação entre tipos incompatíveis.
# resultado = "10" + 5  # Erro: não podemos somar string com inteiro

# ImportError: Erro de importação
# Ocorre quando tentamos importar um módulo que não existe ou não está instalado.
# import modulo_inexistente  # Erro: módulo não encontrado

# Para evitar esses erros, sempre revise seu código, use blocos try-except e valide dados antes de usá-los.
