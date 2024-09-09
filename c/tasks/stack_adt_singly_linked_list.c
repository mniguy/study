#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node *next;
}*stack;

void initialize(){
    stack = NULL;
}

int isEmpty(){
    if (top == NULL)
        return 1;
    else
        return 0;
}

int top(){
    return stack->data;
}

int size(struct node *head){
    if (head == NULL){
        printf("Error: Invalid stack pointer\n");
        return;
    }
    int length = 0;
    while (head != NULL){
        head = head->next;
        length++;
    }
    return length;
}

void push(int num){
    struct node *temp;
    temp = (struct node *)malloc(1*sizeof(struct node));
    temp->data = num;
    if (stack == NULL){
        stack = temp;
        stack->next = NULL;
    }
    else{
        temp->next = stack;
        stack = temp;
    }
}

void pop(){
    struct node *temp;
    if (isEmpty(stack)){
        printf("\nStack is Empty\n");
        return;
    }
    else{
        temp = stack;
        stack = stack->next;
        printf("Removed Element: %d\n", temp->data);
        free(temp);
    }
}

void iterate(struct node *nodePtr){
    while (nodePtr != NULL){
        printf("%d", nodePtr->data);
        nodePtr = nodePtr->next;
        if (nodePtr != NULL)
            printf("->");
    }
    printf("\n");
}

void main(){
    initialize();

}
