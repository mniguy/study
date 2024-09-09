#include <stdio.h>
#include <stdlib.h>

/* Node */
typedef struct Node Node;
struct Node{
    int elem;
    Node *prev;
    Node *next;
};

/* Singly Linked List */
typedef struct List List;
struct List{
    Node *H;
    Node *T; // trailer
    int n;
};

List *ListCreate();
Node *getnode();

void initialize(List*);
void traverse(List*);

void addAtFirst(List*, int);
List *flipList(List*);

void printAll(List*);

void invalidRankException();

List *ListCreate(){
    List *l;
    l = (List*)malloc(sizeof(List));
    initialize(l);
    return l;
}

Node *getnode(){
    Node *node;
    node = (Node*)malloc(sizeof(Node));
    node -> elem = 0;
    node -> prev = NULL;
    node -> next = NULL;
    return node;
}

void initialize(List* l){
    l -> H = getnode();
    l -> T = getnode();
    /* link header and trailer */
    l -> H -> next = l -> T;
    l -> T -> prev = l -> H;
    l -> n = 0;
}

void addAtFirst(List* l, int i){
    Node *p = getnode();
    p -> elem = i;
    /* insert between first node and the header node */
    p -> next = l -> H -> next;
    l -> H -> next -> prev = p;
    l -> H -> next = p;
    p -> prev = l -> H;

    l -> n++;
}

void traverse(List* l){
    Node *p = l -> H -> next;
    while(p != l -> T){
        printf("%d ", p -> elem);
        p = p -> next;
    }
}

List* flipList(List* l){
    Node *p = l -> T -> prev;
    Node *q = l -> H -> next;

    int temp = 0;
    while(p != q){
        /* swap elements */
        temp = p -> elem;
        p -> elem = q -> elem;
        q -> elem = temp;
        /* move to next/prev */
        p = p -> prev;
        q = q -> next;
    }
    return l;
}

void printAll(List* l){
    traverse(l);
}

int main(){
    List* listBeforeFlip = ListCreate();

    for (int i = 1; i < 10; i++)
        addAtFirst(listBeforeFlip, i);
    printAll(listBeforeFlip);

    List* listAfterFlip = flipList(listBeforeFlip);
    printf("\n");
    printAll(listAfterFlip);
}