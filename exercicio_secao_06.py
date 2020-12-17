import random
import math


def question(n):
    if n < 10 and n > 0:
        n = "0" + str(n)
    print("\n\n","---" * 26, "\n\n Questão {} \n\n".format(n))




question(1)

print(f"""
    Multiplos de 3:
      1 x 3: {1*3}
      2 x 3: {2*3}
      3 x 3: {3*3}
      4 x 3: {4*3}
      5 x 3: {5*3}
""")
        


question(2)

num = 0
n = 0

print(" Loop For Numeros: \n") 
for i in range(0,101,1): # for
    print(i, end=" ")


print("\n\n Loop While Numeros: \n")
while num < 101: # while
    print(f"{num}", end=" ")
    num = num + 1


print("\n\n Loop Do While Numeros: 'exemplo' \n")
num = 0

while n < 1000: # Do while
    if num < 101:
        print(f"{num}", end=" ")
        num = num + 1
    else:
        break



question(3)

n = 10

while n >=0:
    print(f"Contagem Regressiva: {n}")
    n = n - 1
print("\n FIM!")



question(4)

num = random.randrange(100000)

print(f"Numero Inicial: {num} \n\n")

while True:
    if num < 0 or num > 100000:
        print("\n FIM")
        break
    else:
        print(f"{num}")
        num = num + 1000



question(5)

num = 0
soma = 0

for i in range(0, 10):
    print(f"\n Informe o {i + 1}° valor: ", end=" ")
    num = float(input())
    soma = soma + num
print(f"\n A soma e igual a {soma}")



question(6)

c = 0
num = 0
media = 0

while c < 10:
    print(f"\n Informe o {c + 1}° Valor: ", end=" ")
    num = int(input())
    media = media + num
    c = c + 1
media = media / 10

print(f"\n A media e {media}")
    


question(7)

c = 0
num = 0
media = 0

while c < 10:
    print(f"\n Informe o {c + 1}° Valor: ", end=" ")
    num = int(input())
    if num < 0:
        print(f"\n Numero {num} Invalido. \n")
    else:
        media = media + num
        c = c + 1
print(f"\n Media: {media / 10}")




question(8)

numeros = []
maior = 0
menor = 0

for i in range(0,10):
    print(f"Informe o {i + 1}° numero: ", end=" ")
    num = int(input())
    numeros.append(num)

maior = max(numeros)    
menor = min(numeros)

print(f"\n Maior: {maior} \n Menor: {menor} \n")




question(9)

print("Informe um numero inteiro: ", end=" ")
num = int(input())

for i in range(0, num):
    if i % 2 != 0:
        print(i)



question(10)

soma = 0

print (" Numeros Pares: \n")

for i in range(51):
    if i % 2 == 0:
        print(i, end=" ")
        soma = soma + i
print(f"\n\n Soma: {soma}")



question(11)

print("Informe um numero inteiro positivo:", end=" ")
num = int(input())

if num < 0:
    print(f"\nNumero {num} Invalido.")
else:
    print("\n Crescente: \n")

    for i in range(num + 1):
        print(i, end=" ")


question(12)

print("Informe um numero inteiro positivo:", end=" ")
num = int(input())

if num < 0:
    print(f"\nNumero {num} Invalido.")
else:
    print("\n Decrescente: \n")

    for i in range(num + 1):
        print(num - i, end=" ")



question(13)

print("Informe um numero inteiro positivo par:", end=" ")
num = int(input())

if num < 0:
    print(f"\nNumero {num} Invalido.")
else:
    for i in range(num + 1):
        if i % 2 == 0:
            print(i, end=" ")



question(14)

print("Informe um numero inteiro positivo par:", end=" ")
num = int(input())
numeros = []

if num < 0:
    print(f"\nNumero {num} Invalido.")
