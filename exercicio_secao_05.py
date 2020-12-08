'''


Beware of the WHILE TRUE theres no break's for them.
Cuidado com os WHILE TRUE não há break para eles.


'''

import math
import random

def MMC(n1, n2, n3):  # MMC de 3 numeros
    v1 = [] # valor 1 n1
    v2 = [] # valor 2 n2
    v3 = [] # valor 3 n3
    cont = 1 # contador / multiplicador
    rst = 0 # resultado
    
    while cont < 20: # impedir loop infinito
        v1.append((n1 * cont)) # lista de multiplos 1
        v2.append((n2 * cont)) # lista de multiplos 2
        v3.append((n3 * cont)) # lista de multiplos 3


        if (n1 > n2 and n1 > n3):  # se valor 1 for o maior
            for i in range(len(v1)): # itinera a lista 
                if (v1[i] in v2 and v1[i] in v3): # busca se o valor ja nao existe nas outras listas
                    rst = v1[i] # resultado recebe o valor em comum
                    return rst # retorna o resultado
                

        elif (n2 > n1 and n2 > n3): # se valor 2 for maior
            for i in range(len(v2)): # itinera a lista
                if (v2[i] in v1 and v2[i] in v3): # busca se o valor ja nao existe nas outras listas
                    rst = v2[i] # recebe o valor em comum
                    return rst # retorna o resultado
                

        elif (n3 > n1 and n3 > n2): # se valor 3 for maior
            for i in range(len(v3)): # itinera a lista
                if (v3[i] in v2 and v3[i] in v1): # busca se o valor ja nao existe nas outras listas
                    rst = v3[i] # recebe o valor em comum
                    return rst # retorna o resultado
                 

        cont = cont + 1  # contador recebe +1
    



"1"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 01\n" + "\n\n")
num1 = float(input("Informe o 1° numero: "))
num2 = float(input("\nInforme o 2° numero: "))

if ( num1 > num2 ):
    print("\nO 1° numero ", num1," e maior que o 2° numero ", num2, ".\n")
else:
    print("\nO 2° numero ", num2," e maior que o 1° numero ", num1, ".\n")



"2"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 02\n" + "\n\n")
num = float(input("Informe o numero: "))

if ( num >= 0):
    print(f"O numero positivo informado e {num} com raiz quadrado de {num ** 0.5}.")
else:
    print(f"O numero {num} e invalido.")



"3"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 03\n" + "\n\n")

num = input("Informe o numero: ")
try: 
    num = float(num)
    if ( num >= 0):
        print(f"\nA raiz quadrada de {num} e {num ** 0.5}")
    else:
        print("\nO quadrado do {} e {}".format(num, (num ** 2)))
except:
    print(f"Informe um numero não '{num}'.")
finally:
    pass


"4"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 04\n" + "\n\n")

num = float(input("Informe um numero: "))
if (num >= 0):
    print("\nO numero digitado {} ao quadrado e {}.".format(num, (num * num)))
    print("\nA raiz quadrada do {} e {}.".format(num, (num * num)))


"5"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 05\n" + "\n\n")

num = float(input("Informe um numero: "))
if ((num % 2) == 0):
    print("\n{} e par.".format(num))
else:
    print("\n{} e impar.".format(num))


"6"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 06\n" + "\n\n")

num1 = float(input("Informe o 1³ numero: "))
num2 = float(input("\nInforme o 2³ numero: "))

if (num1 > num2):
    print("\n{} e maior que {} tendo uma diferença de {}.".format(num1, num2, (num1 - num2)))
else:
    print("\n{} e maior que {} tendo uma diferença de {}.".format(num2, num1, (num2 - num1)))


"7"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 07\n" + "\n\n")
num1 = float(input("Informe o 1³ numero: "))
num2 = float(input("\nInforme o 2³ numero: "))

if (num1 > num2):
    print("\n{} e maior que {} tendo uma diferença de {}.".format(num1, num2, (num1 - num2)))
elif (num1 == num2):
    print("\n\n {} e igual a {}".format(num1, num2))
else:
    print("\n{} e maior que {} tendo uma diferença de {}.".format(num2, num1, (num2 - num1)))


