class Node:
	def __init__( self, data ):
		self.data = data
		self.next = None
		self.previous = None

class LinkedList:
	def __init__( self ):
		self.head = None
		self.tail = None

	def AddNode( self, data ):
		new_node = Node( data )
		if self.head == None:
			self.head = new_node
			new_node.previous=None
		if self.tail != None:
			self.tail.next = new_node
			new_node.previous=self.tail
		self.tail = new_node      
#		print new_node.data

	def reverse_list( self ):
		node = self.head
		temp = None
		while node is not None:
			node.previous = node.next
			node.next=temp
			temp = node
			node = node.previous
		self.head = temp	
		
	def behind( self ):
		node=self.tail
		while node is not self.head:
			print str(node.data)+'->',
			node=node.previous
		if node==self.head:
			print str(node.data)		

	def PrintList( self ):
		node = self.head
		while node != None:
			print str(node.data) + '->',
			node = node.next			

List = LinkedList()
#for i in range(12):
#	List.AddNode(i)
List.AddNode(21)
List.AddNode(23)
List.AddNode(20)
List.AddNode(40)
List.AddNode(10)
List.AddNode(5)

print "nodes"
List.PrintList( )	
print '\n'
print "Reverse order"
List.behind()
print '\n'
print 'reversing a doubly linked list'
List.reverse_list()
List.PrintList()