else:
    for i in range(num + 1):
        if i % 2 == 0:
            numeros.append(i)
            
    for i in range(1, len(numeros) + 1):  # reversing list
        print(numeros[i * (-1)], end=" ") # print reserve list




question(15)

print("Informe um numero inteiro positivo impar:", end=" ")
num = int(input())

if num % 2 == 0:
    print(f"\nNumero {num} Invalido.")
    
else:
    print("0", end=" ")
    for i in range(0, num + 1):
        if i % 2 != 0:
            print(i, end=" ")



question(16)

print("Informe um numero inteiro positivo impar:", end=" ")
num = int(input())

numeros = []

if num % 2 == 0:
    print(f"\nNumero {num} Invalido.")
    
else:
    for i in range(num + 1):
        if i % 2 != 0:
            numeros.append(i)

    numeros.sort(reverse=True)
    
    for i in range(len(numeros)):
        print(numeros[i], end=" ")



question(17)

print("Informe um numero inteiro positivo:", end=" ")
num = int(input())

soma = 0

if num < 0:
    print(f"\n {num} e Invalido. \n")

else:
    for i in range(0, num + 1):
        soma = soma + i
    print(f"\n Soma: {soma}\n")



question(18)

print("Informe a quantidade de numeros:", end=" ")
c = int(input())
num = 0
numeros = []
print("\n")
for i in range(c):
    print(f"Informe o {i + 1}° valor: ", end=" ")
    num = float(input())
    numeros.append(num)

    
maior = max(numeros)
cont = numeros.count(maior)
print(f"\n Maior: {maior} \n Repetições: {cont}")



question(19)

print("Informe um numero entre 100 e 999:", end=" ")
num = input()

if int(num) < 100 or int(num) > 999:
    print(f"\n {num} e invalido.")
else:
    for i in range(1, 4):
        print(num[i * (-1)], end=" ")


question(20)

cont = 0
num = ""
pares = 0

while True:
    print("Informe um numero:", end=" ")
    num = int(input())

    if num == 1000:
        print(f"\n Numero verificados: {cont} \n Pares: {pares}")
        print(" Fim")
        break

    if num % 2 == 0:
        print(f"NUmero: {num} e par\n")
        pares = pares + 1
    else:
        print(f"NUmero: {num} e impar\n")

    cont = cont + 1
    


question(21)

while True:
    print("Informe o 1° numero:", end=" ")
    n1 = int(input())

    print("Informe o 2° numero:", end=" ")
    n2 = int(input())

    soma = 0
    mult = 1

    if n1 < n2:
        n2 = n2 + 1
        for i in range(n1, n2):
            if i % 2 == 0:
                soma = soma + i
            else:
                mult = mult * i
    else:
        n1 = n1 + 1
        for i in range(n2, n1):
            if i % 2 == 0:
                soma = soma + i

            else:
                mult = mult * i


    print(f" Soma: {soma} \n Multiplicação: {mult} \n")



question(22)

num = 0
cont = 1

while True:
    print(" Informe a nota:", end=" ")
    nota = float(input())
    
    if nota < 10 or nota > 20:
        break

    num = num + nota
    media = num / cont
    cont = cont + 1
    print(f"\n Media: {media:.2f} \n")



question(23)

print("Informe um numero positivo: ", end=" ")
num = int(input())
divisores = []


for i in range(1, 100):
    if num % i == 0:
        divisores.append(i)

print(f"\n Os divisores do numero {num} sao {divisores}\n")




question(24)

print("Informe um numero positivo: ", end=" ")
num = int(input())
divisores = []


for i in range(1, 100):
    if num % i == 0:
        divisores.append(i)

divisores.pop()
soma = sum(divisores)
print(f"\n A soma dos divisores do numero {num} sao {soma}\n")



question(25)

c = 1
mult3 = [0]
mult5 = [0]
soma = 0

while True:
    if c > 1000 or max(mult3) > 1000 or max(mult5) > 1000:
        break
    else:
        mult3.append((c * 3))
        mult5.append((c * 5))
        c = c + 1