"8"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 08\n" + "\n\n")
while True:
    print("\nProgama Iniciado com sucesso.....\n")
    while True:
        try:
            num1 = input("\nInforme a 1° nota: ")
            num1 = float(num1)

            if (num1 <= 10 and num1 >= 0):
                print("\n 1° Nota: ",num1)
                break
            else:
                raise ValueError

        except ValueError:
            print(f"\n'{num1}' e invalido")


    while True:
        try:
            num2 = input("\nInforme a 2° nota: ")
            num2 = float(num2)

            if (num2 <= 10 and num2 >= 0):
                print("\n 2° Nota: ",num2)
                break
            else:
                raise ValueError

        except ValueError:
            print(f"\n'{num2}' e invalido")

    print(f"\n\nA media do aluno e {(num1 + num2)/2}\n\n")
    op = input("Deseja repetir? Y / N\n")
    if ( op == "Y" or op == "y"):
        pass
    else:
        break
     

"9"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 09\n" + "\n\n")

num1 = float(input("Informe o salario: "))
num2 = float(input("\nInforme o valor da prestação: "))
v1 = num1 * 0.20
if (num2 < v1):
    print("\nEmpréstimo concedido.")
else:
    print("\nEmpréstimo não concedido.")



"10"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 10\n" + "\n\n")

genero = input("Informe o genero:  M / F  - ")
altura = float(input("\nInforme a altura da pessoa: "))
if (genero == "M" or genero == "m"):
    m = ( 72.7 * altura ) - 58
    print(f"\nO peso ideal para ele e de {m:.2f} Kg")
else:
    f = ( 62.1 * altura ) - 44.7
    print(f"\nO peso ideal para ela e de {f:.2f} Kg")


"10"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 10\n" + "\n\n")

num = input(" Informe um numero maior que zero: ")
soma = 0
try:
    num = str(num)
    for i in range(len(num)):
        soma = int(num[i]) + soma
    print("\n A soma dos digitos do numero {} e {}.".format(num, soma))

except ValueError:
    print("\n'", num, "' e invalido.")

 
"11"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 11\n" + "\n\n")

num = int(input("Informe um numero: "))

if (num > 0):
    print(math.log(num))
else:
    print("Numero invalido")


"12"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 12\n" + "\n\n")

num = int(input("Informe um numero: "))
if (num > 0):
    print("NUmero possitivo".format(num))
else:
    print("Numero Inválido.")


"13"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 13\n" + "\n\n")

n1 = float(input("Informe a 1° nota: ")) * 1
n2 = float(input("Informe a 2° nota: ")) * 2
n3 = float(input("Informe a 3° nota: ")) * 3

mp = ( n1 + n2 + n3 ) / (1 + 1 + 2) #media ponderada

if (mp >= 60):
    print(f"Aluno aprovado com media {mp}")
else:
    print(f"Aluno reprovado com media {mp}")



"14"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 14\n" + "\n\n")

notas = []
pesos = [2, 3, 5]

while True:

    try: # nota 1
        for i in range(1, 4):
            
            nota = float(input(f"\nInforme a {i}° nota: "))

            if ( ( nota <= 10 ) and ( nota >= 0 ) ):
                notas.append(nota * pesos[i - 1])
                
            else:
                raise ValueError
        mp = sum(notas) / sum(pesos)

        if (mp <= 2.9 and mp >= 0):
            print("\nReprovado")
        elif (mp >= 3 and mp <= 4.9):
            print("\nRecuperação")
        else:
            print("\nAprovado")

        break
        
    except ValueError:
        print("Valor invalido.")



"15"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 15\n" + "\n\n")

dia = str(input("Informe o dia, numero, da semana:"))

if (dia == "1"):
    print("\nHoje e domingo!")

elif (dia == "2"):
    print("\nHoje e segunda!")
    
elif (dia == "3"):
    print("\nHoje e terça-feira!")
    
elif (dia == "4"):
    print("\nHoje e quarta-feira!")
    
elif (dia == "5"):
    print("\nHoje e quinta-feira!")
    
elif (dia == "6"):
    print("\nHoje e sexta-feira!")
    
elif (dia == "7"):
    print("\nHoje e sabado!")

else:
    print("\nNenhum dia encontrado :(")




"16"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 16\n" + "\n\n")

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto",
         "Setembro", "Outubro", "Novembro", "Dezembro"]

mes = int(input("Informe o numero do mes: "))

if (mes <= 12 and mes >= 1):
    print(f"\nO mes de numero {mes} e {meses[mes - 1]}")
else:
    print("\nNumero Invalido.")


"17"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 17\n" + "\n\n")

