# 2 - Faça um programa que peça dois números ao usuário e exiba o maior deles. Caso os números
# sejam iguais, exiba uma mensagem informando essa condição.

x=int(input("Digite um número inteiro: "))
y=int(input("Digite um outro número inteiro: "))

if(x>y):
    print(f"O maior número é {x}")
elif(y>x):
    print(f"O maior número é {y}")
else:
    print("Os números são iguais!")
