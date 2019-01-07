#include <bits/stdc++.h>
#include <iostream>

using namespace std;

void printArr(int *array, int size);
void mergeSort(int* array, int l, int r);
void merge(int* arr, int l, int m, int r);

int main(void) {
    int arr[] = {2, 5, 7, 3, 8, 1, 0, 34, 69, 9, 6};
    cout << sizeof(arr) << "\t" << sizeof(arr[0]);
    int arrSize = sizeof(arr) / sizeof(arr[0]);
    printArr(arr, arrSize);

    mergeSort(arr, 0, arrSize-1);
    cout << "After mergesort" << endl;
    printArr(arr, arrSize);

    return 0;
}

void printArr(int *array, int arrSize) {
    cout << endl << "\t";
    for (int i = 0; i < arrSize; i++) {
        cout << array[i] << "\t";
    }
    cout << endl;
}


void mergeSort(int* arr, int l, int r) {
    if (l < r) {
        int m;
        m = l + (r - 1) / 2;
        cout << endl << l << " | " << m << " | " << r << " ::\t";

        for (int i = l; i <= r; i++) {
            cout << arr[i] << "\t";
        }
        cout << "__________" << endl;

        mergeSort(arr, l, m);
        cout << "~~~~~~~~~~~~~ " << m << endl;
        mergeSort(arr, m+1, r);
        cout << "============= " << m+1 << endl;
        merge(arr, l ,m, r);
    }
}


void merge(int* arr, int l, int m, int r) {
    cout << "Merging....." << endl;
    // Make 2 sub arrays
    int i, j, n1 = 0, n2 = 0;
    n1 = m - l + 1;
    n2 = r - m;
    int arr1[n1], arr2[n2]; 

    // Split orginal array into new arrays
    for (i = 0; i < m + 1; i++)
        arr1[i] = arr[i];
    for (j = 0; j < r - m; j++, i++)
        arr2[j] = arr[i];

    cout << "arr: " << l << " | " << m << " | " << r << endl << "\t";
    
    for (int i = 0; i < m + 1; i++) {
        cout << arr1[i] << "\t";
    }
    cout << "||\t";
    
    for (int i = 0; i < r - m; i++) {
        cout << arr2[i] << "\t";
    }
    
    cout << "__________" << endl;
    // printArr(arr1, m + 1);
    // printArr(arr2, r - m - 1);
    
    // merge the two parts back into original array as sorted
    int k = 0;
    i = 0;
    j = 0;
    int newArr[n1+n2];
    // cout << arr[0] << ": " << n1 << "\t" << n2 << endl;
    
    while (i < n1 && j < n2) {
        if (arr1[i] < arr2[j]) {
            newArr[k] = arr1[i];
            i++;
        }
        if (arr1[i] > arr2[j]) {
            newArr[k] = arr2[j];
            j++;
        }
        k++;
    }
    printf("\n");
    for (int p = 0; p < (sizeof(newArr) / sizeof(newArr[0])); p++) {
        cout<<newArr[i] << "\t";
    }
    printf("\n");
    // to move the remaining elements from both parts into main array
    cout << i << " : "  << n1 << " : "  << j << " : "  << n2 << " : " << k << endl;
    while (i < n1) {
        newArr[k] = arr1[i];
        k++;
    }
    
    while (j < n2) {
        newArr[k] = arr2[j];
        k++;
    }
    
    cout << "printed:\t ";
    printArr(arr, sizeof(newArr)/sizeof(newArr[0]));
    cout << "-----------------------------" << endl;
}
