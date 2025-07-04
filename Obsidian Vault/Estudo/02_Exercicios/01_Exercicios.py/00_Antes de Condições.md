
# ===============================

# PYTHON I – INTRODUÇÃO AO PYTHON

# EXERCÍCIOS PRÁTICOS (SEM RESPOSTAS)

# ===============================

## 🧪 BLOCO 1 – FUNDAMENTOS E INPUT

### 1. Olá, Mundo com Nome

```python
# Crie um programa que pergunte seu nome e exiba:
# "Olá, <nome>! Seja bem-vindo ao Python."
nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Seja bem-vindo ao Python.")
````

### 2. Conversão de Tipos

```python
# Peça dois números via input() e imprima:
# - a soma
# - o tipo das variáveis originais
# - o tipo da soma
N1 = int(input("Digite o primeiro número: "))
N2 = int(input("Digite o segundo número: "))
print("A soma é", N1 + N2)
print("Tipo de N1:", type(N1))
print("Tipo da soma:", type(N1 + N2))
```

### 3. Média Aritmética

```python
# Receba 3 notas e exiba:
# - a média
# - se está aprovado (média ≥ 7) ou reprovado
N3 = int(input("Digite a terceira nota: "))
media = (N1 + N2 + N3) / 3
if media >= 7:
    print(f"Aprovado – média: {media:.2f}")
else:
    print(f"Reprovado – média: {media:.2f}")
```

### 4. Antecessor e Sucessor

```python
# Receba um número inteiro e exiba:
# - seu antecessor
# - seu sucessor
N4 = int(input("Digite um número: "))
print("Antecessor:", N4 - 1)
print("Sucessor:", N4 + 1)
```

---

## 🧪 BLOCO 2 – STRINGS

### 5. Formatação e Concatenação

```python
# Peça nome e idade, e mostre:
# "João tem 20 anos." usando f-string
idade = int(input("Qual sua idade? "))
print(f"{nome} tem {idade} anos.")
```

### 6. Contagem de Caracteres

```python
# Peça um texto e:
# - mostre o total de caracteres
# - quantas letras "a" aparecem
texto = input("Digite um texto: ")
total_caracteres = len(texto)
quantidade_a = texto.lower().count("a")
print(f"Total de caracteres: {total_caracteres}")
print(f"Quantidade de letras 'a': {quantidade_a}")
```

### 7. Substituição de Caracteres

```python
# Peça um texto e substitua todas as letras "e" por "*"
texto = input("Digite um texto: ")
texto_modificado = texto.replace("e", "*").replace("E", "*")
print("Texto modificado:", texto_modificado)
```

### 8. Substrings

```python
# Peça um texto e mostre:
# - os 5 primeiros caracteres
# - os 5 últimos
# - os caracteres entre a posição 3 e 8
texto = input("Digite um texto: ")
primeiros_5 = texto[:5]
ultimos_5 = texto[-5:]
entre_3_e_8 = texto[3:9]
print("5 primeiros caracteres:", primeiros_5)
print("5 últimos caracteres:", ultimos_5)
print("Caracteres da posição 3 a 8:", entre_3_e_8)
```

---

## 🧪 BLOCO 3 – LISTAS, TUPLAS, SETS E DICIONÁRIOS

### 9. Lista de Compras

```python
# Crie uma lista com 5 itens digitados pelo usuário e imprima:
# - a lista
# - o primeiro e último item
# - a lista em ordem alfabética
itens = int(input("Quantos itens você quer? "))
numeros = []
for i in range(itens):
    item = input("Digite um item da lista: ")
    numeros.append(item)
print("Lista original:", numeros)
print(f"{numeros[0]} é o primeiro item da lista")
print(f"{numeros[-1]} é o último item da lista")
lista_ordenada = sorted(numeros)
print(f"Lista ordenada: {lista_ordenada}")
```

### 10. Tupla de Notas

```python
# Armazene 4 notas em uma tupla e calcule:
# - a média
# - a maior nota
# - se a nota 10 está presente
contador = int(input("Quantas notas quer adicionar? "))
notas = []
for i in range(contador):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)
notas = tuple(notas)
media = sum(notas) / len(notas)
maior_nota = max(notas)
nt_10 = 10 in notas
print(f"Média: {media:.2f}")
print(f"Maior nota: {maior_nota}")
print(f"Nota 10 presente? {'Sim' if nt_10 else 'Não'}")
```

### 11. Set de Cidades

```python
# Peça 5 cidades visitadas e armazene em um set.
# Depois: peça +2 cidades (algumas podem repetir)
# e exiba o conjunto final (sem duplicatas)
cidades = set()
n_cidades = int(input("Quantas cidades quer adicionar? "))
for i in range(n_cidades):
    cidade = input(f"Digite a cidade {i+1}: ")
    cidades.add(cidade)

pergunta = input("Quer adicionar mais cidades? [Sim = 1 / Não = 2]: ")
if pergunta == "1":
    quantidade = int(input("Quantas cidades a mais quer adicionar? "))
    for i in range(quantidade):
        cidade = input(f"Digite a próxima cidade {i+1}: ")
        cidades.add(cidade)
else:
    print("Ok, sem adicionar novas cidades.")

print("Conjunto final de cidades visitadas:", cidades)
```

```python
# 12. Dicionário de Aluno
# Crie um dicionário com nome, idade e nota de um aluno.
# Mostre:
# - todos os dados
# - se ele está aprovado (nota ≥ 7)

aluno = {
    "nome": input("Nome do aluno: "),
    "idade": int(input("Idade do aluno: ")),
    "nota": float(input("Nota final: "))
}

print("Dados do aluno:", aluno)

if aluno["nota"] >= 7:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")
```
---
## 🧪 BLOCO 4 – CONDICIONAIS

### 13. Par ou Ímpar

```python
# Peça um número e diga se ele é par ou ímpar.
n1 = int(input("Digite um número: "))
if n1 % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
````

### 14. Calculadora de Aumento

```python
# Receba o salário de um funcionário e calcule:
# - aumento de 10% se salário ≤ 2000
# - aumento de 5% se > 2000
salario = float(input("Digite o salário: R$ "))
if salario <= 2000:
    novo_salario = salario * 1.10
else:
    novo_salario = salario * 1.05

print(f"Novo salário: R$ {novo_salario:.2f}")
```

### 15. Distância e Preço

```python
# Peça uma distância (em km) e calcule o valor da passagem:
# - até 200 km → R$ 0,50 por km
# - acima de 200 km → R$ 0,45 por km
distancia = float(input("Digite a distância (em km): "))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"Preço da passagem: R$ {preco:.2f}")
```

