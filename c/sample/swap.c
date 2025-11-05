#include<stdio.h>
void main()
{
 int a,b,temp;
 printf("Enter any two numbers:");
 scanf("%d%d",&a,&b);
 temp=a;
 a=b;
 b=temp;
 printf("The numbers after swap: %d %d ",a,b);
}
