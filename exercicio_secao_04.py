import math
from datetime import date


"1"
print("----" * 18)
print("\n", "Questão 01", "\n")
print("Informe um numero: ")
x = input()
print("O numero informado e: ", x)


"2"
print("\n", "----" * 18)
print("\n", "Questão 02", "\n")
print("Informe um numero: ")
x = input()
if (float(x) % 2) != 0:
    print("Numero informado não e primo")
else:
    print("O numero informado e: ", x, " primo")


"3"
print("\n", "----" * 18)
print("\n", "Questão 03", "\n")
soma = 0
for i in range(1, 4,1):
    print("Infome o ", i,"° numero: ")
    x = float(input())
    print("\n" * 2)
    soma = soma + x
print("A soma dos valores e igual a: ", soma, "\n")


"4"
print("\n", "----" * 18)
print("\n", "Questão 04", "\n")
print("Informe um numero:")
x = float(input())
print("")
print("O quadrado do numero", x, "e igual a", x**2)


"5"
print("\n", "----" * 18)
print("\n", "Questão 05", "\n")
print("Infermo um numero: ")
x = float(input())
print(x/5)


"6"
print("\n", "----" * 18)
print("\n", "Questão 06", "\n")
print("Informe a temperatura em °C: ")
x = float(input())
temp = x * (9.0/5.0) + 32.0
print("A conversão da temperatura", x,"°C em °F igual a", temp)


"7"
print("\n", "----" * 18)
print("\n", "Questão 07", "\n")
print("Informe a temperatura °F: ")
x = float(input())
temp = 5.0 * (x - 32.0) / 9.0
print("A temperatura",x,"°F em °C e igual a","%.2f" % temp,"°C")


"8"
print("\n", "----" * 18)
print("\n", "Questão 08", "\n")

print("Informe a temperatura °K: ")
x = float(input())
temp = x - 273.15
print("A temperatura", x, "°K em °C e igual a", temp, "°C")


"9"
print("\n", "----" * 18)
print("\n", "Questão 09", "\n")
print("Informe a temperatura em °C: ")
x = float(input())
temp = x + 273.15
print("A temperatura", x, "°C em °K e igual a", temp, "°K")


"10"
print("\n", "----" * 18)
print("\n", "Questão 10", "\n")
print("Informe a velocidade em Km/h : ")
x = float(input())
vel = x / 3.6
print("A velocidade", x," em M/s e igual a","%.2f" % vel,"m/s")



"11"
print("\n", "----" * 18)
print("\n", "Questão 11", "\n")
print("Informe a velocidade em M/s: ")
x = float(input())
vel = x * 3.6
print("A velocidade",x,"M/s em Km/s e igual a","%.2f" % vel,"Km/h")



"12"
print("\n", "----" * 18)
print("\n", "Questão 12", "\n")
print("Informe as milhas: ")
x = float(input())
dist = 1.61 * x
print("A distancia de",x," Milhas em Km e igual a",dist,"Km")


"13"
print("\n", "----" * 18)
print("\n", "Questão 13", "\n")
print("Informe a distancia em Km: ")
x = float(input())
dist = x / 1.61
print("A distancia de", x,"Km em Milhas e igual a","%.2f" % dist,"Milhas")


"14"
print("\n", "----" * 18)
print("\n", "Questão 14", "\n")
print("Informe o angulo em graus: ")
x = float(input())
angulo = x * 3.14 / 180
print("O radiano do angulo em grau",x,"° e igual a","%.4f" % angulo,"Rad")


"15"
print("\n", "----" * 18)
print("\n", "Questão 15", "\n")
print("Informe o angulo em Radiano: ")
x = float(input())
angulo = x * 180 / 3.14
print("O angulo em graus do radiano",x,"rad e igual a", "%.3f" % angulo,"°")


"16"
print("\n", "----" * 18)
print("\n", "Questão 16", "\n")
print("Informe o comprimento em polegadas: ")
x = float(input())
comp = x * 2.54
print("O comprimentao em cm das polegadas", x," e igual a", comp,"cm")



"17"
print("\n", "----" * 18)
print("\n", "Questão 17", "\n")
print("Informe o valor em cm: ")
x = float(input())
comp = x / 2.54
print("O comprimento em polegadas de", x,"cm e igual a","%.3f" % comp," Polegadas")


