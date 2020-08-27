"""
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
  a. o produto do dobro do primeiro com metade do segundo .
  b. a soma do triplo do primeiro com o terceiro.
  c. o terceiro elevado ao cubo.
"""

int1 = int(input("Digite um número inteiro: "))
int2 = int(input("Digite outro número inteiro: "))
real = float(input("Agora digite um número real: "))

print("a:", (int1 * 2) * (int2 / 2))
print("b:", (int1 * 3) + real)
print("c:", real ** 3)
