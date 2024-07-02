class Node:
    def __init__(self,data):
        self.data = data
        self.next= None
        
        
class LinkedList:
    def __init__(self,head):
        self.head = head
    
    def insertEnd(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.next
            while True:
                if current_node is None:
                    break
                else:
                    current_node = current_node.next
            current_node = new_node
        
    def show(self):
        current_node = self.head
        while current_node.next is not None:
            print(current_node.data)
            
 
Node_one = Node("One")
Node_two = Node("two")
Node_three = Node("three")



list_one = LinkedList()

list_one.insertEnd(Node_one)
list_one.insertEnd(Node_two)
list_one.insertEnd(Node_three)

list_one.show()

