- [[Python]] 

# For

---

```python 
gamesList = ["Fifa", "God of War", "Red Dead 2", "Uncharted"]

for list in gamesList:
    print(list)

# 1 - Quando a condição for atendida, o loop será encerrado
for list in gamesList:
    if list == "God of War":
        break
    print(list)

# 2 - Quando a condição for atendida, o loop vai para a próxima iteração
for list in gamesList:
    if list == "God of War":
        continue
    print(list)

# 3 - Avaliação Jogo
gameName = input("Digite o nome do jogo\\n")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo\\n"))

sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota para o jogo \\n"))
    sum += note
print(f"Média de avaliação do jogo {gameName} é: {sum/gameRating}")


```


### 🔁 1. Contagem Simples

Mostre os números de 1 a 10, um por linha.

```python
lista = []
qnt = int(input("quantos nuumqeos quer "))
for i in range(qnt):
    num = int(input(f"digite o {i+1} numero "))
    print(num)
    lista.append(num)
print(lista)
print("---"*15)
```

---

### 🔁 2. Contagem Regressiva

Mostre os números de 10 a 1 (ordem decrescente).

```python
for i in range(10, 0, -1):
    print(i, end=" ")
print()
print("---"*15)
```

---

### 🔁 3. Números Pares

Mostre todos os números pares entre 1 e 20.

```python
for i in range(0, 20, 2):
    print(i, end=" ")
print()
print("---"*15)
```

---

### 🔁 4. Tabuada

Peça um número e mostre a tabuada dele de 1 a 10.

```python
n = int(input("digite um numero "))
for i in range(1, 11):
    mat = n * i
    print(mat, end=" ")
print()
print("---"*15)
```

---

### 🔁 5. Soma de Números

Peça 5 números ao usuário e mostre a soma total.

```python
qnt = int(input("quantos numeros quer? "))
numeros = []
for i in range(qnt):
    n1 = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n1)
soma = sum(numeros)
print(soma)
print()
print("---" * 15)
```

---

### 🔁 6. Nome por Letras

Peça um nome e mostre cada letra separadamente.

```python
nome = input("digite o seu nome ")
for i in nome:
    print(i, end=" ")
    print()
```

---

### 🔁 7. Lista de Palavras

Crie uma lista com 4 palavras e mostre cada uma com seu número de letras.

```python
nomes = []
qnt3 = int(input("quantos nomes quer "))
for i in range(qnt3):
    name = input(f"Digite o nome {i+1} ")
    nomes.append(name)
for nam in nomes:
    for i in nam:
        print(i, end=" ")
    print(f"- {len(nam)} letras")
```

---

### 🔁 8. Média de Notas

Peça 4 notas e calcule a média.

```python
qnt4 = int(input("quantos numeros p media "))
numeros1 = []
for i in range(qnt4):
    n = int(input(f"Digite o numero {i+1} "))
    numeros1.append(n)
cont = len(numeros1)
some = sum(numeros1)
media = some / cont
print(media)
```

---

### 🔁 9. Contar Vogais

Peça uma palavra e mostre quantas vogais ela tem.

```python
palavra = input("De-me uma palavra: ")
cont = []
vogais = "aeiouAEIOU"

for letra in palavra:
    if letra in vogais:
        cont.append(letra)

print(f"Número de vogais: {len(cont)}")
print(f"Vogais encontradas: {cont}")
```

---

### 🔁 10. Multiplicação Acumulada

Peça 5 números e mostre o resultado da multiplicação entre eles.

```python
from math import prod

qnt5 = int(input("Digite quantos numeros vc quer "))
lists = []
for i in range(qnt5):
    n = int(input(f"digite o numero {i+1} "))
    lists.append(n)
conta = prod(lists)
print(conta)
```

---


# ====================

# While


## 🔁 O que é o `while`?

Imagina que o `while` é como um **semáforo**:  
Enquanto a luz estiver **verde (condição verdadeira)**, os carros **continuam passando (o código continua repetindo)**.  
Quando fica **vermelho (condição falsa)**, os carros **param (o laço termina)**.

### 🧠 Tradução do `while`:

```python
while condição:
    faça isso
```

---

## 🚦 Exemplo simples

```python
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
```

🧒 Explicando:

- Começa com `contador = 1`
    
- Enquanto `contador` for menor ou igual a 5, ele imprime e soma +1.
    
