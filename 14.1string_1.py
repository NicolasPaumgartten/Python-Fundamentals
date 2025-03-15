#Maiúsculas, Minúsculas e titulo
nome = "nIColAs"

print(nome.upper()) # MAIUSCULO
print(nome.lower()) # MINUSCULO
print(nome.title()) # PRIMEIRA LETRA MAIUSCULA - Titulo

#Eliminando espaços em branco
texto = "  Olá mundo!    "

print(texto + ".") # sem strip
print(texto.strip() + ".") # com strip
print(texto.rstrip() + ".") # com strip a direita
print(texto.lstrip() + ".") # com strip a esquerda


#Junções e centralização
menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))
