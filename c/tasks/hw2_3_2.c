#include <stdio.h>
#include <stdlib.h>

struct Node{
    int elem;
    struct Node *Next;
};

struct Node *head;

void addAtFirst(int x){
    struct Node *A=(struct Node *)malloc(sizeof(struct Node));
    if (A != NULL){
        A -> elem = x;
        A -> Next = head;
        head = A;
    }
}

void printAll(){
    printf("[");
    struct Node *B = head;
    while (B != NULL){
        printf(" %d", B -> elem);
        B = B -> Next;
    }
    printf(" ]\n");
}

int main(){
    head = NULL;
    int d, i = 0, f;
    printf("How many number you want to insert: \n");
    scanf("%d", &d);
    for (i; i < d; i++){
        printf("Enter your number: \n");
        scanf("%d", &f);
        addAtFirst(f);
        printAll();
    }
}