- Quando chegar em 6, para de repetir.
    

📤 Saída:

```
1
2
3
4
5
```

---

## 🔁 Quando usar `while`?

Use quando:

- Você **não sabe quantas vezes vai repetir**.
    
- Vai depender de **algo que o usuário digita**, ou uma **resposta de fora**.
    

---

## 🛑 Cuidado com o loop infinito!

```python
while True:
    print("Nunca vai parar...")
```

😱 Isso nunca para, porque a condição é **sempre verdadeira**!

Você só sai com:

```python
break
```

---

## 🧪 Exemplo com `break` (parar quando quiser)

```python
while True:
    nome = input("Digite seu nome (ou 'sair'): ")
    if nome == "sair":
        break
    print(f"Olá, {nome}!")
```

---

## 🔄 Exemplo comum com média de notas:

```python
nota = 0
soma = 0
qtd = 0

while nota != -1:
    nota = float(input("Digite a nota (ou -1 para parar): "))
    if nota != -1:
        soma += nota
        qtd += 1

print("Média:", soma / qtd)
```

### 📌 Por que usamos `nota = 0` **antes** do `while`?

```python
nota = 0
while nota != -1:
    # código...
```

---

### 🧒 Explicação simples:

A gente **precisa criar a variável `nota` antes de usar ela no `while`**.

Se não fizer isso, o Python vai dizer:

> ❌ “Ei! Que nota é essa? Nunca ouvi falar dessa variável!”

---

### 🔄 Mas por que `0`?

A gente coloca `0` **só para iniciar** com algum valor diferente de `-1`, que é o valor que **faz o `while` parar**.

- Se colocasse `nota = -1` logo no começo, o `while nota != -1` **já daria falso** e **nem entraria no laço**.
    
- Com `nota = 0`, garantimos que o laço comece rodando.
    

---

### 🔁 Depois disso, dentro do `while`, a variável `nota` **é sobrescrita** com o valor digitado pelo usuário:

```python
nota = float(input("Digite a nota: "))  # agora 'nota' vale o que o usuário digitou
```

---

### 🧠 Resumo:

| Linha               | O que faz?                                             |
| ------------------- | ------------------------------------------------------ |
| `nota = 0`          | Cria a variável com um valor inicial                   |
| `while nota != -1`  | Roda enquanto a nota **não** for `-1`                  |
| `nota = float(...)` | Atualiza o valor de `nota` com o que o usuário digitou |

---
# --------------------------
# Exercícios em Python

## 🔁 1. Contagem até N
Conta números anteriores ou posteriores a um valor dado.

```python
def contagem():
    while True:
        entrada = (input("Digite quantos números quer ver: "))
        if entrada.isdigit() and int(entrada) > 0:
            nmber = int(entrada)
            break
        else: 
            print("Digite um numero inteiro positivo ")
    
    while True:
        posi = input("Deseja ver os anteriores ou posteriores? ").lower()
        if posi in ["anterior", "anteriores", "ante", "posterior", "posteriores", "poste"]:
            break
        else: 
            print("Digite apenas 'posteriores' ou 'anteriores' ")
    
    while True: 
        entrada = input("Qual numero? ")
        if entrada.lstrip('-').isdigit():
            n = int(entrada)
            break
        else: 
            print("Digite um inteiro válido, pode ser negativo")
    
    count = 1  # Inicializa o contador
    
    while count <= nmber:
        if posi in ["anterior", "anteriores", "ante"]:
            print(n - count)
        elif posi in ["posterior", "posteriores", "poste"]:
            print(n + count)
        else:
            print("Opção inválida")
            return contagem()  # Reinicia a função
        count += 1
```

---

## 🔁 2. Senha Correta
Validação de senha com loop infinito até acertar.

```python
def Vsenha():
    while True:
        senha = input("Digite a senha: ")
        if not senha.isdigit():
            print("A senha deve conter apenas números.")
            continue
        if not senha:
            print("Senha não pode estar vazia!")
            continue
        if senha == "1234":
            print("Acesso permitido!")
            break
        else: 
            print(f"Senha incorreta: {senha}")
```

---

## 🔁 3. Número Positivo
Pede um número positivo e valida a entrada.

