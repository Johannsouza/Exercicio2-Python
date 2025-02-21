# Peça ao usuário três números representando os lados de um triângulo. O programa deve
# verificar e informar se os valores formam um triângulo válido (a soma de dois lados deve ser
# sempre maior que o terceiro).

lado1 = int(input("Digite o valor do primeiro lado do triângulo: "))
lado2 = int(input("Digite o valor do segundo lado do triângulo: "))
lado3 = int(input("Digite o valor do terceiro lado do triângulo: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("O triângulo é válido!")
else:
    print("O triângulo não é válido!")
