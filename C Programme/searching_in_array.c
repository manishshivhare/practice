#include <stdio.h>

void main()
{
    int arr[50], i, num, elem, index;
    printf("Enter the no. of elements: ");
    scanf("%d", &num);

    for (i = 0; i < num ; i++)
    {

        scanf("%d", &arr[i]);
    }

    printf("Enter element to search the address: ");
    scanf("%d", &elem);

    for (i = 0; i < num ; i++)
    {
        if (arr[i] == elem)
        {
            index = i;
            printf("address of %d is %d", arr[i], index);
            break;
        }
        if (i == num-1)
        {
            printf("Elemet not found");
        }
    }
}