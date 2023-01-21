def arm(snum,sum1,n):

    for i in snum:
        sum = int(i)**n
        sum1 += sum

    if sum1 == int(snum):
        print(snum,"is a armstrong number")
    else:
        print(snum,"is not a armstrong number")


snum = str(input())
sum1 = 0
n = len(snum)
arm(snum,sum1,n)