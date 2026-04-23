#Uma senha é válida se: tem pelo menos 8 caracteres, contém a letra "@", não contém espaço

senha = input("Digite uma senha: ")

#len() é uma função do python que mostra quantos caracteres (ou itens) algo tem
if len(senha) >= 8 and "@" in senha and " " not in senha:
    print("Senha válida")
else:
    print("Senha inválida")    
