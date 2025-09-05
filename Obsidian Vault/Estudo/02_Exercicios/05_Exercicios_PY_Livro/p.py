# 5. Ordem Decrescente com Quarto Número — Versão Avançada e Recursiva
# Você recebe uma lista de números inicialmente em ordem crescente, mas recebe um novo valor que pode estar em qualquer posição.
# Sem usar laços de repetição, insira o valor na posição correta e exiba toda a lista em ordem decrescente.
# A inserção e a inversão devem ser feitas usando chamadas recursivas.

def numeros():
    lista = []
    qnt = int(input("Digite a quantidade de termos: "))
    for i in range(qnt):
        lista.append(int(input(f"Digite o {i+1} termo: ")))
    print(sorted(lista))
    print(sorted(lista, reverse=True))

numeros()