mult3.append((c * 3))
mult5.pop()
soma = sum(mult3) + sum(mult5)
print(f"\n Soma: {soma}")



question(26)

print("Informe um numero: ", end=" ")
num = int(input())
t = False
a = []
b = []
c = []

for i in range(1, num + 1):
    a.append((11 * i))
    b.append((13 * i))
    c.append((17 * i))

    if max(a) in b and max(a) in c:
        print(f"Multiplo: {max(a)}")
        t = True
        break

if t == False:
    print(f"\n Multiplo não encontrado. \n MMC de 11 13 17: 2431 \n Multiplo Comun: 221")



question(27)

print(" Informe um numero inteiro positivo: ", end=" ")
num = int(input())
soma = 0

for i in range(1, num + 1):
    soma = soma + ( 1 / i )

print(f"\n Soma Harmonica: {soma:.2f} \n")



question(28)

print(" Informe um numero inteiro positivo: ", end=" ")
num = int(input())
soma = 0
fat = 1 # fatorial

for i in range(1, num + 1):

    if i > 1:
        for x in range(1, i + 1):
            fat = fat * x
        soma = soma + ( 1 / fat )
        fat = 1 # reset
        
    else:
        soma = soma + ( 1 / i )

print(f"E = {soma:.2f}")



question(29)

fat = 1
soma = 0

for i in range(0, 5):

    if i == 0:
        soma = soma + i
        
    else:
        for x in range(1, i + 1):
            fat = fat * x
            
        soma = soma + ( i / fat )
        fat = 1

print(f" S = {soma:.4f}")



question(30)

print(" Informe um numero inteiro: ", end=" ")
num = int(input())
soma = 0
soma2 = 0
soma3 = 0

for i in range(num + 1):
    soma = soma + i
    
for i in range(1, num + 1, 2):
    soma2 = soma2 + (i - (i + 1))
    soma3 = soma3 + i

print(f" Sequencia 1: {soma} \n Sequencia 2: {soma2} \n Sequencia 3: {soma3} \n ")



question(31)

x = 0

for i in range(1, 51):
    x = (2 * i) - 1
    print(f"{x} / {i}", end="\n\n")



question(32)

print("Informe o numero de lançamentos: ", end=" ")
num = int(input())
d1 = 0
d2 = 0

print("\n Ex.: d1 > d2 / d1 = d2 / d1 < d2 \n")

for i in range(num):
    print(f"Lançamento {i + 1}:")
    d1 = random.randrange(1,7)
    d2 = random.randrange(1,7)

    if (d1 < d2):
        print(f"{d1} < {d2} \n")

    elif (d1 == d2):
        print(f"{d1} = {d2} \n")

    else:
        print(f"{d1} > {d2} \n")



question(33)

num = list("NIJ")

for i in range(3):
    print(f"Informe um numero inteiro positivo diferente de 0 para {num[i]}:", end=" ")
    num[i] = int(input())
    if num[i] < 1:
        print("valor Invalido.")
        break
    
valores = {num[1]:[], num[2]:[]}

for i in range(num[0]):
    valores[num[1]].append((num[1] * i))
    valores[num[2]].append((num[2] * i))

lista = valores[num[1]] + valores[num[2]]
lista = list(dict.fromkeys(lista))
lista.sort()

print("\n Resultado: ", end=" ")
for i in range(num[0]):
    print(lista[i], end=" ")



question(34) # sem resposta

cont = 2520
t = False
print(cont)

while cont < 100000000:

    for i in range(1,21):
        if cont % i != 0:
            break

        elif cont % i == 0:
            if i == 20:
                t = True
    if t:
        print(cont)
        break
    else:
        cont = cont + 1



question(35)

soma = 0

