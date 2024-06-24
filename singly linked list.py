class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while True:
                if last_node.next is None:
                    break
                else:
                    last_node = last_node.next
            last_node.next = new_node
            
    def printList(self):
        if self.head is None:
            print("List is empty!!!")
            return
        current_node = self.head
        while True:
            if current_node is None:
                break
            print(current_node.data)
            current_node = current_node.next
            
    def insertHead(self, new_node):
        temp = self.head
        self.head =new_node
        self.head.next =temp
        
        
        
Node1 = Node("node 1")
Node2 = Node("node 2")
Node3 = Node("node 3")
Node4 = Node("node 4")
Node5 = Node("node 5")
Node6 = Node("node 6")
list1 = LinkedList()
list1.insert(Node1)
list1.insert(Node2)
list1.insert(Node3)
list1.insertHead(Node6)
list1.insert(Node4)

list1.printList()