from exercicio_secao_07 import question
import random
import numpy as np
import pandas as pd


def PM(m):
    c = []
    for i in range(len(m[0])):
        c.append(" ")

    x = pd.DataFrame(m, columns=c)
    print(x.to_string(index=False))


question(1)

matrix = [[],[],[],[]]

for a in range(len(matrix)):
    for b in range(10):
        matrix[a].append(random.randrange(100))

print("Matrix: ")
for i in range(len(matrix)):
   print(matrix[i])



question(2)

matrix = [[],[],[],[],[]]

for a in range(len(matrix)):
    matrix[a].append(1)
    for b in range(9):
        matrix[a].append(0)

print("Matrix")
for i in range(len(matrix)):
    print(matrix[i])


question(3)

matrix = [[],[],[],[]]

for a in range(len(matrix)):
    for b in range(10):
      matrix[a].append(a * b)

print("Matrix: ")
for i in range(len(matrix)):
    print(matrix[i])


question(4)


matrix = [[],[],[],[]]

for a in range(len(matrix)):
    for b in range(10):
      matrix[a].append(a * b)

print("Matrix: ")
for i in range(len(matrix)):
    print(matrix[i])

print(f"Maior: {max(max(matrix))}")


question(5)

matrix = [[],[],[],[],[]]

for a in range(1, len(matrix) + 1):
    for b in range(10):
        matrix[a - 1].append(a * b)


print("Informe um numero: ",end=" ")
n = int(input())
x = ""
y = ""
c = 0


for i in range(len(matrix)):
    if n in matrix[i]:
        x += str(i)
        y += str(matrix[i].index(n))

if x != "" and y != "":
    c = int(len(str(x)) + len(str(y)) / 2) - 1
    for i in range(c):
        print(f"{i + 1}. {n} encontrado na matrix {x[i]} linha {y[i]}.")
else:
    print(f"{n} não encontrado.")




question(6)

matrix =[[],[],[],[]]
matrix2 = [[],[],[],[]]

for a in range(len(matrix)):
    for b in range(10):
        matrix[a].append(a * b)

for a in range(len(matrix2)): 
    matrix2[a].append(max(matrix[a]))

for i in range(len(matrix2)):
    print(matrix2[i])



question(7)

matrix = [[],[],[],[],[],[],[],[],[],[]]

for i in range(len(matrix)):
    for j in range(10):
        matrix[i].append(i * j)

print(f"Matrix v1: ")
for i in range(len(matrix)):
    print(matrix[i])
    
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][i] < matrix[i][j]:
            matrix[i][j] = (2 * i) + (7 * j) - 2
            
        elif matrix[i][i] == matrix[i][j]:
            matrix[i][j] = 2 * (i ** 2) - 1

        elif matrix[i][i] > matrix[i][j]:
            matrix[i][j] = ( 4 * (i ** 3)) - (5 * (j ** 2)) + 1

print("\n\n Matrix v2: ")
for i in range(len(matrix)):
    print(matrix[i])




question(8)

matrix = [[],[],[]]

for a in range(len(matrix)):
    for b in range(3):
        matrix[a].append(b)

print(f"Matrix: ")
for i in range(len(matrix)):
    print(matrix[i])

print("\n\n Soma Acima: ")
for i in range(1 , len(matrix)):
    print(matrix[i][i] + matrix[i - 1][i])




question(9)

matrix = [[],[],[]]

for a in range(len(matrix)):
    for b in range(3):
        matrix[a].append(b)

print(f"Matrix: ")
for i in range(len(matrix)):
    print(matrix[i])

print("\n\n Soma Abaixo: ")
for i in range(0 , len(matrix) - 1):
    print(matrix[i][i] + matrix[i + 1][i])



question(10)

matrix = [[],[],[]]

for a in range(len(matrix)):
    for b in range(3):
        matrix[a].append(b)

print(f"Matrix: ")
for i in range(len(matrix)):
    print(matrix[i])

print("\n\n Soma Diagonal: ")
for i in range(0 , len(matrix) - 1):
    print(matrix[i][i] + matrix[i + 1][i + 1])



