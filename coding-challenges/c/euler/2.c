#include <stdio.h>
#include <stdlib.h>

int main() {
  int a=0,b=1,sum=0,c=0,d;
  printf( "\n# This program sums the even parity terms of the fibonacci sequence, for values less than n.\n\n# Please enter an integer for n: ");
  scanf("%d",&d);
  for(a = 1;a < d;a) {
    if(a%2==0) {
      sum += a;
    }
  c = b;
  b += a;
  a = c;
  }
  printf("%d\n",sum);
}
