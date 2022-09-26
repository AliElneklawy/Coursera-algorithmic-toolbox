#include <stdio.h>
#include <stdlib.h>

unsigned long long fib(int);

int main()
{
    int n;
    unsigned long long ans = 0;
    scanf("%d", &n);
    if(n == 0){
        printf("%d", 0);
    }
    else{
        ans = fib(n);
        printf("%llu", ans);
    }
}

unsigned long long fib(int n)
{
    unsigned long long f[n];
    int i;
    f[0] = 0;
    f[1] = 1;
    for(i = 2; i <= n; i++){
        f[i] = f[i-1] + f[i-2];
    }
    return f[i-1];
}
