#include <stdio.h>
#include <stdlib.h>
#define intmax 2147483647

int findMin(long long w, long long capacity)
{
    return ((w<capacity)?w:capacity);
}

double maxloot(long long capacity, long long weight[], long long value[], int num_items)
{
    if(capacity == 0)   return 0;
    int index, m;
    long long price = -1;
    for(int i=0; i<num_items; i++){
        if(value[i] > price){
            index = i;
            price = value[i];
        }
    }
    //printf("%d ", index);
    long long amount = findMin(weight[index], capacity);
    //printf("\n%lli", amount);
    price = value[index] * (amount/weight[index]);
    int length = sizeof(value)/sizeof(value[0]);
    long long temp1 = value[length-1];
    long long temp2 = weight[length-1];

    value[length] = value[index];
    weight[length] = weight[index];
    value[length] = '\0';
    weight[length] = '\0';


    return price + maxloot(capacity, weight, value, num_items);

}

int main()
{
    long long capacity;     int num_items;
    scanf("%d %lli", &num_items, &capacity);
    long long value[num_items], weight[num_items];
    for(int i=0; i<num_items; i++){
        scanf("%lli %lli", &value[i], &weight[i]);
    }

    /*for(int i=0; i<num_items; i++){
        printf("%lli %lli\n", value[i], weight[i]);
    }*/
    double ans = maxloot(capacity, weight, value, num_items);
    printf("%.4lf", ans);
}
