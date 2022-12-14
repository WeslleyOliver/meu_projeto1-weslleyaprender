codigo_compra = int(input("Digite o código de compra: "))

codigo_compra = 5111

if codigo_compra == 5222:
    print("compra a vista ")
elif codigo_compra == 5333:
    print("Compra parcelada")
elif codigo_compra == 5444:
    print("Compra no boleto")
else:
    print("Código não cadastrado")