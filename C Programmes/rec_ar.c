#include <stdio.h>
#include<conio.h>
// area of triangle

int main(){

    int length, breadth, area;

    printf("\nEnter the length of rectangle:\nEnter the breadth of rectangle ");
    scanf("%d%d", &length,&breadth);

    area = length*breadth;

    printf("\narea of rectangle is: %d", area );

    return 0;
    clearscr();
    
}

