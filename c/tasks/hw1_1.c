#include <stdio.h>
#include <malloc.h>

int MostOnes(int** A, int n) {
	int i, j, row;
	i = j = row = 0;
	while ((i < n) && (j < n)) {
		if (A[i][j] == 0)
			i += 1;
		else {
			row = i;
			j += 1;
		}
	}
	return row;
}
int main() {
	int n = 10;
	int** A;
	A = (int**)malloc(n * sizeof(int*));

	for (int i = 0; i < n; i++) {
		A[i] = (int*)malloc(n * sizeof(int));
	}
	printf("Assume that 1s in any row of A precede 0s in that row \n");
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			printf("A[%d][%d] -> Enter 0 or 1: ", i, j);
			scanf("%d", &A[i][j]);
			if (A[i][j] == 1)
				continue;
			else if (A[i][j] == 0)
				continue;
			else {
				printf("Re-Enter 0 or 1\n");
				scanf("%d", &A[i][j]);
			}
		}
	}
	printf("The Matrix A is\n");
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			printf("%d", A[i][j]);
		}
		printf("\n");
	}
	printf("%d\n", MostOnes(A, n));
	return 0;
}
