
#include <iostream>
#include <conio.h>

using namespace std;

void merge(int *, int, int , int);

void mergeaort(int *a, int low, int high) {
    int mid;

    if(low < high) {
        mid = (low+high)/2;
        mergesort(a, low, mid);
        mergesort(a, mid, high);
        merge(a, low, high, mid);
    }
    return;
}

void merge(int *a, int low, int high, int mid) {
    int i, j, k, c[50];
    i = low;
    k = low;
    j = mid + 1;

    while(i <= mid && j <= high) {
        if(a[i] <= a[j]) {
            c[k] = a[i];
            k++;
            i++;
        }
        else {
            c[k] = a[j];
            k++;
            j++;
        }
    }

    while(i <= mid) {
        c[k] = a[i];
        k++;
        i++;
    }

    while(j <= high) {
        c[k] = a[j];
        k++;
        j++;
    }

    for(i = low; i < k; i++) {
        a[i] = c[i];
    }
}
