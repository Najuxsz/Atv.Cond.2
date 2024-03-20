#Pedir a idade em anos, e o tempo de serviço em anos também, de um trabalhador
#Verificar se pode se aposentar ou não
#PODE SE APOSENTAR SE:
#Possui 65 anos ou mais
#Possui 30 anos de serviço ou mais
#Possui pelo menos 60 anos e pelo menos 25 anos de serviço.

print("")
nome = input("Olá, qual seu nome? ")
print("")

idade = int(input(f"{nome}, qual sua idade, em anos? "))
tempoServico = int(input(f"{nome}, qual seu tempo de serviço, em anos? "))

if idade >= 65:
    print("Você já pode se aposentar!!")

elif tempoServico >= 30:
    print("Você já pode se aposentar!")

elif idade >=60 and tempoServico >= 25:
    print("Você já pode se aposentar!")

else:
    print("Não pode se aposentar ainda!")
    

