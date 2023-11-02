
#include <stdio.h>

int main()
{
    int matrix1[3][3];
    int matrix2[3][3];
    int matrix3[3][3];

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("Enter the value of a%d x b%d element: ", i + 1, j + 1);
            scanf("%d", &matrix1[i][j]);
        }
    }

    printf("matrix1 = \n");

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%d ", matrix1[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("Enter the value of a%d x b%d element: ", i + 1, j + 1);
            scanf("%d", &matrix2[i][j]);
        }
    }

    printf("matrix2 = \n");

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%d ", matrix2[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            matrix3[i][j] = matrix1[i][j] + matrix2[i][j];
        }
        
    }
    printf("The sum of matrix1 and matrix2 = \n");

for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%d ", matrix3[i][j]);
        }
        printf("\n");
    }
    

}