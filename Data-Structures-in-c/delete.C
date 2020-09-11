#include<stdio.h>
#include<conio.h>
void insert(int arr[],int size,int pos,int item)
{
	int i, j = size;
	size = size+1;
	while(j>=pos)
	{
		arr[j+1]=arr[j];
		j--;
	}
	arr[pos] = item;

	printf("\n The final array is: \n");
	for(i=0; i<size; i++)
	{
		printf("%d ", arr[i]);
	}
}
void main()
{
	int a[5] = {1,4,8,3,6};
	int pos, choice, size=5, i, item;
	//char more = 'y';
	clrscr();
	printf("\n The initial array is: \n");
	for(i=0; i<size; i++)
	{
		printf("%d ", a[i]);
	}
	printf("\n Enter the element you want to add: ");
	scanf("%d", &item);
	printf("Menu: \n");
	printf("1. Insert at beginning: \n ");
	printf("2. Insert at the end: \n");
	printf("3. Insert at any given position: \n");
	printf("Enter choice: ");
	scanf("%d", &choice);
       //	do{
	switch(choice)
	{
		case 1: insert(a,size,pos=0,item);
			break;
		case 2: insert(a,size,pos=5,item);
			break;
		case 3: printf("\n Enter the index number to insert the element: ");
			scanf("%d",&pos);
			insert(a,size,pos,item);
			break;
	}

	getch();
}