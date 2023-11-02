#include <stdio.h>

// void printArr(int *ptr, int n)
void printArr(int arr[], int n)

{
    for (int i = 0; i < n; i++)
    {
        // printf("The value of Elemnt %d is: %d\n", i + 1, *(ptr + i));
        printf("The value of Elemnt %d is: %d\n", i + 1, arr[i]);
    }
}
int main()
{
    int arr[] = {756, 876, 457, 878, 9876};
    printArr(arr, 5);
}