#include<stdio.h>
#include<conio.h>
void main()
{
	int i,pos,item,size=5;
	int a[5] = {4,8,6,5,1};
	clrscr();
	printf("The initial array is: \n");
	for(i=0; i<size; i++)
	{
		printf("%d ",a[i]);
	}
	printf("\n\nEnter the index number of the element to be updated: ");
	scanf("%d",&pos);
	printf("\nEnter the new element: ");
	scanf("%d",&item);
	a[pos-1] = item;
	printf("\n\nThe final array is: \n");
	for(i=0; i<size; i++)
	{
		printf("%d ",a[i]);
	}
	getch();
}