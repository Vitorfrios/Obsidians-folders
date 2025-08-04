# 🔁 1. Contagem até 5
# Use while para mostrar os números de 1 até 5.
def contagem():
    while True:
        entrada = (input("Digite quantos números quer ver: "))
        if entrada.isdigit() and int(entrada) > 0:
            nmber = int(entrada)
            break
        else: print("Digite um numero inteiro positivo ")
    
    while True:
        posi = input("Deseja ver os anteriores ou posteriores? ").lower()
        if posi in ["anterior", "anteriores", "ante", "posterior", "posteriores", "poste"]:
            break
        else: print("Digite apenas 'posteriores' ou 'anteriores' ")
    
    while True: 
        entrada = input("Qual numero? ")
        if entrada.lstrip('-').isdigit():
            n = int(entrada)
            break
        else: print("Digite u inteiro válido, pode ser negativo")
    
    
    count = 1  # inicializa o contador dentro da função
    
    while count <= nmber:
        if posi in ["anterior", "anteriores", "ante"]:
            print(n - count)
        elif posi in ["posterior", "posteriores", "poste"]:
            print(n + count)
        else:
            print("Opção inválida")
            return contagem()  # chama a função novamente para tentar de novo
        count += 1

def quantidade():
    while True:
        entrada = input("Deseja repetir quantas vezes ")
        if entrada.isdigit()and int(entrada) == 0:
            return
        elif entrada.isdigit() and int(entrada) > 0:
            qnt = int(entrada)
            break
        else: print("Digite um numero válido ")
    for i in range(qnt):
        contagem()


# 🔁 2. Senha Correta
# - Use um loop while True para pedir a senha.
# - Peça a senha com input.
# - Se a senha for "1234", mostre "Acesso permitido!" e use break para sair.
# - Se for errada, avise e continue pedindo.
# - Valide para não aceitar entrada vazia.

def Vsenha():
    while True:
        senha = input("Digite a senha ")
        if not senha.isdigit():
            print("A senha deve conter apenas números.")
            continue
        if not senha:
            print("Senha não pode estar vazia!")
            continue
        if senha == "1234":
            print("Acesso permitido ")
            break
        else: print(f"Senha incorreta {senha}")

# 🔁 3. Número Positivo (nível intermediário)
# - Crie uma função chamada pedir_numero.
# - Dentro dela, use um loop while.
# - Peça um número e verifique se ele é um número com isdigit().
# - Se for positivo (maior que 0), retorne esse número.
# - Se for zero, negativo ou não for número, avise o usuário e repita.

def pedir_numero():
    while True:
        entrada = input("Digite um numero ")
        if entrada.isdigit() and int(entrada) > 0:
            print(f"Número positivo {entrada}")
            break
        else: print("Digite um numero positivo inteiro  ")




# 🔁 4. Jogo da Soma (nível intermediário)
# - Crie uma função chamada jogo_da_soma.
# - Comece com soma = 0 e contador = 0.
# - Use um while para continuar enquanto soma ≤ 100.
# - Peça números com input.
# - Verifique se é número com isdigit(), senão repita.
# - Converta e adicione à soma.
# - A cada rodada, mostre a soma atual.
# - Ao final, mostre quantos números foram digitados.

def jogo_da_soma():
    cont = 0 
    soma = 0
    while soma <=100:
        while True:
            n1 = input("Digite o primeiro numero ")
            if not n1.isdigit():
                print("Digite um numero inteiro ex:'1'")
            else:    break
        while True:
            n2 = input("digite o segundo numero ")
            if not n2.isdigit():
                print("Digite um numero inteiro ex:'1'")
            else:    break

        soma += int(n1)+int(n2)
        cont += 1 
        if soma <= 100:
            print(f"A conta {cont} deu {soma}")
        else:
            print(f" A soma final {cont} deu {soma}")
            break            
        






# 🔁 5. Contar Palavras (nível intermediário)
# - Crie uma função chamada contar_palavras.
# - Use while True para pedir palavras.
# - Se a palavra for "fim", pare (use .lower()).
# - Ignore palavras vazias (ex: "" ou só espaços).
# - Guarde as palavras válidas numa lista.
# - No final, mostre:
#   - Quantas palavras foram digitadas.
#   - Todas as palavras juntas separadas por vírgula.

def contar_palavras():
    usr = " "
    palavras = []
    while usr != "fim":
        usr = input("Digite a palavra desejada ").strip().lower()
        while True:
            if usr == "":
                print("Digite uma palavra válida ")
                break
            elif usr =="fim":
                print(f"Voce digitou {len(palavras)} palavras e elas foram: " + ', '.join(palavras))
                return
            else : 
                palavras.append(usr)
                break








# 🔁 6. Acertar o Número (nível intermediário)
# - Crie uma função chamada jogo_adivinha.
# - Gere um número aleatório de 1 a 10 (use import random e randint).
# - Peça um palpite com input, dentro de um while.
# - Verifique se o palpite é um número e está entre 1 e 10.
# - Dê dica se o palpite é maior ou menor.
# - Quando acertar, mostre mensagem de parabéns e número de tentativas.
from random import randint

def jogo_adivinha():
    palt = None

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




# 🔁 7. Soma Simples (nível fácil)
# - Crie uma função chamada soma_simples.
# - Peça ao usuário quantos números deseja somar.
# - Peça os números um a um, validando para aceitar apenas inteiros.
# - Some todos os números digitados.
# - Mostre a soma total e os números que foram somados.

