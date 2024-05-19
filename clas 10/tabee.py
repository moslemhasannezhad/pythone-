def countDown (num):
    if num>=0:
        if num ==0:
            print(num)
        else:
            print(num)
            countDown(num-1)

def countUp(num):
    if num >=0:
        if num==0:
            print(num)
        else:
            countUp(num-1)
            print(num)

countDown(5)
countUp(4)