#include<stdio.h>
#include<stdlib.h>
void main()
{
  int l,b,area,p;
  printf("Enter the length of the rectangle:");
  scanf("%d",&l);
  printf("Enter the breadth of the rectangle:");
  scanf("%d",&b);
  area=l*b;
  p=2*(l+b);
  printf("The area of rectangle: %d",area);
  printf("\nThe perimeter of rectangle: %d",p);
}
 
