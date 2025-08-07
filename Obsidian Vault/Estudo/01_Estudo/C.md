
---

# 📘 Fundamentos C + Python

## ✅ Parte 1 - Metodologias até Modularização

---

### 📌 1. Metodologias de Desenvolvimento 

#### ✅ Entender o problema antes de codar

- 🎯 Etapas:
    
    - Analisar → Planejar → Codificar → Testar
        
- 🧃 **Analogia**:  
    Como montar um móvel com manual:  
    Entende o que precisa fazer → separa ferramentas → segue os passos → confere se montou certo
    

#### 💡 Exemplo prático:

Problema: mostrar se um número é maior que 10

#### 🔣 Código em C

```c
#include <stdio.h>

int main() {
    int numero;
    printf("Digite um número: ");
    scanf("%d", &numero);

    if (numero > 10) {
        printf("Maior que 10\n");
    } else {
        printf("10 ou menor\n");
    }
    return 0;
}
```

#### 🐍 Código em Python

```python
numero = int(input("Digite um número: "))
if numero > 10:
    print("Maior que 10")
else:
    print("10 ou menor")
```

---

### 🔡 2. Tipos Básicos e Variáveis

#### ✅ Guardar valores com tipos definidos

- 📦 Tipos em C:
    
    - `int`: inteiros
        
    - `float`: números reais
        
    - `char`: caracteres
        
- 🧃 Analogia:  
    Variáveis = potes com etiquetas
    

#### 💡 Exemplo prático: guardar nome, idade e altura

#### 🔣 Código em C

```c
#include <stdio.h>

int main() {
    int idade = 20;
    float altura = 1.75;
    char inicial = 'V';

    printf("Idade: %d\n", idade);
    printf("Altura: %.2f\n", altura);
    printf("Inicial: %c\n", inicial);
    return 0;
}
```

#### 🐍 Código em Python

```python
idade = 20
altura = 1.75
inicial = 'V'

print("Idade:", idade)
print("Altura:", round(altura, 2))
print("Inicial:", inicial)
```

---

### 🖨️ 3. Entrada e Saída no Console

#### ✅ Receber e mostrar informações

- 🗣️ Mostrar → `printf` (C) | `print()` (Python)
    
- 👂 Ler → `scanf` (C) | `input()` (Python)
    
- ❗ Em C, usar `&` no `scanf` (endereço da variável)
    

#### 💡 Exemplo prático: perguntar o nome da pessoa

#### 🔣 Código em C

```c
#include <stdio.h>

int main() {
    char nome[20];
    printf("Qual seu nome? ");
    scanf("%s", nome);
    printf("Olá, %s!\n", nome);
    return 0;
}
```

#### 🐍 Código em Python

```python
nome = input("Qual seu nome? ")
print(f"Olá, {nome}!")
```

---

### ➕ 4. Operadores e Expressões

#### ✅ Calcular, comparar e decidir

- Aritméticos: `+`, `-`, `*`, `/`, `%`
    
- Relacionais: `==`, `!=`, `>`, `<`, `>=`, `<=`
    
- Lógicos: `&&`, `||`, `!` (C) | `and`, `or`, `not` (Python)
    

#### 💡 Exemplo prático: verificar se número está entre 5 e 10

#### 🔣 Código em C

```c
#include <stdio.h>

int main() {
    int n = 7;
    if (n >= 5 && n <= 10) {
        printf("Está entre 5 e 10\n");
    } else {
        printf("Fora do intervalo\n");
    }
    return 0;
}
```

#### 🐍 Código em Python

```python
n = 7
if 5 <= n <= 10:
    print("Está entre 5 e 10")
else:
    print("Fora do intervalo")
```

---

### 🧩 5. Estruturas Condicionais

#### ✅ Fazer escolhas no código

- `if`, `else`, `else if` (C)
    
- `if`, `elif`, `else` (Python)
    

#### 💡 Exemplo prático: classificar a idade

#### 🔣 Código em C

```c
#include <stdio.h>

int main() {
    int idade = 25;
    if (idade < 18) {
        printf("Menor de idade\n");
    } else if (idade <= 60) {
        printf("Adulto\n");
    } else {
        printf("Idoso\n");
    }
    return 0;
}
```

