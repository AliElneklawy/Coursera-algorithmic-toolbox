#include <stdio.h>
#include <stdlib.h>

//long long PairWiseProd(long long [], int *);
long long PairWiseProdFast(long long arr[], int *n);

int main()
{
    int n;
    scanf("%d", &n);
    long long arr[n];
    for(int i = 0; i < n;){
        scanf("%lli", &arr[i++]);
    }

    long long res2 = PairWiseProdFast(arr, &n);
    printf("%lli", res2);
}

/*long long PairWiseProd(long long arr[], int *n)       //slow solution
{
    long long max_prod = 0, res;
    for(int i = 0; i < *n; i++){
        for(int k = 0; k < *n; k++){
            res = arr[i]* arr[k];
            if((res > max_prod) && i != k){
                max_prod = res;
            }
        }
    }
    return max_prod;
}*/

long long PairWiseProdFast(long long arr[], int *n)     //fast solution
{
    long long max_prod=0, max[2], find=0;
    int k=0, dec=2, j=0;
    while(dec--){
        for(int i = 0; i < *n; i++){
            if(arr[i] > find){
                find = arr[i];
                k = i;
            }
        }
        arr[k] = 0;
        max[j++] = find;
        find = 0;
    }
    max_prod = max[0] * max[1];
    return max_prod;
}
