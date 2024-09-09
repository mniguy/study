#include <stdio.h>
#include <stdlib.h>

#define SIZE 4

int items[SIZE];
int front = -1, rear = -1;

int isFull(){
    if ((front == rear + 1) || (front == 0 && rear == SIZE - 1))
        return 1;
    return 0;
}

int isEmpty(){
    if (front == -1)
        return 1;
    return 0;
}

void addAtFirst(int element){
    int i=rear;
    if (isFull())
        printf("\n Queue is full!!! \n");
    else{
        if (front == -1){
            front = rear = 0;
            items[front] = element;
        }
        else{
            if (front == 0){
                front = SIZE - 1;
            }
            else{
                front--;
            }
            items[front] = element;
        }
        printf("\n Inserted -> %d", element);
    }
}

int removeAtFirst(){
    int element;
    if (isEmpty()){
        printf("\n Queue is empty!!! \n");
        return (-1);
    }
    else{
        element = items[front];
        if (front == rear){
            front = -1;
            rear = -1;
        }
        else{
            front = (front + 1) % SIZE;
        }
        printf("\n Deleted element -> %d \n", element);
        return (element);
    }
}

void printAll(){
    int i;
    if (isEmpty())
        printf(" \n Empty Queue\n");
    else{
        printf("\n Items -> ");
        for (i = front; i != rear; i = (i + 1) % SIZE){
            printf("%d ", items[i]);
        }
        printf("%d ", items[i]);
    }
}

int main(){
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
}