#### 🐍 Código em Python

```python
idade = 25
if idade < 18:
    print("Menor de idade")
elif idade <= 60:
    print("Adulto")
else:
    print("Idoso")
```

---


### 🔁 Estruturas de Repetição — Exemplos para cada laço

|Laço|C|Python|
|---|---|---|
|`while`|enquanto condição|enquanto condição|
|`for`|com contagem|com `range()`|
|`do while`|executa ao menos 1x|não existe (usa `while`)|

---

#### 💡 Exemplo 1: **`while`** — contar de 1 a 5

##### 🔣 Código em C

```c
#include <stdio.h>

int main() {
    int i = 1;
    while (i <= 5) {
        printf("%d\n", i);
        i++;
    }
    return 0;
}
```

##### 🐍 Código em Python

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

---

#### 💡 Exemplo 2: **`for`** — contar de 1 a 5

##### 🔣 Código em C

```c
#include <stdio.h>

int main() {
    for (int i = 1; i <= 5; i++) {
        printf("%d\n", i);
    }
    return 0;
}
```

##### 🐍 Código em Python

```python
for i in range(1, 6):
    print(i)
```

---

#### 💡 Exemplo 3: **`do while`** — contar de 1 a 5 (executa ao menos 1x)

##### 🔣 Código em C

```c
#include <stdio.h>

int main() {
    int i = 1;
    do {
        printf("%d\n", i);
        i++;
    } while (i <= 5);
    return 0;
}
```

---

### 🧱 7. Modularização (Funções)

#### ✅ Separar o código em blocos reutilizáveis

- C: define funções com tipo e retorno
    
- Python: usa `def` e retorna valor
    

#### 💡 Exemplo: função que calcula o dobro de um número

#### 🔣 Código em C

```c
#include <stdio.h>

int dobrar(int n) {
    return n * 2;
}

int main() {
    int valor = 5;
    printf("Dobro: %d\n", dobrar(valor));
    return 0;
}
```

#### 🐍 Código em Python

```python
def dobrar(n):
    return n * 2

valor = 5
print("Dobro:", dobrar(valor))
```

---

# ---------

## ✅ Parte 2 - Modularização, Ponteiros, Recursão, Arquivos, Vetores e Matrizes

---

### 🔁 8. Modularização com Parâmetros

#### ✅ Enviar valores para uma função trabalhar com eles

- 📌 Antes: função fazia tudo sozinha
    
- Agora: função **recebe valores** como entrada (parâmetros)
    
- 🧃 **Analogia**:  
    Uma **máquina de suco** onde você escolhe a fruta:  
    A máquina (função) precisa **receber o sabor (parâmetro)** para fazer o suco certo.
    

#### 💡 Exemplo: função que soma dois números

#### 🔣 Código em C

```c
#include <stdio.h>

int somar(int a, int b) {
    return a + b;
}

int main() {
    int resultado = somar(3, 7);
    printf("Soma: %d\n", resultado);
    return 0;
}
```

#### 🐍 Código em Python

```python
def somar(a, b):
    return a + b

resultado = somar(3, 7)
print("Soma:", resultado)
```

---

### 🔂 9. Recursividade

#### ✅ Função que chama ela mesma para resolver um pedaço do problema

- A função resolve **um caso simples** (caso base)
    
- Depois **chama ela mesma** para resolver o resto
    
- 🧃 **Analogia**:  
    Como **escalar uma escada degrau por degrau**.  
    Cada passo depende do anterior, e o processo se repete até chegar ao topo.
    

#### 💡 Exemplo: calcular fatorial de 5

`5! = 5 × 4 × 3 × 2 × 1`

#### 🔣 Código em C

```c
#include <stdio.h>

int fatorial(int n) {
    if (n == 0) return 1;
    return n * fatorial(n - 1);
}

int main() {
    printf("Fatorial de 5: %d\n", fatorial(5));
    return 0;
}
```

#### 🐍 Código em Python

```python
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

print("Fatorial de 5:", fatorial(5))
```

---

### ✉️ 10. Ponteiros

#### ✅ Armazenam **endereços de memória**, não valores diretamente

- Um ponteiro **aponta para onde** a variável está guardada
    
