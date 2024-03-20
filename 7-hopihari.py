#ver se um visitante do Hopi Hari está liberado ou proibido de andar na montanha russa do parque.
#com base na idade (em anos) e no peso (em kg) informados pelo usuário
#Liberado= maior de 15 anos e não pesar mais que 120kgs.

print("")
nome = input("Olá, qual seu nome? ")
print("")
print(f"{nome}, vamos verificar se voce pode andar na montanha russa!")

idade = int(input("Digite sua idade aqui, em anos: "))
peso = float(input("Digite seu peso aqui, em kgs: "))

if idade > 15 and peso < 120:
    print("Liberado!!")

else:
    print("Voce não pode andar na montanha russa")

