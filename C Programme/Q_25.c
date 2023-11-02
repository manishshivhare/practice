#include <stdio.h>
#include <stdlib.h>

int main()
{

    int n;
    int *ptr;

    printf("Enter the lenght of the array: ");
    scanf("%d", &n);

    ptr = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++)
    {
        printf("Enter the number%d: ", i + 1);
        scanf("%f", &ptr[i]);
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (ptr[i] == ptr[j])
            {
                for (int k = j; k < n; k++)
                {
                    ptr[k] = ptr[k + 1];
                }
                n--;
                j--;
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        printf("%d ", ptr[i]);
    }
}