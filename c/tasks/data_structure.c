#include <stdio.h>
#include <stdlib.h>

struct Node {
	int elem;
	struct Node* next;
};
int main() {
	struct Node* head = NULL;
	struct Node* second = NULL;

	head = (struct Node*)malloc(sizeof(struct Node));
	second = (struct Node*)malloc(sizeof(struct Node));

	head->elem = 7;
	head->next = second;
}