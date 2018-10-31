//to check for how many 1010 types in range in their binary forms

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

long to_bin(long num);
int read_input(int **inputs);
int check(long bin);

int main(void)
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int** inp = NULL;
    int n = read_input(inp);
    int count = 0, i;
    for (i = 0; i < n; i++)
    {
        for (long j = (long) inp[i][0]; j <= (long) inp[i][1]; j++)
        {
            long bin = to_bin(j);
            count += check(bin);
        }
        printf("%d", count);
    }
    
    return 0;
}

int check(long bin)
{
    int len;
    long bin2 = bin;
    
    while (bin2 != 0)
    {
        bin /= 10;
        len++;
    }
    if (len % 2 == 1)
        return 0;
    
    len /= 2;
    int base = 1;
    
    for (int i = 0; i < len; i++)
    {
        int remainder = bin % 10;
        bin2 = bin2 + (remainder * base);
        bin /= 10;
        base *= 10;
    }
    
    if (bin == bin2)
        return 1;
    else
        return 0;
    
}

int read_input(int **inputs)
{
    int n, i;
    scanf("%d", &n);
    
    printf("n = %d", n);
    
    for (i = 0; i < n; i++)
    {
       scanf("%d %d", &inputs[i][0], &inputs[i][1]);
       printf("%d %d", inputs[i][0], inputs[i][1]);
    } 
    
    
    return n;
}

long to_bin(long num)
{
    long decimal_num, remainder, base = 1, binary = 0;

    decimal_num = num;
    while (num > 0)
    {
        remainder = num % 2;
        
        binary = binary + (remainder * base);
        num = num / 2;
        base = base * 10;
    }
    printf("%ld \t %ld", decimal_num, binary);
    return binary;
}
