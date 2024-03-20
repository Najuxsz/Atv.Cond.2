#Duas notas bimestrais de um estudante
#Código da faculdade, 1 ou 2
#--------1 para PUCPR ----- 2 para UNICAMP

print("")
nome = input("Olá, qual seu nome? ")
print("")

codigo = int(input(f"{nome}, digite seu codigo aqui: "))

if codigo == 1:
    print("Você estuda na PUCPR!!")
elif codigo == 2:
    print("Você estuda na UNICAMP!!")
else:
    print("ERRO!")

#Agora que sabemos onde ele estuda, vamos descobrir sua media.

print("")
media = float(input("Coloque sua média aqui: "))
print("")

if codigo == 1 and media >=7:
    print("Você está aprovado!")
elif codigo == 1 and media >= 4 and media < 7:
    print("Você está no exame final!")
elif codigo == 1 and media < 4:
    print("REPROVADO!")

#Caso o estudante seja da UNICAMP:
    
if codigo == 2 and media >= 5:
    print("Você está aprovado!")
elif codigo == 2 and media < 5:
    print("Em exame!")
elif codigo != 1:
    print("Erro!!")