while True:

    try:
        print(" Defina o valor inicial: ", end=" ")
        n1 = int(input())
        
        print(" Defina o valor final: ", end=" ")
        n2 = int(input())

        if n2 < n1:
            raise ValueError

        else:
            for i in range(n1, n2):
                if i % 3 == 0:
                    soma = soma + i
            print(f" Soma dos impares neste intervalo: {soma} \n")
            
    except ValueError:
        print("\n Intervalo de valores inválido. \n")



question(36)

soma = 0
soma2 = 0

for i in range(1, 101):
    soma = soma + ( i ** 2 )
    soma2 = soma2 + i

soma2 = soma2 ** 2
print(f"{soma2} - {soma} = {soma2 - soma}")



question(37)

num = ""
test = 0

for i in range(1000, 10000):

    num = str(i)
    test = ( int(num[0:2]) + int(num[2:4]) ) ** 2

    if test == i:
        print(i, end=" ")



question(38)

a = 0
x = 0
c = 0

for b in range(1, 500): 
    if 1000 * (500 - b) % (1000 - b) == 0:
        x = b
        a = 1000 * (500 - b) / (1000 - b)
        c = 1000 - (x + a)
        print(f"{a:.0f} + {x} + {c:.0f} = 1000")
        break


question(39)

area = 0
while True:
    print("Informe a base do triangulo: ", end=" ")
    b = float(input())
    if b <= 0:
        print(" VALOR INVALIDO. ")
    else:
        print("Informe a altura do triangulo: ", end=" ")
        h = float(input())
        if h <= 0:
            print(" VALOR INVALIDO. ")
        else:
            area = (b * h) / 2
            print(f"Area = {area} \n")



question(40)

c = 0
numeros = []

print("DIgite um numero negativo para cancelar. \n\n")

while True:
    c = c + 1
    print(f"Informe o {c}° numero:", end="")
    num = float(input())

    if num < 0:
        print(f" Maior: {max(numeros)} \n Menor: {min(numeros)}\n\n")
        break
    else:
        numeros.append(num)



question(41)

while True:
    print("Informe R1: ", end=" ")
    r1 = float(input())
    
    print("Informe R2: ", end=" ")
    r2 = float(input())

    r = (r1 * r2) / ( r1 + r2 )
    print(f"Resistencia: {r:.4f} \n\n")

    if r == 0:
        break



question(42)

while True:
    print(f"Informe um numero: ", end=" ")
    n = int(input())

    if n <= 0:
        break

    print(f"  Quadrado: {n ** 2} \n " +
          f" Cubo: {n ** 3} \n " +
          f" Raiz Quadrada: {math.sqrt(n)}\n\n")


question(43)

idades = []
media = 0

while True:
    print("Informe uma idade: ", end=" ")
    idade = int(input())

    if idade == 0:
        media = sum(idades) / len(idades)
        print(f"\n Idade Media: {media}")
        break
    
    else:
        idades.append(idade)
        


question(44)

print("Informe um numero inteiro positivo: ", end=" ")
num = int(input())

a = 1
b = 0
x = 0

print(0, end=" ")
for i in range(num):

    x = a + b
    b = a
    a = x
    print(b, end=" ")

    if b > num:
        break



question(45)


while True:

    v = 0 # velocidade
    c = 0 # conversao

    print(" Qual opção deseja executar: \n" +
          "  1. Km / h para M / s \n" +
          "  2. M / s para km / h \n" +
          "  3. Sair. \n\n" +
          "Escolha: ", end=" ")
    op = input()

    if op == "1":
        print("\n Informe a velocidade em Km/H: ", end=" ")
        v = float(input())
        c = v / 3.6
        print(f"\n {v} Km/h em M/s = {c} M/s \n")
        
        
    elif op == "2":
        print("\n Informe a velocidade em M/s: ", end=" ")
        v = float(input())
        c = v * 3.6
        print(f"\n {v} M/s em Km/h = {c} Km/h \n")
    else:
        print("\n Cya. \n")
        break



