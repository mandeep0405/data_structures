class Node:

	def __init__(self,info): #constructor of class
	
	  self.info = info  #information for node
	  self.left = None  #left leef
	  self.right = None #right leef
	  self.level = None #level none defined

      #def __str__(self):

          #return str(self.info) #return as string


class searchtree:

	def __init__(self): #constructor of class
	
	  self.root = None
			
	def create(self,val):  #create binary search tree nodes
	
	  if self.root == None:
	
		 self.root = Node(val)
	
	  else:
	
		 current = self.root
	
		 while 1:
	
			 if val < current.info:
	
			   if current.left:
				  current = current.left
			   else:
				  current.left = Node(val)
				  break;      
	
			 elif val > current.info:
			 
				if current.right:
				   current = current.right
				else:
				   current.right = Node(val)
				   break;      
	
			 else:
				break 

	def isbst( self ):
		++
		
			
		
		

tree = searchtree()     
arr = [8,3,1,6,4,7,10,14,13,33,9]
for i in arr:
    tree.create(i)
