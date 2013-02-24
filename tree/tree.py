### using binary search to create a balanced tree of sorted array

class Node:

      def __init__(self,info): #constructor of class

          self.info = info  #information for node
          self.left = None  #left leef
          self.right = None #right leef
          self.level = None #level none defined

      def __str__(self):

          return str(self.info) #return as string


class searchtree:

      def __init__(self): #constructor of class

          self.root = None


      def create(self,val,start,end):
		  if ( end < start):
			  return None
		  mid= ( start+end)/2
		  n = Node(val[mid])
		  n.left = self.create(val,start,mid-1)	  
		  n.right = self.create(val,mid+1,end)
		  print n
		  self.root = n
		  return n

      def inorder(self,node):
#           print "ff" 
           if node is not None:
              
              self.inorder(node.left)
              print node.info
              self.inorder(node.right)

		  
tree = searchtree()     
arr = [1,2,3,4,5,6,7,8]
tree.create(arr,0,len(arr)-1)
print 'Inorder Traversal'
tree.inorder(tree.root) 