question(46)

num = random.randrange(1,1001)
c = 0

while True:

    print("Tente um numero: ", end=" ")
    test = int(input())
    c = c + 1

    if test == num:
        print(f"\n Tentativas: {c}. Vitoria. \n")
        break

    elif num > test:
        print(f"O numero e maior que {test}.\n")

    elif num < test:
        print(f"O numero e menor que {test}\n")



question(47)

r = 0

ope = ["+", "-", "*", "/"]

while True:
        
    print("""
 1. Adição
 2. Subtração
 3. Multiplicação
 4. Divisão
 5. Saída

 Escolha: """, end=" ")

    op = input()

    if op == "5":
        print("\n Cya. \n")
        break

    print("\n Informe 1° numero: ", end=" ")
    n1 = float(input())

    print("\n Informe 2° numero: ", end=" ")
    n2 = float(input())

    if op == "1":
        r = n1 + n2
        
    elif op == "2":
        r = n1 - n2
    
    elif op == "3":
        r = n1 * n2
        
    elif op == "4":
        r = n1 / n2

    print(f"\n Resultado: {n1} {ope[int(op)-1]} {n2} = {r} \n")



question(48)

a = 1
b = 0
x = 0
soma = 0

while b < 4000000:

    x = a + b
    b = a
    a = x

    if b % 2 == 0:
        soma = soma + b

print(f"Soma: {soma}")




question(49)

print("Informe o salario de Carlos: ", end=" ")
sal = float(input()) # salario
sal2 = sal / 3
meses = 0


while True:
    sal = sal + ( sal * 0.5 )
    sal2 = sal2 + ( sal2 * 0.7)
    meses = meses + 1
    if sal2 > sal:
        break
    if sal2 == sal:
        break
    
print(f"\n Salario: \n Carlos: R$ {sal:.2f} \n João: R$ {sal2:.2f} \n Meses: {meses}")




question(50)

c = 150
z = 110
a = 0

while c > z:
    c = c + 2
    z = z + 3

    a = a + 1

print(f"São necessários {a} anos para Zé ser maior que Chico.")



question(51)

sal = 2000
aum = 0.015 # aumento
ano = 1996

sal = sal + (sal * aum)

while ano < 2020:
    ano = ano + 1
    aum = aum * 2
    sal = sal + (sal * aum)


print(f"Salario atual: {sal}")


question(52)


print("Sacar: R$ ", end=" ")
v = float(input())

while True:
    if v >= 100:
        x = v // 100
        v = v - (x * 100 )
        print(f"\n Notas de 100 : {x} \n")

    elif v >= 50:
        x = v // 50
        v = v - ( x * 50 )
        print(f"\n Notas de 50 : {x} \n")

    elif v >= 20:
        x = v // 20
        v = v - ( x * 20 )
        print(f"\n Notas de 20 : {x} \n")

    elif v >= 10:
        x = v // 10
        v = v - ( x * 10 )
        print(f"\n Notas de 10 : {x} \n")

    elif v >= 5:
        x = v // 5
        v = v - ( x * 5 )
        print(f"\n Notas de 5 : {x} \n")

    elif v >= 2:
        x = v // 2
        v = v - ( x * 2 )
        print(f"\n Notas de 2 : {x} \n")

    elif v >= 1:
        x = v // 1
        v = v - ( x * 1 )
        print(f"\n Notas de 1 : {x} \n")

    else:
        print(f"\n Resto: {v:.2f} \n")
        break



question(53)

print("Informe um numero inteiro positivo: ", end=" ")
n = int(input())
c = 1
print("\n")
for i in range(1, n + 1):
    for x in range(0, i):
        print(c, end=" ")
        c = c + 1
    print("\n")



question(54)

