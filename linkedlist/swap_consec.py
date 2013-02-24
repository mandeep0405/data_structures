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
#		print new_node.data

	def PrintList( self ):
		node = self.head
		while node != None:
			print str(node.data) + '->',
			node = node.next	
	
	def swap( self ):
		node=self.head
		self.head=None
		prev=None
		while node and node.next is not None:
			tmp=node.next
			node.next=node.next.next
			tmp.next=node
			if prev is not None:
				prev.next=tmp
			prev=node
			node=node.next				
			if (self.head==None):
				self.head=tmp
									
List = LinkedList()		
for i in range(7):
	List.AddNode(i)

List.PrintList()
print '\n'
print 'after swap->'	
List.swap()
List.PrintList()
