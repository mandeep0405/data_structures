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
		
		prev = None
		head = self.head
		#print val
		while ( head != None and head.data == val):
			#print head.data
			#tmp = head
			head = head.next
		
		self.head = head
		if (head == None):
			return
#		print head.data
		node = head		
		while ( node.next != None ):
			#print node.data
			if ( node.next.data==val ):
				
				#print "enter if"
				new = node.next
				node.next = new.next
			else:	
				#prev = node
				node = node.next

	def PrintList( self ):
		node = self.head
		while node != None:
			print str(node.data) + '->',
			node = node.next			

List = LinkedList()
#for i in range(12):
#	List.AddNode(i)
List.AddNode(2)
List.AddNode(2)
List.AddNode(2)
List.AddNode(4)
List.AddNode(2)
List.AddNode(2)

List.AddNode(5)
List.AddNode(5)
List.AddNode(5)
List.AddNode(2)

print "nodes"
List.PrintList( )	
List.RemoveNode(2)
print '\n'
print "remove"
List.PrintList( )			
