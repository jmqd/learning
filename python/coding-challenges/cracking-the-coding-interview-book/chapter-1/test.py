test = [1,2,3,4,4,5,5,6,6,1]
test = "aaaabbbbccccdddd"
x = 10
while True:
    x += 1
    if x % 1000 == 0:
        print("########################")
    print(set(test))
