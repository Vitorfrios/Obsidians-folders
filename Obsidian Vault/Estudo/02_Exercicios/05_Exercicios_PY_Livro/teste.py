## Exercícios para aprender recursividade

#### Nível 0: Função universal
##### Crie uma função universal para pedir um numero
def pedirn():
    valor = input("Digite um número: ")
    return int(valor) if valor.isdigit() and int(valor) >= 0 else print("Digite um valor inteiro positivo")


#### Nível 1: Conceitos básicos

##### 1. Fatorial de um número  
######   Escreva uma função recursiva que calcule o fatorial de um número inteiro positivo.
def fat(n):
    return 1 if n == 1 else n*fat(n-1)
def ex1():
    numero = pedirn()
    print(fat(numero))




##### 2. Soma dos números até n  
######    Crie uma função recursiva que some todos os números de 1 até n.
def soma(n):
    return 1 if n == 1 else n+soma(n-1) 
def ex2():
    numero = pedirn()
    print(soma(numero))



#### Nível 2: Manipulação de listas e strings

##### 3. Somar elementos de uma lista  
######    Implemente uma função que receba uma lista de números e retorne a soma usando recursão.

def somar(n):
    return 0 if len(n) == 0 else n[0]+somar(n[1:])

def ex3():
    lista = []
    while True:
        numero = pedirn()
        if numero == 0:
            break
        else: lista.append(numero)
    print(f"A soma da lista {lista} é {somar(lista)}")




##### 4. Inverter uma string  
######    Faça uma função recursiva que inverta uma string.
def stringIN(n):
    return n if len(n) <= 1 else n[-1] + stringIN(n[:-1])
def ex4():
    string = input("Digite alguma coisa: ")
    while len(string) == 0:
        string = input("Digite alguma coisa sem ser vazio" ": ")
    print(stringIN(string))
    pass


#### Nível 3: Problemas clássicos de recursão

