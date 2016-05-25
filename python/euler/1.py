import sys
def is_divis(x): return x % 3 == 0 or x % 5 ==0
def getInteger(): return(int(input("Enter 0 to quit. Until what Integer? > ")))
def getAnswer(): return(sum(filter(is_divis,range(2,range_end))))
range_end = 1
while(range_end != 0):
  range_end  = getInteger()
  answer = getAnswer()
  print answer
