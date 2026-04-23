#receba: nota (0 a 10) e frequência (%); Regras: aprovado: nota ≥ 7 e frequência ≥ 75; recuperação: nota ≥ 5 e < 7; reprovado: resto

nota = int(input("Digite a nota do aluno: "))
frequencia = int(input("Digite a frequência do aluno: "))

if nota >= 7 and frequencia >= 75:
    print("Aluno aprovado")
elif nota >= 5 and nota < 7:
    print("Aluno de recuperação")
else:
    print("Aluno reprovado")