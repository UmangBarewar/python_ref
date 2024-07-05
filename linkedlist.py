class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next = next
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        last_node.next=self.head
        
