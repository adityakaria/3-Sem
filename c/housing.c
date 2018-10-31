#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int find(int *nos, int size);

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int i, size, *v;
    
    scanf("%d", &size);
    v = malloc(size * sizeof(int));
    
    for(i=0; i < size; i++)
        scanf("%d", &v[i]);
    
    int n = find(v, size);
    
    printf("%d\n", n);
    
    return 0;
}

int find(int *nos, int size)
{
    int sum1 = 0, sum2 = 0, sum3 = 0, sum = 0;
    
    for (i = 0; i < size; i++)
        sum += nos[i];

    for (i = 0; i < size-2; i++)
    {
        sum1 = sum2 = sum3 = 0;
        for (j = 0; j < size-r; j++)
        {
            sum1 += nos[j];
        }

        sum3 = sum - sum1;
        if (sum1 == sum3)
                return (sum1);

        for (j = size - 1; j >= size - r; j--)
        {
            sum3 -= nos[j];
            if (sum1 == sum3)
                return (sum1);
        }
        return 0;
        /*for (j = size - r; j < size; j++)
        {    
            sum3 = 0;
            for (k = j; k < size; k++)
            {
                sum3 += nos[k];
            }
            if (sum1 == sum3)
                return (sum1);
        }
        */
        r++;
    }

    return 0;
}

