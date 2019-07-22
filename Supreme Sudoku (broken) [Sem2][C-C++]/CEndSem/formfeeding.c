#include<stdio.h>
int main()
{
	printf("\nHi\nBye\n");
	printf("Okay, accepting here:\f");printf("\n\nOkay. Done.");
	char a[100];
	printf("\r\f");
	scanf("%s",a);
	printf("\r\r");
	scanf("%s",a);	
	return 0;
}