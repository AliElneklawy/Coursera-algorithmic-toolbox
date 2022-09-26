#include <stdio.h>
#include <stdlib.h>

int change(int m, int denominations[3])
{
    int maxcoin = 0;
    if(m == 0){
        return 0;
    }
    for(int i = 0; i < 3; i++){
        if(denominations[i] <= m){
            maxcoin = denominations[i];
        }

    }
    //printf("%d ", maxcoin);
    m = m - maxcoin;
    return 1+change(m, denominations);
}

int main()
{
    int m, numOfCoins = 0, denominations[3] = {1, 5, 10};
    scanf("%d", &m);
    numOfCoins = change(m, denominations);
    printf("%d", numOfCoins);
}
