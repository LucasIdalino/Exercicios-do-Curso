soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        contador += 1
print(f"Ao todo, {contador} números são múltiplos de 3. A soma de todos é {soma}.")
