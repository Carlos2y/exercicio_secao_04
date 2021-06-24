import random
import math
import numpy
import pandas as pd


def question(n):
    if n < 10 and n > 0:
        n = "0" + str(n)
    print("\n\n","---" * 26, "\n\n Questão {} \n\n".format(n))

'''

question(1)

v = [1,0,5,-2,-5,7]

foo = v[0] + v [1] + v[5]
print(f"Soma: {foo} \n")

v[4] = 100
print(v[4], "\n")

for i in range(len(v)):
    print(f"V[{i}] = {v[i]}")




question(2)

lista = []

for i in range(6):
    print(f"Informe o {i + 1}°: ", end=" ")
    foo = int(input())

    lista.append(foo)

print(f"Valores: {lista}")



question(3)

n = []
n2 = []

for i in range(10):
    print(f"Informe o {i+1}°:", end=" ")
    foo = float(input())
    n.append(foo)
    n2.append(foo ** 2)

print(f"\n Valores : {n} \n Valores ao quadrado: {n2} ")



question(4)

lista = []

for i in range(8):
    lista.append(random.randrange(0,100))

x = random.randrange(0, 8)
y = random.randrange(0, 8)
print(f"Soma: {lista[x] + lista[y]}")



question(5)

lista = []
c = 0

for i in range(10):
    lista.append(random.randrange(0, 1000))

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        c += 1
print(f"Existem {c} valores pares")




question(6)

v = []

for i in range(10):
    print(f"Informe o {i+1}° valor: ", end=" ")
    foo = float(input())
    v.append(foo)

print(f"\n Maior: {max(v)} \n Menor: {min(v)}")




question(7)

v = []

for i in range(10):
    print(f"Informe o {i+1}° valor: ", end=" ")
    foo = float(input())
    v.append(foo)

print(f" Vetor: {v} \n Maior: {max(v)} \n Index: [{v.index(max(v))}]")



question(8)

v = []

for i in range(1, 7):
    v.append(i)
print(v)
print(v[::-1])



question(9)

v = []

for i in range(2, 14, 2):
    v.append(i)
print(v)
print(v[::-1])



question(10)

v = []

for i in range(15):
    v.append(random.randrange(0,11))
print(v)
print( sum(v) / len(v) )



question(11)

v = []
c = 0
p = 0

for i in range(10):
    v.append(random.randrange(-100, 100))

for i in range(10):
    if v[i] <= 0:
        c += 1
    else:
        p += v[i]

print(f" Numeros negativos: {c} \n Soma dos positivos: {p} ")



question(12)

lista = []

for i in range(1, 6):
    foo = random.randrange(0,100)
    print(f"{i}° valor: {foo}")
    lista.append(foo)
    
print(f"\n Maior Valor: {max(lista)} \n Menor Valor: {min(lista)} \n " +
      f"Media dos valores: {max(lista) / len(lista)}")



question(13)


lista = []

for i in range(1, 6):
    foo = random.randrange(0,100)
    print(f"{i}° valor: {foo}")
    lista.append(foo)
    
print(f"\n Index do maior: {lista.index(max(lista))}" +
      f"\n Index do menor: {lista.index(min(lista))}")



question(14)

v = []
c = []

for i in range(10):
    v.append(random.randrange(0,100))
    
for i in range(10):
    if v.count(v[i]) >= 2:
        if v[i] not in c:
            c.append(v[i])
print(c)



question(15)

v = []

for i in range(20):
    v.append(random.randrange(0,100))

print("Duplicatas removidos: ",end=" ")
for i in range(len(v)):
    try:
        if v.count(v[i]) > 1:
            print(v[i],end=" ")
            v.remove(v[i])
    except:
        break

v.sort()
print("\n\n Lista: ",v)




question(16)

v = []
for i in range(5):
    v.append(random.randrange(0,100))

while True:
        
    print("""
        1. Ordem Direta
        2. Ordem Inversa
        Sair.
    Opção: """, end=" ")
    op = input()
    
    if op == "1":
        v.sort()
        print(f"Ordem direta: {v}")

    elif op == "2":
        print(f"Ordem Inversa: {v[::-1]}")

    else:
        print("Codigo Invalido")



question(17)

v = []

for i in range(10):
    v.append(random.randrange(-100, 100))

print(v)

for i in range(len(v)):
    if v[i] < 0:
        v[i] = 0

print(v)



question(18)

v = []

for i in range(100):
    v.append(random.randrange(0,100))

print("Informe um numero: ", end=" ")
num = int(input())

print(f"Multiplos de {num} no vetor:", end=" ")
for i in range(max(v)):
    if i * num in v:
        print(num * i, end=" ")




question(19)

v = []

for i in range(50):
    foo = (i + 5 * i) % (i + 1)
    v.append(foo)

print(f"Vetor: {v}")



question(20)

v = []
imp = []

for i in range(10):
    v.append(random.randrange(0,50))

v.sort()

for i in range(10):
    if v[i] % 2 != 0:
        imp.append(v[i])


print("Vetores: \n Vetor || Impares ")
for i in range(10):
    print(f"    {v[i]} ||", end=" ")
    try:
        print(f" {imp[i]}",end=" ")
    except:
        print(" ", end=" ")
    print("\n")



question(21)

a = []
b = []
c = []

for i in range(10):
    a.append(random.randrange(0,100))
    b.append(random.randrange(0,100))

for i in range(10):
    c.append(a[i] - b[i])

print(f"Vetor c: {c}")


question(22)

a = []
b = []
c = []

for i in range(10):
    a.append(random.randrange(0,100))
    b.append(random.randrange(0,100))

for i in range(10):
    c.append(a[i])
    c.append(b[i])

print(f"Vetor: {c}")



question(23)

x = []
y = []
s = 0

for i in range(5):
    x.append(random.randrange(0,100))
    y.append(random.randrange(0,100))

print(f"Vetor 1: {x} \n Vetor 2: {y} \n")

for i in range(5):
    s += x[i] * y[i]

print(f"Produto Escalar: {s}")



question(24)

x = {}
maior = 0
menor = 100

for i in range(10):
    x[i] = float(str(random.randrange(1,3)) + "." + str(random.randrange(100)))

for i in range(10):
    if x[i] < menor:
        menor = x[i]

    if x[i] > maior:
        maior = x[i]

for a, b in x.items():
    if menor == b:
        print(f"Aluno {a} e o menor aluno com altura de {b} metros.")

    if maior == b:
        print(f"Aluno {a} e o maior aluno com altura de {b} metros.")



question(25)

v = [] # vetor dos naturais
m = [] # multiplos de N
c = 0 # contador

for i in range(100):
    m.append(i * 7)
    
while len(v) < 100:
    c += 1
    if c not in m:
        if "7" not in str(c):
            v.append(c)

print(v)



question(26)

v = []
soma = 0
x = 0
y = 0
media = 0
r = 0

for i in range(10):
    v.append(i)

for i in range(len(v)):
    soma += v[i]

media = soma / len(v)

for i in range(len(v)):
    x = v[i] - media
    y +=  x * x

r = math.sqrt(y / len(v))

print(f"Desvio padrão: \n Vetor: {v} \n Desvio: {r:.2f}")


question(27)

v = []
t = []
foo = 0

for i in range(10):
    v.append(random.randrange(3,1000))

for i in range(len(v)):

    if v[i] % 2 == 0:
        pass
    else:
        for x in range(1, i + 1):
            
            foo = v[i] / x
            if int(foo) == foo:
                t.append(x)
                
        if len(t) == 2:
            print(f"Index: {i} Valor: {v[i]}")
            t.clear()
        else:
            t.clear()



question(28)

v = []
v1 = []
v2 = []

for i in range(10):
    v.append(random.randrange(3,1000))

for i in range(len(v)):
    if v[i] % 2 == 0:
        v1.append(v[i])
    else:
        v2.append(v[i])

print(v1)
print(v2)



question(29)

v = []
x = 0

for i in range(10):
    v.append(random.randrange(1, 11))

print(f" Pares: ", end=" ")
for i in range(10):
    if v[i] % 2 == 0:
        print(v[i],end=" ")
        x += v[i]
        
print(f"\n Soma dos pares: {x}\n ")
x = 0
print(f" Impares: ", end=" ")
for i in range(10):
    if v[i] % 3 == 0:
        print(v[i], end=" ")
        x += v[i]
        
print(f"\n Soma dos impares: {x}")



question(30)

a = []
b = []
c = []

for i in range(10):
    a.append(random.randrange(11))
    b.append(random.randrange(11))

for i in range(10):
    if a[i] in b:
        if a[i] not in c:
            c.append(a[i])

print(c)



question(31)

a = []
b = []
c = []

for i in range(10):
    a.append(random.randrange(110))
    b.append(random.randrange(110))

for i in range(10):
    if a[i] not in c:
        c.append(a[i])
        
    if b[i] not in c:
        c.append(b[i])

c.sort()
print(c)
print(set(a + b) == set(c))


question(32)

x = []
y = []
a = []
d = []
foo = 0
foo2 = 0
p = ["VALORES A|B", "SOMA", "PRODUTO", "DIFERENÇA", "INTERSEÇÃO"]

while True:
    if len(x) == 5 and len(y) == 5: # tamanho das listar precisam ser iguais len(x) == len(y)
        break
    else:
        if len(x) < 5:
            foo = random.randrange(10)
            if foo not in x:
                x.append(foo)

        if len(y) < 5:
            foo = random.randrange(1, 11)
            if foo not in y:
                y.append(foo)

a = x

for i in range(len(x)):
    if x[i] not in y:
        foo = x[i]
    else:
        foo = ""

    if x[i] in y:
        foo2 = x[i]
    else:
        foo2 = ""

    if y[i] not in a:
        a.append(y[i])

    d.append([f"{x[i]} {y[i]}", x[i] + y[i], x[i] * y[i], foo, foo2])


x = pd.DataFrame(d, columns=p)

print(x.to_string(index=False))

print(f"\n\n União: {a}")



question(33)

v = []

for i in range(15):
    print("abc: ",end=" ")
    foo = int(input())
    v.append(foo)

if 0 in v:
    for i in range(v.count(0)):
        v.remove(0)
print(v)



question(34)

v = []

while len(v) < 10:
    print("Informe um numero: ", end=" ")
    foo = int(input())

    if foo not in v:
        v.append(foo)
    else:
        print(f"\n Digite outro numero. \n")

print(f"Vetor: {v}")



question(35)

a = str(random.randrange(10000))
b = str(random.randrange(10000))

va = []
vb = []
vc = []

x = list(a)
x.remove(min(a))
x.insert(0, min(a))
va = x

x = list(b)
x.remove(min(b))
x.insert(0, min(b))
vb = x

x = 5

for i in range(x):
    if i > len(va) and i > len(vb):
        vc.append( int(0) + int(0) )

    elif i > len(va):
        vc.append( int(0) + int(vb[i]) )

    elif i < len(vb):
        vc.append( int(va[i]) + int(vb[i]) )

    elif i > len(va) or i > len(vb):
        vc.append( int(va[i]) + int(vb[i]) )

print(f"""
    Numero A: {a}
    Numero B: {b}
    Vetor A: {va}
    Vetor B: {vb}
    Vetor c: {vc}
""")



question(36)

v = []

for i in range(10):
    v.append(random.randrange(100))


print(f"Vetor Desordenado: {v}")

v.sort()

print(f"Vetor Ordenado: {v}")



question(37)

v = []

for i in range(11):
    v.append(random.randrange(1000))

v.sort()

print(f"Vetor Ordenado: {v}")


question(37)

v = []
for i in range(11):
    v.append(random.randrange(100))


v.sort()
x = v.copy()
print(x)




question(38)

v = []

for i in range(10):
    foo = random.randrange(100)
    print(f"{i + 1}° Valor: {foo}")
    v.append(foo)

v.sort()
print(f"\n\nVetor: {v}")



question(39)

n = 10

v = [[1], [1,1]]

for i in range(1, n):

    l = [1]
    
    for x in range(0, len(v[i])-1):
        l += [ v[i][x] + v[i][x+1] ]
        
    l += [1]
    v += [l]


for i in range(len(v)):
    print(v[i])

panda = pd.DataFrame(v)

print("\n\n", panda)

'''
