print("linked list")

class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertAtBegin(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        else:
            node.next=self.head
            self.head=node
    
    def insertAtEnd(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        #assign head to new variable
        current_node=self.head
        while(current_node.next):
            current_node=current_node.next
        current_node.next=node
  
    def insertAtIndex(self,data,index):
        node=Node(data)
        current_node=self.head
        position=0
        if position==index:
            self.insertAtBegin(data)
        else:
            while(current_node!=None and position+1!=index):
                position=position+1
                current_node=current_node.next
            if current_node!=None:
                node.next=current_node.next
                current_node.next=node
            else:
                print("index out of range")
    
    def updateNodeAtIndex(self,data,index):
        current_node=self.head
        position=0
        if position==index:
            current_node.data=data
        else:
            while(current_node!=None and position+1!=index):
                position=position+1
                current_node=current_node.next
            if current_node!=None:
                current_node.data=data
            else:
                print("index out of range")
    
    def removeFirstNode(self):
        if self.head==None:
            return
        self.head=self.head.next
    
    def removeLastNode(self):
        if self.head==None:
            return
        current_node=self.head
        while(current_node.next.next):
            current_node=current_node.next
        current_node.next=None
        
    def removeNodeAtIndex(self,index):
        current_node=self.head
        position=0
        if position==index:
            self.removeFirstNode()
        else:
            while(current_node!=None and position+1!=index):
                position=position+1
                current_node=current_node.next
            if current_node!=None:
                current_node.next=current_node.next.next
            else:
                print("index out of range")
    
    def removeNode(self,data):
        current_node=self.head
        if current_node!=None and current_node.data==data:
            self.head=current_node.next
            return
        else:
            while(current_node!=None and current_node.next.data==data):
                current_node=current_node.next
            if current_node==None:
                return
            else:
                current_node.next=current_node.next.next
      
    def sizeOfLinkedList(self):
        size=0
        if self.head==None:
            return 0
        else:
            current_node=self.head
            while current_node:
                size=size+1
                current_node=current_node.next
            return size
    
    def printLinkedList(self):
        if self.head==None:
            print("empty linked list")
        else:
            current_node=self.head
            while current_node:
                print(current_node.data)
                current_node=current_node.next


sll=LinkedList()
sll.insertAtEnd('a')
sll.insertAtEnd('b')
sll.insertAtBegin('c')
sll.insertAtEnd('d')
sll.insertAtIndex('g',2)

print("Node data")
sll.printLinkedList()

# remove a nodes from the linked list
print("\nRemove First Node")
sll.removeFirstNode()
sll.printLinkedList()
print("Remove Last Node")
sll.removeLastNode()
sll.printLinkedList()
print("Remove Node at Index 1")
sll.removeNodeAtIndex(1)
sll.printLinkedList()

print("\nUpdate node Value")
sll.updateNodeAtIndex('z', 0)
sll.printLinkedList()
 
print("\nSize of linked list :", end=" ")
print(sll.sizeOfLinkedList())