import union
string = " tekihcan"
reversed_string = []
s= union.Stack()
s.push(string)

while not s.isempty():
    reversed_string += s.pop()

print(reversed_string)
