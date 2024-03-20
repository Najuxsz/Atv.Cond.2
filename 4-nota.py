#Ler a nota do estudante
#Se a nota for igual ou acima de 7, informar "aprovado"
#Se a nota estiver entre 4 e menor que 7, informar "recuperação"
#Se estiver abaixo de 4, informar "reprovado"

print("")
notaEstudante = float(input("Digite sua nota aqui: "))
print("")
if notaEstudante >= 7:
    print("Você está aprovado!")

elif notaEstudante >= 4 and notaEstudante < 7:
    print("Você ficou em recuperação!!")
    diferenca = 7-notaEstudante
    print(f"Você ficou em recuperação por {diferenca:.1f} pontos. ")

else:
    print("Você está reprovado!")



