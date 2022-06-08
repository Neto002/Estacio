#include<stdio.h>


main() {

int i = 3, j = 5, k ;

int *p = &i, *q = &j;

k = *p - *q;

printf("%d", k);

}