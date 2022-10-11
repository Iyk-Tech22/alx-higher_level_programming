#include <stdio.h>

int main(void)
{
	int num;
	int *ptr;

	num = 10;
	ptr = &num;
	void add(int *nptr)
	{
		*nptr += 10;
	}
	add(&num);
	printf("%d\n", num);
	return (0);
}
