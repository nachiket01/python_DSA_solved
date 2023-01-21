nterms = 10
n1, n2 = 0, 1
count = 0
ls = []
j = int(input())

while count < nterms:
    nth = n1 + n2
    ls.append(nth)
    n1 = n2
    n2 = nth
    count += 1
print(ls)
if ls[j]%2 == 0:
    print("dead")
else:
    print("live")