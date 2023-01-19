class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Linkedlist:
	def __init__(self):
		self.head = None

	def Push(self,data):
		New_node = Node(data)
		New_node.next = self.head
		self.head = New_node

	def AddEnd(self,data):
		New_node = Node(data)
		temp = self.head

		while temp.next != None:
			temp = temp.next
		temp.next = New_node

	def InsertAfter(self,data,item):
		New_node = Node(data)
		prev = self.head
		if prev.data == item:
			New_node.next = prev.next
			prev.next = New_node

		while prev != None:
			prev = prev.next
			if prev.data == item:
				New_node.next = prev.next
				prev.next = New_node
				break

	def Count_using_loop(self):
		count = 0
		temp = self.head

		while temp != None:
			count += 1
			temp = temp.next

		print("\n" + str(count))

	def Count_using_recursion(self,temp):
		if temp == None:
			return 0

		else:
			return 1 + self.Count_using_recursion(temp.next)

	def Delete_Node(self,item):
		temp = self.head

		if temp.data == item:
			self.head = temp.next
			temp = None
			return 
		
		while temp.next != None:
			if temp.data == item:
				break
			prev = temp
			temp = temp.next

		prev.next = temp.next
		temp = None



	def Print(self):
		temp = self.head
		while temp != None:
			print(temp.data,end = " ")
			temp = temp.next



if __name__ == "__main__":

	LList = Linkedlist()
	LList.Push(3)
	LList.Push(2)
	LList.Push(1)
	LList.InsertAfter(4,3)
	LList.Delete_Node(3)
	LList.Print()
	LList.Count_using_loop()
	# print(LList.Count_using_recursion(LList.head))


	