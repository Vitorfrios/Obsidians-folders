## Links
[[Template_Estudo]]

---
# Horários de estudo

| Dia     | Horário     | Tipo    |
| ------- | ----------- | ------- |
| Segunda | 08:45–10:15 | Prática |
| Segunda | 16:00–17:30 | Teoria  |
| Terça   | 10:30–12:00 | Teoria  |
| Quarta  | 07:00–08:30 | Prática |
| Quinta  | 08:45–10:15 | Teoria  |
| Sexta   | 07:00–08:30 | Prática |
| Sexta   | 16:00–17:30 | Prática |

---
# Planejamento Python
# ------------------------------------------------------
## ✅ Progresso Python I - Fundamentos e Controle

### 🧩 Condições | Exercícios - [[01_Condições|Condições com If/Else]]

-  [x] **Utilizando** Condições com If / Else
    
    - Se a condição for verdadeira, faz uma coisa
        
    - Se for falsa, faz outra
        
    - Exemplo:
	     
```python
        if idade >= 18:     print("Maior de idade") else:     print("Menor de idade")
```
        
-  [x] Utilizando Condições com If, Elif e Else
    
    - Escolhe entre várias opções
        
    - Primeiro testa o `if`, depois `elif`s, no fim o `else`
        
    - Exemplo:
        
```python
        `if idade < 18:     print("Menor de idade") elif idade <= 60:     print("Adulto") else:     print("Idoso")`
```
        

---
### ---------------------------------
### 🔄 Laços de Repetição | Exercícios - [[02_Laços|Laços For e While]]

-  [ ] **Utilizando o Laço de Repetição For**
    
    - **Para que serve?**  
        Repetir um bloco de código várias vezes, uma vez para cada item de uma lista, string, ou números.
        
    - **Como funciona?**  
        O `for` cria uma variável que recebe cada item da sequência, um por um, e executa o código para cada um.
        
    - **Exemplo 1: números de 0 a 4**
        
        ```python
        for i in range(5):  # i vai de 0 até 4
            print(i)
        ```
        
        - `range(5)` cria uma sequência: 0, 1, 2, 3, 4
            
        - Para cada número, o print é executado.
            
    - **Exemplo 2: percorrendo uma lista**
        
        ```python
        frutas = ["maçã", "banana", "laranja"]
        for fruta in frutas:
            print(fruta)
        ```
        
        - A variável `fruta` recebe cada elemento da lista
            
        - Imprime "maçã", depois "banana", depois "laranja"
            

---

-  [ ] **Utilizando o Laço de Repetição While**
    
    - **Para que serve?**  
        Repetir um bloco de código **enquanto** uma condição for verdadeira.
        
    - **Como funciona?**  
        Primeiro verifica a condição. Se for `True`, executa o bloco. Depois verifica novamente, e assim por diante até a condição ser `False`.
        
    - **Exemplo: contar até 4**
        
        ```python
        contador = 0
        while contador < 5:
            print(contador)
            contador += 1  # soma 1 no contador
        ```
        
        - Começa com `contador = 0`
            
        - Enquanto `contador` for menor que 5, imprime o valor
            
        - Incrementa o contador em 1 a cada rodada
            
        - Para quando `contador` chegar a 5
            

---

-  [ ] **Utilizando List Comprehension**
    
    - **Para que serve?**  
        Criar listas de forma rápida e elegante, usando laços dentro de uma única linha.
        
    - **Como funciona?**  
        A sintaxe é:
        
        ```python
        [expressão for item in sequência if condição]
        ```
        
        Isso gera uma nova lista com itens que obedecem à condição.
        
    - **Exemplo: criar lista dos números pares de 0 a 9**
        
        ```python
        pares = [x for x in range(10) if x % 2 == 0]
        print(pares)  # [0, 2, 4, 6, 8]
        ```
        
    - É a forma compacta do código:
        
        ```python
        pares = []
        for x in range(10):
            if x % 2 == 0:
                pares.append(x)
        ```
        

