#include <stdio.h>

int foo(int n)
{
	if (n == 1)
		return 1;
	else if (n == 2)
		return 2;
	else if (n == 3)
		return 4;
	else
		return foo(n - 1) + foo(n - 2) + foo(n - 3);
}

int main() {
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++)
	{
		int n;
		scanf("%d", &n);
		printf("%d\n", foo(n));
	}
	return 0;
}