while True:
    
    try:
        bMaior = float(input("\nInforme a Base maior: "))

        if (bMaior < 0):
            print("\nBase Maior Invalida")
            
        else:
            
            bMenor = float(input("\nInforme a Base menor: "))

            if (bMenor < 0):
                print("\nBase Menor Invalida")
                
            else:
                altura = float(input("\nInforme a altura: "))
                area =  (bMaior + bMenor) * altura  / 2
                print(f"\nA área do trapezio e igual a {area}")
                break
            
    except ValueError:
        print("\nValor Invalido.")



"18"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 18\n" + "\n\n")

op = ("+", "-", "*", "/", "%")

opd = input("Informe a operação: '+' -l- '-' -l- '*' -l- '/'  -l- % \n") # operador

if (opd == op[0]):
    n1 = float(input("Informe o 1° numero: "))
    n2 = float(input("Informe o 2° numero: "))
    print(f"\nA soma de {n1} mais {n2} e {n1 + n2}.")
    
elif (opd == op[1]):
    n1 = float(input("Informe o 1° numero: "))
    n2 = float(input("Informe o 2° numero: "))
    print(f"\nA subtração de {n1} menos {n2} e {n1 - n2}.")
    
elif (opd == op[2]):
    n1 = float(input("Informe o 1° numero: "))
    n2 = float(input("Informe o 2° numero: "))
    print(f"\nA multiplicação de {n1} por {n2} e {n1 * n2}.")
    
elif (opd == op[3]):
    n1 = float(input("Informe o 1° numero: "))
    n2 = float(input("Informe o 2° numero: "))
    print(f"\nA divisao de {n1} por {n2} e {n1 / n2}.")

else:
    n1 = float(input("Informe o 1° numero: "))
    n2 = float(input("Informe o 2° numero: "))
    print(f"\nO módulo da divisao de {n1} por {n2} e {n1 % n2}.")



"19"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 19\n" + "\n\n")

num = int(input("\nInforme um numero: "))
if ( (num % 2 == 0) or (num % 3 == 0) ):
    
    if ( (num % 2 == 0) and (num % 3 > 0) ):
        print(f"{num} e divisel por 2 mas não 3.")
        
    elif ( (num / 2 > 0) and (num % 3 == 0) ):
        print(f"{num} e divisel por 3 mas não 2.")



"20"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 20\n" + "\n\n")
lados = []
m1 = 0 # menor 1
m2 = 0 # menor 2
for i in range(3):
    lado = int(input(f"Informe o {i+1}° lado: "))
    lados.append(lado)

m1 = min(lados)

for i in range(3):
    v = lados[i]
    if (v > m1 and v < max(lados)):
        m2 = v

if ( (m1 + m2) > (max(lados))):
    if (lados[0] == lados[1] == lados[2]):
        print("\nTriangulo Equilatero\n")
        
    elif (lados[0] != lados[1] != lados[2]):
        print("\nTriangulo Escaleno\n")

    else:
        print("\nTriangulo Isósceles\n")

else:
    print("\nOs valores informados não são triangulos\n")
lados = []



"21"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 21\n" + "\n\n")

while True:
    print(" Escolha a opção: \n" +
          "  1 - Soma de Números \n" +
          "  2 - Diferença entre 2 números (maior pelo menor) \n" +
          "  3 - Produto entre 2 números. \n" +
          "  4 - Divisão entre 2 números (o demonidor não pode ser zero).\n")

    op = input("\n OPção: ")
    if (op == "1"):
        n1 = float(input("\nInforme o 1° numero: "))
        n2 = float(input("Informe o 2° numero: "))
        print(f"\nA soma e igual a {n1 + n2}\n")

    elif (op == "2"):
        n1 = float(input("\nInforme o 1° numero: "))
        n2 = float(input("Informe o 2° numero: "))
        if (n1 > n2):
            print(f"\nA diferença e de {n1 - n2} numeros\n")
        else:
            print(f"\nA diferença e de {n2 - n1} numeros\n")

    elif (op == "3"):
        n1 = float(input("\nInforme o 1° numero: "))
        n2 = float(input("Informe o 2° numero: "))
        print(f"\nO produto e igual a {n1 * n2}\n")

    elif (op == "4"):
        n1 = float(input("\nInforme o 1° numero: "))
        n2 = float(input("Informe o 2° numero: "))
        print(f"\nO produto e igual a {n1 / n2}\n")

    else:
        print("\nOperação invalida\n")
        print("\nDeseja Continuar? Y / N")
        opt = input()
        if (opt == "Y" or opt == "y"):
            pass
            print("\n")
        else:
            break


