#peça: usuário e senha; Condição: usuário correto: "admin" senha correta: "1234"; Mostre: "Acesso permitido" ou "Acesso negado"

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")