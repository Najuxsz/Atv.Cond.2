#Equação de segundo grau ax² + bx + c = 0
#Os valores do coeficientes são conhecidos e a =! 0
#Se a equação for positiva, duas raizes reais distintas 
#Se a aquação for nula, existem duas raízes iguais
#Se for negativo, existem duas raízes imáginarias conjulgadas.
#Descobrir valor de a, b, c, delta, x1 e x2
#Se o usuario colocar o valor de a = 0, a equação não é do segundo grau, e o programa deverá parar
#Se o delta for calculado negativo, não haverá raizes, encerre o programa
#Delta = b² - 4ac
#Raízes = (-b + ou - Raiz de delta)/2a
print("")
print("Vamos descobrir as raizes da equação de segundo grau")
print("")
a = float(input("Informe o valor de a: "))

if a != 0:
    b = float(input("Informe o valor de b: "))
    c = float(input("Informe o valor de c: "))

    delta = (b**2) - 4*a*c

    if delta < 0:
        print("O valor de delta é igual a %.1f e não possui raizes reais" %(delta))

    elif delta == 0:
        raiz = (-b + delta**0.5)/(2*a)
        print("O valor de delta é igual a %.1f e possui apenas uma raiz igual a %.1f" %(delta, raiz))
    else:
        raiz1 = (-b + delta**0.5)/(2*a)
        raiz2 = (-b - delta**0.5)/(2*a)
        print("O valor de delta é igual a %.1f" %(delta))
        print("Valor da raiz 1 = %.1f" %(raiz1))
        print("Valor da raiz 2 = %.1f" %(raiz2))

else:
    print("Não é uma equação de segundo grau")
    




