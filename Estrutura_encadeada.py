from importlib import find_loader


valor = input("Digite um valor")
valor = float(valor)

if valor <=1830.29:
    valor -=valor*0.08
elif valor <=3050.52:
    valor -=valor*0.09
elif valor <=6101.06:
    valor -= valor*0.11

print(f"Valor desconto {valor}")