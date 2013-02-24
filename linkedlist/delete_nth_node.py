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
		
	def RemoveNode( self, val ):
		pass
			

	def PrintList( self ):
		node = self.head
		while node != None:
			print str(node.data) + '->',
			node = node.next			

List = LinkedList()
for i in range(7):
	List.AddNode(i)
List.PrintList()	