"22"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 22\n" + "\n\n")

idade = int(input(" Informe a idade do trabalhador: "))
tempo = int(input(" Informe o tempo de serviço: "))

if (idade >= 65):
    print("\n Pode se aposentar.")
    
elif (tempo >= 30):
    print("\n Pode se aposentar.")
    
elif (idade >= 60 and tempo >= 25):
    print("\n Pode se aposentar.")
    
else:
    print("\n Não pode se aposentar.\n")



"23"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 23\n" + "\n\n")

ano = int(input("\nInforme o ano: "))

if ( (ano % 4 == 0) or (ano % 400 == 0) and (ano / 100) > 0):
    print(f"{ano} e bissexsto.")
    
else:
    print(f"{ano} não e bissexto.")



"24"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 24\n" + "\n\n")

while True:
    valor = float(input(" Informe o valor do produto: "))
    estado = input("\nInforme o estado: \n 1. MG \n 2. SP \n 3. RJ \n 4. MS \n Escolha: ")
        
    if (estado == "1"):
        pf = valor + (valor * 0.07) # preço final
        print(f"\n O valor final do produto em em MG e de {pf}\n")
        
    elif (estado == "2"):
        pf = valor + (valor * 0.12) 
        print(f"\n O valor final do produto em em SP e de {pf}\n")
        
    elif (estado == "3"):
        pf = valor + (valor * 0.15) 
        print(f"\n O valor final do produto em em RJ e de {pf}\n")
        
    elif (estado == "4"):
        pf = valor + (valor * 0.08)
        print(f"\n O valor final do produto em em MS e de {pf}\n")
        
    else:
        print("\n Estado Invalida. \n")



"25"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 25\n" + "\n\n")

valores = []
letras = ["A", "B", "C"]

while True:

    try:
        for i in range(3):
            print("Informe o valor de", letras[i],": ", end="")
            valor = int(input())
            valores.append(valor)
            
        if (valores[0] == 0):
            print("\nNão existe equação do segundo grau.\n")
            
        else:
            delta = (valores[1] ** 2) - (4 * valores[0] * valores[2])

            if (delta < 0):
                print("\nNão existe raiz.\n")

            elif (delta == 0):
                x = ( - valores[1] ) + (math.sqrt(delta)) / (2 * valores[0])

                print("\nExiste uma Raiz Única.\n X¹ = {}\n".format(x))
                
            else:
                x =  (- (valores[1]) + (math.sqrt(delta))) / (2 * valores[0])
                y =  (- (valores[1]) - (math.sqrt(delta))) / (2 * valores[0])

                print(f"\n X¹ = {x} \n X² = {y}\n")
                
        valores = []
        
    except ValueError:
        print("valor Invalido.")
        break



"26"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 26\n" + "\n\n")

km = float(input("Informe a distancia: "))
litros = float(input("Informe a gasolina consumida: "))

consumo = km / litros

if (consumo <= 8):
    print(f"Consumo menor que 8, {consumo}, Venda o carro!")

elif (consumo < 14 and consumo > 8):
    print(f"Consumo menor entre 8 e 14, {consumo}, Econômico!")

elif (consumo > 12):
    print(f"Consumo maior que 12, {consumo}, Super Econômico!")



"27"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 27\n" + "\n\n")

cat = ("Infantil A", "Infantil B", "Juvenil A", "Juvenil B", "Sênior") # categorias

idade = int(input("\n Informe a idade:"))

if (idade >= 5 and idade <= 7):
    print(f" Categoria: {cat[0]}")

elif (idade >= 8 and idade <= 10):
    print(f" Categoria: {cat[1]}")

elif (idade >= 11 and idade <= 13):
    print(f" Categoria: {cat[2]}")

elif (idade >= 14 and idade <= 17):
    print(f" Categoria: {cat[3]}")

elif (idade >= 18):
    print(f" Categoria: {cat[4]}")

else:
    print("Idade invalida")




"28"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 28\n" + "\n\n")

