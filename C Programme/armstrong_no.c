#include <stdio.h>
#include <math.h>

int main()
{

    int num, Anum, remainder, result;
    printf("Enter the No: ");
    scanf("%d", &num);
    Anum = num;
    result = 0;
    while (Anum != 0)
    {
        remainder = Anum % 10;
        result += remainder * remainder * remainder;

        Anum /= 10;
    }

    if (result == num)
    {
        printf("%d is a Astronout number", num);
    }
    else
    {

        printf("%d is not a Astronout number", num);

    }

    return 0;
}






// int res(int num);
// int main()
// {
//     int num, result;
//     printf("Enter the number: ");
//     scanf("%d", &num);
//     int res(int num);
//     printf("%d ", result);
//     if ( result == num)
//     {
//         printf("yes");
//     }
//     else
//     {
//         printf("no");
//     }
// }
// int res(int num)
// {
//     int Onum, rem, result = 0;

//     num = Onum;
//     while (Onum != 0)
//     {
//         rem = Onum % 10;
//         result += rem * rem * rem;
//         Onum /= 10;
//     }
//     return result;
// }
