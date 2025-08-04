- [[Python]] 
---


# Funções  
# ============

## Função (normal)  

Função é um bloco de código que executa uma tarefa específica.  
Você chama a função para repetir essa tarefa sem reescrever o código.

Exemplo simples:

```python
def saudacao():
    print("Olá, tudo bem?")
````

Uso:

```python
saudacao()  # Imprime: Olá, tudo bem?
saudacao()  # Pode chamar várias vezes
```

Outro exemplo:

```python
def bom_dia():
    print("Bom dia!")
```

---

## Função com argumentos

Funções podem receber valores para trabalhar com eles. Esses valores são chamados **argumentos**.

Exemplo:

```python
def saudacao(nome):
    print(f"Olá, {nome}!")
```

Uso:

```python
saudacao("Vitor")   # Olá, Vitor!
saudacao("Maria")   # Olá, Maria!
```

Mais argumentos:

```python
def soma(a, b):
    print(a + b)
```

Uso:

```python
soma(2, 3)   # 5
soma(10, 7)  # 17
```

---

## Função recursiva

Função que chama ela mesma para resolver um problema dividindo ele em partes menores.
Sempre precisa de um **caso base** para parar a recursão, evitando que rode para sempre.

Exemplo clássico: fatorial

```python
def fatorial(n):
    if n == 1:
        return 1  # Caso base
    return n * fatorial(n - 1)  # Chamada recursiva
```

Uso:

```python
print(fatorial(3))  # 6 (3 * 2 * 1)
print(fatorial(5))  # 120 (5 * 4 * 3 * 2 * 1)
```

Outro exemplo: contar regressivamente

```python
def contar(n):
    if n == 0:
        print("Fim")
        return
    print(n)
    contar(n - 1)
```

Uso:

```python
contar(3)
# Saída:
# 3
# 2
# 1
# Fim
```

## =============

## Exercicios usando funções - normais e com argumentos -

## -----------------

### 🔁 1. Contagem até N

#### Peça um número N e mostre números anteriores ou posteriores a um número dado.

```python
def contagem():
    while True:
        entrada = input("Digite quantos números quer ver: ")
        if entrada.isdigit() and int(entrada) > 0:
            nmber = int(entrada)
            break
        else:
            print("Digite um número inteiro positivo ")

    while True:
        posi = input("Deseja ver os anteriores ou posteriores? ").lower()
        if posi in ["anterior", "anteriores", "ante", "posterior", "posteriores", "poste"]:
            break
        else:
            print("Digite apenas 'posteriores' ou 'anteriores' ")

    while True:
        entrada = input("Qual número? ")
        if entrada.lstrip('-').isdigit():
            n = int(entrada)
            break
        else:
            print("Digite um inteiro válido, pode ser negativo")

    count = 1
    while count <= nmber:
        if posi in ["anterior", "anteriores", "ante"]:
            print(n - count)
        else:
            print(n + count)
        count += 1
```


### 🔁 2. Senha Correta

#### Peça a senha até a pessoa digitar "1234".

```python
def Vsenha():
    while True:
        senha = input("Digite a senha ")
        if not senha:
            print("Senha não pode estar vazia!")
            continue
        if not senha.isdigit():
            print("A senha deve conter apenas números.")
            continue
        if senha == "1234":
            print("Acesso permitido")
            break
        else:
            print(f"Senha incorreta {senha}")
```

---

### 🔁 3. Pedir Número Positivo

#### Peça um número inteiro positivo, valide e retorne.

```python
def pedir_numero():
    while True:
        entrada = input("Digite um número ")
        if entrada.isdigit() and int(entrada) > 0:
            print(f"Número positivo {entrada}")
            return int(entrada)
        else:
            print("Digite um número positivo inteiro")
```

---

### 🔁 4. Jogo da Soma

#### Peça pares de números e some até passar de 100.

```python
def jogo_da_soma():
    cont = 0
    soma = 0
    while soma <= 100:
        while True:
            n1 = input("Digite o primeiro número ")
            if not n1.isdigit():
                print("Digite um número inteiro ex:'1'")
            else:
                break
        while True:
            n2 = input("Digite o segundo número ")
            if not n2.isdigit():
                print("Digite um número inteiro ex:'1'")
            else:
                break

        soma += int(n1) + int(n2)
        cont += 1
        if soma <= 100:
            print(f"A conta {cont} deu {soma}")
        else:
            print(f"A soma final {cont} deu {soma}")
            break
```

---

### 🔁 5. Contar Palavras

#### Peça palavras até digitar "fim". No final, mostre o total e as palavras.

```python
def contar_palavras():
    palavras = []
    while True:
        usr = input("Digite a palavra desejada ").strip().lower()
        if usr == "":
            print("Digite uma palavra válida")
            continue
        if usr == "fim":
            print(f"Você digitou {len(palavras)} palavras e elas foram: " + ', '.join(palavras))
            return
        palavras.append(usr)
```

---

### 🔁 6. Jogo da Adivinhação

#### Adivinhe um número entre intervalo dado, com número de tentativas.

```python
from random import randint

def jogo_adivinha():
    while True:
        entrada = input("Digite quantas tentativas quer: ").strip()
        if entrada.isdigit():
            count = int(entrada)
            break
        else:
            print("Digite um número adequado.")

    while True:
        entrada = input("Digite o primeiro número de início: ")
        if entrada.isdigit():
            n1 = int(entrada)
            break
        else:
            print("Digite um número válido.")

    while True:
        entrada = input("Digite até que número vai: ")
        if entrada.isdigit():
            n2 = int(entrada)
            if n2 != n1 and n2 > n1:
                break
            else:
                print("O número deve ser diferente e maior que o primeiro.")
        else:
            print("Digite um número válido e diferente.")

    rand = randint(n1, n2)
    print(f"Você tem {count} tentativas.")

    palt = None
    while palt != rand and count > 0:
        entrada = input(f"Digite um número entre {n1} e {n2}: ")
        if entrada.isdigit():
            palt = int(entrada)
        else:
            print("Digite um número válido.")
            continue

        if palt != rand:
            count -= 1
            print(f"Você tem {count} tentativa(s) restante(s).")
        else:
            print(f"Parabéns! Você acertou, o número era mesmo {rand}.")

    if count == 0:
        print(f"Você perdeu. O número era {rand}.")
```
## -----------------


## Exercicios usando a recursividade 