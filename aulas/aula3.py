#estruturas condicionais
opcao = int(input("Escolha um sabor de bolo:\n [1] Chocolate \n [2] Baunilha \n [3] Cenoura \n"))

if opcao == 1:
    print("Sabor chocolate escolhido")
elif opcao == 2:
    print("Sabor baunilha escolhido")
elif opcao ==3:
    print("Sabor cenoura escolhido")
else: 
    print("Sabor inválido")

#estruturas de repetição
texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:   #else não necessário coloquei apenas pra demonstrar for/else
    print ()

#letra upper transforma em maiusculo
#print () adiciona uma quebra de linha

#range
print(list (range(4)))

#range com o for

for numero in range(0, 11):
    print(numero, end=" ")

#exibindo a tabuada d0 5

for numero in range(0, 51, 5):
    print(numero, end=" ")

#while
opcao = -1

while opcao != 0:
    opcao = int(input("\n[1] Sacar \n[2] Extrato \n[0] Sair \n:"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
        print("Obrigado por utilizar o sistema bancário")
