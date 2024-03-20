#Dados de entrada: Altura e sexo do usuario
#Calcule o peso ideal
#Para homens: (72.7*h) – 58
#Para mulheres: (62.1*h)-44.7 
#(sendo h = altura)

sexoUsuario = input("Digite seu sexo aqui, com letra maiuscula: ")
alturaUsuario = float(input("Qual sua altura? "))

mulher = (62.1*alturaUsuario)-44.7
homem = (72.7*alturaUsuario) - 58 

if sexoUsuario == ("Mulher"):
    mulher = float(mulher)
    print(f"Seu peso ideal é {mulher:.1f} kg")

elif sexoUsuario == ("Homem"):
    homem = float(homem)
    print(f"Seu peso ideal é {homem:.1f} kg")

else:
    print("Erro")


