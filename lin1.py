def conti(a,x,n,z):
   
    for i in range(n):
        i=0
        if a[i] < 0:
            del(a[i])
        else:
            break

    for i in range(len(a)):
        if a[x] < 0:
            del(a[x])
        else:
            break

    for j in range(len(a)):
        z += a[j]
    print(z)


#driver seat

a = [1,-2,-3,-3,5,-6,-7,-8,-9]
x = -1
n = len(a)
z = 0
conti(a,x,n,z)