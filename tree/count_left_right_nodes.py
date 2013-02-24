class Node:

	def __init__(self,info): #constructor of class
	
	  self.info = info  #information for node
	  self.left = None  #left leef
	  self.right = None #right leef
	  self.level = None #level none defined
	  self.lc = None
	  self.rc =  None

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
	
	def is_bal( self,node ):
		if node==None:
			return 0
		l=self.is_bal(node.left)
		r=self.is_bal(node.right)	
		if (abs(l-r) > 1 ):
			return False
		else:
			return max(self.is_bal(node.left),self.is_bal(node.right)+1)	
	
	
	def inorder(self,node):
		
	   if node is not None:
		  
		  self.inorder(node.left)
		  print str(node.info) +'\t'+str(node.lc)+'\t'+str(node.rc)
		  print '\n'
		  self.inorder(node.right)	
		
	def count( self,node ):

		if node.left is not None:
			l=1+self.count(node.left)
			node.lc=l
			#return l
		else:
			l=0
			node.lc=l
			#return l

		if node.right is not None:
			r=1+self.count(node.right)
			node.rc=r
			#return r
		else:
			node.rc=0
			r=0
			#return r			
		return l+r	

tree = searchtree()     
arr = [8,3,1,6,4,7,10,14,13,33,9]
#arr = [5,4,6]
for i in arr:
    tree.create(i)
tree.count(tree.root)	
tree.inorder(tree.root)
