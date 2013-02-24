class Node:
	def __init__( self, data ):
		self.data = data
		self.next = None

class LinkedList:
	def __init__( self ):
		self.head = None
		self.tail = None

	def AddNode( self, data ):
		new_node = Node( data )
		if self.head == None:
			self.head = new_node
		if self.tail != None:
			self.tail.next = new_node
		self.tail = new_node      
	
	def intersection_point( self,l1,l2 ):
		len1=0
		len2=0
		node=l1.head
		while ( node is not None):
			len1+=1
			node=node.next
		node=l2.head
		while ( node is not None):
			len2+=1
			node=node.next
		d=abs(len1-len2)
		node1=l1.head
		i=0
		node2=l2.head
		
		while i<d:
			node1=node1.next
			i+=1
		
		print node1.data		
		while node1 is not None:
			if node1.data==node2.data:
				print "merging point"+str(node1.data)
				break	
			else:
				node1=node1.next
				node2=node2.next

	def traverse( self):
		node=self.head
		while ( node is not None):
			print str(node.data)+'->',
			node=node.next

l1=LinkedList()
l2=LinkedList()
l=LinkedList()
for i in range(10):
	l1.AddNode(i)
l2.AddNode(12)
l2.AddNode(7)
l2.AddNode(8)
l2.AddNode(9)
l1.traverse()	
print '\n'
l2.traverse()
print '\n'
print "length of L1"
l.intersection_point(l1,l2)
