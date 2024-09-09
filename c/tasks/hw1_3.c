#include <stdio.h>
#define Num_of_Coin 4
#define Ten_Won 10
#define Fifty_Won 50
#define One_Hundred_Won 100
#define Five_Hundred_Won 500

int Count(int nwon, int coins[], int coinIdx) {
	int CurCoinValue = coins[coinIdx];
	int CurCoinCnt = 0;
	int ways = 0;

	if (Num_of_Coin == coinIdx) {
		if (nwon == 0)
			return 1;
		else
			return 0;
	}
	for (CurCoinCnt = 0; CurCoinValue * CurCoinCnt <= nwon; CurCoinCnt++) {
		ways += Count(nwon - (CurCoinValue * CurCoinCnt), coins, coinIdx + 1);
	}
	return ways;
}
int main() {
	int nwon;
	printf("Enter the value to be converted into coins: ");
	scanf("%d", &nwon);

	int coins[Num_of_Coin] = { Five_Hundred_Won, One_Hundred_Won, Fifty_Won, Ten_Won };
	int Num_of_Count = Count(nwon, coins, 0);

	printf("Num of Count: %d\n", Num_of_Count);

	return 0;
}