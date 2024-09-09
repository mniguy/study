#include <stdio.h>

#define N 4

int arrListADT[N];
int n; // size of list
int f; // first index
int l; // last index

int size();

int get(int);

void traverse();
void initialize();

void addAtFirst(int);
void removeAtFirst();
void printAll();

void invalidRankException();
void fullListException();
void emptyListException();

int size(){
    return (N - f + l + 1) % N;
}

int get(int r){
    if ((r < 0) || (r >= size()))
        invalidRankException();
    return arrListADT[(f + r) % N];
}

void traverse(){
    n = size();
    for (int i = 0; i < n; i++)
        printf("%d ", get(i));
}

void initialize(){
    n = 0;
    f = 0;
    l = n - 1;
    return;
}

void addAtFirst(int e){
    n = size();

    if (n == 0){
        arrListADT[f] = e;
        l = 0;
        return;
    }

    if (n == N - 1){
        fullListException();
        return;
    }
    arrListADT[(N + f -1) % N] = e;
    f = (N + f - 1) % N;
    return;
}

void removeAtFirst(){
    n = size();
    if (n == 0)
        emptyListException();
    else
        f = (f + 1) % N;
}

void printAll(){
    traverse();
    return;
}

void invalidRankException(){
    printf("wrong access.\n");
    return;
}

void fullListException(){
    printf("List is full.\n");
    return;
}

void emptyListException(){
    printf("List is empty.\n");
    return;
}

int main(){
    initialize();
    addAtFirst(3);
    addAtFirst(7);
    removeAtFirst();
    addAtFirst(6);
    removeAtFirst();
    addAtFirst(1);
    addAtFirst(2);
    removeAtFirst();
    addAtFirst(4);
    printAll();
    return 0;
}