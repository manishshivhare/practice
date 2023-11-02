class GetNOde:
    def __init__(self, x):
        self.next = None
        self.prev = None
        self.data = x
class DoublyLinkedList:
    
    def __init__(self):
        self.start = None
    def insert(self, val):
        newNode = GetNOde(val)
        if(self.start ==None):
            self.start = newNode
        else:
            temp = self.start
            while(temp.next != None):
                temp = temp.next 
            temp.next = newNode
            newNode.prev = temp   
    def display(self):
        temp = self.start
        while(temp != None):
            copy = temp  
            # print(copy.data, end = " ")     
            temp = temp.next   
        while(copy != None):
            print(copy.data, end = " ")    
            copy = copy.prev
             
       
myList = DoublyLinkedList()
myList.insert(14)
myList.insert(15)
myList.insert(17)
myList.display()