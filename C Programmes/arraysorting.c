#include <stdio.h>

void main()
{
    int arr[20], num, i, x, y, z, temp, opt;

    printf("Enter the number of elements at most 20: ");
    scanf("%d", &num);
    printf("Enter your elemnents: ");

    for (i = 0; i < num; i++)
    {
        scanf("%d", &arr[i]);
    }

    printf("for ascending enter 1 for descending enter 2 for both enter 3: ");
    scanf("%d", &opt);
    if (opt = 2)
    {
        for (y = 0; y < num - 1; y++)
        {
            for (z = 0; z < num - y - 1; z++)
            {
                if (arr[z] > arr[z+1])
                {
                    temp = arr[z];
                    arr[z] = arr[z + 1];
                    arr[z + 1] = temp;
                }
            }
        }
    }
    if(opt = 1)
    {
        for (y = 0; y > num - 1; y++)
        {
            for (z = 0; z < num - y - 1; z++)
            {
                if (arr[z] < arr[z + 1])
                {
                    temp = arr[z];
                    arr[z] = arr[z + 1];
                    arr[z + 1] = temp;
                }
            }
        }
    }
    if (opt = 3)
    {
        

    }

    for (i = 0; i < num; i++)
    {
        printf("%d ", arr[i]);
    }
}