```python
def pedir_numero():
    while True:
        entrada = input("Digite um número: ")
        if entrada.isdigit() and int(entrada) > 0:
            print(f"Número positivo: {entrada}")
            break
        else: 
            print("Digite um número positivo inteiro.")
```

---

## 🔁 4. Jogo da Soma
Soma números até atingir ou ultrapassar 100.

```python
def jogo_da_soma():
    cont = 0 
    soma = 0
    while soma <= 100:
        while True:
            n1 = input("Digite o primeiro número: ")
            if not n1.isdigit():
                print("Digite um número inteiro (ex: '1')")
            else:    
                break
        while True:
            n2 = input("Digite o segundo número: ")
            if not n2.isdigit():
                print("Digite um número inteiro (ex: '1')")
            else:    
                break

        soma += int(n1) + int(n2)
        cont += 1 
        if soma <= 100:
            print(f"Rodada {cont}: Soma atual = {soma}")
        else:
            print(f"Soma final ({cont} rodadas): {soma}")
            break
```

---

## 🔁 5. Contar Palavras
Conta palavras até o usuário digitar "fim".

```python
def contar_palavras():
    usr = " "
    palavras = []
    while usr != "fim":
        usr = input("Digite uma palavra: ").strip().lower()
        while True:
            if usr == "":
                print("Digite uma palavra válida.")
                break
            elif usr == "fim":
                print(f"Você digitou {len(palavras)} palavras: {', '.join(palavras)}")
                return
            else: 
                palavras.append(usr)
                break
```

---

## 🔁 6. Acertar o Número
Jogo de adivinhação com dicas e limite de tentativas.

```python
from random import randint

def jogo_adivinha():
    palt = None
    # Configuração do jogo
    while True:
        entrada = input("Digite quantas tentativas quer: ").strip()
        if entrada.isdigit():
            count = int(entrada)
            break
        else:
            print("Digite um número válido.")

    while True:
        entrada = input("Digite o número mínimo: ")
        if entrada.isdigit():
            n1 = int(entrada)
            break
        else:
            print("Digite um número válido.")

    while True:
        entrada = input("Digite o número máximo: ")
        if entrada.isdigit():
            n2 = int(entrada)
            if n2 > n1:
                break
            else:
                print("O máximo deve ser maior que o mínimo.")
        else:
            print("Digite um número válido.")

    rand = randint(n1, n2)
    print(f"Você tem {count} tentativas.")

    # Loop principal do jogo
    while palt != rand and count > 0:
        entrada = input(f"Digite um número entre {n1} e {n2}: ")
        if entrada.isdigit():
            palt = int(entrada)
        else:
            print("Digite um número válido.")
            continue

        if palt != rand:
            count -= 1
            print(f"Tentativas restantes: {count}")
        else:
            print(f"Parabéns! O número era {rand}.")

    if count == 0:
        print(f"Você perdeu. O número era {rand}.")
```

---

## 🔁 7. Soma Simples
Soma N números digitados pelo usuário.

```python
def soma_simples():
    nmrs = []
    count = 0
    while True:
        entrada1 = input("Quantos números quer somar? ")     
        if entrada1.isdigit():
            qnt = int(entrada1)
            break
        else: 
            print("Digite um número inteiro válido.")
    
    while qnt > 0:
        while True:
            entrada2 = input(f"Digite o {count + 1}º número: ")
            if entrada2.isdigit():
                count += 1
                qnt -= 1
                nmrs.append(int(entrada2))
                break
            else:
                print("Digite um número válido.")
    
    soma = sum(nmrs)
    print(f"Soma dos {count} números ({nmrs}): {soma}")
```

---

## 🔁 8. Contar Até N
Conta de um número inicial até um final.

```python
def contar_ate_n():
    lista = []
    while True:
        entrada = input("Digite o número inicial: ")
        if entrada.isdigit():
            n1 = int(entrada)
            break
        else: 
            print("Digite um número válido.")
    
    while True:
        entrada2 = input("Digite o número final: ")
        if entrada2.isdigit():
            n2 = int(entrada2)
            if n2 > n1:
                break
            else:
                print("O final deve ser maior que o inicial.")            
        else:
            print("Digite um número válido.")
    
    inicio = n1
    while n1 < n2:
        n1 += 1 
        lista.append(n1)
    
    print(f"Números entre {inicio} e {n2}: {lista}")
```

---

