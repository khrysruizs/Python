#operadores aritmeticos
produto1 = 12
produto2 = 3

print(produto1 + produto2)

print(produto1 - produto2)

print(produto1 * produto2)

print(produto1 / produto2)

#divisão inteira
print(12 // 2)

#modulo(resto da divisão)
print(10 % 3)

#exponenciação
print(2 ** 3)

#precedência de operadores:
print(10 / 2 * 4)

print((10 - 5) * 2)

x = (10 + 5) * 4
y = (10 / 2) + 25 * ((2 - 2) ** 2)
print(x)
print(y)

#operadores de comparação
saldo = 450
saque = 200

print(saldo == saque)

print(saldo != saque)

print(saldo > saque)

print(saldo >= saque)

print(saldo < saque)

print(saldo <= saque)

#operadores de atribuição

#simples
saldo = 500
print(saldo)

#atribuição com adição
saldo += 200
print(saldo)

#atribuição com subtração
saldo = 500
saldo -= 200
print(saldo) 

#atribuição com multiplicação
saldo = 500
saldo *= 2
print(saldo) 

#atribuição com divisão
saldo = 500
saldo /= 5
print(saldo)

saldo = 500
saldo //= 5
print(saldo)

#também pode ser feito com módulo e exponenciação

#operadores lógicos
saldo = 1000
saque = 200
limite = 100

#operador E: os dois precisam ser verdadeiros
print(True and True)
print(True and False)


print(saldo >= saque and saque <= limite)

print(saldo >= saque and saque >= limite)

#operador OU: pelo menos um precisa ser verdadeiro
print(True or False)
print(False or False)

print(saldo >= saque or saque <= limite)

#operador negação: inverso da verdade
print(1000 > 1500)

print(not 1000 > 1500)

#parênteses pra organizar 
saldo = 1000
saque = 250
limite = 200
conta_especial = True

print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))

#operadores de identidade
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)

print(curso is not nome_curso)

print(saldo is limite)

#operadores de associação
curso = "Curso de Python"
frutas = ["laranja", "uva", "maçã"]
saques = [1500, 100]

print("Python" in curso)

print("Limão" not in frutas)

print(200 in saques)