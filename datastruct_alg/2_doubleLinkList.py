class Node(object):
	def __init__(self, item):
		self.elem = item
		self.next = None
		self.prev = None


class DoubleLinkList(object):
	def __init__(self, node = None):
		self.__head = node

	def is_empty(self):
		return self.__head == None

	def length(self):
		count = 0
		cur = self.__head
		while cur != None:
			count += 1
			cur = cur.next
		return count

	def travel(self):
		cur = self.__head
		while cur != None:
			print cur.elem
			cur = cur.next

	def add(self, item):
		node = Node(item)
		self.__head.prev = node
		node.next = self.__head
		self.__head = node
 
 	def append(self, item):
 		node = Node(item)
 		if self.is_empty():
 			self.__head = node
 		else:
	 		cur = self.__head
	 		while cur.next != None:
	 			cur = cur.next
	 		cur.next = node
	 		node.prev = cur

	def insert(self, pos, item):
		if pos <=0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			count = 0
			cur = self.__head
			node = Node(item)
			while count < pos:
				count += 1
				cur =  cur.next
			node.next = cur
			node.prev = cur.prev
			cur.prev.next = node
			cur.prev = node

 	def search(self, item):
 		cur = self.__head
 		while cur != None:
 			if cur.elem != item:
 				cur = cur.next
 			else:
 				return True
 		return False

 	def remove(self, item):
 		cur = self.__head
 		while cur != None:
 			if cur.elem == item:
 				# if the item is the first node
 				if cur == self.__head:
 					self.__head = cur.next
 					if cur.next:
 						# if the link list only has one node
 						cur.next.prev = None
 				else:
					cur.prev.next = cur.next
					if cur.next:
						cur.next.prev = cur.prev
				break
			else:
				cur = cur.next
		return False

if __name__ == "__main__":
	ll = DoubleLinkList()
	print(ll.is_empty())
	print(ll.length())

	ll.append(1)
	print(ll.is_empty())
	print(ll.length())


	ll.append(2)
	ll.add(8)
	ll.append(3)
	ll.append(4)
	ll.append(5)
	ll.append(6)
	ll.insert(-1,9)
	ll.travel()
	ll.insert(3,100)
	ll.travel()
	ll.insert(10,200)
	ll.travel()
	ll.remove(100)
	ll.travel()
	ll.remove(9)
	ll.travel()
	ll.remove(200)
	ll.travel()


