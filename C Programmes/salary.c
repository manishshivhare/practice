#include <stdio.h>

void main()
{

    float Bsalary, Da, Bs, Hra, GrossSalary, Pf, ProvidentFund;
    
    int NetSalary;

    printf("Enter basic salary: ");
    scanf("%f", &Bsalary);

    Da = 0.25 * Bsalary;
    Hra = 0.15 * Bsalary;

    GrossSalary = (Bsalary + Da + Hra);

    ProvidentFund = 0.10 * GrossSalary;
    ProvidentFund = pf;
     

    NetSalary = GrossSalary - pf ;

    printf("%d", NetSalary);
}
