#include <stdio.h>
#include <conio.h>

int main()
{
    int marks;
    printf("Otained marks by student\n");
    scanf("%d", &marks);
    switch (marks)
    {
    case 100:
        printf("A");
        break;
    default:
        printf("Nan");
        break;
    }

    return 0;
}