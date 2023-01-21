if __name__ == '__main__':
    li= []
    li1=[]
    for _ in range(int(input())):
        name = input()
        li.append(name)
        score = float(input())
        li1.append(score)

    hi = 1
    lo = 0

    for i in range(len(li1)):
        if li1[lo]>li1[hi]:
            hi,lo=lo,hi
            lo+=1
            break
        else:
            hi+=1

    print(hi,lo)