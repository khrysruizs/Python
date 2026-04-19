# tipo de dados

print(11 + 10)
print(1.5 + 2)
print(True)
print(False)
print("Python")

int()
float()
str()
bool()

#variaveis

#podem ser criadas dos dois jeitos
age = 21
name = 'Khrys'
print(f'Meu nome é {name} e eu tenho {age} anos de idade')

age, name = (23, 'Khrys')
print(f'Meu nome é {name} e eu tenho {age} anos de idade')

#variável com letras maiuscula = constante

#guarda caminha absoluto, flag(ligado,desligado), lista de estados, valor numerico
ABS_PATH = 'https://docs.google.com/document/d/1PdsfZbzAM2DVp2RfkXlyn_v4jbK65nk_OTr42zlDmBs/edit?usp=sharing'
DEBUG = True
STATES = [
    'RJ',
    'SP',
    'MG',
]
AMOUNT = 30.2

nome = 'João'
idade = 21

print(nome, idade)

taxa_juros = 15

print(f'a taxa de juros é de {taxa_juros}%')

#Converter tipos de variáveis
#int pra float
preco = 10
print(preco)

preco = float(preco)
print (preco)

preco = 10 / 2
print(preco)

#float pra int
preco = 10.30
print(preco)

preco = int(preco)
print (preco)

#conveter por divisão
preco = 10
print(preco)

print(preco / 2)

print(preco // 2) #duas barras preserva numero inteiro

#numérico pra string
preco = 10.50
idade = 28

print(str(preco))

print(str(idade))

texto = f"idade {idade} preco {preco}"
print(texto)

#string para número
preco = "10.50"
idade = "28"

print(float(preco))

print(int(idade))

#entrada e saida
#input
nome = input("Informe o seu nome: ")
#print
nome = "Khrys"
sobrenome = "Ruiz"
#sep separa e end termina
print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="!")