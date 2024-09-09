#include <stdio.h>
#include <stdlib.h>

/* Node */
typedef struct Node Node;
struct  Node {
    int elem;
    Node *next;
};

/* Singly Linked List */
typedef struct List List;
struct List{
    Node *headNode;
    int n;
};

List *ListCreate();
Node *getnode();

void initialize(List *);
void traverse(List *);

void addAtFirst(List *, int);
void printAll(List *);

void invalidRankException();

List *ListCreate(){
    List *l;
    l = (List *)malloc(sizeof(List));
    initialize(l);
    return l;
}

Node *getnode(int i){
    Node *node;
    node = (Node *)malloc(sizeof(Node));
    node -> elem = i;
    node -> next = NULL;
    return node;
}

void initialize(List *l){
    l -> n = 0;
}

void addAtFirst(List *l, int i){
    Node *p = getnode(i);
    if (l -> n == 0){
        l -> headNode = p;
    }
    else{
        p -> next = l -> headNode;
        l -> headNode = p;
    }
    l -> n++;
}

void traverse(List *l){
    Node *p = l -> headNode;
    while (p != NULL){
        printf("%d ", p -> elem);
        p = p -> next;
    }
}

void printAll(List *l){
    traverse(l);
}

void invalidRankException(){
    printf("Wrong access.");
    return;
}

int main(){
    List* SinglyLinkedList = ListCreate();

    for (int i = 1; i < 10; i++)
        addAtFirst(SinglyLinkedList, i);

    // for (int i = 1; i < 50; i+=2): 홀수 출력

    printAll(SinglyLinkedList);
    return 0;
}