## 🔁 9. Verificar Par ou Ímpar
Verifica a paridade de múltiplos números.

```python
def par_ou_impar():
    lista = []
    count = 0
    flag = False
    while not flag:
        entrada = input("Quantos números quer verificar? ")
        if entrada.isdigit():
            qnt = int(entrada)
            flag = True
        else:
            print("Digite um número válido.")
    
    while qnt > 0:
        entrada1 = input(f"Digite o {count + 1}º número: ")
        if entrada1.isdigit():
            number = int(entrada1)
            if number % 2 == 0:
                lista.append((number, "Par"))
            elif number == 0:
                lista.append((number, "Zero"))
            else:
                lista.append((number, "Ímpar"))
            count += 1
            qnt -= 1
        else:
            print("Digite um número válido.")
    
    print("Resultados:", ", ".join([f"{num} ({tipo})" for num, tipo in lista]))
```

---

## 🔁 10. Média de Valores
Calcula a média de N números.

```python
def calcular_media():
    lista = []
    while True:
        entrada = input("Quantos números na média? ")
        if entrada.isdigit():
            qnt = int(entrada)
            break
        else:
            print("Digite um número válido.")
    
    for i in range(qnt):
        while True:
            entrada2 = input(f"Digite o {i+1}º número: ")
            if entrada2.isdigit():
                lista.append(int(entrada2))
                break
            else: 
                print("Digite um número válido.")
    
    media = sum(lista) / len(lista)
    print(f"Média dos {len(lista)} números ({lista}): {media:.2f}")
```

---

## 🔁 11. Contador Decrescente
Contagem regressiva de N até 0.

```python
def contador_decrescente():
    while True:
        entrada = input("Digite um número positivo: ")
        if entrada.isdigit():
            num = int(entrada)
            break
        else: 
            print("Digite um número válido.")
    
    lista = []
    inicio = num
    lista.append(inicio)
    
    while num > 0:
        num -= 1
        lista.append(num)
    
    print(f"Contagem regressiva de {inicio} a 0: {sorted(lista, reverse=True)}")
```

---

## 🔁 12. Número Primo
Verifica se um número é primo.

```python
def verificar_primo():
    n = int(input("Digite um número > 1: "))
    div = []
    for i in range(2, n):
        if n % i == 0:
            div.append(i)
    
    if not div:
        print(f"{n} é primo.")
    else:
        print(f"{n} não é primo (divisível por: {div}).")
```
## Revisão

## 🔁 1. Contador até N (fácil)
Conta de 1 até um número N com opções de exibição.

```python
def ex1():
    def pedir_numero(mensagem):
        while True:
            valor = input(mensagem)
            if valor.isdigit() and int(valor) > 0:
                return int(valor)
            print("Digite um número inteiro positivo válido.")

    def escolher_formato():
        while True:
            escolha = input("Você quer ver os números em 'lista' ou 'coluna'? ").lower()
            if escolha in ['lista', 'coluna']:
                return escolha
            print("Escolha inválida. Digite 'lista' ou 'coluna'.")

    def exibir_contagem(num, formato):
        if formato == 'coluna':
            for i in range(1, num + 1):
                print(i)
                print('-----')
        else:
            numeros = list(range(1, num + 1))
            print(f"A lista do 1 até {num} é: {numeros}")

    def contador_ate_n():
        repeticoes = pedir_numero("Quantas vezes você quer repetir o processo? ")

        for rep in range(1, repeticoes + 1):
            print(f"\nRepetição {rep}")
            formato = escolher_formato()
            numero = pedir_numero("Digite o número limite para contar: ")
            exibir_contagem(numero, formato)

        while True:
            resposta = input("Deseja repetir tudo novamente? (sim/nao): ").lower()
            if resposta == 'sim':
                contador_ate_n()
                break
            elif resposta == 'nao':
                print("Programa encerrado.")
                break
            else:
                print("Responda com 'sim' ou 'nao'.")
    
    contador_ate_n()
```

---

## 🔁 2. Par ou Ímpar (fácil)
Verifica a paridade de números com opções de exibição.

