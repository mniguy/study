#include <stdio.h>

#define N 10

int arrListADT[N];
int n;

int size();
void traverse();
void initialize();
int addAtFirst(int);

void fullListException();

int size(){
    return n;
}

void traverse(){
    for (int i = 0; i < n; i++)
        printf("%d ", arrListADT[i]);
}

void initialize(){
    n = 0;
    return;
}

int addAtFirst(int e){
    if (n == N){
        fullListException();
        return 0;
    }
    else{
        for (int i = n-1; i >= 0; i--)
            arrListADT[i+1] = arrListADT[i];
        arrListADT[0] = e;
        n += 1;
    }
    return 1;
}

void fullListException(){
    printf("List is full.\n");
    return;
}

int main(){
    initialize();
    int i = 1;
    while(1){
        if (!addAtFirst(i)){
            traverse();
            break;
        }
        i++;
    }

/*  
    int i = 10; :10에 2씩 곱하며 커지는 배열의 역순
    while(1){
        if (!addAtFirst(i)){
            traverse();
            break;
        }
        i *= 2;
    } 
*/
    return 0;
}