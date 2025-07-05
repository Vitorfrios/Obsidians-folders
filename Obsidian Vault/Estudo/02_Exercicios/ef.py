# 🔁 1. Contagem Simples
# Mostre os números de 1 a 10, um por linha.
lista = []
qnt = int(input("quantos nuumqeos quer "))
for i in range (qnt):
    num = int(input(f"digite o {i+1} numero "))
    print(num)
    lista.append(num)
print(lista)
print("---"*15)

# 🔁 2. Contagem Regressiva
# Mostre os números de 10 a 1 (ordem decrescente).
for i in range (10,0,-1):
    print(i,end=" ")
print()
print("---"*15)

# 🔁 3. Números Pares
# Mostre todos os números pares entre 1 e 20.
for i in range (0,20,+2):
    print(i,end=" ")
print()
print("---"*15)

# 🔁 4. Tabuada
# Peça um número e mostre a tabuada dele de 1 a 10.
n=int(input("digite um numero "))
for i in range (1,11):
    mat = n*i
    print(mat,end=" ")
print()
print("---"*15)

# 🔁 5. Soma de Números
# Peça 5 números ao usuário e mostre a soma total.
qnt = int(input("quantos numeros quer? "))
numeros = []
for i in range(qnt):
    n1 = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n1)
soma = sum(numeros)
print(soma)
print()
print("---" * 15)


# 🔁 6. Nome por Letras
# Peça um nome e mostre cada letra separadamente.
nome = input("digite o seu nome ")
for i in nome:
    print(i,end="")
    print()


# 🔁 7. Lista de Palavras
# Crie uma lista com 4 palavras e mostre cada uma com seu número de letras.
nomes = []
qnt3 = int(input("quantos nomes quer "))
for i in range (qnt3):
    name = input(f"Digite o nome {i+1} ")
    nomes.append(name)
for nam in nomes:
    for i in nam:
        print(i,end=" ")
    print(f"- {len(nam)} letras")

# 🔁 8. Média de Notas
# Peça 4 notas e calcule a média.

qnt4 = int(input("quantos numeros p media "))
numeros1 =[]
for i in range(qnt4):
    n=int(input(f"Digite o numero {i+1} "))
    numeros1.append(n)
cont = len(nam)
some=sum(numeros1)
media = some/cont
print(media)

# 🔁 9. Contar Vogais
# Peça uma palavra e mostre quantas vogais ela tem.

palavra = input("De-me uma palavra: ")
cont = []
vogais = "aeiouAEIOU"

for letra in palavra:
    if letra in vogais:
        cont.append(letra)

print(f"Número de vogais: {len(cont)}")
print(f"Vogais encontradas: {cont}")


# 🔁 10. Multiplicação Acumulada
# Peça 5 números e mostre o resultado da multiplicação entre eles.
from math import prod
qnt5 = int(input("Digite quantos numeros vc quer "))
lists = []
for i in range(qnt5):
    n = int(input(f" digite o numero {i+1} "))
    lists.append(n)
conta = prod(lists)
print(conta) 