try:
    num1 = int(input("1° numero: "))
    num2 = int(input("2° numero: "))
    num3 = int(input("3° numero: "))

    op = input("\n\n Informe a opção: \n 1. Geométrica \n 2. Ponderado \n 3. Harmônica \n 4. Aritmética \n Escolha: ")

    if (op == "1"):
        valor = math.sqrt(num1 * num2 * num3)
        print("\n A Media Geometrica vale: ", valor, "\n")
            
    elif (op == "2"):
        valor = ((num1 + 2) * (num2 + 3) * num3) / 6
        print("\n A Media Ponderada vale: ", valor,"\n")
        
    elif (op == "3"):
        mmc = MMC(num1, num2,num3)
        valor = (mmc * 1 )/ ( 1 + 1 + 1 )
        print("\n A Media Harmônica vale: ", valor,"\n")
        
    elif (op == "4"):
        valor = num1 + num2 + num3
        print("\n A media Aritmética vale; ",valor,"\n")
    else:
        print("\n Opção Invalida. \n")
        
except ValueError:
    print("\n Valor Invalido. \n")



"29"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 29\n" + "\n\n")

cont = 0
num1 = []
num2 = []
resposta = []
rsp = 0 #resposta
acertos = 0
while cont < 5: 
    a = random.randrange(0, 100)
    b = random.randrange(0, 100)

    if  (a == b) :
        a = random.randrange(0, 100)

    else:
        cont = cont + 1
        num1.append(a)
        num2.append(b)
        print(f"{cont}° Qual a soma de {a} + {b} ?")
        rsp = int(input("R : "))
        resposta.append(rsp)
        print("\n")

        
print("\n Respostas: \n")
for i in range(5):
    if (resposta[i] == (num1[i] + num2[i])):
        acertos = acertos +1
    print(f"\n Qual a soma de {num1[i]} + {num2[i]} ? \n Resposta: {num1[i] + num2[i]}")
print(f"\n Numero de questões acertadas: {acertos}\n")



"30"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 30\n" + "\n\n")

ordem = []
for i in range(3):
    x = input(f"informe o {i+1}° valor: ")
    ordem.append(float(x))

ordem.sort()
print(ordem)


"31"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 31\n" + "\n\n")

h = float(input("Informe a altura: "))# altura
w = float(input("Informe o peso: "))# peso

if (h <= 1.20):
    if (w <= 60):
        print("\n A \n")
        
    elif (w > 60 and w <= 90):
        print("\n D \n")

    elif (w > 90):
        print("\n G \n")

elif (h > 1.20 and h <= 1.70):
    if (w <= 60):
        print("\n B \n")
        
    elif (w > 60 and w <= 90):
        print("\n E \n")

    elif (w > 90):
        print("\n H \n")

elif (w > 1.7):
    if (w <= 60):
        print("\n C \n")
        
    elif (w > 60 and w <= 90):
        print("\n F \n")

    elif (w > 90):
        print("\n I \n")



"32"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 32\n" + "\n\n")

cod = int(input("\nInforme o codigo do produto: "))
qtn = int(input("Informe a quantidade: "))

produtos = ["Cachorro Quente", 100, 1.20, "Bauru Simples", 101, 1.30,
            "Bauru com Ovo", 102, 1.50, "Hamburguer", 103, 1.20,
            "Cheeseburguer", 104, 1.70, "Suco", 105, 2.20,
            "Refrigerante", 106, 1.10]

if (cod not in produtos):
    print("Produto Inexistente")
    
else:
    x = produtos.index(cod)
    print(f"\n Produto : {produtos[x - 1]} \n Quantidade: {qtn} \n Valor: R$ {produtos[x + 1] * qtn}")


"33"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 33\n" + "\n\n")

prc = float(input("Informe o preço antigo: ")) # preço

if (prc <= 50):
    prc = prc + ( prc * 0.05)

elif (prc > 50 and prc <= 100):
    prc = prc + ( prc * 0.10)

else:
    prc = prc + ( prc * 0.15)

if (prc <= 80):
    print(f"\n Preço: {prc} \n Barato!")
    
elif (prc > 80 and prc <= 120):
    print(f"\n Preço: {prc} \n Normal!")

elif (prc > 120 and prc <= 200):
    print(f"\n Preço: {prc} \n Caro!")

else:
    print(f"\n Preço: {prc} \n Muito Caro!")



"34"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 34\n" + "\n\n")

nota = float(input("\nInforme a nota: "))
faltas = int(input("Informe as faltas: "))

