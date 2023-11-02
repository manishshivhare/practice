#include <stdio.h>

void display(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%d ", arr[i]);
    }
}

void insert(int arr[], int element, int size, int index)
{
    for (int i = size - 1; i < index; i--)
    {
        arr[size + 1] = arr[size];
    }
    arr[index] = element;
}
void sorting(int arr[], int size)
{
    int temp;
    for (int y = 0; y < size - 1; y++)
    {
        for (int z = 0; z < size - y - 1; z++)
        {
            if (arr[z] > arr[z + 1])
            {
                temp = arr[z];
                arr[z] = arr[z + 1];
                arr[z + 1] = temp;
            }
        }
    }
}

int main()
{
    int arr[50] = {1, 52, 65, 85, 75};
    int element, position;
    printf("Enter the element you want to insert: ");
    scanf("%d", &element);
    printf("Enter the position: ");
    scanf("%d", &position);
    insert(arr, element, 5, position);
    sorting(arr, 5);
    display(arr, 5);

    return 0;
}