"18"
print("\n", "----" * 18)
print("\n", "Questão 18", "\n")
print("Informe o valor em M³: ")
x = float(input())
volume = 1000 * x
print("O volume de", x,"m³ em litros e igual a", volume,"L")


"19"
print("\n", "----" * 18)
print("\n", "Questão 19", "\n")
print("Informe o volume : ")
x = float(input())
volume = x / 1000
print("O volume", x,"L em m³ e igual a", volume,"m³")


"20"
print("\n", "----" * 18)
print("\n", "Questão 20", "\n")
print("Informe a massa em quilogramas: ")
x = float(input())
peso = x / 0.45
print("O quilograma ", x," convertigo em libras e igual a","%.2f" % peso," Libras" )


"21"
print("\n", "----" * 18)
print("\n", "Questão 21", "\n")
print("Informe a massa em libras:")
x = float(input())
peso = x * 0.45
print("O peso em quilogramas de",x,"Libras e igual a",peso,"Quilogramas.")


"22"
print("\n", "----" * 18)
print("\n", "Questão 22", "\n")
print("Informe as jardas :")
x = float(input())
distancia = 0.91 * x
print("O valor em metros das", x,"jardas e igual a", distancia," Metros.")



"23"
print("\n", "----" * 18)
print("\n", "Questão 23", "\n")
print("Informe os metros: ")
x = float(input())
distancia = x / 0.91
print("O valor em jardas dos", x," Metros e igual a",distancia," Jardas.")


"24"
print("\n", "----" * 18)
print("\n", "Questão 24", "\n")
print("Informe os m²: ")
x = float(input())
area = x * 0.000247
print("O valor em acres de ",x,"m² e igual a",area," Acres.")


"25"
print("\n", "----" * 18)
print("\n", "Questão 25", "\n")
print("Informe o valor em acres: ")
x = float(input())
area = x * 4048.58
print(f"A area {x}Acres em m² e igual a {area}m? ")


"26"
print("\n", "----" * 18)
print("\n", "Questão 26", "\n")
print("Informe os m²: ")
x = float(input())
area = x * 0.0001
print(f"A area {x}m² em hectares e igual a {area} Hectares")



"27"
print("\n", "----" * 18)
print("\n", "Questão 27", "\n")
print("Informe os hectares: ")
x = float(input())
area = x * 10000
print(f"A area {x} hectares em m² e igual a {area} m²")


"28"
print("\n", "----" * 18)
print("\n", "Questão 28", "\n")
cont = 0
for i in range(1,4,1):
    print("Informe a",i,"° Nota: ")
    nota = float(input())
    soma = nota * nota
    cont = cont + soma
print(cont)



"29"
print("\n", "----" * 18)
print("\n", "Questão 29", "\n")
notas = []
num = 0
for i in range(0,4,1):
    print("Informe a ",i+1,"° Nota:")
    num = float(input())
    notas.insert(i, num)
print(((sum(notas))/(len(notas))))


"30"
print("\n", "----" * 18)
print("\n", "Questão 30", "\n")
print("Informe o valor em R$: ", end=" ")
x = float(input())
print("Informe a cotação do dolar: ", end=" ")
y = float(input())
conv = y * x
print("O valor em dolares de R$", x,"e igual a U$","%.2f" % conv)


"31"
print("\n", "----" * 18)
print("\n", "Questão 31", "\n")
print("informe um numero inteiro:", end=" ")
x = int(input())
print(f"O antecessor de {x} e {x-1} e o seu sucessor e {x+1}")


"32"
print("\n", "----" * 18)
print("\n", "Questão 32", "\n")
print("Informe um numero inteiro: ", end=" ")
x = int(input())
rst = (((x * 3) + 1) + ((x * 2) - 1))
print("A soma de tudo e igual a :", rst)


"33"
print("\n", "----" * 18)
print("\n", "Questão 33", "\n")
print("Informe o lado do quadrado : ", end=" ")
x = float(input())
area = x * x
print("A area do quadrado informa e igual a", area)


"34"
print("\n", "----" * 18)
print("\n", "Questão 34", "\n")
print("Informe o raio do circulo : ", end=" ")
x = float(input())
area = 3.141592 * (x * x)
print("A area do circulo informa e igual a", area, " raio. ")


