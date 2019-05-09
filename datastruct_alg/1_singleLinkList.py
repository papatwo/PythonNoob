class Node(object):
	"""node"""
	def __init__(self,elem):
		self.elem = elem
		self.next = None



# node = Node(100)
class SingleLinkList(object):
	"""obj method"""
	def __init__(self, node = None):
		self._head = node # private property

	def is_empty(self):
		return self._head == None

	def length(self):
		cur = self._head
		count = 0
		while cur != None:
			count += 1
			cur = cur.next
		return count

	def travel(self):
		cur = self._head
		while cur != None:
			print(cur.elem)
			cur = cur.next
			print ""


	def add(self, item):
		"""add from top"""
		node = Node(item)
		# order is important
		node.next = self.__head
		self.__head = node

	def append(self, item):
		"""add from bottom"""
		node = Node(item)
		if self.is_empty():
			self._head = node
		else:
			while cur.next != None:
				cur = cur.next
			cur.next = node


	def insert(self, pos, item):
		"""add at pointed pos"""
		if pos <= 0:
			self.add(item)
		elif pos > self.length() - 1:
			self.append(item)
		else:
			node = Node(item)
			pre = self.__head
			count = 0
			while count < pos - 1:
				count += 1
				pre = pre.next
			node.next = pre.next
			pre.next = node

	def remove(self, item):
		pre = None
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				# justify if item is 1st node
				if cur == self.__head:
					self._head = cur.next
				else:
					pre.next = cur.next
				break
			else:
				pre = cur
				cur = cur.next
		return 

	def serach(self, item):
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				return True
			else:
				cur = cur.next
		return False




if __name__ == "__main__":
	ll = SingleLinkList()
	print ll.is_empty()
	print ll.length()

	ll.append(1)
	print ll.is_empty()
	print ll.length()