##### 5. Sequência de Fibonacci  
######    Gere os n números da sequência de Fibonacci usando recursão.
def fibo(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        lista = fibo(n - 1)
        proximo = lista[-1] + lista[-2]
        lista.append(proximo)
        return lista

    

    
def ex5():
    while True:
        numero = pedirn()
        if numero not in {0,1}:
            break
        else: print("Digite um numero diferente de 0 e 1")
    print(fibo(numero))
    



##### 6. Busca em lista  
######    Implemente uma função recursiva para verificar se um elemento existe em uma lista.
def Nexis(n):
    if not n:
        return False
    return True if n[0] == 2 else Nexis(n[1:])

def ex6():
    lista = []
    while True:
        numero = pedirn()
        if numero == 0:
            break
        else:lista.append(numero)
    if Nexis(lista) == True:
        print(f"O numero 2 tem na lista {lista}")
    else:print("O numero 2 nao tem na lista")
    pass


##### 7. Contar ocorrências de um elemento na lista
###### Crie uma função recursiva que recebe uma lista e um elemento e retorne quantas vezes esse elemento aparece na lista.


def contar_ocorrencias(n, elemento):
    if not n:
        return 0 
    elif n[0] == elemento:
        return 1 + contar_ocorrencias(n[1:],elemento)
    else: return 0 + contar_ocorrencias(n[1:],elemento)
    
    pass

def ex7():
    lista = []
    numero = pedirn()
    while numero != 0:
        lista.append(numero)    
        numero = pedirn()

    ocorrencias = contar_ocorrencias(lista,2)
    if ocorrencias > 0:
        print(f"O numero 2 aparece na lista {lista} {ocorrencias} veez")
    else:print("O numero 2 nao tem na lista")
    pass


##### 8. Verificar se uma string é palíndromo

###### Implemente uma função recursiva que verifica se uma string é igual a ela mesma invertida.


def eh_palindromo(s):
    if len(s) <=1:
        return True
    elif s[0] != s[-1]:
        return False
    else: return eh_palindromo(s[1:-1])

def ex8():
    string = input("Digite uma palavra ")
    pal = eh_palindromo(string)
    if pal == True :
        print(f"A palavra {string} é um palindromo")
    else:print("Não é um alindromo")
    pass


##### 9. Encontrar o maior elemento numa lista

###### Crie uma função recursiva que retorna o maior valor dentro de uma lista de números.


def maior_elemento(n):
    if len(n) <= 1:
        return None
    return max(n)
    pass

def ex9():
    numero = pedirn()
    lista = []
    while numero != 0:
        lista.append(numero)
        numero = pedirn()
    Melemento = maior_elemento(lista)
    print(f"O maior elemento de{lista} é {Melemento}")
    
    pass


##### 10. Flatten (achatar) uma lista de listas arbitrariamente aninhadas

###### Dada uma lista que pode conter elementos e outras listas (ex: `[1, [2, 3], [[4]], 5]`), crie uma função que retorne uma lista simples com todos os elementos.


def flatten(n):
    if len(n) == 0:
        return []
    elif type(n[0]) != list:
        return [n[0]] + flatten(n[1:])
    else: return flatten(n[0]) + flatten(n[1:])
    pass

def ex10():
    lista = [1, [2, 3], [[4]], 5]
    resultado = flatten(lista)
    print(f"A lista achatada de {lista} é {resultado}")

##### 11. Potências de um número

###### Escreva uma função recursiva que calcule `base^expoente`, para expoentes inteiros não negativos.


def potencia(b, e):
    if e == 0:
        return 1
    else: return b* potencia(b,e-1)
    pass

def ex11():
    base = pedirn()
    expoente = pedirn()
    conta = potencia(base,expoente)
    print(conta)
    pass


##### 12. Imprimir números de n até 1 em ordem decrescente

def imprimir_decrescente(n):
    if n == 1:
        return [1]
    else: return [n] + imprimir_decrescente(n-1)
    pass

def ex12():
    numero = pedirn()
    desc = imprimir_decrescente(numero)
    for i in desc:
        print(i)
    pass




#### 13. Soma dos dígitos de um número

##### Crie uma função recursiva que calcule a soma dos dígitos de um número inteiro positivo.

def soma_digitos(n):
    if n == 0:
        return 0
    else: return n%10 + soma_digitos(n//10)

    pass

def ex13():
    numero = pedirn()
    conta = soma_digitos(numero)
    print(conta)
    pass



#### 14. Mínimo elemento em uma lista

##### Implemente uma função recursiva que retorne o menor elemento de uma lista de números.
from random import randint

def menor_elemento(mn):
    if mn[1:] == []:
        return mn[0]
    elif mn[0] == menor_elemento(mn[1:]):
        return mn[0]
    else: return menor_elemento(mn[1:])

    pass

def ex14():
    lista = []
    timer = 10
    while timer:
        num = randint(1,9)
        lista.append(num)
        timer -= 1
    mini = menor_elemento(lista)
    print(lista,mini)
    pass

#### 15. Tamanho de uma lista (sem usar `len`)

##### Escreva uma função recursiva que calcule o tamanho de uma lista, sem usar a função `len`.

def tamanho_lista(tl):
    if tl == []:
        return 0
    else:
        return 1 + tamanho_lista(tl[:-1])  

def ex15():
    lista = []
    timer = 10
    while timer:
        num = randint(1,9)
        lista.append(num)
        timer -= 1
    mini = tamanho_lista(lista)
    print(lista,mini)

#### Dicionário de exercícios
exercicios = {
    1: ex1,
    2: ex2,
    3: ex3,
    4: ex4,
    5: ex5,
    6: ex6,
    7: ex7,
    8: ex8,
    9: ex9,
    10: ex10,
    11: ex11,
    12: ex12,
    13: ex13,
    14: ex14,
    15: ex15,
}




#### Menu de execução
print("Escolha qual exercício quer: ")

try:
    ex = int(input("Digite o número do exercício: "))
    if ex in exercicios:
        exercicios[ex]()  #### Chama a função do exercício
    else:
        print("Exercício inválido.")
except ValueError:
    print("Digite apenas números!")
