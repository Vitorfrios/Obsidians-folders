# 1. Faça um programa que receba quatro números inteiros,
# calcule e mostre a soma desses números.


def numero(mensagem):
    valor = input(mensagem)
    return int (valor) if valor.isdigit() and int(valor) > 0 else  numero(mensagem) 

"""
def lists(tm):
    lista = []
    for i in range(tm):
        numeros = numero(f"Digite o {i+1} numero: ")
        lista.append(numeros)
    return lista
"""
def lists(tm):
    if tm <= 0:
        return []
    else: return [numero(f"Digite o {tm} numero: " )] + lists(tm-1)

def conta(lista):
    soma = sum(lista)
    return lista,soma

def resultado():
    qnt = numero("Digite a quantidade de numeros que deseja somar: ")
    numeros = lists(qnt)
    lista,soma = conta(numeros)
    print(f"a lista de numeros é {lista} e a sona é {soma}")

resultado()