- Em C, ponteiros são declarados com `*` e acessados com `&`
    
- 🧃 **Analogia**:  
    Uma **etiqueta com o endereço da casa**, em vez da casa em si.  
    A variável é a casa, o ponteiro é o papel com o endereço.
    

#### 💡 Exemplo: alterar o valor de uma variável via ponteiro

#### 🔣 Código em C

```c
#include <stdio.h>

void dobrar(int *p) {
    *p = *p * 2;
}

int main() {
    int x = 10;
    dobrar(&x);
    printf("Dobrado: %d\n", x);
    return 0;
}
```

#### 🐍 Código em Python (sem ponteiros explícitos, mas comportamento semelhante):

```python
def dobrar(x):
    return x * 2

x = 10
x = dobrar(x)
print("Dobrado:", x)
```

---

### 📁 11. Arquivos

#### ✅ Ler e gravar informações em arquivos no disco

- Abrir arquivo → escrever ou ler → fechar
    
- Em C: `fopen`, `fprintf`, `fscanf`, `fclose`
    
- 🧃 **Analogia**:  
    Como abrir um **caderno**:  
    Escrever algo, guardar, depois reabrir e ler
    

#### 💡 Exemplo: gravar e depois ler um nome

#### 🔣 Código em C

```c
#include <stdio.h>

int main() {
    FILE *f = fopen("nome.txt", "w");
    fprintf(f, "Vitor\n");
    fclose(f);

    char nome[20];
    f = fopen("nome.txt", "r");
    fscanf(f, "%s", nome);
    printf("Lido do arquivo: %s\n", nome);
    fclose(f);

    return 0;
}
```

#### 🐍 Código em Python

```python
with open("nome.txt", "w") as f:
    f.write("Vitor\n")

with open("nome.txt", "r") as f:
    nome = f.readline().strip()

print("Lido do arquivo:", nome)
```

---

### 📦 12. Vetores e Matrizes — Parte 1

#### ✅ Guardar vários valores em sequência

- Vetor = lista de valores
    
- Matriz = tabela (linhas e colunas)
    
- 🧃 **Analogia**:  
    Vetor = fila de pessoas  
    Matriz = sala com cadeiras (linhas × colunas)
    

#### 💡 Exemplo: armazenar e imprimir 3 números

#### 🔣 Código em C

```c
#include <stdio.h>

int main() {
    int numeros[3] = {10, 20, 30};
    for (int i = 0; i < 3; i++) {
        printf("%d\n", numeros[i]);
    }
    return 0;
}
```

#### 🐍 Código em Python

```python
numeros = [10, 20, 30]
for n in numeros:
    print(n)
```

---

### 🧮 13. Vetores e Matrizes — Parte 2

#### ✅ Trabalhar com estruturas bidimensionais (matriz)

- Uma matriz em C é como um vetor de vetores
    

#### 💡 Exemplo: somar os elementos de uma matriz 2×2

#### 🔣 Código em C

```c
#include <stdio.h>

int main() {
    int m[2][2] = {{1, 2}, {3, 4}};
    int soma = 0;

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            soma += m[i][j];
        }
    }

    printf("Soma: %d\n", soma);
    return 0;
}
```

#### 🐍 Código em Python

```python
m = [[1, 2], [3, 4]]
soma = 0

for linha in m:
    for valor in linha:
        soma += valor

print("Soma:", soma)
```

---

### 🧭 14. Vetores com Ponteiros

#### ✅ Vetores e matrizes também podem ser manipulados via ponteiros

- Um vetor em C é um ponteiro para o primeiro elemento
    
- Pode usar aritmética de ponteiros para navegar
    
- 🧃 **Analogia**:  
    Como usar **um dedo para percorrer uma lista**, sem saber o tamanho — só andando de elemento em elemento
    

#### 💡 Exemplo: acessar vetor com ponteiro

#### 🔣 Código em C

```c
#include <stdio.h>

int main() {
    int v[3] = {5, 10, 15};
    int *p = v;

    for (int i = 0; i < 3; i++) {
        printf("%d\n", *(p + i));
    }

    return 0;
}
```

#### 🐍 Código em Python (equivalente conceitual):

```python
v = [5, 10, 15]
for i in range(len(v)):
    print(v[i])
```

