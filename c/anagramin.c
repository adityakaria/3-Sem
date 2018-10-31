#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int check_anagram(char a[], char b[]);

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    
    int n;
    scanf("%d", &n);
    
    char inputs[n][100];
    
    int i;
    for (i = 0; i < n; i++)
    {
        scanf("%s", inputs[i]);
    }
    
    int count = 0;
    for (i = 0; i < n; i++)
    {
        if (strcmp(inputs[i], " ") == 0)
        {
            continue;
        }
        printf("%d", i+1);
        count++;
        for (int j = i + 1; j < n; j++)
        {
            if (check_anagram(inputs[i], inputs[j]) == 1)
            {
                printf(" %d", j+1);
                strcpy(inputs[j], " ");
            }
        }
        printf("\n");
    }
    return 0;
}

int check_anagram(char a[], char b[])
{
  int first[26] = {0}, second[26] = {0}, c = 0;
 
  while (a[c] != '\0')
  {
    first[a[c]-'a']++;
    c++;
  }
 
  c = 0;
 
  while (b[c] != '\0')
  {
    second[b[c]-'a']++;
    c++;
  }
 
 
  for (c = 0; c < 26; c++)
  {
    if (first[c] != second[c])
      return 0;
  }
 
  return 1;
}

