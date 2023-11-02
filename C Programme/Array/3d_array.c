#include <stdio.h>
void mul(int *arr, int num, int level, int n)
{
    for (int i = 0; i < n; i++)
    {
        arr[level][i] = num * (i + 1);
    }

    for (int i = 0; i < 10; i++)
    {
        printf("%dX%d = %d", n, i + 1, arr[level][i]);
    }
}
int main()
{
    int num1, num2, num3;

    printf("Enter three numbers whose table you want to print: ");
    scanf("%d%d%d", &num1, &num2, &num3);
    int arr[3][10];
    mul(arr, num1, 0, 10);
    mul(arr, num2, 1, 10);
    mul(arr, num3, 2, 10);

    return 0;
}