while True: # PRIMOS / https://pt.wikibooks.org/wiki/Teoria_de_n%C3%BAmeros/10000_primos
    
    print("\nInforme um numero inteiro: ", end=" ")
    num = int(input())

    test = []

    if num > 1:
        if num == 2:
            print("E primo.")

        elif num % 2 == 0:
            print("Não e primo")
            
        else:
            for i in range(1, num + 1):
                x = num / i
                if int(x) == x:
                    test.append(x)

            if len(test) == 2:
                print(f"{num} e primo.")

            else:
                print(f"{num} não e primo.")

                
    else:
        print("\n Valor Invalido. \n")



    test.clear()



question(55)

print("\n Informe um numero inteiro positivo: ", end=" ")
num = int(input())

test = [] # testador
p = [] # lista de numeros primos
c = 0 # contador

if num > 1:

    while num > c:

        c = c + 1

        if c == 2:
            p.append(2.0)
            
        elif c % 2 == 0:
            pass
        
        else:
            for i in range(1, c + 1):
                x = c / i
                if int(x) == x:
                    test.append(x)

            if len(test) == 2:
                p.append(test[0])

            test.clear()
                
else:
    print("Valor invalido.")

print(f" Soma de todos os numeros primos ate {num} e {sum(p)}")



question(56)

test = [] 
p = [] 
c = 0 

while 2000000 > c:

    c = c + 1

    if c == 2:
        p.append(2.0)
        
    elif c % 2 == 0:
        pass
    
    else:
        for i in range(1, c + 1):
            x = c / i
            if int(x) == x:
                test.append(x)

        if len(test) == 2:
            p.append(test[0])

        test.clear()

print(sum(p))


question(57)

print("Numero inicial: ", end=" ")
a = int(input())

print("Numero final: ", end=" ")
b = int(input())

test = [] 
p = [] 
c = 0

while a != b :

    if a > b:
        b = b + 1
        c = b
    else:
        a = a + 1
        c = a


    if c == 2:
        p.append(2.0)
        
    elif c % 2 == 0:
        pass
    
    else:
        for i in range(1, c + 1):
            x = c / i
            if int(x) == x:
                test.append(x)

        if len(test) == 2:
            p.append(test[0])

        test.clear()


print(f" Existem {len(p)} numeros primos no intervalo.")


question(58)

print("Numero inicial: ", end=" ")
a = int(input())

print("Numero final: ", end=" ")
b = int(input())

test = [] 
p = [] 
c = 0

while a != b :

    if a > b:
        b = b + 1
        c = b
    else:
        a = a + 1
        c = a


    if c == 2:
        p.append(2.0)
        
    elif c % 2 == 0:
        pass
    
    else:
        for i in range(1, c + 1):
            x = c / i
            if int(x) == x:
                test.append(x)

        if len(test) == 2:
            p.append(test[0])

        test.clear()


print(f" A soma dos numeros primos no intervalo e {sum(p)}")



question(59)

print("Informe o numero de habitantes: ", end=" ")
n = int(input())

print("Qual o valor do Kwh: ", end=" ")
k = float(input())


maior = 0
menor = 0
media = 0

valores = {1:[], 2:[], 3:[], 4:[]}

print(""" \n
 Codigos:
 1 - Residencial
 2 - Comercial
 3 - Industrial \n
""")

for i in range(1, n + 1):
    print(f"\n {i}° Habitante consumo do mes: ", end=" ")
    foo = float(input())

    print(f"\nQual o codigo do usuário? \n Codigo:", end=" ")
    c = input()
    
    if c == "1":
        valores[1].append(foo)

    elif c == "2":
        valores[2].append(foo)

    elif c == "3":
        valores[3].append(foo)

    else:
        valores[4].append(foo)

if max(valores[1]) > max(valores[2]) > max(valores[3]):
    maior = max(valores[1])
    
elif max(valores[2]) > max(valores[1]) > max(valores[3]):
    maior = max(valores[2])

else:
    maior = max(valores[3])