question(11)

matrix = [[],[],[]]

for a in range(len(matrix)):
    for b in range(3):
        matrix[a].append(b)

print(f"Matrix: ")
for i in range(len(matrix)):
    print(matrix[i])

print("\n\n Soma Secundaria: ")
for i in range(0 , len(matrix) - 1):
    print(matrix[i][len(matrix[i]) - 1 - i] + matrix[i + 1][len(matrix[i]) - 2 - i])



question(12)

matrix = [[],[]]
# matrix2 = []  // use this matrix to save the transpost matrix
foo = []
x = 0
y = 0

for a in range(len(matrix)):
    for b in range(4):
        matrix[a].append(b)

print(f"Matrix: ")
for i in range(len(matrix)):
    print(matrix[i])

if len(matrix) == len(matrix[0]):
    x = len(matrix[0])
    y = len(matrix)
else:
    y = len(matrix)
    x = len(matrix[0])

print("\n\n Matrix Transposta: ")

for a in range(x):
    foo.clear()
    for b in range(y):
        foo.append(matrix[b][a])

    print(foo)
    # matrix2.append(foo)

# print(matrix2)



question(13)

matrix = [[],[],[],[]]

for a in range(len(matrix)):
    for b in range(1, 21):
        matrix[a].append(b)

print("Matrix: ")
for i in range(len(matrix)):
    print(matrix[i])

print("\n\nMatriz Triangular inferior: ")
for i in range(1, len(matrix)):
    matrix[i-1][i] = 0
matrix[i][i + 1] = 0

for i in range(0, len(matrix)):
    print(matrix[i])



question(14)

numeros = []
cartela = [[],[],[],[],[]]

for i in range(100):
    numeros.append(i)

random.shuffle(numeros)
for a in range(len(cartela)):
    for b in range(5):
        foo = int(numeros.pop())
        cartela[a].append(foo)

print("Cartela:")
x = pd.DataFrame(cartela, columns=[" "," "," "," "," "])
print(x.to_string(index=False))



question(15)


escolha = ["a","b","c","d"]

respostas = [[],[],[],[],[]]

resposta = []

acerto = 0
erro = 0

for a in range(len(respostas)):
    random.shuffle(escolha)
    for b in range(10):
        respostas[a].append(escolha[random.randrange(5)])

for a in range(10):
    random.shuffle(escolha)
    resposta.append(escolha[random.randrange(5)])

for a in range(len(respostas)):
    for b in range(10):
        if respostas[a][b] != resposta[b]:
            erro += 1
        else:
            acerto += 1
    print(f"{a+1}° Aluno: acertos = {acerto} / erros = {erro} ")
    acerto = 0
    erro = 0


question(16)

escolha = ["a","b","c","d", "e"]

respostas = {}

resposta = []

acerto = 0
ap = ""
t = 0

for i in range(1, 4):
    print(f"Informe a matriculo do {i}° ALuno: ",end=" ")
    n = int(input())
    respostas[n] = []

for a,x in respostas.items():
    random.shuffle(escolha)
    for b in range(10):
        respostas[a].append(escolha[random.randrange(5)])

for a in range(10):
    random.shuffle(escolha)
    resposta.append(escolha[random.randrange(5)])

print("\n\n")
for a,x in respostas.items():
    for b in range(10):
        if respostas[a][b] == resposta[b]:
            acerto += 1

    if acerto < 7:
        ap = "reprovado"
    else:
        ap = "aprovado"
        
    print(f"Aluno de Matricula {a+1}: respostas: {respostas[a]} / Acerto: {acerto*10}% - {ap} / Nota: {acerto}")
    t += acerto*10
    acerto = 0
    print("\n")
print(f"\n\nTaxa de acerto: {t /len(respostas)} %")


question(17)

escolha = ["a","b","c","d", "e"]

respostas = {}
# aluno = []
resposta = []

acerto = 0
acertos = [[],[],[]]

