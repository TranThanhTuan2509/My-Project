class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class CircularLinkedList:
	def __init__(self):
		self.head = None
		self.last = None

	def Push(self,data):
		New_node = Node(data)
		temp = self.head

		New_node.next = self.head
 
		if temp != None:
			while temp.next != self.head:
				temp = temp.next

			temp.next = New_node
		else:
			New_node.next = New_node

		self.head = New_node

	def EmptyList(self,data):
		New_node = Node(data)
		self.last = New_node
		self.last.next = self.last
		
	def AddBegin(self,data):

		if self.last == None:
			return self.EmptyList(data)

		else:
			New_node = Node(data)
			New_node.next = self.last.next
			self.last.next = New_node
	
	def AddEnd(self,data):

		if self.last == None:
			return self.EmptyList(data)

		else:
			New_node = Node(data)
			New_node.next = self.last.next
			self.last.next = New_node
			self.last = New_node

	def AddAfter(self,data,item):
		if self.last == None:
			return self.EmptyList(data)

		else:
			New_node = Node(data)
			prev = self.last.next
			while prev != None:
				if prev == item:
					New_node.next = prev.next
					prev.next = New_node

					if prev == self.last:
						self.last = New_node
						return self.last

					else:
						return self.last

				prev = prev.next

				if prev == self.last.next:
					print(f"{item} not exist")
					break

	def print(self):
		pass
			

	# This function sorted node in linnkedlist
	def EmptyNode(self,data):
		New_node = Node(data)
		New_node.next = New_node
		self.head = New_node

	def SortedInsert(self,data):

		current = self.head
		New_node = Node(data)

		if current == None:
			return self.EmptyNode(data)

		if current.data >= New_node.data:
			while current.next != self.head:
				current = current.next
			New_node.next = self.head
			current.next = New_node
			self.head = New_node

		if (current.data < New_node.data):
			while (current.next != self.head) and (current.next.data < New_node.data):
				current = current.next

			New_node.next = current.next
			current.next = New_node

	
	def DeleteNode(self,item):
		temp_1 = self.head
		temp_2 = self.last

		if temp_1 == None:
			print("Empty list")

		if (temp_1.data == item and temp_1.next == self.head):
			temp_1 = None
			self.head = self.last

		if temp_1 == item:
			while temp_2.next != self.head:
				temp_2 = self.last.next

			temp_2.next = self.head.next
			self.head = self.last.next

			





		




			


	




		
			

			
	




 
# Driver Code
if __name__ == '__main__':
 
	llist = CircularLinkedList()
 
	# last = llist.EmptyList(1)
	# last = llist.AddBegin(0)
	# last = llist.addBegin(-1)
	# last = llist.addEnd(2)
	# last = llist.addEnd(3)
	# last = llist.addAfter(10,8)
 
	# llist.traverse()
	llist.DeleteNode(2)



	

   
		


