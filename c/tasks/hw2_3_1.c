#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int elem;
    struct Node *next;
}Node;

Node *list;

void init(){
    if (list == NULL){
        return;
    }
    else{
        Node *cur;
        cur = list;
        while (cur != NULL){
            list = cur -> next;
            free(cur);
            cur = list;
        }
    }
}

void add(int key) {

	Node * new_node = (Node*)malloc(sizeof(Node));
	new_node -> elem = key;
	new_node -> next = NULL;

	// Check first element
	if (list == NULL) {
		list = new_node;
	}
	else {
		// Add new node to head
		new_node -> next = list;
		list = new_node;
	}
}

void printAll(){

	Node* cur = list;
	while (cur != NULL){
		printf("%d ", cur -> elem);
		cur = cur -> next;
	}
	printf("\n");
}

int main(){
    int a, size;
    printf("Size of the list?: ");
    scanf("%d", &size);
    init();
    for (int i = 0; i < size; ++i){
        printf("Type element: ");
        scanf("%d", &a);
        add(a);
    }
    printAll();
    
}