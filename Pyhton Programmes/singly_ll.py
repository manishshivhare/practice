class GetNode:
    def __init__(self,x):
        self.next = None
        self.data = x
class LinkedList:
    def __init__(self):
        self.start = None
    def deleteFirst(self):
        
        if(self.start == None):
            print("Underflow")
        else:
            
            self.start = self.start.next
    def insertLast(self,val):
        newNode = GetNode(val)
        if(self.start == None):
            self.start = newNode
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
    def display(self):
        if(self.start ==None):
            print("List is empty")
        else:
            temp = self.start
            while temp!= None:
                print(temp.data , end= ' ')
                temp = temp.next
            
          

mylist = LinkedList()
mylist.insertLast(14)
mylist.insertLast(10)
mylist.insertLast(8)
mylist.insertLast(6)
mylist.deleteFirst()
mylist.display()




        
        