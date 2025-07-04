# 1. Maior de Dois Números
# Peça dois números e informe qual é o maior (ou se são iguais).

num = []
qnt = int(input("digite a quantidade de numeros desejados "))
for i in range (qnt):
    numeros = int(input(f"digite o numero {i+1}"))
    num.append(numeros)

if len(num) == 0:
    print("Nenhum número foi digitado.")
elif all(x == num[0] for x in num):
    print("Todos os números são iguais.")
else: print(f"o maior numero é {max(num)} e o menor é {min(num)}")



# 2. Verificação de Idade
# Peça a idade de uma pessoa e diga se ela é:
# - Criança (0–12)
# - Adolescente (13–17)
# - Adulto (18–59)
# - Idoso (60+)

qnt2 = int(input("Quantas pessoas você quer verificar? "))
pessoas = []
for i in range(qnt2):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    if 0 <= idade <= 12:
        Verificar = "É criança"
        print("É criança")

    elif 13 <= idade <= 17:
        Verificar = "Adolescente"
        print("Adolescente")

    elif 18 <= idade <= 59:
        Verificar = "Adulto"
        print("Adolescente")

    elif idade >= 60:
        Verificar = "Idoso"
        print("Idoso")
    else:
        Verificar = "Idade inválida"
        

    pessoas.append((idade, Verificar))

print(pessoas)


# 3. Nota para Conceito
# Peça uma nota (0 a 10) e informe o conceito:
# - A (9 a 10)
# - B (8 a 8.9)
# - C (7 a 7.9)
# - D (6 a 6.9)
# - F (abaixo de 6)

qnt3 = int(input("Digite quantas notas quer verificar: "))
notas = []

for i in range(qnt3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    if nota < 6:
        notas.append((i+1, nota, "F"))
    elif 6 <= nota <= 6.9:
        notas.append((i+1, nota, "D"))
    elif 7 <= nota <= 7.9:
        notas.append((i+1, nota, "C"))
    elif 8 <= nota <= 8.9:
        notas.append((i+1, nota, "B"))
    elif 9 <= nota <= 10:
        notas.append((i+1, nota, "A"))
    else:
        notas.append((i+1, nota, "Nota inválida"))

print(notas)



# 4. Número Negativo ou Positivo
# Peça um número e diga se ele é positivo, negativo ou zero.
qnt4 = int(input("Digite quantos numeros quer "))
nmbr = []
for i in range(qnt4):
    n1 = int(input("digite o numero "))
    if n1 > 0:
        print("positivo")
        classi = "positivo"
    elif n1 < 0 :
        print("negativo")
        classi ="negativo"
    elif n1==0: 
        print("zero")
        classi = "zero"
    nmbr.append((n1,classi))
print(nmbr)

# 5. Login Simples
# Peça um nome de usuário e uma senha.
# Valide se eles são "admin" e "1234", e diga se o login foi bem-sucedido ou não.
user = {
    "admin": "1234",
    "joao": "senha123",
    "maria": "abc987"
}
usuario = input("seu user ")
senha = input("sua senha")

if usuario in user and user[usuario] == senha:
        print("Login bem-sucedido!")
else:
    print("Usuário ou senha incorretos.")


# 6. Par, Ímpar ou Zero
# Peça um número e diga se ele é par, ímpar ou zero (caso especial).
qnt5 = int(input("Digite quantos umeros quer "))
nmrs = []
for i in range(qnt5):
    nu = int(input(f"digite o {i+1}º numero "))
    if nu == 0:
        print("zero")
        cls = "zero"
    elif nu % 2 == 0:
        print("par")
        cls = "par"
    else:cls = "impar" ;print("impar")
    nmrs.append((nu,cls))
print(nmrs)

# 7. Calculadora com Operador
# Peça dois números e uma operação (+, -, *, /) e exiba o resultado.

num1 = int(input("digite o prieiro num "))
num2 = int(input("digite o seg num "))
op = input("digite o operador (+, -, *, /) ")
if op == "+":
    sum = num1+num2
    print(sum)
elif op == "-":
    sum = num1-num2
    print(sum)
elif op== "/":
    sum = num1/num2
    print(sum)
elif op == "*":
    sum = num1*num2
    print(sum)

# 8. Aposentadoria
# Peça a idade e o tempo de contribuição de uma pessoa.
# Diga se ela pode se aposentar (idade ≥ 60 e contribuição ≥ 30 anos).
id = int(input("digite sua idade "))
cont = int (input("tempo de contribuição "))
if id >= 60 and cont >= 30:
    print("pode aposentar" )
else:print("nao pode aposentar")