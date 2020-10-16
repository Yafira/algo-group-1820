class Node:
	def __init__(self, data):
		self.val = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def traverse(self):
		if not self.head:
			return None
		n = self.head # temp variable to store the head node
		while n: # at each iteration, we print out the node value and set the current node to its next node.
			print(n.val) 
			n = n.next
	
	def insertLeft(self, data):
		newNode = Node(data)
		newNode.next = self.head
		self.head = newNode

	def insertRight(self, data):
		newNode = Node(data)
		if not self.head:
			self.head = newNode
			return
		n = self.head
		while n.next:
			n = n.next
		n.next = newNode
	
	def appendRecursively(self, val):
		def helper(node):
			if not node:
				newNode = Node(val)
				print('end of LL reached, creating a new node:', newNode.val)
				return newNode
			node.next = helper(node.next)
			print(node.val, 'is being returned (from bottom to top)')
			return node
		self.head = helper(self.head)

	def insertAfter(self, x, data):
		n = self.head
		while n:
			if n.val == x:
				break
			n = n.next
		if not n:
			print('x not in list')
		else:
			newNode = Node(data)
			newNode.next = n.next
			n.next = newNode

	def insertBefore(self, x, data):
		if not self.head:
			return None

		if self.head.val == x:
			newNode = Node(data)
			newNode.next = self.head
			self.head = newNode
			return

		n = self.head
		while n.next:
			if n.next.val == x:
				break
			n = n.next

		if not n.next:
			print('item x not in the list')
		else:
			newNode = Node(data)
			newNode.next = n.next
			n.next = newNode 

	def insertAt(self, idx, data):
		if idx == 0:
			newNode = Node(data)
			newNode.next = self.head
			self.head = newNode
			return
		
		i, n = 0, self.head
		while i < idx-1 and n:
			n = n.next
			i += 1
		if not n:
			print('idx out of range')
		else:
			newNode = Node(data)
			newNode.next = n.next
			n.next = newNode

	def count(self):
		if not self.head: # if the head node is None, we can return 0
			return 0
		
		i, n = 0, self.head ## let i be the counter variable; n be the head node
		while n: # while n is not None, we keep pointing it to its next node and increment i by 1
			n = n.next
			i += 1
		return i

	def searchItem(self, x):
		if not self.head:
			return None
		n = self.head
		found = False
		while n:
			if n.val == x:
				found = True
				break
			n = n.next
		return found

	def makeList(self):
		num = int(input("how many nodes? "))
		if not num:
			return
		for _ in range(num):
			val = int(input("input value for the next node: "))
			self.insertRight(val)

	def deleteFirstNode(self):
		if not self.head:
			return None
		self.head = self.head.next

	def deleteLastNode(self):
		if not self.head:
			return None
		n = self.head
		while n.next.next:
			n = n.next
		n.next = None

	def deleteNode(self, x):
		if not self.head: # if the list is empty, we reutnr nothing
			return None
		if self.head.val == x: # if the head node is the item we want to delete, then point the head node to its next node
			self.head = self.head.next
			return 
		# otherwise, let n be the head node and traverse it just like we did in searching an item
		n = self.head 
		while n.next:
			if n.next.val == x:
				break
			n = n.next
		if not n:
			print('item not in list')
		else: # once we find it, we point the next node of the current foudn node to the next next node.
			n.next = n.next.next

	def reverse(self):
		if not self.head:
			return None
		prev, curr = None, self.head # prev - previous element of my current node; curr - used to traverse the list
		while curr: # while the current node is not None
			next = curr.next # make a copy of the next node
			curr.next = prev # point the next node of mmy current node to the previous node
			prev = curr # update the previous node with the current node
			curr = next # set curr to the temporarily stored next item in order to traverse the list.
		self.head = prev

	def bubbleSortDataExchange(self):
		end = None
		while end != self.head:
			p = self.head
			while p.next != end:
				q = p.next
				if p.val > q.val:
					p.val, q.val = q.val, p.val
				p = p.next
			end = p

	def bubbleSortLinkChange(self):
		end = None
		while end != self.head:
			prev = p = self.head
			while p.next != end:
				q = p.next
				if p.val > q.val:
					p.next = q.next
					q.next = p
					if p != self.head:
						prev.next = q
					else:
						self.head = q
					p, q = q, p
				prev = p
				p = p.next
			end = p

	def merge(self, list2):
		newList = LinkedList()
		newList.head = self.mergeHelper(self.head, list2.head)
		return newList
	
	def mergeHelper(self, p, q):
		if p.val <= q.val:
			dummy = Node(p.val)
			p = p.next
		else:
			dummy = Node(q.val)
			q = q.next
		
		curr = dummy
		while p and q:
			if p.val <= q.val:
				curr.next = Node(p.val)
				p = p.next
			else:
				curr.next = Node(q.val)
				q = q.next
			curr = curr.next
		
		if not p:
			curr.next = q
		else:
			curr.next = p

		return dummy

	def removeNthFromEnd(self, head, n):
		dummy = Node('pocket')
		dummy.next = head
		slow = fast = dummy
		for _ in range(n):
			fast = fast.next
		while fast and fast.next:
			slow, fast = slow.next, fast.next
		#print(fast.val)
		slow.next = slow.next.next
		return dummy.next

	def removeNthFromEnd2(self, head, n):
		#count from backwards. 123456
		def index(node):
			if not node:
				return 0
			i = index(node.next) + 1
			if i > n:
				print('#'+str(i), 'node.next '+ str(node.next.val), 'is getting replaced by,' 'current node ' + str(node.val)) 
				node.next.val = node.val
			return i
		index(head)
		return head.next

M = LinkedList()
M.insertRight(4)
M.insertRight(5)
M.insertLeft(9)
M.appendRecursively(50)
			