---
### ---------------------------------
### 🛠️ Funções | Exercícios - [[03_Funcoes|Funções]]  

-  [ ] **Utilizando Funções**
    
    - **Pra que serve?**  
        Guardar um bloco de código que pode ser reutilizado quando a gente quiser, só chamando o nome da função.
        
    - **Como funciona?**  
        Você define a função com `def`, dá um nome pra ela, e coloca o código dentro. Depois chama ela pelo nome.
        
    - **Exemplo:**
        
        ```python
        def saudacao():
            print("Olá, seja bem-vindo!")
        
        saudacao()  # Chama a função
        ```
        

---

-  [ ] **Utilizando Função com Argumentos**
    
    - **Pra que serve?**  
        Para passar informações para dentro da função (como nomes, números, textos).
        
    - **Como funciona?**  
        A função recebe argumentos nos parênteses e usa eles lá dentro.
        
    - **Exemplo:**
        
        ```python
        def saudacao(nome):
            print(f"Olá, {nome}!")
        
        saudacao("Vitor")  # Mostra: Olá, Vitor!
        ```
        

---

-  [ ] **Utilizando Função Recursiva**
    
    - **Pra que serve?**  
        Quando uma função chama ela mesma, geralmente para resolver um problema que se divide em partes menores (como calcular fatorial).
        
    - **Como funciona?**  
        Tem que ter uma **condição de parada**, senão vira um loop infinito.
        
    - **Exemplo: fatorial de um número**
        
        ```python
        def fatorial(n):
            if n == 1:
                return 1
            else:
                return n * fatorial(n - 1)
        
        print(fatorial(5))  # Resultado: 120
        ```
        

---

-  [ ] **Utilizando Função com *Args e **Kwargs**
    
    - **Pra que serve?**  
        Usar funções que aceitam muitos argumentos sem saber quantos serão.
        
    - **Como funciona?**
        
        - `*args` → recebe vários valores em forma de **tupla**
            
        - `**kwargs` → recebe vários pares `chave=valor` em forma de **dicionário**
            
    - *_Exemplo com _args:__
        
        ```python
        def somar(*numeros):
            return sum(numeros)
        
        print(somar(1, 2, 3))  # Resultado: 6
        ```
        
    - **Exemplo com **kwargs:**
        
        ```python
        def mostrar_info(**dados):
            for chave, valor in dados.items():
                print(f"{chave}: {valor}")
        
        mostrar_info(nome="Vitor", idade=20)
        ```
        

---

-  [ ] **Função Lambda**
    
    - **Pra que serve?**  
        Criar funções simples e rápidas em **uma linha só**, sem usar `def`.
        
    - **Como funciona?**  
        Usada geralmente dentro de outras funções como `map`, `filter` ou para ordenar.
        
    - **Exemplo:**
        
        ```python
        dobro = lambda x: x * 2
        print(dobro(5))  # Resultado: 10
        ```
        
    - **Mais útil ainda com listas:**
        
        ```python
        numeros = [1, 2, 3]
        dobrados = list(map(lambda x: x * 2, numeros))
        print(dobrados)  # [2, 4, 6]
        ```
        

---
### ---------------------------------
### 🎯 Projeto Final | Exercícios – [[04_Gerenciamento|Gerenciamento jogadores e times]]
- [ ] Exercício Final: Gerenciamento jogadores e times  
### ---------------------------------
## -------------------------------------------------------------------
## ✅ Progresso Python II - Módulos e PIP

### 📦 Introdução a Módulos | Exercícios [[05_Módulos|Módulos]]  
- [ ] Motivação para usar Módulos  
- [ ] O que é um Módulo  
- [ ] Vantagens de usar Módulos  
- [ ] Criando o Primeiro Módulo  
### ---------------------------------

### 📚 Módulos Builtin | Exercícios [[06_Módulo_OS|Módulo OS]], [[07_Módulo_Math|Módulos Math e Statistic]]
- [ ] Módulo OS  
- [ ] Módulo HTTPServer  
- [ ] Módulo Webbrowser  
- [ ] Módulo Math  
- [ ] Módulo Statistic  
### ---------------------------------

