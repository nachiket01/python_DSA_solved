sortString = str()
String='miyami'

#getting uniqe list

for i in String:
	if i  not in sortString:
		sortString = sortString+i

sortString= list(sortString)

# sorting uniqe list

for i in range(0,len(sortString)):
	for j in range(i+1, len(sortString)):
		if sortString[i]>= sortString[j]:
			sortString[i],sortString[j]=sortString[j],sortString[i]

count = 0

# checking no duplicates in string 

for i in sortString:
	for j in range(len(String)):
		if i == String[j]:
			count +=1	
	print(i,"-",count)
	count = 0




