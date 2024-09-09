#include<stdio.h>
#include<stdlib.h>

struct Node {
    int elem;
    struct Node *next;
};

struct Node *create_list(struct Node *head);
void display(struct Node *head);
struct Node *addAtEnd(struct Node *head, int data);
struct Node *flipList(struct Node *head);

int main(){
    int data;
    struct Node *head;
    head = (struct Node *)malloc(sizeof(struct Node));
    head -> elem = 0;
    head -> next = NULL;

    head = create_list(head);
    head = flipList(head);
    display(head);
    return 0;
}

struct Node *create_list(struct Node *head){
    int i, n, data;
    printf("\nEnter the number of nodes: ");
    scanf("%d", &n);

    for(i = 1; i <= n; i++){
        printf("\nEnter the element to be inserted: ");
        scanf("%d", &data);
        head = addAtEnd(head, data);
    }
    return head;
}

void display(struct Node *head){
    struct Node *p;
    if (head -> next == NULL){
        printf("\nList is empty\n");
        return;
    }
    p = head -> next;
    printf("\nList is: \n");
    while (p != NULL){
        printf("%d ", p -> elem);
        p = p -> next;
    }
    printf("\n");
}

struct Node *addAtEnd(struct Node *head, int data){
    struct Node *p, *tmp;
    tmp = (struct Node *)malloc(sizeof(struct Node));
    tmp -> elem = data;
    p = head;
    while(p -> next != NULL)
        p = p -> next;
    p -> next = tmp;
    tmp -> next = NULL;
    return head;
}

struct Node *flipList(struct Node *head)
{
        struct Node *prev, *ptr, *next;
        prev = NULL;
        ptr = head -> next;
        while(ptr != NULL)
        {
                next = ptr -> next;
                ptr -> next = prev;
                prev = ptr;
                ptr = next;
        }
        head -> next = prev;
        return head;
}