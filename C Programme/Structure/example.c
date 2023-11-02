#include <stdio.h>
#include <string.h>
struct customer
{
    char name[20];
    int debt;
};
void show(struct customer cust[4])
{
    for (int i = 0; i < 4; i++)
        printf("%s: %d\n", cust[i].name, cust[i].debt);
}

int main()
{
    struct customer cust[4];

    for (int i = 0; i < 4; i++)
    {
        printf("Enter the name of customer%d: ", i + 1);
        gets(cust[i].name);

        printf("Enter the debt amount of %s: ", cust[i].name);
        scanf("%d", &cust[i].debt);

        fflush(stdin);
    }

    show(cust);
}