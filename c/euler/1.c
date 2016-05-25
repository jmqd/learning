#include <stdio.h>
#include <stdlib.h>
int main() {
  int n,sum=0,d=0;
  printf( "\n# This program sums all integers (divisible by 3 or 5) being less than n.\n\n# Please enter an integer for n: ");
  scanf("%d",&d);
    for(n=0;n<d;n++) {
      if (d==0) {
        exit(0);
      }
      if (n%3==0||n%5==0){
        sum += n;
      }
      if (n == d - 1){
        printf("\n#################\n\n$  Of all integers below %d, the sum of those integers \n$  which are divisible by either 3 or 5 is %d.",d,sum);
        sum = 0,n=0; 
        printf("\n#################\n\n$  Please enter an integer for n to compute again, or 0 to quit > ");
        scanf("%d",&d);
      }
    }
 }  
