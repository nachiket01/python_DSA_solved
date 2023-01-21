def me(li):
	inp = input().split()
	op = inp[0]
	val = inp[1:]

	if op == "print":
		print(li)

	else:
		qu = "li."+op+"("+",".join(val)+")"
		#     li.remove(,val)
		eval(qu)

li = []
for i in range(int(input())):
	me(li)
