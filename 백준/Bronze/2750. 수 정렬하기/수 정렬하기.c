#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int i, j, min, index, num, temp, data[1000];
    scanf("%d", &num);
    
    for (i = 0; i < num; i++)
    {
        scanf("%d", &data[i]);
    }

    for (i = 0; i < num; i++)
    {
        min = 1001;
        for (j = i; j < num; j++)
        {
            if (data[j] < min)
            {
                min = data[j];
                index = j;
            }
        }
        temp = data[i];
        data[i] = data[index];
        data[index] = temp;
    }

    for (i = 0; i < num; i++)
        printf("%d\n", data[i]);

    return 0;
}