---

# --------

## ✅ Parte 3 - Manipulação de caracteres, Structs, Classes, Exceções

---

### 🅰️ 15. Manipulação de Caracteres

#### ✅ Trabalhar com letras, palavras e textos simples

- Em C, texto = **vetor de `char`**, com finalizador `\0`
    
- Em Python, texto = `str`, manipulação mais direta
    
- 🧃 **Analogia**:  
    Como uma **fila de letras**: cada caractere é um elemento, e o último é o sinal de fim (`\0`)
    

#### 💡 Exemplo: contar quantas letras tem um nome

#### 🔣 Código em C

```c
#include <stdio.h>
#include <string.h>

int main() {
    char nome[50];
    printf("Digite seu nome: ");
    scanf("%s", nome);
    printf("Quantidade de letras: %lu\n", strlen(nome));
    return 0;
}
```

#### 🐍 Código em Python

```python
nome = input("Digite seu nome: ")
print("Quantidade de letras:", len(nome))
```

---

### 🧱 16. Structs (Registros)

#### ✅ Agrupar várias informações em um único tipo de dado

- Struct = **caixa com campos diferentes**: nome, idade, altura…
    
- 🧃 **Analogia**:  
    Como uma **ficha de cadastro**: nome, idade, CPF, tudo junto, mas separado em campos
    

#### 💡 Exemplo: guardar dados de uma pessoa

#### 🔣 Código em C

```c
#include <stdio.h>

struct Pessoa {
    char nome[20];
    int idade;
    float altura;
};

int main() {
    struct Pessoa p = {"Vitor", 20, 1.80};
    printf("Nome: %s\n", p.nome);
    printf("Idade: %d\n", p.idade);
    printf("Altura: %.2f\n", p.altura);
    return 0;
}
```

#### 🐍 Código em Python (com `class`)

```python
class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

p = Pessoa("Vitor", 20, 1.80)
print("Nome:", p.nome)
print("Idade:", p.idade)
print("Altura:", p.altura)
```

---

### 🧩 17. Classes (Orientação a Objetos)

#### ✅ Representar entidades com **dados** (atributos) e **ações** (métodos)

- Em **C**, orientação a objetos é manual (simulada)
    
- Em **Python**, é nativa com `class`, `self`, e herança
    
- 🧃 **Analogia**:  
    Classe = **molde de bolo**,  
    Objeto = **bolo pronto** com sabor, cor, recheio, etc.
    

#### 💡 Exemplo: classe Pessoa com método para exibir dados

#### 🔣 Código em C (simulado com struct + função)

```c
#include <stdio.h>

struct Pessoa {
    char nome[20];
    int idade;
};

void exibir(struct Pessoa p) {
    printf("Nome: %s, Idade: %d\n", p.nome, p.idade);
}

int main() {
    struct Pessoa p1 = {"Vitor", 21};
    exibir(p1);
    return 0;
}
```

#### 🐍 Código em Python

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

p1 = Pessoa("Vitor", 21)
p1.exibir()
```

---

### 🔐 18. Tratamento de Exceções (Python)

> 🔒 **Apenas existe em Python**  
> C **não tem try/catch nativo**, erros precisam ser prevenidos com testes manuais

#### ✅ Interrompe a execução normal em caso de erro

- 🧃 **Analogia**:  
    Como **amortecedor de impacto**: se der erro, em vez de quebrar, o programa reage com calma
    

#### 💡 Exemplo: evitar divisão por zero

#### 🐍 Código em Python

```python
try:
    x = int(input("Digite o numerador: "))
    y = int(input("Digite o denominador: "))
    resultado = x / y
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Erro: divisão por zero!")
except ValueError:
    print("Digite apenas números!")
```

---

#### ❌ Em C:

> Para evitar erro, você precisa **verificar manualmente antes de fazer a operação**:

##### 🔣 Código em C

```c
#include <stdio.h>

int main() {
    int x, y;
    printf("Digite dois números: ");
    scanf("%d %d", &x, &y);

    if (y == 0) {
        printf("Erro: divisão por zero!\n");
    } else {
        printf("Resultado: %d\n", x / y);
    }
    return 0;
}
```

---



# --------

