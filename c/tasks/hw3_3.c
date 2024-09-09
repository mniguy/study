#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Stack{
    int top;
    unsigned capacity;
    int* array;
};

struct Stack* initialize(unsigned capacity){
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    if (!stack)
        return NULL;
    stack->top = -1;
    stack->capacity = capacity;
    stack->array = (int*) malloc(stack->capacity*sizeof(int));
    return stack;
}

int isEmpty(struct Stack* stack){
    return stack->top == -1 ;
}

char peek(struct Stack* stack){
    return stack->array[stack->top];
}

char pop(struct Stack* stack){
    if (!isEmpty(stack))
        return stack->array[stack->top--] ;
    return '$';
}

void push(struct Stack* stack, char op){
    stack->array[++stack->top] = op;
}

int operand(char ch){
    return (ch >= '0' && ch <= '9');
}

int Prec(char ch){
    switch (ch){
    case '+':
    case '-':
        return 1;
    case '*':
    case '/':
        return 2;
    }
    return -1;
}

int convert(char* exp){
    int i, k;
    struct Stack* stack = initialize(strlen(exp));
    if(!stack)
        return -1 ;
    for (i = 0, k = -1; exp[i]; ++i){
        if (operand(exp[i]))
            exp[++k] = exp[i];
        else if (exp[i] == '(')
            push(stack, exp[i]);
        else if (exp[i] == ')'){
            while (!isEmpty(stack) && peek(stack) != '(')
                exp[++k] = pop(stack);
            if (!isEmpty(stack) && peek(stack) != '(')
                return -1;           
            else
                pop(stack);
        }
        else {
            while (!isEmpty(stack) && Prec(exp[i]) <= Prec(peek(stack)))
                exp[++k] = pop(stack);
            push(stack, exp[i]);
        }
    }
    while (!isEmpty(stack))
        exp[++k] = pop(stack);
    exp[++k] = '\0';
    printf( "Output: %s", exp );
}

int main(){
    char exp[10000];
    printf("Input: ");
    fgets(exp, sizeof(exp), stdin);
    convert(exp);
    return 0;
}