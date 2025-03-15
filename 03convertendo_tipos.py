#Conversão de tipos : para converter uma variavel de um tipo para outro.

print(int(1.97348728)) 
print(int("10"))
print(float("10.10"))
print(float(100))

valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))

print(100 / 2)
print(100 // 2)

#Numérico para string
preço = 10.50
idade = 26

print(str(preço))
#>>> '10.5'

print(str(idade))
#>>> '26'

texto = f"idade {idade} e preço {preço}" #
print(texto)
#>>> 'idade 26 e preço 10.5'