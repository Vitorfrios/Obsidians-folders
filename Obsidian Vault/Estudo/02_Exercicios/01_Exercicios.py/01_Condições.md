- [[Python]] 

# 1. Maior de Dois Números  
Peça dois números e informe qual é o maior (ou se são iguais).

```python
num = []
qnt = int(input("Digite a quantidade de números desejados: "))
for i in range(qnt):
    numeros = int(input(f"Digite o número {i+1}: "))
    num.append(numeros)

if len(num) == 0:
    print("Nenhum número foi digitado.")
elif all(x == num[0] for x in num):
    print("Todos os números são iguais.")
else:
    print(f"O maior número é {max(num)} e o menor é {min(num)}")
````

---

# 2. Verificação de Idade

Peça a idade de uma pessoa e diga se ela é: Criança (0–12), Adolescente (13–17), Adulto (18–59), Idoso (60+).

```python
qnt2 = int(input("Quantas pessoas você quer verificar? "))
pessoas = []
for i in range(qnt2):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    if 0 <= idade <= 12:
        classificacao = "Criança"
        print("É criança")
    elif 13 <= idade <= 17:
        classificacao = "Adolescente"
        print("Adolescente")
    elif 18 <= idade <= 59:
        classificacao = "Adulto"
        print("Adulto")
    elif idade >= 60:
        classificacao = "Idoso"
        print("Idoso")
    else:
        classificacao = "Idade inválida"
        print("Idade inválida")
    pessoas.append((idade, classificacao))

print(pessoas)
```

---

# 3. Nota para Conceito

Peça uma nota (0 a 10) e informe o conceito: A (9 a 10), B (8 a 8.9), C (7 a 7.9), D (6 a 6.9), F (abaixo de 6).

```python
qnt3 = int(input("Digite quantas notas quer verificar: "))
notas = []

for i in range(qnt3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    if nota < 6:
        conceito = "F"
    elif 6 <= nota <= 6.9:
        conceito = "D"
    elif 7 <= nota <= 7.9:
        conceito = "C"
    elif 8 <= nota <= 8.9:
        conceito = "B"
    elif 9 <= nota <= 10:
        conceito = "A"
    else:
        conceito = "Nota inválida"
    notas.append((i+1, nota, conceito))

print(notas)
```

---

# 4. Número Negativo ou Positivo

Peça um número e diga se ele é positivo, negativo ou zero.

```python
qnt4 = int(input("Digite quantos números quer: "))
nmbr = []
for i in range(qnt4):
    n1 = int(input(f"Digite o número {i+1}: "))
    if n1 > 0:
        print("Positivo")
        classi = "positivo"
    elif n1 < 0:
        print("Negativo")
        classi = "negativo"
    else:
        print("Zero")
        classi = "zero"
    nmbr.append((n1, classi))
print(nmbr)
```

---

# 5. Login Simples

Peça um nome de usuário e uma senha. Valide se eles são "admin" e "1234", e diga se o login foi bem-sucedido ou não.

```python
usuarios = {
    "admin": "1234",
    "joao": "senha123",
    "maria": "abc987"
}
usuario = input("Seu usuário: ")
senha = input("Sua senha: ")

if usuario in usuarios and usuarios[usuario] == senha:
    print("Login bem-sucedido!")
else:
    print("Usuário ou senha incorretos.")
```

---

# 6. Par, Ímpar ou Zero

Peça um número e diga se ele é par, ímpar ou zero (caso especial).

```python
qnt5 = int(input("Digite quantos números quer: "))
nmrs = []
for i in range(qnt5):
    nu = int(input(f"Digite o {i+1}º número: "))
    if nu == 0:
        print("Zero")
        cls = "zero"
    elif nu % 2 == 0:
        print("Par")
        cls = "par"
    else:
        print("Ímpar")
        cls = "impar"
    nmrs.append((nu, cls))
print(nmrs)
```

---

# 7. Calculadora com Operador

Peça dois números e uma operação (+, -, \*, /) e exiba o resultado.

```python
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
op = input("Digite o operador (+, -, *, /): ")

if op == "+":
    resultado = num1 + num2
elif op == "-":
    resultado = num1 - num2
elif op == "*":
    resultado = num1 * num2
elif op == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operador inválido"

print(f"Resultado: {resultado}")
```

---

# 8. Aposentadoria

Peça a idade e o tempo de contribuição de uma pessoa. Diga se ela pode se aposentar (idade ≥ 60 e contribuição ≥ 30 anos).

```python
idade = int(input("Digite sua idade: "))
contribuicao = int(input("Digite seu tempo de contribuição (anos): "))

if idade >= 60 and contribuicao >= 30:
    print("Pode se aposentar")
else:
    print("Não pode se aposentar")
```

---

