#include <stdio.h>
#include <stdlib.h>

int main(){
    int num_f,h_f,num_filho;
    float val_hora,sal,sal_final;
    puts("Digite o seu número de identificação:");
    scanf("%d",&num_f);
    puts("Digite suas horas trabalhadas:");
    scanf("%d",&h_f);
    puts("Digite o valor ganho por hora:");
    scanf("%f",&val_hora);
    puts("Informe quantos filhos você tem com idade menor de 14 anos:");
    scanf("%d",&num_filho);

    sal = h_f*val_hora;

    if(num_filho > 0){
        sal_final = sal + (sal / (num_filho * 0.1));

        puts("************");

        printf("ID:%d\nHoras Trabalhadas:%d\nValor por Hora:R$%.2f\nNum. filhos:%d\nSalário Final:R$%.2f\n",num_f,h_f,val_hora,num_filho,sal_final);
    } else{
        puts("************");
        printf("ID:%d\nHoras Trabalhadas:%d\nValor por Hora:R$%.2f\nNum. filhos:%d\nSalário Final:R$%.2f\n",num_f,h_f,val_hora,num_filho,sal);
    }
}