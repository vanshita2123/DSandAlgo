#include<stdio.h>
#include<conio.h>
void main()
{
	int i,j,pos,size=5;
	int a[5] = {3, 4, 9, 7, 2};
	clrscr();
	printf("The initial array is: \n");
	for(i=0; i<size; i++)
	{
		printf("%d ",a[i]);
	}
	printf("\nEnter the index number of the element to be deleted: ");
	scanf("%d",&pos);
	j = pos;
	while(j<size)
	{
		a[j-1] = a[j];
		j++;
	}
	size--;
	printf("The final array is: \n");
	for(i=0; i<size; i++)
	{
		printf("%d ",a[i]);
	}
	getch();
}








