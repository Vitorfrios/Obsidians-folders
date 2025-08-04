def pedir_numero(mensagem):
    while True:
        valor = input(mensagem)
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        else: print("Digite um valor válido ")

### 5. Sequência de Fibonacci até N termos

# Peça um número inteiro positivo N.
# Gere e mostre os N primeiros termos da sequência de Fibonacci (0, 1, 1, 2, 3, 5, 8, ...).
# Use `while` ou `for` e funções internas para calcular.


def ex6():
    n1 = pedir_numero("Digite ate que numero deseja ver: ")
    lista = [0,1]
    count1 = 0
    count2 = 1
    for i in range(n1):
        resultado = count1 + count2
        count1 = count2
        count2 = resultado
        lista.append(resultado)
    print(lista)


### 6. Verificar número perfeito

# Peça um número inteiro positivo.
# Verifique se ele é um número perfeito (soma dos divisores próprios, excluindo ele mesmo, é igual ao número).
# Mostre se é perfeito ou não.
# Use `for` para encontrar divisores e `if` para checar.


def verificar_numero():
    num_pedido = pedir_numero("digite um numero para ver se é perfeito ou nao: ")
    lista = []
    for i in range(num_pedido+1):
        num = i + 1
        div = num_pedido % num
        if div == 0:
            lista.append(num)
    
    soma_lista = sum(lista)
    if soma_lista == num_pedido:
        print(f"Este numero {num_pedido} é perfeito")
    else : print(f"esse numero {num_pedido} não é perfeito pois a soma dos divisores é igual a {soma_lista} ")

def ex7():
    verificar_numero()

### 7. Contador regressivo com pausa

# Peça um número inteiro positivo.
# Conte regressivamente até zero, imprimindo cada número a cada segundo (use `time.sleep(1)`).
# Ao final, imprima “Fim!”.
# Use `while` e funções internas.

def ex8():
    num = pedir_numero("Digite um numero para contar regressivamente ate zero: ")
    for i in range (num, -1 , -1):
        print(i)
        

### 8. Soma dos números pares até N

# Peça um número inteiro positivo N.
# Some todos os números pares de 2 até N (inclusive, se for par).
# Mostre a soma total.
# Use `for` com passo 2 para otimizar.

def ex9():
    numero = pedir_numero("Digite um numero para somar seus pares: ")
    soma = 0
    for i in range(2, numero+1, 2):
        soma += i
    print(soma)






# -
# Dicionário de exercícios
exercicios = {
    1: ex6,
    2: ex7,
    3: ex8,
    4: ex9
}

# -
print("Escolha qual exercício quer:")
print("1 - """)
print("2 - """)
print("3 - """)
print("4 - """)
print("5 - """)

try:
    ex = int(input("Digite o número do exercício: "))
    if ex in exercicios:
        exercicios[ex]()  # Chama a função do exercício
    else:
        print("Exercício inválido.")
except ValueError:
    print("Digite apenas números!")