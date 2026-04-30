#String em python
#maiscula, minuscula e titulo

curso = "pYtHon"

print(curso.upper())

print(curso.lower())

print(curso.title())

#eliminando espaços em branco

curso = "   Python "

print(curso.strip())

print(curso.lstrip())

print(curso.rstrip())

#junções e centralização

curso = "Python"

print(curso.center(10, "#"))
#o 10 é a soma dos numeros da palavra + quantos caracteres vc quer colocar

print(".".join(curso))