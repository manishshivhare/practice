#include <stdio.h>

char main()
{
    char name_str[20];
    // long str[20];
    
    printf("Enter Your Name: ");
    scanf("%s", name_str);

    char *ptr = name_str;
    // long *ptr1 = str;
    
    while (*ptr != '\0')
    {

        if (*ptr == 'a')
        {
            printf("    *    \n  *   *  \n * * * *\n*       *\n*       *\t");
        }
        else if (*ptr == 'b')
        {
            printf("* * *  \n*     *\n* * *   \n*     *\n* * *  \t");
        }
        else if (*ptr == 'c')
        {
            printf("     *\n  * \n*\n*\n  * \n     *  \t");
        }
        ptr++;
        
    }
    
    
}