if (nota <= 10.0 and nota >= 9.0):
    if (faltas <= 20 ):
        print("\n Conceito: A \n")
    elif (faltas > 20):
        print("\n Conceito: B \n")
        
elif (nota <= 8.9 and nota >= 7.5):
    if (faltas <= 20 ):
        print("\n Conceito: B \n")
    elif (faltas > 20):
        print("\n Conceito: C \n")

elif (nota <= 7.4 and nota >= 5.0):
    if (faltas <= 20 ):
        print("\n Conceito: C \n")
    elif (faltas > 20):
        print("\n Conceito: D \n")

elif (nota <= 4.9 and nota >= 4.0):
    if (faltas <= 20 ):
        print("\n Conceito: D \n")
    elif (faltas > 20):
        print("\n Conceito: E \n")

elif (nota <= 3.9 and nota >= 0):
    if (faltas <= 20 ):
        print("\n Conceito: E \n")
    elif (faltas > 20):
        print("\n Conceito: E \n")



"35"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 35\n" + "\n\n")

meses  = [1, 3, 5, 7, 8, 10, 12]

while True:
    try:
        dia = int(input(" Dia: "))
        
        if (dia > 31 or dia < 1) :
            print(f"\n Dia: {dia}")
            raise ValueError

        mes = int(input(" Mes: "))

        if (mes > 12 or mes < 1):
            print(f"\n Mes: {mes}")
            raise ValueError

        ano = int(input(" Ano: "))

        if (ano > 9999 or ano < 1):
            print(f"\n Ano: {ano}")
            raise ValueError

        if (ano % 4 == 0 or ano % 400 == 0 and ano % 100 != 0) and (mes == 2):
            if (dia > 29):
                print(f"\n Dia: {dia}")
                raise ValueError
            else:
                print(f"\n Data: {dia} / {mes} / {ano} , valida. \n")

        elif (mes not in meses and dia > 30):
            print(f"\n Dia: {dia}")
            raise ValueError
        
        else:
            print(f"\n Data: {dia} / {mes} / {ano} , valida. \n")

            
    except ValueError:
        print(" Valor Invalido.\n")




"36"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 36\n" + "\n\n")

valor = float(input("\n Informe o valor da venda: "))

if (valor < 20000):
    com = 400 + (valor * 0.14)# comissão
    print(f"\n 1. Comissão: {com:.2f} \n")
    
elif (valor >= 20000 and valor < 40000):
    com = 500 + (valor * 0.14) # comissão
    print(f"\n 2. Comissão: {com:.2f} \n")

elif (valor >= 40000 and valor < 60000):
    com = 550 + (valor * 0.14) # comissão
    print(f"\n 3. Comissão: {com:.2f} \n")

elif (valor >= 60000 and valor < 80000):
    com = 600 + (valor * 0.14) # comissão
    print(f"\n 4. Comissão: {com:.2f} \n")
    
elif (valor >= 60000 and valor < 100000):
    com = 650 + (valor * 0.14) # comissão
    print(f"\n 5. Comissão: {com:.2f} \n")

else:
    com = 700 + (valor * 0.16) # comissão
    print(f"\n 6. Comissão: {com:.2f} \n")



"37"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 37\n" + "\n\n")

try:
    h1 = int(input("\n Informe a Hora de entrada: ")) # hora de chegada
    m1 = int(input(" Informe os Minutos de entrada: ")) # minuto de chegada

    if (h1 > 24 or m1 >= 60):
        raise ValueError
    
    h2 = int(input("\n Informe a Hora de saida: ")) # hora de saida
    m2 = int(input(" Informe os Minutos de saida: ")) # minuto de saida
    
    if (h2 > 24 or m2 >= 60):
        raise ValueError
    
    m1 = m1 + ( h1 * 60 ) # conversao das horas para minutos
    m2 = m2 + ( h2 * 60 ) 

    if (m2 < m1): # caso o tempo de partida seja menor que o tempo de chegada
        tempo = ( 1440 - m1 ) + m2 # subtrai as horas que faltam para 24 horas e soma com os minutos que faltam para m2
        horas = tempo // 60
        minutos = tempo % 60
    else:
        tempo = m2 - m1
        horas = tempo // 60
        minutos = tempo % 60

    if (horas <= 2 and horas >= 0):
        valor = horas * 1.00
        
    elif (horas <= 4 and horas >= 3):
        valor = horas * 1.40

    elif (horas >= 5):
        valor = horas * 5
        
    print(f"\n O Tempo de Estacimento e de {horas} Horas e {minutos} Minutos. " +
          f"\n O valor a pagar e de: R$ {valor:.2f}")

