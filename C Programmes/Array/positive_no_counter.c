#include <stdio.h>
void count(int *arr, int n)
{
    int c = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] > 0)
        {
            c++;
        }
    }
    
    printf("There are %d postive integers",c);
    
}
int main()
{
    int arr[10];

    printf("Enter 10 postives and negative numbers: ");
    for (int i = 0; i < 10; i++)
    {
        scanf("%d", &arr[i]);
    }
    
    count(arr, 10);
}