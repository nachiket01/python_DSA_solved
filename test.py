class node:
    def __init__(self,data = None) -> None:
        self.data = data
        self.next = None

class sll:
    def __init__(self):
        self.head = None
    
    def listprint(self):
        printd =self.head
        while printd is not None:
            print(printd.data)
            printd = printd.next
    

lisr = sll()
lisr.head = node("mon")
e2 = node("Tue")
e3 = node("web")

lisr.head.next = e2
e2.next=e3
lisr.listprint()

