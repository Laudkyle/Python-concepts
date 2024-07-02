class Node:
    def __init__(self,head):
        self.head = head
        self.next= None
        
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
            current_node =new_node
        
        
        
class LinkedList:
    def __init__(self,data):
        self.data = data
 
 
Node_one = Node()
Node_one.insertEnd("One")        
list_one = LinkedList()

