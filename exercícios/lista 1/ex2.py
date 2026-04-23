#receba um número e verifique: se está entre 10 e 20 (inclusive), caso contrário, informe que está fora

num = int(input("Digite um número: "))

if num >= 10 and num <= 20:
    print("O número está entre 10 e 20.")
else:
    print("O número está fora do intervalo.")