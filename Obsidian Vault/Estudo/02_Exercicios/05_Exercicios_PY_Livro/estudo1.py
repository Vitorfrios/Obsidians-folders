def pnum(mensagem):
    valor= input(mensagem)
    if valor.isdigit() and int(valor)>0:
        return int(valor)
    else: 
        print("Digite um numero diferente e valido")
        return pnum(mensagem)



def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibo(n-1)+fibo(n-2) 
def fiboL(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        sequ = fiboL(n-1)
        prox = sequ[-1]+sequ[-2]
        sequ.append(prox)
        return sequ
def ex1():
    #sequencia de fibonacci recursiva
    num = pnum("Digite o numero: ")
    print(f"O numero {num} da sequencia de fibonacci eh {fibo(num)} e a sequencia ate esse numero eh {fiboL(num)}")
    pass



def star(linha_atual, altura_total):
    if linha_atual == 1:  # caso base
        print(" " * ((altura_total - 1) // 2) + "*")
        return
    else:
        star(linha_atual - 2, altura_total)  # chama a linha anterior
        espacos = (altura_total - linha_atual) // 2
        print(" " * espacos + "*" * linha_atual)

def ex2():
#imprimir piramide de *
    qnt = pnum("DIGite ate que quntidade de * deseja ver de altura: ")
    # for i in range(1,qnt+1,2):
    #     print(" "*((qnt-i)//2)+ "*"*i)
    star(qnt,qnt)



#3️⃣ Recursão
def soma(n):
    if n == 1:
        return 1
    else: 
        somar = n + soma(n-1)
        return  somar
def returne(n):
    if n ==1 :
        return [1]
    else: 
        ante = returne(n-1)
        return ante +[n]
        
def fiboR(n):
    if n ==1:
        return [0]
    elif n ==2:
        return [0,1]
    else:
        lista = fiboR(n-1)
        proximo = lista[-1]+lista[-2]
        lista.append(proximo)
        return lista

def piramide(numeros,altura):
    if numeros == 1:  # caso base
        print(" " * (altura-1) + "1")
        return
    else:
        star(numeros - 2, altura)  # chama a linha anterior
        espacos = (altura - numeros) // 2
        print(" " * espacos + "*" * numeros)

num =0
temp = num 
num +=1
print(num)


def ex3():
# Crie uma função recursiva que retorna a soma de todos os números de 1 até n.
    num =pnum("DIgite o numero: ")
    print(soma(num))

# Crie uma função recursiva que retorna a lista de números de 1 até n.
    print(returne(num))
# Refatore o exercício da sequência de Fibonacci usando somente recursão para gerar a lista completa.
    print(fiboR(num))
# Crie uma função recursiva que imprime uma pirâmide de números, como:
#    1
#   1 2
#  1 2 3
    print(piramide(num,num))

    pass


# -
# Dicionário de exercícios
exercicios = {
    1: ex1,
    2: ex2,
    3:ex3
}

try:
    ex = int(input("Digite o número do exercício: "))
    if ex in exercicios:
        exercicios[ex]()  # Chama a função do exercício
    else:
        print("Exercício inválido.")
except ValueError:
    print("Digite apenas números!")