### 🧩 Módulos Avançados | Exercícios [[08_Módulo_Regex|Módulo Regex]], [[09_Módulo_Collections|Módulos Hashlib, Json, Collections e Random]], [[10_Módulo_Tkinter|Módulo Tkinter]]  
- [ ] Módulo Regex I  
- [ ] Módulo Hashlib  
- [ ] Módulo Json  
- [ ] Módulo Collections  
- [ ] Módulo Random  
- [ ] Módulo Tkinter  
### ---------------------------------

### 📥 Gerenciamento de Pacotes | Exercícios [[11_Pip|PIP e Gerenciamento de Dependências]]  
- [ ] Comandos Pip  
### ---------------------------------

## -------------------------------------------------------------------
## ✅ Progresso Python III - Programação Orientada a Objetos (POO)

### 📘 Conceitos Básicos | Exercícios [[12_POO_Básico|Conceitos Básicos POO]]  
- [ ] O que é POO  
- [ ] Criando a primeira classe  
- [ ] Instanciando a Classe  
- [ ] Utilizando construtor e str  
- [ ] Utilizando métodos  
### ---------------------------------

### 📗 Avançado | Exercícios [[13_POO_Avançado|POO Avançado e Herança]]  
- [ ] Utilizando Variável de Classe  
- [ ] Utilizando Método de Classe  
- [ ] Utilizando Método Estático  
- [ ] Compreendendo o Encapsulamento  
- [ ] Fornecendo Maior Segurança com Encapsulamento  
- [ ] Métodos Getter e Setter  
- [ ] Quiz 1  
### ---------------------------------

### 🌿 Herança e Polimorfismo | Exercícios [[13_POO_Avançado|POO Avançado e Herança]]  
- [ ] Compreendendo a Herança  
- [ ] Utilizando a Herança na Prática  
- [ ] Utilizando Método Super  
- [ ] Utilizando Polimorfismo  
- [ ] Utilizando Composição  
### ---------------------------------

### 🧩 Decorators | Exercícios [[14_Decorators|Decorators]]  
- [ ] Compreendendo Decorators  
- [ ] Criando Decorators  
- [ ] Utilizando o Decorator Property  
### ---------------------------------

### 🎯 Projeto Final POO | Exercícios [[15_Exercício_Final_POO|Exercício Final POO]]  
- [ ] Exercício Final  
### ---------------------------------

## -------------------------------------------------------------------
## ✅ Progresso SQL e Banco de Dados

### 🗄️ SQL e SGBD  
| Exercícios        |                            |                      |                      |
| ----------------- | -------------------------- | -------------------- | -------------------- |
| [[19_SQL_Básico]] | [[21_SQL_Relacionamentos]] | [[20_SQL_Consultas]] | [[22_SQL_Modelagem]] |
- [ ] Compreendendo SQL e SGBD  
- [ ] SQLite: criação e manipulação de tabelas  
- [ ] PostgreSQL e PgAdmin  
### ---------------------------------

### 🎯 Projeto | Exercícios [[22_SQL_Modelagem|Modelagem de Banco de Dados]]  
- [ ] Projeto Gerenciamento de Blog  
### ---------------------------------



## -------------------------------------------------------------------
## ✅ Progresso Integração Banco de Dados Python

### 📂 SQLite  
| Exercícios                                                  |                                                             |
| ----------------------------------------------------------- | ----------------------------------------------------------- |
| [[23_SQLite \| SQLite Básico]]                              | [[24_SQLite_Manipulação \| Manipulação de Dados no SQLite]] |

- [ ] Compreendendo o SQL  
- [ ] Conhecendo o SQLite  
- [ ] Criando o Banco de Dados no SQLite  
- [ ] Inserindo Dados na Tabela  
- [ ] Lendo Dados de uma Tabela  
- [ ] Atualizando Dados de uma Tabela  
### ---------------------------------