def soma_simples():
    nmrs = []
    count = 0
    while True:
        entrada1 = input("Digite a quantidade de numeros que quer somar ")     
        if entrada1.isdigit():
            qnt = int(entrada1)
            break
        else: print("digite um numero inteiro válido")
    while qnt > 0:
        while True:
            entrada2 = input(f" digite o numero {count + 1} da lista ")
            if entrada2.isdigit():
                count += 1
                qnt -= 1
                nmrs.append(int(entrada2))
                break
            else:print("Digit um numero adequado ")
    soma = sum(nmrs)
    print(f"A soma total de todos os {count} numeros ({nmrs}) foi {soma}")



### # 🔁 8. Contar Até N (nível fácil)

# - Crie uma função chamada contar\_ate\_n.

# - Peça um número inteiro positivo.

# - Use um while para contar de 1 até esse número, imprimindo cada valor.

def contar_ate_n():
    lista = []
    while True:
        entrada = input("Digite o numero inicial que deseja contar ")
        if entrada.isdigit():
            n1 = int(entrada)
            break
        else: print("Digite um numero válido ")
    while True:
        entrada2 = input("Digite o numero final ")
        if entrada2.isdigit():
            n2 = int(entrada2)
            if n2 != n1 and n2 > n1:
                break
            else:
                print("O número deve ser diferente e maior que o primeiro.")            
        else:print("Digite um numero vpálido")
    inicio = n1
    while n1 != n2:
        n1 += 1 
        lista.append(n1)
    print(f"Os numeros entre {inicio} e {n2} são {lista}")


### # 🔁 9. Verificar Par ou Ímpar (nível médio)

# - Crie uma função chamada par\_ou\_impar.

# - Peça um número inteiro ao usuário.

# - Verifique se o número é par ou ímpar.

# - Mostre a mensagem correspondente.

def par_ou_impar():
    lista = []
    count = 0
    flag = False
    while not flag:
        entrada = input("Digite quantos numeros quer verificar ")
        if entrada.isdigit():
            qnt = int(entrada)
            flag = True
        else:
            print("Digite um numero válido ")
    while qnt > 0:
        entrada1 = input(f"Qual o {count + 1}° numero ")
        if entrada1.isdigit():
            number = int(entrada1)
            if number % 2 == 0:
                lista.append((number,"Par"))
                count += 1
                qnt -= 1
            elif number == 0:
                lista.append((number,"zero"))
                count += 1
                qnt -= 1

            else:
                lista.append((number, "Impar"))
                count += 1
                qnt -= 1
        else:print("Digite um numero válido ")
    print(f"Os números são: {lista}".replace("[", "").replace("]", "").replace("'",""))



### # 🔁 10. Média de Valores (nível médio)

# - Crie uma função chamada calcular\_media.

# - Peça 5 números inteiros ao usuário.

# - Calcule a média deles.

# - Mostre o resultado.

def calcular_media():
    lista = []
    count = 0
    Numeral = 0
    ItemL = 0
    flag = False
    while not flag:
        entrada = input("Digite quantos numeros quer fazer a media ")
        if entrada.isdigit():
            qnt = int(entrada)
            flag = True
        else:print("Digite um numero válido ")
    while qnt > 0:
        while True:
            entrada2 = input(f"Digite o {Numeral + 1}° numero da média: ")
            if entrada2.isdigit():
                n= int(entrada2)
                lista.append(n)
                qnt -= 1
                Numeral += 1
                break
            else: print("Digite um numero correto ")
    for i in lista:
        count += 1
    soma = sum(lista)/count
    print(f"A média dos numeros de{lista} por {count} dela é {soma}")



### # 🔁 11. Contador Decrescente (nível intermediário)

# - Crie uma função chamada contador\_decrescente.

# - Peça um número inteiro positivo N.

# - Use um while para mostrar a contagem regressiva de N até 0.

# - Mostre “Fim!” ao final.


def contador_decrescente():
    lista = []
    while True:
        entrada = input("Digite um numero ")
        if entrada.isdigit():
            num = int(entrada)
            
            break
        else: print("Digite um numero válido ")
    Inicio = num
    lista.append(Inicio)
    while num != 0:
        num -= 1
        lista.append(num)
    listOrd = sorted(lista,reverse=True)
    print(f"Os numeros do {Inicio} até Zero são {listOrd}")





### # 🔁 12. Número Primo (nível intermediário)

# - Crie uma função chamada verificar\_primo.

# - Peça um número inteiro maior que 1.

# - Verifique se o número é primo (divisível apenas por 1 e ele mesmo).

# - Mostre se o número é primo ou não.

def verificar_primo():
    n = int(input("Digite um numero: "))
    div = []
    count = 0
    flag = True
    for i in range (2,n):
        if n % i == 0:
            div.append(i)
            flag = False
    if flag == True:
        print(f"O número {n} é primo")
    else:
        print(f"O número {n} não é primo, é divisível por {div}")

        

















# ----------------------------------------------------------------

print("Escolha qual exercício quer")

ex = int(input("Digite o número do exercício: "))

if ex == 1:
    quantidade()  # exercício de contagem com anterior/posterior
elif ex == 2:
    Vsenha()  # verificação de senha com while
elif ex == 3:
    pedir_numero()  # número positivo
elif ex == 4:
    jogo_da_soma()  # soma até ultrapassar 100
elif ex == 5:
    contar_palavras()  # contar palavras até digitar 'fim'
elif ex == 6:
    jogo_adivinha()  # adivinhar número secreto
elif ex == 7:
    soma_simples()  # soma simples de dois números
elif ex == 8:
    contar_ate_n()  # contagem até N
elif ex == 9:
    par_ou_impar()  # verifica se número é par ou ímpar
elif ex == 10:
    calcular_media()  # calcula média de 5 números
elif ex == 11:
    contador_decrescente()  # contagem regressiva
elif ex == 12:
    verificar_primo()  # verifica se número é primo
else:
    print("Exercício inválido.")