if min(valores[1]) < min(valores[2]) and min(valores[1]) < min(valores[3]):
    menor = min(valores[1])

elif min(valores[2]) < min(valores[1]) and min(valores[2]) < min(valores[3]):
    menor = min(valores[2])

else:
    menor = min(valores[3])

media = ( sum(valores[1]) + sum(valores[2]) + sum(valores[3])  ) / n

print(f"""
 Maior consumidor: {maior * k:.2f} kwh
 Menor consumidor : {menor * k:.2f} kwh
 Media dos habitantes: {media * k:.2f} kwh

 1 - Total Residencial {sum(valores[1]) * k:.2f} kwh
 2 - Total Comercial: {sum(valores[2]) * k:.2f} kwh
 3 - Total Industrial {sum(valores[3]) * k:.2f} kwh
""")



question(60)

numeros = []
pares = 0

while True:
    print("\nInforme um numero:", end=" ")
    num = float(input())

    if num == 0:
        print("\n CYA")
        break
    else:
        if num % 2 == 0:
            pares = pares + num
        numeros.append(num)

    print(f"""\n
 Soma de todos os numeros digitados: {sum(numeros)}

 Quantidade de numeros digitados: {len(numeros)}

 Media dos numeros digitados: {sum(numeros) / len(numeros)}

 Maior numero digitado: {max(numeros)}

 Menor numero digitado: {min(numeros)}

 Media dos numeros pares: {pares}
\n""")




question(61)

maior = 0
mult = []

for i in range(100, 1000):
    for x in range(100, 1000):
        num = str(i * x)
        r = num[::-1]
        if  num == r and int(num) > int(maior):
            mult.clear()
            maior = num
            mult.insert(0, i)
            mult.insert(1, x)

print(f"\n Maior palíndromo: {maior} \n Produtos: {mult[0]} * {mult[1]} \n")



question(62)


palavras = ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
            'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa', 'cem', 'cento',
            'duzentos', 'trezentos', 'quatrocentos', 'quientos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos', 'mil']

soma = 0

for i in range(len(palavras)): # itera a lista de palavras

    if i >= 19 and i != 37: # verifica se ja passo dos 19 primeiros numeros e o numero atual nao e MIL

        print("\n")

        if i >= 27: # se passar do numero cem

            if i == 27: # mostra o cem
                print(palavras[i])
                soma = soma + len(palavras[i])

            else: # e começa a contar as centenas

                print(palavras[i]) # mostra o numero de inicio
                soma = soma + len(palavras[i])

                for x in range(19): # itera entre os vinte primeiros numeros
                    print(palavras[i] + " e " + palavras[x]) # mostra os numeros
                    soma = soma + len(palavras[i] + "e" + palavras[x])
                    
                for y in range(19, 27): # itera de vinte ao numero noventa e nove
                    print("\n")
                    print(palavras[i] + " e " + palavras[y])
                    soma = soma + len(palavras[i] + "e" + palavras[y])

                    for p in range(9): # itera os numeros de um a nove
                        print(palavras[i] + " e " + palavras[y] + " e " + palavras[p]) # imprime os numeros na casa das centenas
                        soma = soma + len(palavras[i] + "e" + palavras[y] + "e" + palavras[p])


        else: # casa das dezenas de dez a noventa e nove

            print(palavras[i]) # mostra o numero atual
            soma = soma + len(palavras[i])

            for x in range(9): # imprime a combinação dos numero atual mais suas nove variações

                print(palavras[i] + " e " + palavras[x]) # imprime o numero
                soma = soma + len(palavras[i] + "e" + palavras[x])

            
    else:
        print(palavras[i]) # mostra os dezenove primeiros numeros
        soma = soma + len(palavras[i])

print(f"\n\n Sao necessarios {soma} letras para se escrever por extenso os numeros de um a mil sem contar os espaços em branco. \n\n")
