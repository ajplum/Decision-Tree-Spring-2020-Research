from z3 import *
from sympy import simplify

s = Solver()

#tree of states
state = [1.2, 2.1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0,0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0,0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0,0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0]

class Node: 
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key 


child_left =  [1,3,9,5,7]
child_right = [2,4,10,68]
tree_feature = [1,30,25,40,0]
tree_threshold = [0.1963, 0.5, 0.5, 0.5, 3]
tree_value = [None,None,None,None,4]

print("Traverse the tree using the children_left and children_right attributes"
      "(check this code), here are some example values:")
print(child_left[0:4])
print("...")
#index 0 left child node 0
print(child_right[0:4])
print("...")
print("Feature and threshold to split on is in feature and threshold array")
print(tree_feature[0:4])
print("...")
print(tree_threshold[0:4])
print("...")
print(tree_value[0:4])
print("...")




#with Z3, values can not be updated after they are set. First order logic, not imperative
#Can we fill in values using a loop???
#Or do we have to build out tree manually?
#You can't predict a tree's structure, so it would have to be built manually?
#Can't make a loop for tree up, left, right, etc. 

#Would I do tree.up(tree.up())?
#Or would I do tree.up(trees[0]) after setting tree values?

# create function to check satisfiability of traversal using Z3
# implement function in tree traversal functions



#compare state to threshold, must start at some root. what is root?
# greater than threshold means go to right node, less than means go to left

def Traverse_root(root): 

    if state[1] < threshold[0]:
            #go to left child
        traverse_root(root.left)
        current = root.left
	    # print the data of node 
        print(root.val), 
    elif state[1] > threshold[0]:
	    #go to left child
        traverse_root(root.right)
        current = root.right
	    # print the data of node 
        print(root.val),


def Traverse_nodes(current):

    #for loop to stay in array, and do full traversal
    
    	if current < threshold[i]: 

            #go to left child
		Traverse_nodes(current.left)
		current = current.left
	    # print the data of node 
		print(current.val), 
        elif current > threshold[i]:
	    #go to left child
		Traverse_nodes(current.right)
		current = current.right
	    # print the data of node 
		print(current.val),

    



##for a in tree_feature[0:]:
##    for b in tree_threshold[0:]:
##        if child_left[a] > 0.5:
##            print("True")
##        elif child_left[a] < 0.5:
##            print("False")
##        else:
##            print("None")


# Driver code
Tree = Datatype('Node')
Tree.declare('node', ('label', IntSort()), ('left', Tree), ('up', Tree), ('right', Tree))
Tree = Tree.create()


s.add(
root = Tree(state[1]), 
root.left = Tree(child_left[0]), 
root.right = Tree(child_right[0]),
#need to make the following more dynamic 
root.left.left = Tree(child_left[1]),
root.left.right = Tree(child_right[1]),
)

print(s.check)

print("Preorder traversal of binary tree is")
printTraverse_root(root)

printTraverse_nodes(current)




#state is described by feature
#feature is the index of the state array, state[feature[i]]
# if ( state[feature] < threshold) then left child, else right child
#index corresponding to branch node will have something in left, right, feature and threshold arrays
#leaf node means no children, no entries. Make 5th array for value
# value contains prediction... prediction of what? Action? 
# leaf node will have nothing in left, right, feature and threshold arrays, but have "None" in value array
# final leaf nodes should have command functions for turn right, turn left, go forward, go back, stop, etc.
# if action made at final, satisfiable
#if no action/stop, unsatisfiable
