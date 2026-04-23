#receba valor da compra: acima de 100 → 10% de desconto; caso contrário → sem desconto; Mostre valor final.

compra = float(input("Digite o valor da compra: "))

if compra > 100:
    desconto = compra * 0.10
    valor_final = compra - desconto
    print("Você recebeu um desconto de 10%: ")
    print("Valor final: ", valor_final)
else:
    print("Compra sem desconto")
    print("Valor final: ", compra)