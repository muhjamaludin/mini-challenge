#include <stdio.h>
#include "twoDimentionFigure.h"

void rectangularFill(int num)
{
    for (int i = 0; i < num; i++)
    {
        for (int j = 0; j < num; j++)
        {
            printf("* ");
        }
        printf("\n");
    }
}
