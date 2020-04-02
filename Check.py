from z3 import *
from sympy import simplify

##Tree = Datatype('Node')
##Tree.declare('nil')
##Tree.declare('node', ('label', IntSort()), ('left', Tree), ('up', Tree), ('right', Tree))
##Tree = Tree.create()
##trees = [Const('t' + str(i), Tree) for i in range(3)] #figure out what trees is
##
##child_left =  [1,3,9,5,7]
##child_right = [2,4,10,68]
##tree_feature = [1,30,25,40,0]
##tree_threshold = [0.1963, 0.5, 0.5, 0.5, 3]
##tree_value = [None,None,None,None,4]
##
##
##s = Solver()
##
##s.add(
##  Tree.up(trees[0]) == Tree.nil, 
##  Tree.left(trees[0]) == child_left[0],
##  Tree.right(trees[0]) == child_right[0],
###need to make the following more dynamic 
##  Tree.left(Tree.left(trees[0])) == Tree(child_left[1]),
##  Tree.right(Tree.left(trees[0])) == Tree(child_right[1])
##)
##
##print(s.check())

# make satisfiable tree
# apply conditions, by setting out states
# run loop to determine how tree traverses
# print action at end
# if maneuverable conditions, make action. Else, crash 

#I think we can determine crashing this way
#Don't think we can determine freezing, only actions made based upon conditions


# We want an array with 3 elements.
# 1. Bad solution
X = Array('x', IntSort(), IntSort())
# Example using the array
print(X[0] + X[1] + X[2] >=0)

# 2. More efficient solution
X = IntVector('x', 3)
print(X[0] + X[1] + X[2] >= 0)
print(Sum(X) >= 0)
