#Pedir idade do usuário
#Se menor que 16 anos = não eleitor 
#Se entre 16 e 18 anos = eleitor facultativo
#Dos 18 aos 65 anos = eleitor obrigatório

print("")
nome = input("Olá, qual seu nome? ")
print("")

idade = int(input(f"{nome}, qual sua idade? "))

if idade < 16:
    print("Que pena, voce ainda não é eleitor!")

elif idade >= 16 and idade < 18:
    print("Oba, voce já é um eleitor facultativo!")

elif idade >= 18 and idade <= 65:
    print("Parabéns, voce é um eleitor obrigatório")

else:
    print("Show! Voce não precisa votar")
