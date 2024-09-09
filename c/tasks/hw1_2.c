#include<stdio.h>

void rprintDigits(int n) {
	if (n < 10) {
		printf("%d", n);
	}
	else {
		printf("%d\n", n % 10);
		rprintDigits(n / 10);
	}
}
void printDigits() {
	int n = 0;
	printf("Enter a number\n");
	scanf("%d", &n);
	if (n < 0) {
		printf("Negative number\n");
	}
	else {
		rprintDigits(n);
	}
}