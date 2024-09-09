#include <stdio.h>
#include <stdlib.h>

/* 
Easier to implement addAtFirst because there was no need to check if the list is 
empty of to care about the pointer, pointing to the first element(head node),
unlike without a header. Also, it is more intuitive.
*/

/* Node */
typedef struct Node Node;
struct Node{
    int elem;
    Node *next;
};

/* Singly Linked List */
typedef struct List List;
struct List{
    Node *H; // header
    int n; // size
};

List *ListCreate();
Node *getnode();

void initialize(List*);
void traverse(List*);

void addAtFirst(List*, int);
void printAll(List*);

void invalidRankException();

List *ListCreate(){
    List *l;
    l = (List *)malloc(sizeof(List));
    initialize(l);
    return l;
}

Node *getnode(int elem){
    Node *node;
    node = (Node*)malloc(sizeof(Node));
    node -> elem = elem;
    node -> next = NULL;
    return node;
}

void initialize(List* l){
    l -> H = getnode(0); // create header
    l -> n = 0;
}

void addAtFirst(List* l, int i){
    Node *p = getnode(i); // new node
    p -> next = l -> H -> next; // insert at first
    l -> H -> next = p;
    l -> n++; // update size
}

void traverse(List* l){
    Node *p = l -> H -> next;
    while(p != NULL){
        printf("%d ", p -> elem);
        p = p -> next;
    }
}

void printAll(List* l){
    traverse(l);
}

void invalidRankException(){
    printf("Wrong access.");
    return;
}

int main(){
    List* singlyLinkedList_H = ListCreate();

    for (int i = 1; i < 10; i++){
        addAtFirst(singlyLinkedList_H, i);
    }

    printAll(singlyLinkedList_H);
    return 0;
}
