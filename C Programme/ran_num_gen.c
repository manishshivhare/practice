#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{

    int number, guess, guesscount;
    srand(time(0));
    number = rand() % 100 + 1;
    printf("%d", number);

    do
    {

        printf("Guess the number between 1 to 100: ");
        scanf("%d", &guess);
        if (guess > number)
        {
            printf("the number is lower\n");
        }
        else if (number > guess)
        {
            printf("the number is higher\n");
        }
        else
        {
            printf("you gussed the right number in %d time", guesscount);
        }

    } while (guess != number);

    guesscount++;
    return 0;
}