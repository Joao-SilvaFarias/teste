n = int(input("Digite um número para calcular seu fatorial: "))

c = n
s = n

while c > 1:
    n *= (c-1)
    c -= 1

print(f"O número {s} fartorial é igual a {n}.")   
