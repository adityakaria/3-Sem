#include <stdio.h>
#include <stdlib.h>
#define MAX 256

int main(void) {
    char copier, sourceName[MAX], destName[MAX];
    FILE *source, *dest;

    // Get source filename
    a:
    printf("\nEnter name of SOURCE file:\t");
    scanf("%s", sourceName);

    //check for errors
    source = fopen(sourceName, "r");
    if (source == NULL) {
        printf("ERROR: File could not be opened. Please try again:\n");
        goto a;
    }

    // get destination filename
    b:
    printf("\nEnter name of DESTINATION file:\t");
    scanf("%s", destName);

    // check for errors
    dest = fopen(destName, "w");
    if (dest == NULL) {
        printf("ERROR: File could not be opened. Please try again:\n");
        goto b;
    }

    // copy contents
    while ((copier = fgetc(source)) != EOF) {
        fputc(copier, dest);
    }
    
    fclose(source);
    fclose(dest);
    
    // to  delete original file and check for errors
    int status = remove(sourceName);
    if (status == 0) {
        printf("Original file deleted Succesfully\n");
    }
    else {
        printf("ERROR: Could not delete original file");
    }

    printf("\nOPERATION SUCCESSFULL\n");
    return 0;
}
