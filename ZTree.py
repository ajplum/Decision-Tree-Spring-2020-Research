from z3 import *
from sympy import simplify


Tree = Datatype('Tree')
Tree.declare('nil')
Tree.declare('node', ('label', IntSort()), ('left', Tree), ('up', Tree), ('right', Tree))
Tree = Tree.create()
trees = [Const('t' + str(i), Tree) for i in range(3)]


s = Solver()
#create a function to generate tree procedurally 
s.add(
  Tree.up(trees[0]) == Tree.nil,
  Tree.left(trees[0]) == trees[1], # left node from root
  Tree.right(trees[0]) == trees[2], # right node from root
  Tree.up(trees[1]) == trees[0], # root from left node
  Tree.up(trees[2]) == trees[0] #root from right node 
)

print(s.check()) # sat -> your constraints are satisfiable

TreeList = Datatype('TreeList')
Tree     = Datatype('Tree')
Tree.declare('leaf', ('val', IntSort()))
Tree.declare('node', ('left', TreeList), ('right', TreeList))
TreeList.declare('nil')
TreeList.declare('cons', ('car', Tree), ('cdr', TreeList))

Tree, TreeList = CreateDatatypes(Tree, TreeList)

t1  = Tree.leaf(10)
tl1 = TreeList.cons(t1, TreeList.nil)
t2  = Tree.node(tl1, TreeList.nil)
print(t2)
print(simplify(Tree.val(t1)))

t1, t2, t3 = Consts('t1 t2 t3', TreeList)

solve(Distinct(t1, t2, t3))
print(trees)
