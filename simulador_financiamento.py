nome_cliente = input("Qual o seu nome? ")
renda = int(input("Qual a sua renda? "))
parcela = int(input("Qual a parcela? "))

if renda * 0.30 >= parcela:
    print(f"Olá {nome_cliente}, seu financiamento foi aprovado!")
    print(f"Parcela: R$ {parcela:.2f} | Limite: R$ {renda * 0.30:.2f}")
else:
    print(f"Olá {nome_cliente}, seu financiamento foi reprovado.")
    print(f"Parcela: R$ {parcela:.2f} | Limite: R$ {renda * 0.30:.2f}")
