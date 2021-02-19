#include <stdio.h>

int main() {
	int t[ 6 ] = {5, 2, 4, 6, 1, 3};
	int insert[6];
	int i=0, j=0, cle=0;
	for (j = 1; j < 6; j++) {
		cle = t[j];
		insert[j] = t[j];
		i = j - 1;
		while (i > 0 && insert[i] > cle) {
			insert[i+1] = insert[i];
				i = i -1; 
		insert[i+1] = cle; 
		}	
	}	
	for (j = 0; j < 6; j++) {
		printf("Element[%d]: %d\n", j, insert[j]);
	}
}
