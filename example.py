from z3 import *
\
from sympy import simplify
\
\
\
#tree of states
\
state = [1.2, 2.1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0,0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0,0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0,0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0]
\
child_left =  [1,3,9,5,7]
\
child_right = [2,4,10,68]
\
tree_feature = [1,30,25,40,0]
\
tree_threshold = [0.1963, 0.5, 0.5, 0.5, 3]
\
tree_value = [None,None,None,None,4]\
\
\

\
Tree = Datatype('Tree')
\
Tree.declare('nil')
\
Tree.declare('node', ('label', IntSort()), ('left', Tree), ('up', Tree), ('right', Tree))
\
Tree = Tree.create()
\
trees = [Const('t' + str(i), Tree) for i in range(3)]
\

\

\
s = Solver()
\
#create a function to generate tree procedurally 
\
s.add(
\
  Tree.up(trees[0]) == state[0],
\
  Tree.left(trees[0]) == child_left[1], # left node from root
\
  Tree.right(trees[0]) == child_right[2], # right node from root
\
  Tree.up(child_left[1]) == trees[0], # root from left node
\
  Tree.up(hild_right[2]) == trees[0] #root from right node 
\
)
\

\
print(s.check()) # sat -> your constraints are satisfiable}


