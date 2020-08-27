# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganhosHora = float(input("Quanto você ganha por hora? "))
horasMes = int(input("Quantas horas você trabalha por mês? "))
salario = ganhosHora * horasMes

print("Seu salário mensal é R$", salario)
