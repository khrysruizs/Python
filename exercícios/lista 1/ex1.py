#um programa que receba um números diga se ele é par ou ímpar e compare com outro número mostrando qual é o maior 

n1 = int(input("Digite um número: "))

if n1 % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")


n2 = int(input("Digite outro número: "))


if n1 > n2:
    print(n1, "é maior que", n2)
elif n2 > n1:
    print(n2, "é maior que", n1)
else:
    print("Os dois números são iguais.")

