class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def Push(self,data):
        New_node = Node(data)
        temp = self.head

        New_node.next = self.head

        if temp != None:
            while temp.next != temp:
                temp = temp.next
            temp.next = New_node

        else:
            New_node.next = New_node

        self.head = New_node

      
        


    


if __name__ == "__main__":
    Cllist = CircularLinkedList()
    Cllist.Push(8)
    Cllist.Push(9)
    














    
