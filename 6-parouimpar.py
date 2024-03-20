#Veja se o número é par ou ímpar
#Quando for par armazenar esse valor em P
#Quando for ímpar armazená-lo em I.
#Exibir o valor de P e de I ao final.

print("")
numero = float(input("Digite um número aqui: "))
print("")

if numero%2 == 0:
    float(input(f"O número inserido ({numero:.1f}) é par e está armazenado em P."))

else:
    float(input(f"O número inserido {numero:.1f} é ímpar e está armazenado em I."))


