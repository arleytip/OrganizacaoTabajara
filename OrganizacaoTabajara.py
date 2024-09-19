salario=int(input("Me diga seu salário: "))
#valor_porcentagem = 100 * (20 / 100)
#valor_porcentagem = 100 * 0.2
if salario <= 280:
    valor = salario * (20/100)
    print(
        salario, "o salario antes do reajuste;\n",
        "20% o percentual de aumento aplicado; \n",
        valor, "o valor do aumento;\n",
        salario + valor, " o novo salário, após aumento"
    )
elif salario <= 700:
    valor = salario * (15 / 100)
    print(
        salario, "o salario antes do reajuste;\n",
        "15% o percentual de aumento aplicado; \n",
        valor, "o valor do aumento;\n",
        salario + valor, " o novo salário, após aumento"
    )
elif salario <= 1500:
    valor = salario * (10 / 100)
    print(
        salario, "o salario antes do reajuste;\n",
        "10% o percentual de aumento aplicado; \n",
        valor, "o valor do aumento;\n",
        salario + valor, " o novo salário, após aumento"
    )
else:
    valor = salario * (5 / 100)
    print(
        salario, "o salario antes do reajuste;\n",
        "5% o percentual de aumento aplicado; \n",
        valor, "o valor do aumento;\n",
        salario + valor, " o novo salário, após aumento"
    )