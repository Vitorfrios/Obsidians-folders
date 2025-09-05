"""

---

3. Maior Número — Versão Avançada e Recursiva
Receba uma sequência de números inteiros (quantidade desconhecida no início) e determine o maior valor sem usar estruturas de repetição.
O processo deve ser pensado como: compare o primeiro número com o maior do restante da lista, resolvendo o mesmo problema para a lista menor até chegar a um único elemento.

---

4. Ordem Crescente — Versão Avançada e Recursiva
Receba `n` números distintos e apresente-os em ordem crescente sem usar laços de repetição.
Pense o problema como:

1. Encontre o menor número da lista.
2. Coloque-o no início.
3. Ordene o restante recursivamente.

---

5. Ordem Decrescente com Quarto Número — Versão Avançada e Recursiva
Você recebe uma lista de números inicialmente em ordem crescente, mas recebe um novo valor que pode estar em qualquer posição.
Sem usar laços de repetição, insira o valor na posição correta e exiba toda a lista em ordem decrescente.
A inserção e a inversão devem ser feitas usando chamadas recursivas.

---

6. Número Par ou Ímpar — Versão Avançada e Recursiva
Receba um número inteiro (positivo ou negativo) e determine se é par ou ímpar sem usar o operador de resto (`%`) e sem laços de repetição.
A lógica deve ser construída subtraindo ou somando 2 recursivamente até chegar a 0 (par) ou ±1 (ímpar).

---

7. Regras de Acompanhamento — Versão Avançada e Recursiva
Receba um valor inteiro `I` e três números reais `A`, `B` e `C`. Dependendo de `I`:

| Valor de I | Ação (todas feitas recursivamente quando envolver ordenação) |
| ---------- | ------------------------------------------------------------ |
| 1          | Ordenar `A`, `B` e `C` em ordem crescente                    |
| 2          | Ordenar `A`, `B` e `C` em ordem decrescente                  |
| 3          | Mostrar o maior número entre os dois menores valores         |

---

8. Menu de Opções — Versão Avançada
Mostre um menu com opções e execute a escolhida.
No caso de cálculos numéricos (ex.: soma de dois números), permita que o usuário insira valores até decidir parar.
A lógica de repetição do menu deve ser feita usando recursão.

---

9. Data e Hora do Sistema — Versão Avançada
Mostre a data e hora do sistema nos formatos:

* DD/MM/AAAA
* Mês por extenso
* Hora\:minuto

Depois, mostre a diferença (em dias e horas) entre essa data e outra fornecida pelo usuário.
A contagem dos dias deve ser feita recursivamente, tratando anos bissextos e variação no número de dias por mês.

---

10. Data Cronologicamente Maior — Versão Avançada e Recursiva
Receba duas datas (dia, mês, ano) e determine qual é a mais recente.
A comparação deve ser feita analisando ano, depois mês, depois dia, mas sem usar estruturas de repetição.
Se as datas forem iguais, peça ao usuário para fornecer novas datas até haver desempate, usando chamadas recursivas.

---

"""

def pnum(mensagem):
    valor= input(mensagem)
    if valor.isdigit() and int(valor)>0:
        return int(valor)
    else: 
        print("Digite um numero diferente e valido")
        return pnum(mensagem)



def ex1():
    pass

# -
# Dicionário de exercícios
exercicios = {
    1: ex1
}

try:
    ex = int(input("Digite o número do exercício: "))
    if ex in exercicios:
        exercicios[ex]()  # Chama a função do exercício
    else:
        print("Exercício inválido.")
except ValueError:
    print("Digite apenas números!")