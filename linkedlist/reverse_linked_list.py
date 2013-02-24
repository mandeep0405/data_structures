class Node:
	def __init__( self, data ):
		self.data = data
		self.next = None

class LinkedList:                    ## create a linked list
	def __init__( self ):
		self.head = None
		self.tail = None

	def AddNode( self, data ):       ## inserts new nodes
		new_node = Node( data )
		if self.head == None:
			self.head = new_node
		if self.tail != None:
			self.tail.next = new_node
		self.tail = new_node      

	def reverse( self ):           ### reversing a linked list
		node = self.head
		previous = None
		while node is not None:
			tmp = node.next
			node.next = previous
			previous = node
			node = tmp
		self.head = previous	

	def PrintList( self ):          ## print the linked list
		node = self.head
		while node != None:
			print str(node.data) + '->',
			node = node.next			

List = LinkedList()
print "initial"
for i in range(12):
	List.AddNode(i)
List.PrintList()
print "reversing"
List.reverse()
List.PrintList()
