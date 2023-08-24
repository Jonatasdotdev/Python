valor_hora=float (input("digite o valor recebido por hora: "))
horas_trabalhadas=int (input("digite a quantidade de horas trabalhadas no mês: "))

salario_bruto= valor_hora * horas_trabalhadas
fgts= salario_bruto * 0.11
if salario_bruto <= 900:
  ir = 0
elif salario_bruto <= 1500:
  ir = salario_bruto * 5/ 100
elif salario_bruto <= 2500:
  ir = salario_bruto * 10 / 100
else:
  ir = salario_bruto * 20 / 100

inss= salario_bruto * 10 / 100
sind= salario_bruto * 3 / 100

total_descontos = ir + inss + sind
salario_liquido = salario_bruto - total_descontos

print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas}): R$ {salario_bruto:.2f}")
print(f"(-) IR ({ir*100/salario_bruto:.0f}%): R$ {ir:.2f}")
print(f"(-) INSS ({inss*100/salario_bruto:.0f}%): R$ {inss:.2f}")
print(f"(-) Sindicato ({sind*100/salario_bruto:.0f}%): R$ {sind:.2f}")
print(f"FGTS (11%): R$ {fgts:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
