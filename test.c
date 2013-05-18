#include <stdio.h>

extern char foo[];

int
main(void)
{
    puts(foo);
}
