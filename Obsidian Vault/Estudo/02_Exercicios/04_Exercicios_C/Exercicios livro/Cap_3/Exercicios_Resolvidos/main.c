#include <stdio.h>
#include <stdlib.h>


float Pnumero(char mensagem[])
{
    float valor;
    printf("%s",mensagem);
    scanf("%f",&valor);

    if (valor >= 0){
        return valor;
    } else {
        printf("Digite um numero inteiro nao negativo \n") ;
        return Pnumero(mensagem);
    }
}


int ex1(){
    //1. Receba quatro números inteiros, calcule e mostre a soma.
    int qnt = Pnumero("Digite quantos valores deseja: ");
    int soma = 0;
    int valores[qnt];
    char mensagem[50];

    for (int i=0; i < qnt; i++){
        sprintf(mensagem,"Digite o %d numero: ",i+1);
        valores[i]=Pnumero(mensagem);
        soma += valores[i];

    }
    printf("A soma dos valores é %d",soma);
    return 0;
}



int ex2(){
//2. Receba três notas, calcule e mostre a média aritmética.
    int qnt = Pnumero("Digite quantos valores deseja: ");
    float soma = 0;
    float valores[qnt];
    char mensagem[50];

    for (int i = 0; i <qnt; i++){
        sprintf(mensagem,"Digite o %d numero: ",i+1);
        valores[i]=Pnumero(mensagem);
        soma += valores[i];
    }
    float media = soma/qnt;
    printf("A media aritimetica eh  %.2f ",media);
    return 0;
}



int ex3(){
//3. Receba três notas e seus pesos, calcule e mostre a média ponderada.
    int qnt = Pnumero("Digite a quantidade de notas: ");
    int peso [qnt];
    float nota[qnt],somaP = 0,somaN=0;
    char mensagem[50];

    for (int i = 0; i<qnt; i++){
        sprintf(mensagem,"Digite o %d peso: ",i+1);
        peso[i]=Pnumero(mensagem);
        sprintf(mensagem,"Digite a %d nota: ",i+1);
        nota[i]=Pnumero(mensagem);

        somaP += peso[i];
        somaN += (nota[i]*peso[i]);

    }
    float media = somaN/somaP;
    printf("A media ponderada dos valores eh %.2f",media);
    return 0;
}



int ex4(){
//4. Receba o salário de um funcionário, calcule e mostre o novo salário com aumento de 25%.

    float sal = Pnumero("Digite seu salário: "), nsal,Vaument;
    float aumento = Pnumero("Digite o valor do aumento em decimais: ");
    nsal = sal*(1+aumento/100);
    Vaument = sal*(aumento/100);
    printf("O aumento foi de %.2f e o salario novo eh %.2f\n",Vaument,nsal);
    return 0;
}


/*Exercício 05,06,07 – Análise de salário com operações compostas
Escreva um programa que receba o salário base de um funcionário e permita aplicar múltiplas operações sobre ele. O usuário deverá escolher, entre as opções a seguir, quais operações deseja aplicar:
    Aumento fixo de 25%;
    Aumento com percentual informado pelo usuário;
    Gratificação de 5%;
    Desconto de 7%.
O programa deve permitir aplicar mais de uma operação na mesma execução, conforme a escolha do usuário.
Ao final, apresente:
    O valor total de acréscimos;
    O valor total de descontos;
    O salário final;
E uma mensagem informando se houve ou não perda salarial (isto é, se o salário final ficou menor que o salário base).
*/

float aumenEx5(float n){
    float aumento = Pnumero("Digite o valor do aumento: ")/100.0f;
    if (aumento > 0){
        return n*(1+aumento);
    } else{ printf("Digite um valor acima de zero\n");return aumenEx5(n);}
}
float descEx5(float dsc){
    float desconto = Pnumero("Digite o valor do desconto: ")/100.0f;
    if (dsc>0){
        return dsc*(1-desconto);
    } else{printf("Digite um valor acima de zero\n"); return descEx5(dsc);}
}
int ex5(){
    float sal = Pnumero("DIgite seu salario: ");
    float nsal= sal;
    int pergunta,qnta = 0,qntd = 0;
    int qnt = (int)Pnumero("Digite quantos salarios quer ver: ");

    for (int i = 0; i<qnt; i++){
        printf("Voce deseja verificar o que? \n 1-Acrescimos \n 2-Descontos\n");
        scanf("%d",&pergunta);

        switch (pergunta){
            case 1:
                nsal = aumenEx5(nsal);
                qnta ++;
                break;
            case 2:
                nsal = descEx5(nsal);
                qntd ++;
                break;
            default:
                printf("Opcao invalida");
                i--;
                break;
        }

    }
    if (nsal==sal){
        printf("não teve alteracao no salario\n");
    } else {printf("O salario foi alterado, o antigo era %.2f e o novo eh %.2f \n A diferenca foi de %.2f\n", sal, nsal, nsal - sal);;}
    printf("teve %d de descontos e %d de aumento\n",qntd,qnta);
    return 0;

}


int conta(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return conta(n-1) + conta(n-2);
}

int ex6() {
    int n = Pnumero("Digite o termo que quer ver: ");
    printf("O termo %d da sequencia de Fibonacci eh %d\n", n, conta(n));
    int val = Pnumero("Digite quantos valores quer ver: ");
    for (int i = 0; i<val+1; i++){
        printf("%d, ",conta(i));
    }
    return 0;
}



int main() {
    int num;
    int (*exercicios[30])() = {
        ex1, ex2, ex3, ex4, ex5, ex6 NULL
    };

    while (1) {
        printf("Escolha o numero do exercicio (0 para sair): ");
        scanf("%d", &num);

        if (num == 0) {
            printf("Saindo dos exercicios!\n");
            break;
        } else if (num > 0 && num <= 30 && exercicios[num - 1] != NULL) {
            exercicios[num - 1]();
        } else {
            printf("Exercicio %d nao existe.\n", num);
        }

    }

    return 0;
}