for i in range(10):
    print(f"Informe a matriculo do {i+1}° ALuno: ",end=" ")
    n = int(input())
    respostas[n] = [[],[],[]]
    # aluno += [[]]

for a,x in respostas.items():
    random.shuffle(escolha)
    for b in range(3):
        for c in range(10):
            respostas[a][b].append(escolha[random.randrange(5)])

for a in range(10):
    random.shuffle(escolha)
    resposta.append(escolha[random.randrange(5)])

print("\n\n")
for a,x in respostas.items():
    for b in range(len(x)):
        for c in range(10):
            if respostas[a][b][c] == resposta[b]:
                acerto += 1
        acertos[b].append(acerto)
        acerto = 0


#descompacta as notas em uma matriz de 10x3
#for a in range(len(acertos)):
#    for b in range(len(resposta)):
#        aluno[b].append(acertos[a][b])
#        
#for x in range(len(aluno)):
#    print(aluno[x], "\n\n")

  
foo = 0
for i in range(len(acertos)):
    for j in range(len(acertos[i])):
        if acertos[i][j] < 7:
            foo += 1
    print(f"\nPior Aluno da {i+1}° Prova: {min(acertos[i])} / Reprovados: {foo}")
    foo = 0


question(18)

matriz = [[],[],[]]
soma = []
r = 0

for a in range(len(matriz)):
    for b  in range(3):
        print(f"Insira o numero da posição ({a}, {b}): ", end=" ")
        n = float(input())
        matriz[a].append(n)

for a in range(len(matriz)):
    for b  in range(3):
        r += matriz[b][a]
    soma.append(r)
    r = 0

print("\n Matriz: ")
for i in range(len(matriz)):
    print(matriz[i])

print(f"\n Array: {soma}")



question(19)

matriz = {}
lista = ["Matrícula", "média das provas", "media dos Trabalhos", "nota final"]
nf = []
soma = 0

for a in range(5):
    print(f"Informe a {lista[0]}: ", end=" ")
    mat = int(input())
    matriz[mat] = []

print("\n")
for a,x in matriz.items():
    for b in range(1, len(lista)):
        print(f"Informe a {lista[b]} da matricula {a}: ", end=" ")
        foo = float(input())
        matriz[a].append(foo)
    print("\n")

for a,x in matriz.items():
    foo += matriz[a][0] + matriz[a][1]
    print(f"Matricula {a}: nota final = {foo}\n")
    nf.append(foo)
    foo = 0

for a,x in matriz.items():
    if matriz[a][0] + matriz[a][1] == max(nf):
        print(f"Matricula {a} com a maior nota de {max(nf)}")
        break
    soma += matriz[a][2]

print(f"Media das notas finais: {soma / len(matriz)}")


question(20)

matriz = [[],[],[]]
soma = 0
m1 = 0
m2 = 0

for a in range(len(matriz)):
    for b in range(6):
        matriz[a].append(random.randrange(10))

for a in range(len(matriz)):
    for b in range(len(matriz[a])):
        if b % 2 != 0:
            soma += matriz[a][b]

print(f"\nSoma das columas impares : {soma}")

for a in range(len(matriz)):
    for b in range(len(matriz[a])):
        if b == 1:
            m1 += matriz[a][b]
        elif b == 3:
            m2 += matriz[a][b]

print(f"\nMedia Aritimetica da segunda columna: {m1}")
print(f"Media Aritimetica da quarta columna: {m2}")
print("\n Matriz Original: ")

for i in range(len(matriz)):
    print(matriz[i])

print("\n Matriz Modificada: ")
for i in range(len(matriz)):
	matriz[i][len(matriz[a]) - 1] = matriz[i][0] + matriz[i][1]

for i in range(len(matriz)):
    print(matriz[i])


question(21)

a = [[],[]]
b = [[],[]]
c = [[],[]]
const = False

for x in range(2):
    for y in range(2):
        a[x].append(random.randrange(10))
        b[x].append(random.randrange(10))

