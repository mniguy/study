#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node {
   int elem;	
   struct Node *next;
   struct Node *prev;
};

struct Node *head = NULL;

struct Node *last = NULL;

struct Node *current = NULL;

bool isEmpty() {
   return head == NULL;
}

int length() {
   int length = 0;
   struct Node *current;
   for(current = head; current != NULL; current = current->next){
      length++;
   }
   return length;
}

void printAll() {
   struct Node *ptr = head;
   while(ptr != NULL) {        
      printf("%d ", ptr->elem);
      ptr = ptr->next;
   }
}

void flipList() {
   struct Node *ptr = last;
   printf("\n");
   while(ptr != NULL) {    
      printf("%d ", ptr->elem);
      ptr = ptr ->prev;
   }	
}

void addAtFirst(int elem) {
   struct Node *link = (struct Node*) malloc(sizeof(struct Node));
   link->elem = elem;
	
   if(isEmpty()) {
      last = link;
   } else {
      head->prev = link;
   }
   link->next = head;
   head = link;
}

void main(){
    addAtFirst(4);
    addAtFirst(3);
    addAtFirst(2);
    addAtFirst(1);
    printAll();
    flipList();
}