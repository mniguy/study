#include <stdio.h>
#include <stdlib.h>

/* Node */
typedef struct Node Node;
struct Node{
    int elem;
    Node *next;
};

/* Singly Linked List */
typedef struct List List;
struct List{
    Node *H;
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
    node -> next = NULL;
    return node;
}

void initialize(List* l){
    l -> H = getnode();
    l -> n = 0;
}

void addAtFirst(List* l, int i){
    Node *p = getnode();
    p -> elem = i;
    p -> next = l -> H -> next;
    l -> H -> next = p;
    l -> n++;
}

void traverse(List* l){
    Node *p = l -> H -> next;
    while(p != NULL){
        printf("%d ", p -> elem);
        p = p -> next;
    }
}

List* flipList(List* l){
    Node *p = l -> H -> next;
    List *l2 = ListCreate();
    while(p != NULL){
        addAtFirst(l2, p -> elem);
        p = p -> next;
    }
    return l2;
}

void printAll(List* l){
    traverse(l);
}

void invalidRankException(){
    printf("Wrong access.");
    return;
}

int main(){
    List* listBeforeFlip = ListCreate();

    for (int i = 1; i < 10; i++){
        addAtFirst(listBeforeFlip, i);
    }

    printAll(listBeforeFlip);

    List* listAfterFlip = flipList(listAfterFlip);
    printf("\n");
    printAll(listAfterFlip);

    return 0;
}