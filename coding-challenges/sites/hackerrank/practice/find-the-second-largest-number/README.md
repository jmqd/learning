# find the second largest number

## Problem:

---
You are given N numbers. Store them and find the second largest number.

The first line contains N. The second line contains an array A of N
integers each separated by a space.

## Solution:

---
Use a heap. Heaps are made for such problems. Could solve this the old
fashioned way, iterating through the `distinct_arr`, of course... but
where's the fun in that?

## Gotcha:

---
Make a set of the array, because we're looking for the second largest
number, not the value of the element in the array ranked 2nd.
