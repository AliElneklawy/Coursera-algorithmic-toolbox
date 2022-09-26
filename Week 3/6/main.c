#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    long long n;
    int ans[] = {};
    scanf("%lli", &n);
    int k = 0, sum = 0;
    long long x = sqrt((n+1)/2);
    for(int i = 1; i <= x; i++){
        sum = sum + i;
    }
    int final_num = n - sum;
    printf("%d", final_num);
}
