/*
 * We are given two sorted array. We need to merge these two arrays such that the initial numbers (after complete sorting) are in the first array and the 
   remaining numbers are in the second array. Extra space allowed in O(1).
 *
 * Input: ar1[] = {1, 5, 9, 10, 15, 20};
 *        ar2[] = {2, 3, 8, 13};
 * Output: ar1[] = {1, 2, 3, 5, 8, 9}
 *         ar2[] = {10, 13, 15, 20}  
 *
 * Date : 1st February, 2016.
 *
 */

#include<stdio.h>
int main()
{
    int ar1[] = {1,5,9,10,15,20};
    int ar2[] = {2,3,8,13} ;
    int size_of_ar2 = sizeof(ar2)/sizeof(int);
    int size_of_ar1 = sizeof(ar1)/sizeof(int);
    int i,j;
    for(i=size_of_ar2-1; i>=0 ; i--)
    {
        int last = ar1[size_of_ar2-1];
        printf("%d\n",ar2[i]);
        for(j=size_of_ar1-1 ; j>=0 && ar1[j] > ar2[i] ; j--)
        {
            ar1[j+1] = ar1[j];
            printf("\t%d\n",ar1[j+1]);
        }
        if(j != size_of_ar1 )
        {
            ar1[j+1] = ar2[i];
            ar2[i] = last;
        }
    }
    for(i=0;i<size_of_ar1;i++)
    {
        printf("%d ",ar1[i]);

    }
    printf("\n");
    for(i=0;i<size_of_ar2;i++)
    {
        printf("%d ",ar2[i]);

    }
}


