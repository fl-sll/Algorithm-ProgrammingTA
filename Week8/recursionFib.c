#include <stdio.h>
#include <time.h>

int recursionFib(int n)
{
    if (n <= 1)
    {
        return n;
    }
    else
    {
        return (recursionFib(n-1) + recursionFib(n-2));
    }
}

int main()
{
    int n, c;
    int i = 0;
    printf("Enter number of fibonnaci numbers: ");
    scanf("%d", &n);
    clock_t t;
    t = clock();
    for (c = 1; c <= n; c++)
    {
        printf("%d ", recursionFib(i));
        i++;
    }
    t = clock()-t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC;
    printf("Time taken: %f", time_taken);
}