### 🛠️ ORM | Exercícios [[25_ORM|ORM e Projeto Blog]]  
- [ ] O que é um ORM  
- [ ] Projeto Gerenciamento de Blog  
### ---------------------------------



## -------------------------------------------------------------------
## ✅ Progresso Git e GitHub

### 🔧 Git Básico | Exercícios [[26_Git_Básico|Git Básico]]  
- [ ] Conhecendo o Git  
- [ ] Instalando o Git  
- [ ] O Fluxo de Trabalho Básico do Git  
### ---------------------------------

### 🌿 Branches e Merge | Exercícios [[27_Git_Branches|Branches e Merge]]  
- [ ] Entendendo as Branches  
- [ ] Praticando o Uso de Branches  
- [ ] Resolvendo Conflitos de Merge  
### ---------------------------------

### 🌐 GitHub | Exercícios [[28_GitHub|GitHub e Repositórios Remotos]]  
- [ ] Repositórios Remotos e GitHub  
- [ ] Criando uma Conta no GitHub  
### ---------------------------------


# -------------

# Progresso de estudos

## **1. Fundamentos e lógica de programação**

  

- [x] Entrada e saída de dados

- [x] Tipos e conversões

- [x] Operações matemáticas

- [x] Estruturas de controle (`if`, `while`, `for`)

- [x] Validações simples e compostas

- [x] Modularização com funções

- [x] Recursão clássica

  

## **2. Estruturas de dados homogêneas**

  

- [x] Listas e manipulação com `append`, `len`, `sorted`, slicing

- [x] Tuplas e sets com suas principais características

- [x] Dicionários (estrutura, acesso e verificação)

  

## **3. Manipulação de dados**

  

- [x] Strings e seus métodos (`replace`, `count`, `lower`, etc.)

- [x] Laços aplicados em listas e strings

- [x] Processamentos comuns: soma, contagem, filtro, busca, ordenação

  

## **4. Recursão**

  

- [x] Funções recursivas com caso base e chamada

- [x] Aplicações: fatorial, Fibonacci, busca, somas, inversão, palíndromo, flatten, potência, contagem decrescente, etc.

  

---

## 1. **Matrizes (listas 2D)**

  

- [ ] Percorrer com `for` aninhado

- [ ] Somar linhas/colunas

- [ ] Diagonal principal/secundária

- [ ] Aplicações visuais (tabuleiros, mapas)

  

## 2. **Estruturas heterogêneas**

  

- [ ] `dict` com listas ou outros `dicts`

- [ ] Representar objetos complexos (ex: aluno com nome, notas, média)

- [ ] Filtros com múltiplos critérios

  

## 3. **Passagem por referência (efeito colateral)**

  

- [ ] Quando uma função altera a lista original

- [ ] Comparação entre cópia e referência

  

## 4. **Orientação a objetos (OO - primeiros passos)**

  

- [ ] Classe, objeto, atributos e métodos

- [ ] `__init__`, `self`

- [ ] Exemplo simples: criar uma classe `Pessoa`, `Aluno`, etc.

  

## 5. **Boas práticas de projeto**

  

- [ ] Modularização mais refinada

- [ ] Separação de responsabilidades (entrada, lógica, saída)

- [ ] Testes manuais e pequenos testes automatizados (`assert`)

  

## 6. **Análise de algoritmos**

  

- [ ] Contagem de operações

- [ ] Noção de complexidade (ex: linear vs exponencial em recursão)

  

---

  

### 🧭 **Recomendo seguir por aqui, agora:**

  

- Trabalhar com **matrizes e estruturas aninhadas**

- Simular **pequenos sistemas com dicionários e listas combinadas**

- Começar a **explorar classes básicas*- (mesmo sem OO avançada ainda)

- Praticar **algoritmos clássicos*- de busca (linear e binária) e ordenação (bubble, selection...)

  

Se quiser, posso montar pequenos desafios focados nesses próximos tópicos. Deseja seguir por qual deles primeiro?