"35"
print("\n", "----" * 18)
print("\n", "Questão 35", "\n")
print("Informe o cateto A :", end=" ")
a = int(input())
print("Informe o cateto B :", end=" ")
b = int(input())
hipo = (a ** 2) + (b ** 2)
hipo = math.sqrt(hipo)
print(hipo)


"36"
print("\n", "----" * 18)
print("\n", "Questão 36", "\n")
print("Informe a atura do cinlindro: ", end="")
x = int(input()) #altura
print("Informe o raio do cilindro: ", end="")
y = int(input()) #raio
volume = 3.141592 * (y ** 2) * x
print(f"O volume do cilindro e igual a {volume:.2f} m³")


"37"
print("\n", "----" * 18)
print("\n", "Questão 37", "\n")
print("Informe o valor do produto: ", end=" ")
x = float(input())
valor = x - (x * 0.12)
print(f"O valor do produto R$ {x} com desconto de 12% e igual a R$ {valor:.2f}")


"38"
print("\n", "----" * 18)
print("\n", "Questão 38", "\n")
print("Informe o salário do funcionario a ser aumentado: ", end="")
x = float(input())
valor = x + ( x * 0.25 )
print(f"O valor do salário R$ {x} foi aumentado em 25% para R$ {valor:.2f}")


"39"
print("\n", "----" * 18)
print("\n", "Questão 39", "\n")
num = 780.000
print("Valor Inicial: R$", f"{num:.3f}")
print("O primeiro colocado, ganhou: R$", f"{(num * 0.46):.3f}")
print("O segundo colocado, ganhou: R$", f"{(num * 0.32):.3f}")
print("O terceiro colocado, ganhou: R$", f"{(num * 0.22):.3f}")


"40"
print("\n", "----" * 18)
print("\n", "Questão 40", "\n")
dias = int(input("Informe o numero de dias trabalhados: "))
slr = dias * (30 - (30 * 0.08))   #salario
print(f"A quantidade a ser paga e igual a R$ {slr:.2f}")


"41"
print("\n", "----" * 18)
print("\n", "Questão 41", "\n")
pag = float(input("Informe o valor da hora trabalhada em R$: ")) #pagamento
horas = float(input("\nInforme o numero de horas trabalhadas: "))
slr = (pag * horas)
ori = slr
slr = slr + (slr * 0.10)
print(f"\nCom base no R$ {pag} valor/hora e as {horas} Horas trabalhadas o valor a" +
      " ser pago e igual R% {slr}, ja com o acrecimo de 10% no valor originial R$ {ori}\n")


"42"
print("\n", "----" * 18)
print("\n", "Questão 42", "\n")
slr = float(input("Informe o salario-base do funcionario: R$ "))#salario
slr = (slr + (slr * 0.05)) - (slr * 0.07)
print(F"\nO salario-base final apos o calculo e igual a R$ {slr} \n")


"43"
print("\n", "----" * 18)
print("\n", "Questão 43", "\n")
total = float(input("Informe o valor total do produto: R$"))
v1 = total - (total * 0.10)# valor 1
v2 = total / 3  # valor 2
v3 = v1 * 0.05 # valor 3
v4 = total * 0.05
print(f"\n O valor total do produtoe R$ {total:.2f} com 10% de desconto fica R$ {v1}" +
      f"\n O valor da parcela em 3 vezes e de R$ {v2:.2f}" + 
      f"\n A comissão do vendedor caso a venda seja a vista e de R$ {v3}" +
      f"\n A comissão do vendedor caso a venda seja parcelada e de R$ {v4}")


"44"
print("\n", "----" * 18)
print("\n", "Questão 44", "\n")
altura = int(input("Informe a altura que deseja alcançar em metros: "))
degraus = int(input("\nInforme a altura dos dregaus em cm: "))
total = altura / (degraus / 100)
print(f"\nPara uma altura de {altura} Metros são necessarios {total:.1f} Passos para se alcançar o topo" +
      f" atraves de degraus com altura de {degraus} cm.")




"45"
print("\n", "----" * 18)
print("\n", "Questão 45", "\n")
letra = input(("Informe uma letra maiúscula: "))

