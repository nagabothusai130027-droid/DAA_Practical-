#include <stdio.h>

int main()
{
    int arr[100], n, num;

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    printf("Enter the sorted array elements:\n");
    for(int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    printf("Enter the element to search: ");
    scanf("%d", &num);

    int low = 0;
    int high = n - 1;
    int found = 0;

    while(low <= high)
    {
        int mid = (low + high) / 2;

        if(arr[mid] == num)
        {
            printf("Element found at index %d", mid);
            found = 1;
            break;
        }
        else if(arr[mid] < num)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }

    if(found == 0)
    {
        printf("Element not found");
    }

    return 0;
}