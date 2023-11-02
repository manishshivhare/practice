#include <stdio.h>

void sorting(int arr[], int size)
{
    int temp;
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size - i; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
void display(int arr[], int size)
{
    for (int i = 0; i < size - 1; i++)
    {
        printf("%d ", arr[i]);
    }
}

void searching(int arr[], int item, int end)
{
    int beg = 0;

    int mid = (end + beg) / 2;

    while (beg <= end && arr[mid] != item)
    {
        if (item > arr[mid])
        {
            beg = mid + 1;
        }
        else
        {
            end = mid - 1;
        }
        mid = (end + beg) / 2;
    }
    if (arr[mid] == item)
    {
        printf("\n%d", mid);
    }
}

int main()
{
    int arr[100] = {1, 2, 3, 4, 5, 6};

    // sorting(arr, 6);
    display(arr, 6);
    searching(arr, 5, 6);
}