class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def Push(self,data):
        New_node = Node(data)
        New_node.next = self.head
        New_node.prev = None
        
        if self.head != None:
            self.head.prev = New_node


        self.head = New_node

    def InsertAfter(self,data,item):
        New_node = Node(data)
        temp = self.head

        if temp == None:
            self.head = New_node

        while temp.next != None:
            if temp.data == item:
                New_node.next = temp.next
                temp.next = New_node
                New_node.prev = temp
                if New_node.next != None:
                    New_node.next.prev = New_node
                break
            temp = temp.next

                


        print(self.head.data)
        print(New_node.prev.data)
        print(New_node.data)



if __name__ == "__main__":
    DLList = DoubleLinkedList()
    DLList.Push(4)
    DLList.Push(2)
    DLList.Push(1)
    DLList.InsertAfter(3,2)
    DLList.InsertAfter(5,4)