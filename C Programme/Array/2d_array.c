#include <stdio.h>
void printarr(int *hNumber, int n_houses, int house_d)
{
    
    
    for (int i = 0; i < n_houses; i++)
    {
        for (int j = 0; j < house_d; j++)
        {
            printf("The house number of house%d is %d\n", i + 1,  hNumber[i][j]);
        }
    }
    return 0;
}



int main()
{
    int n_houses = 10;
    int house_d = 1;

    int hNumber[10][2];

    for (int i = 0; i < n_houses; i++)
    {
        for (int j = 0; j < house_d; j++)
        {
            printf("Enter the house number of house%d\n", i + 1);
            scanf("%d", &hNumber[i][j]);
        }
    }
    // for (int k = 0; k < n_houses; k++)
    // {
    //     for (int l = 0; l < house_d; l++)
    //     {
    //         printf("The house number of house%d is %d\n", k + 1, hNumber[k][l]);
    //     }
    // }

    printarr(hNumber[10][2], 10, 1);
    return 0;
}
