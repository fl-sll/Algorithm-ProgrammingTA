#include <stdio.h>
#include <time.h>

int fibLoop(int n)
{
    int first = 0, second = 1, next;
    for (int i = 0; i <= n; i++)
    {
        printf("%d ", first);
        next = first + second;
        first = second;
        second = next;
    }
}

int main()
{
    int n;
    printf("Enter number of fibonnaci numbers: ");
    scanf("%d", &n);
    clock_t t;
    t = clock();
    fibLoop(n-1);
    t = clock()-t;
    double time_taken = ((double)t)/CLOCKS_PER_SEC;
    printf("Time taken: %f", time_taken);
}