#Ler a temperatura, em graus, (ºC)
#Se estiver abaixo de 15ºC, print "Está frio!!!"
#Se estiver acima de 25ºC, print "Está calor!!"
#Caso contrário, print "temperatura agradável!"

import re

print("Vamos ver como está o clima hoje")

temperatura_input = input("Como está a temperatura hoje (exemplo: 30°C)? ")

match = re.match(r'(\d+)(°C)', temperatura_input)

if match:
    temperatura = int(match.group(1))
    print(f"A temperatura de hoje é de {temperatura}°C")

    if temperatura > 25:
        print("Está calor!")

    elif temperatura < 15:
        print("Está frio!")

    else:
        print("Está uma temperatura agradável hoje!")

else:
    print("Por favor, forneça a temperatura no formato correto (por exemplo, 30°C).")
















