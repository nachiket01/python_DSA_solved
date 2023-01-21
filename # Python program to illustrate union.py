def Union(a,b):
    m = a[-1]
    n = b[-1]

    if m>n:
        ans = m
    else:
        ans = n

    newt = [0]*(ans +1)
    print(a[0], end = " ")


    newt[a[0]] += 1

    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            print(a[i], end = " ")
            newt[a[i]]

    for j in range(0, len(b)):
        if newt[b[0]] ==0:
            print(b[j], end = " ")
            newt[b[j]] +=1

if __name__=="__main__":
    a = [1,2,3,4,5]
    b = [2,3,6]
    Union(a,b)
