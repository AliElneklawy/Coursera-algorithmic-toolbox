#include <stdio.h>
#include <stdlib.h>

long long int fib(int) ;

int main()
{
    long long int n = 0;
    scanf("%d", &n);
    n = fib(n);
    printf("%d", n);
    return 0;

}


long long int fib(int n)
{
    if (n <= 1){
       return n;
    }

    return fib(n-1) + fib(n-2);
}
