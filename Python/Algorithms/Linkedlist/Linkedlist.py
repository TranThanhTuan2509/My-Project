class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


class Linkedlist:
	def __init__(self):
		self.head = None

	# insert a element in the first node
	def Push(self,data):
		# initialize a new node
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def Insert_After(self,Prev,data):
		if Prev.data == None:
			print(f"no node have name {Prev}")
			return None

		# initialize a new node
		new_node = Node(data)
		new_node.next = Prev.next
		Prev.next = new_node


	def Append(self,data):
		temp = self.head
		new_node = Node(data)
		while temp.next != None:
			temp = temp.next
		temp.next = new_node

	def Delete(self,data):
		temp = self.head

		if temp != None:
			if temp.data == data:
				self.head = temp.next
				temp = None
				return temp

		while temp != None:
			if temp.data == data:
				break
			prev = temp
			temp = temp.next

		if temp == None:
			return temp

		prev.next= temp.next

		temp = None
	# count_using using loop
	def count_using_loop(self):
		c = 0
		temp = self.head

		while temp != None:
			c += 1
			temp = temp.next

		print(f"Have {c} Node")

		
	def count_using_recursion(self,temp):
		if temp == None:
			return 0

		else:
			return 1 + self.count_using_recursion(temp.next)

	def search_using_loop(self,data):
		temp = self.head

		while temp != None:
			if temp.data == data:
				return True
			temp = temp.next

		return False

	# search using recursion
	def search_using_recursion(self,temp,data):
		# if node head has null value return False
		if temp == None:
			return False

		# check value
		if temp.data == data:
			return True

		return self.search_using_recursion(temp.next,data)
		

			
		

		

		
		
			


	
	
	# print element
	def print(self):
		temp = self.head
		while temp != None:
			print(temp.data)
			temp = temp.next

if __name__ == "__main__":
	llist = Linkedlist()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)
	llist.head.next = second
	second.next = third
	# llist.Push(0)
	# llist.Insert_After(llist.head,9)
	llist.Append(99)
	# llist.Delete(3)
	# print(f"-->{llist.count_using_recursion(llist.head)}<--")
	# if llist.search_using_loop(10):
	# 	print(f"Yes")

	# else:
	# 	print("No")

	if llist.search_using_recursion(llist.head,5):
		print(f"Yes")

	else:
		print("No")



	# llist.print()
	