```python
def pedir_numero(mensagem):
    while True:
        valor = input(mensagem)
        if valor.isdigit() and int(valor) >= 0:
            return int(valor)
        print("Digite um número inteiro positivo válido.")

def obter_formato_exibicao():
    while True:
        form = input("Você quer exibir em 'coluna' ou 'linha'? ").lower()
        if form in ["coluna", "linha"]:
            return form
        print("Digite 'coluna' ou 'linha'.")

def determinar_paridade(numero):
    if numero == 0:
        return "zero"
    elif numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

def exibir_resultados(resultados, formato):
    if formato == "coluna":
        for num, tipo in resultados:
            print(f"{num} - {tipo}")
    else:
        print("Lista dos números e seus tipos:")
        print(resultados)

def ex2():
    quantidade = pedir_numero("Quantas vezes quer repetir? ")
    formato = obter_formato_exibicao()
    resultados = []

    for i in range(quantidade):
        num = pedir_numero(f"Digite o número {i+1}: ")
        tipo = determinar_paridade(num)
        resultados.append((num, tipo))

    exibir_resultados(resultados, formato)

    while True:
        repetir = input("Deseja mais algum número? (sim/nao) ").lower()
        if repetir == "sim":
            ex2()
            break
        elif repetir == "nao":
            print("Encerrando o programa.")
            break
        else:
            print("Digite 'sim' ou 'nao'.")
```

---

## 🔁 3. Soma de N números (médio)
Soma números com possibilidade de adicionar mais valores.

```python
def pedir_numero(mensagem):
    while True:
        valor = input(mensagem)
        if valor.isdigit() and int(valor) != 0:
            return int(valor)
        else: print("Digite o valor correto ")

def somar(numeros):
    return sum(numeros)

def repetir(numeros):
    while True:
        rep = input("Voce deseja adicionar mais algum numero a soma? 'sim' ou 'nao' ").lower()
        if rep == "sim":
            qnte = pedir_numero("Quantos números quer somar? ")
            for i in range(qnte):
                number_add = pedir_numero(f"Digite o número {i+1} adicionado da soma: ") 
                numeros.append(number_add)
        else:
            break

def ex3():
    print("🎯 Verificador de soma")
    quantidade = pedir_numero("Quantos números quer somar? ")
    numeros = [pedir_numero(f"Digite o número {i+1} da soma: ") for i in range(quantidade)]
    repetir(numeros)
    resultado = somar(numeros)
    print(f"A soma de todos os numeros {numeros} é {resultado}")
```

---

## 🔁 4. Tabuada personalizada (médio)
Gera tabuadas com opções de formatação.

```python
def ex4():
    def pedir_numero(mensagem):
        while True:
            valor = input(mensagem)
            if valor.isdigit() and int(valor)>0:
                return int(valor)
            print("Digite um número inteiro positivo válido.")

    def formato():
        while True:
            escolha = input("Voce deseja ver a tabuada em coluna ou em lisa ").lower()
            if escolha in ["coluna","lista"]:
                return escolha
            print("Digite lista ou coluna")
    
    def tabuada():
        numero_inicial = pedir_numero("Digite o numero para a tabuada ")
        numero_final = pedir_numero("Digite ate que numero quer ir ")
        formatar = formato()
        if formatar == "coluna":
            for mult in range(1,numero_final+1):
                resultado = numero_inicial * mult
                print(f"{numero_inicial} x {mult} = {resultado}")
                print("----")
        else:
            lista = []
            for mult in range(1, numero_final + 1):
                resultado = numero_inicial * mult
                lista.append(resultado)
            print(f"A lista de resultados é: {lista}")

    def verificar_rep():
        while True:    
            verificar = input("Deseja mais algum numero? Sim/Não ").lower()
            if verificar in ["sim", "nao"]:
                return verificar
            else: print("Digite sim ou nao ")

    def repetir():
        qnt = pedir_numero("Quantas vezes quer repetir ")
        count = 0
        for count in range(qnt):
            print(f"Esta é a {count+1} repetição")
            tabuada()
            count += 1
        val_rep = verificar_rep()

        if val_rep == "sim":
            return repetir()
        else: 
            print("Encerrando o programa")
    
    repetir()
```

---

## 🔁 5. Fatorial (intermediário)
Calcula o fatorial de um número.

```python
def pedir_numero(mensagem):
    while True:
        valor = input(mensagem)
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        else: print("Digite um valor válido ")

def ex5():
    numero = pedir_numero("Digite um numero inteiro ")
    resultado = 1
    for mult in range(1,numero+1):
        resultado *= mult
    print(resultado)
```
```

