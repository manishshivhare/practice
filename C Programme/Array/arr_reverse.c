#include <stdio.h>
void reverse(int *arr, int n)
{
    int temp;
    for (int i = 0; i < (n / 2); i++)
    {
        temp = arr[i];
        arr[i] = arr[n - i - 1];
        arr[n - i - 1] = temp;
    }
}
int main()
{
    int arr[10];
    printf("Enter the 10 numbers to print them in reverse: ");
    {
        for (int i = 0; i < 10; i++)
            scanf("%d", &arr[i]);
    }
    reverse(arr, 10);

    for (int i = 0; i < 10; i++)
    {
        printf("%d\t", arr[i]);
    }
}