while True:
    print("""\n
        1. Soma as duas matrizes
        2. Subtrair a primeira matriz da segunda
        3. Adicionar uma constante as duas matrizes
        4. Imprimir as matrizes
        5. Sair
        Escolha: """, end=" ")
    op = input()

    if const:
        a[lin][col] = constante
        b[lin][col] = constante

    c = [[],[]]

    if op == "1":
        for x in range(2):
            for y in range(2):
                c[x].append(a[x][y] + b[x][y])

        print("\nSoma das Matrizes A e B: ")
        PM(c)

    elif op == "2":
        for x in range(2):
            for y in range(2):
                c[x].append(a[x][y] - b[x][y])

        print("\nSubtração das Matrizes A e B: ")
        PM(c)
        
    elif op == "3":
        const = True
        print("\n Matriz 2x2\n")
        
        print("Informe a linha: ", end=" ")
        lin = int(input())
        
        print("Informe a coluna: ", end=" ")
        col = int(input())
        
        print("Informe a constante: ", end=" ")
        constante = int(input())

        
    elif op == "4":
        print("\n Matriz A:")
        PM(a)

        print("\n\n")
        print(" Matriz B:")
        PM(b)
    else:
        print("CYA.")
        break


question(22)

a = [[],[],[]]
b = [[],[],[]]
c = [[],[],[]]

for x in range(len(a)):
    for y in range(3):
        a[x].append(random.randrange(10))
        b[x].append(random.randrange(10))

for x in range(len(a)):
    for y in range(len(a[x])):
        c[x].append(a[x][y] + b[x][y])

print("Matriz A: ")
PM(a)

print("\nMatriz B: ")
PM(b)

print("\nMatriz C: ")
PM(c)



question(23)

a = [[],[],[]]
b = [[],[],[]]


for x in range(len(a)):
    for y in range(3):
        a[x].append(random.randrange(10))

for x in range(len(a)):
    for y in range(len(a[x])):
        b[x].append(a[x][y] ** 2)

print("Matriz A: ")
PM(a)

print("\nMatriz B: ")
PM(b)



question(24)

x = ""
c = 0
m = []
md = 0 # Maior na diagonal
mc = 0 # Maior em cima
mb = 0 # Maior em baixo
me = 0 # Maior na esquerda
mr = 0 # Maior na direita (right)


with open("matriz.txt", "r") as matrix:
	for line in matrix:
		m += [[]]
		for item in line:
			x += item
			if item == " ":
				x = ""
				pass
			elif item == "\n":
				x = ""
				pass
			elif len(x) == 2:
				m[c].append(x)
		c += 1

for i in range(m.count([])):
	m.remove([])

for a in range(len(m)):
	for b in range(len(m[a])):
		m[a][b] = int(m[a][b])

for a in range(len(m) - 3):
	for b in range(len(m[a]) - 3):
		foo = m[a][b] * m[a+1][b+1] * m[a+2][b+2] * m[a+3][b+3]
		if foo > md:
			md = foo
			
for a in range(len(m) - 3):
	for b in range(len(m[a])):
		foo = m[a+3][b] * m[a+2][b] * m[a+1][b] * m[a][b]
		if foo > mc:
			mc = foo

for a in range(len(m) - 3):
	for b in range(len(m[a])):
		foo = m[a][b] * m[a+1][b] * m[a+2][b] * m[a+3][b]
		if foo > mb:
			mb = foo

for a in range(len(m)):
	for b in range(0, len(m[a]), 4):
		foo = m[a][len(m[a]) - 1 - b] * m[a][len(m[a]) - 2 - b] * m[a][len(m[a]) - 3 - b] * m[a][len(m[a]) - 4 - b]
		if foo > me:
			me = foo

for a in range(len(m)):
	for b in range(len(m[a]) - 3):
		foo = m[a][b] * m[a][b+1] * m[a][b+2] * m[a][b+3]
		if foo > mr:
			mr = foo

valores = [md, mb, mc, me, mr]
nomes = ["Diagonal", "Baixo", "Cima", "Esquerda", "Direita"]
print(f"O maior produto de 4 numeros e na direção {nomes[valores.index(max(valores))]} com o valor {max(valores)}")



question(25)
