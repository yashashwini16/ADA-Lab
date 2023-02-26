class Node:
 def __init__(self,data):
    self.data=data
    self.l=None
    self.r=None
class BST:
 def __init__(self):
  self.root=None
 def insert(self,data):
  ctr=0
  node=Node(data)
  if self.root==None:
   self.root=node
  else:
   temp=self.root
  while True:
   if data<temp.data and temp.l is None:
     temp.l=node
   break
   if data>temp.data and temp.r is None:
    temp.r=node
   break
   if data<temp.data and temp.l!=None:
    temp=temp.l
   if data>temp.data and temp.r!=None:
    temp=temp.r
  print("Node inserted")
  ctr+=1
 def searching(self,root,n):
   if n==root.data:
    print("Element found",root.data)
    return
   elif n>root.data:
    if self.root.r is not None:
      self.searching(root.r,n)
   else:
      return "No match found"
    
 def postorder(self,root):
  if root:
   self.postorder(root.l)
   self.postorder(root.r)
   print(root.data)
 def preorder(self,root):
  if root:
   print(root.data)
   self.preorder(root.l)
   self.preorder(root.r)
 def inorder(self,root):
  if root:
   self.inorder(root.l)