except ValueError:
    print("\n Valor Invalido.")



"38"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 38\n" + "\n\n")

meses  = [1, 3, 5, 7, 8, 10, 12] # 
while True:
    try:
        dia = int(input(" Dia: "))
        
        if (dia > 31 or dia < 1) :
            print(f"\n Dia: {dia}")
            raise ValueError

        mes = int(input(" Mes: "))

        if (mes > 12 or mes < 1):
            print(f"\n Mes: {mes}")
            raise ValueError

        ano = int(input(" Ano: "))

        if (ano > 9999 or ano < 1):
            print(f"\n Ano: {ano}")
            raise ValueError

        if (ano % 4 == 0 or ano % 400 == 0 and ano % 100 != 0) and (mes == 2):
            if (dia > 29):
                print(f"\n Dia: {dia}")
                raise ValueError
            else:
                print(f"\n Data: {dia} / {mes} / {ano} , valida. \n")

        elif (mes not in meses and dia > 30):
            print(f"\n Dia: {dia}")
            raise ValueError
        
        else:
            print(f"\n Data: {dia} / {mes} / {ano} , valida. \n")

            
    except ValueError:
        print(" Valor Invalido.\n")



"39"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 39\n" + "\n\n")

while True:
    sal = float(input("Salario Atual: ")) # salario
    tempo = int(input("Tempo de serviço: ")) # tempo de serviço
    salA = sal

    # Reajustes
    if (sal <= 500):
        sal = sal + ( sal * 0.25)
        
    elif (sal <= 1000 and sal > 500):
        sal = sal + ( sal * 0.20)
        
    elif (sal <= 1500 and sal > 1000):
        sal = sal + ( sal * 0.15)

    elif (sal <= 2000 and sal > 1500):
        sal = sal + ( sal * 0.10)

    elif (sal > 2000):
      print("\n Salário acima de 2000,00 - SEM REAJUSTE.\n")


    # Bonus
    if (tempo < 1):
        print("\n Tempo de serviço inferior a 1 ano. - SEM BONUS\n")

    elif (tempo > 1 and tempo <= 3):
        sal = sal + 100

    elif (tempo > 4 and tempo <= 6):
        sal = sal + 200

    elif (tempo > 7 and tempo <= 10):
        sal = sal + 300

    elif (tempo > 10):
        sal = sal + 500

    print(f" O salario apos o reajuste e acrecimo de bonus e: R$ {sal} \n Tempo de Serviço: {tempo} Anos \n Salário Antigo: {salA} \n")



"40"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 40\n" + "\n\n")

while True:
    cf = float(input("Custo de Fábrica: "))# custo de fabrica
    custo = 0
    if ( cf <= 12000 ):
        custo = cf + ( cf * 0.05) + (0)
        print(f"Custo do Consumidor: R$ {custo:.2f}\n")
        
    elif (cf > 12000 and cf <= 25000):
        custo = cf + ( cf * 0.10 ) + ( cf * 15 )
        print(f"Custo do Consumidor: R$ {custo:.2f}\n")

    else:
        custo = cf + ( cf * 0.15 ) + ( cf * 20 )
        print(f"Custo do Consumidor: R$ {custo:.2f}\n")



"41"
print("\n\n" + ( "-----" * 16 ) + "\nQuestão 41\n" + "\n\n")
while True:
    peso = float(input("Informe seu peso: "))
    altura =  float(input("Informe sua altura: "))

    imc = peso / ( altura * altura)

    if (imc <= 18.5):
        print(f"Imc: {imc:.2f} - Abaixo do peso.")
        
    elif (imc >= 18.6 and imc <= 24.9):
        print(f"Imc: {imc:.2f} - Saudável.")
        
    elif (imc >= 25.0 and imc <= 29.9):
        print(f"Imc: {imc:.2f} - Peso em excesso.")
        
    elif (imc >= 30.0 and imc <= 34.9):
        print(f"Imc: {imc:.2f} - Obesidade Grau I.")
        
    elif (imc >= 35.0 and imc <= 39.9):
        print(f"Imc: {imc:.2f} - Obesidade Grau II.")
        
    elif (imc >= 40.0):
        print(f"Imc: {imc:.2f} - Obesidade Grau III.")

    print("\n")
