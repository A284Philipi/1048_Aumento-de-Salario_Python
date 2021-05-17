salario_antigo = float(input())
if salario_antigo > 2000:
    reajuste = float(salario_antigo * 0.04)
    salario_novo = float(salario_antigo + reajuste)
    percentual = int(4)
elif salario_antigo > 1200:
    reajuste = float(salario_antigo * 0.07)
    salario_novo = float(salario_antigo + reajuste)
    percentual = int(7)
elif salario_antigo > 800:
    reajuste = float(salario_antigo * 0.1)
    salario_novo = float(salario_antigo + reajuste)
    percentual = int(10)
elif salario_antigo > 400:
    reajuste = float(salario_antigo * 0.12)
    salario_novo = float(salario_antigo + reajuste)
    percentual = int(12)
else:
    reajuste = float(salario_antigo * 0.15)
    salario_novo = float(salario_antigo + reajuste)
    percentual = int(15)
print("Novo salario: %.2f"%(salario_novo))
print("Reajuste ganho: %.2f"%(reajuste))
print("Em percentual: {} %".format(percentual))