maior = []
menor = []

for i in range(65, 91): # letras maisculas
    maior.append(chr(i))

for i in range(97, 123): # letras miniculas
    menor.append(chr(i))

if letra in maior:
    x = maior.index(letra)
    print(f"\nA letra '{letra}' maiuscula e igual a '{menor[x]}' minuscula.")
else:
    print(f"\nA letra '{letra}' nao e maiuscula.")



"46"
print("\n", "----" * 18)
print("\n", "Questão 46", "\n")
num = str(input("Informe um numero de 3 digitos (100 a 999): "))
if (int(num) >= 100):
    print(num[::-1])
else:
    print("Num invalido")


"47"
print("\n", "----" * 18)
print("\n", "Questão 47", "\n")
num = str(input("Informe um numero de 4 digitos (1000 a 9999) : "))
print("\n")
for i in range(len(num)):
    print(num[i])


"48"
print("\n", "----" * 18)
print("\n", "Questão 48", "\n")
sec = int(input(("Informe o valor em segundos: ")))
horas = sec / 3600
minutos = sec / 60
secundos = sec % 60
print(f"Apos a conversão de {sec} segundo(s) o tempo e de {horas:.2f} Horas," +
      f" {minutos:.2f} Minutos e {secundos:.2f} Segundos")


"49"
print("\n", "----" * 18)
print("\n", "Questão 49", "\n")
horas = int(input("\nInforme a Hora de inicio: "))
minutos = int(input("\nInforme os Minutos de inicio: "))
segundos = int(input("\nInforme os Segundos de inicio: "))
dura = int(input("\nInforme A duração do experimento em segundos: "))
if ((dura // 360) >= 0):
    horaNew = horas + (dura // 3600)

if (((dura // 60) //  60) >= 0):
    minNew = minutos + (((dura // 60) //  60) - 1)

segNew = dura % 60
print(f"\nO experimento teve inicio as {horas} Horas, {minutos} Minutos e " +
      f"{segundos} Segundos com duração de {dura} segundos")
print(f"\nO experimento terminou as {horaNew:.2f} Horas, " +
      f"{minNew:.2f} Minutos e {segNew:.2f} Segundos.")


"50"
print("\n", "----" * 18)
print("\n", "Questão 50", "\n")
hoje = date.today()
ano = hoje.strftime("%Y")
idade = int(input("Informe sua idade atual: "))
rst = int(ano) - idade#resultado
print(rst)


"51"
print("\n", "----" * 18)
print("\n", "Questão 51", "\n")
x1 = float(input("Informe a distancia X - 1: "))
x2 = float(input("Informe a distancia X - 2: "))

y1 = float(input("Informe a distancia y - 1: "))
y2 = float(input("Informe a distancia y - 2: "))

distancia = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
print(f"\n A distancia da Origem (0,0) entre os pontos X ({x1}, {x2}) e Y ({y1}, {y2}) e {distancia:.2f}")


"52"
print("\n", "----" * 18)
print("\n", "Questão 52", "\n")
ap1 = float(input("Informe quanto deseja apostar 1°: ")) #apostador 1
ap2 = float(input("\nInforme quanto deseja apostar 2³: ")) #apostador 2
ap3 = float(input("\nInforme quanto deseja apostar 3°: ")) #apostador 3

vt = ap1 + ap2 + ap3 # valor total
v3 = round(vt / 7, 2) # vencedor 3
v2 = round(v3 * 2, 2) # vencedor 2
v1 = (round(v3 * 4, 2) - 0.01) # vencedor 1

print(f"\n\n O valor total apostado e {vt:.2f} \n\n O 1° lugar ganhou {v1:.2f} " +
      f"\n\n O 2° lugar ganhou {v2:.2f} \n\n O 3° lugar ganhou {v3:.2f}")


"53"
print("\n", "----" * 18)
print("\n", "Questão 53", "\n")
c = int(input("Informe o comprimento do terreno em metros: "))
l = int(input("\nInforme o largura do terreno metros: "))
p = float(input("\nInforme o preço do metro de tela: "))
valor =  (c * l) * p
print(f"\nO terremo mede {c * l} m² e o preço do metro de tela e {p:.2f} o valor" +
      f" total e igual a {valor:.2f}")

