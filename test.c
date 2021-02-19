#include <stdio.h>
 
int main () {

   int n[ 10 ] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}; /* n is an array of 10 integers */
   int i,j;
 
   /* initialize elements of array n to 0 */         
   /*for ( i = 0; i < 10; i++ ) {
      n[ i ] = i + 100;
   }*/
   printf("Size of n: %d\n", sizeof(n)); 
   /* output each array element's value */
   for (j = 0; j < 10; j++ ) {
      printf("Element[%d] = %d\n", j, n[j] );
   }
 
   return 0;
}
