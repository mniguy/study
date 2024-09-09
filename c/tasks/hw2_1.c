#include <stdio.h>
#include <stdlib.h>

#define MAX_LIST_SIZE 10

typedef int element;

typedef struct {
    element array[MAX_LIST_SIZE];
    int size;
} ArrayListType;

void error(char *message){
    fprintf(stderr, "%s\n", message);
    exit(1);
}

void init(ArrayListType* L){
    L->size = 0;
}

int is_empty(ArrayListType* L){
    return L->size == 0;
}

int is_full(ArrayListType* L){
    return L->size == MAX_LIST_SIZE;
}

element get_entry(ArrayListType* L, int pos){
    if (pos<0 || pos>=L->size)
        error("위치 오류");
    return L -> array[pos];    
}

void print_list(ArrayListType *L) {
    int i;
    for (i = 0; i < L -> size; i++){
        printf("%d ", L -> array[i]);
    }
    printf("\n");
}

void insert_first(ArrayListType *L, element item){
    if(!is_full(L)){
        for(int i = (L -> size - 1); i >= 0; i--){
            L -> array[i+1] = L -> array[i];
        }
        L -> array[0] = item;
        L -> size++;
        if (L -> size == MAX_LIST_SIZE){
            print_list(L);
        }
    }
}

int main(void){
    ArrayListType list;
    
    init(&list);
    
    insert_first(&list, 10);
    insert_first(&list, 9);
    insert_first(&list, 8);
    insert_first(&list, 7);
    insert_first(&list, 6);
    insert_first(&list, 5);
    insert_first(&list, 4);
    insert_first(&list, 3);
    insert_first(&list, 2);
    insert_first(&list, 1);

    return 0;
}