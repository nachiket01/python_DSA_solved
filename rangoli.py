import string
alphabet_string = string.ascii_lowercase
n=5
l = []
for i in range(n):
	s="-".join(alphabet_string[i:n])
	l.append((s[::-1]+s[1:]).center(4*n-3,"-"))

#print('\n'.join(l[:0:-1]+l))
print('\n'.join(l[:0:-1]+l))
