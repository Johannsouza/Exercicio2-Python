# Elabore um programa que solicite duas notas ao usuário e calcule a média. Em seguida,
# informe se o aluno foi:
# • Aprovado (média maior ou igual a 7)
# • Recuperação (média entre 5 e 6.9)
# • Reprovado (média abaixo de 5)

nota1=float(input("Digite a nota da av1: "))
nota2=float(input("Digite a nota da av2: "))

media=nota1+nota2/2

if(media>=7):
    print("Aprovado!")
elif(media>=5 or media<=6.9):
    print("Recuperação!")
else:
    print("Reprovado!")
