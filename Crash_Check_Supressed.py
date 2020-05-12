#This version of the script supresses the printed output to only know the node number, action (as Z3 variable), 
#and crash determination for the bounds of each node


from abstract_state_utils import State, StateBounds, StateMapper, TreeInformation
from typing import List
from z3 import *

child_left = [1, 3, 5, 7, 9, 11, 13, -1, -1, -1, -1, -1, -1, -1, -1]
child_right = [2, 4, 6, 8, 10, 12, 14, -1, -1, -1, -1, -1, -1, -1, -1]
feature = [0, 2, 7, 10, 25, 39, 60, -1, -1, -1, -1, -1, -1, -1, -1]
threshold = [1.0, 0.5, 3, 0.5, 0.5, 0.5, 0.5, -1, -1, -1, -1, -1, -1, -1, -1]
value = [-1, -1, -1, -1, -1, -1, -1, 0, 2, 3, 1, 5, 4, 0, 2]

upper_bound: State = [3.14, 4.0, 5.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                      1.0,  1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,1.0, 1.0,
               1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
               1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

lower_bound: State = [-3.14, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
               0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

root_bounds: StateBounds = StateBounds(state_bound_low=lower_bound, state_bound_high=upper_bound)

tree_info: TreeInformation = TreeInformation(root_state_bounds=root_bounds, child_left=child_left,
                                             child_right=child_right, feature=feature, threshold=threshold, value=value)
sm: StateMapper = StateMapper(tree_info)

# This is a list of statebounds.  The index of the list corresponds to node number, and the value of this array is the
#       StateBounds for that node
all_state_bounds: List[StateBounds] = sm.map_abstract_states()

# node = input variable

#print("State Bounds For Node 0")
#print(all_state_bounds[0])
#print("State Bounds For Node 8")
#print(all_state_bounds[8])

# to access the lower or upper bound of node 8, for example do some something like:
# all_state_bounds[8].sbound_low
# all_state_bounds[8].sbound_high




## EVERYTHING BELOW THIS IS AUSTIN'S CODE

#Take lower bound and upper bound and run this check on all states within upper and lower bounds. A is action, leaf is node number
def test(upper,lower, A, leaf):

    all_occupied_1 = []
    all_occupied_2 = []


    for j in range(3,len(upper)):
        if upper[j] >= 0.5:
            all_occupied_1.append(j)
            
    for j in range(3,len(lower)):
        if lower[j] >= 0.5:
            all_occupied_2.append(j)

#    print("All occupied cells from Upper")
#    print(all_occupied_1)
#    print("\n")
#
#    print("All occupied cells from Lower")
#    print(all_occupied_2)
#    print("\n")


    #build array of the potentially dangerous cells as all true for each action
    danger_forward = [7,17,27,8,18,28]
    danger_for_left = [9,19,29,10,20,30]
    danger_for_right = [5,15,25,6,16,26]


    #check these elements of input, if they are occupied then store as c_ else store as Not(c_)
    occ_dang_for_right_up = []
    occ_dang_for_up = []
    occ_dang_for_left_up = []
    occ_dang_for_right_low = []
    occ_dang_for_low = []
    occ_dang_for_left_low = []


    crash_0 = [] # forward right crash
    crash_2 = [] # forward crash
    crash_4 = [] # forward left crash

    for i in danger_for_right:
        a = Bools('c%d' % i)
        crash_0.append(a[0])

    for i in danger_forward:
        b = Bools('c%d' % i)
        crash_2.append(b[0])

    for i in danger_for_left:
        c = Bools('c%d' % i)
        crash_4.append(c[0])
        
    #check these elements of input, if they are occupied then store as c_ else store as Not(c_)
    def filler(danger,occ_upper,occ_lower,upper, lower):
        
        for i in danger:
            if upper[i] >= 0.5:
                filled = Bools('c%d' % i)
                occ_upper.append(filled[0])
            else:
                empty = Bools('c%d' % i)
                occ_upper.append(Not(empty[0]))
                
#        print("Upper:")
#        print(occ_upper)
        
        for i in danger:
            if lower[i] >= 0.5:
                filled = Bools('c%d' % i)
                occ_lower.append(filled[0])
            else:
                empty = Bools('c%d' % i)
                occ_lower.append(Not(empty[0]))
        
#        print("Lower:")
#        print(occ_lower)
        
        return occ_upper,occ_lower
        

    def prove(f):
        s = Solver() # if I remove I get an interesting result
        s.add(Not(f))
        if str(s.check()) == 'unsat': #determine sat or unsat
            return "crash"
        else:
            return "safe action"

    
    # If both crash, then definitely crash
    # If  only one crashes, may crash in a subspace of the node space
    # If both don't crash, then no crash
    def crash_check(occ_upper,occ_lower,crash):
    
        s = Solver()
        
        def bounds_check(occ):
            for i in range(len(crash)):
                s.push()
                crashing = And(occ[i],crash[i]) == Or(And(occ[i],crash[i]), crash[i])
                check = prove(crashing)
                if str(check) == 'crash':
                    return print("The robot will crash into an object in cell " + str(occ[i]))
                s.pop()
           
            return print("safe action")
        
        print("Upper Bound check...")
        bounds_check(occ_upper)
        print("\n")
        print("Lower Bound check...")
        bounds_check(occ_lower)

        return s.check()


    # "Potentially dangerous occupied" means cells in immediate range of causing a crash for a specific action, given the described constraints, any cell outside of this range would be far enough that the robot would be able to recalibrate and make a "safer" decision

    
    if str(A) == 'a0':
        #print("Cells that will cause a crash if Action 0")
        #print(crash_0)
        #print("\n")
       # print("Currently occupied potentially dangerous cells if action = 0 for node " + str(leaf))
        filler(danger_for_right,occ_dang_for_right_up,occ_dang_for_right_low,upper,lower) #action 0
        #print("\n")
        crash_check(occ_dang_for_right_up,occ_dang_for_right_low, crash_0)


    elif str(A) == 'a2':
       # print("Cells that will cause a crash if Action 2")
        #print(crash_2)
        #print("\n")
        #print("Currently occupied potentially dangerous cells if action = 2 for node " + str(leaf))
        filler(danger_forward,occ_dang_for_up,occ_dang_for_low, upper, lower) #action 2
        #print("\n")
        crash_check(occ_dang_for_up, occ_dang_for_low, crash_2)

        

    elif str(A) == 'a4':
       # print("Cells that will cause a crash if Action 4")
        #print(crash_4)
        #print("\n")
        #print("Currently occupied potentially dangerous cells if action = 4 for node " + str(leaf))
        filler(danger_for_right,occ_dang_for_left_up, occ_dang_for_left_low, upper, lower) #action 4
        #print("\n")
        crash_check(occ_dang_for_left_up,occ_dang_for_left_low, crash_4)

    else:
        print("safe action")


    return



act = [Int('a%s' % i) for i in range(6)]

#print A #a0, a1, a2, a3, a4, a5, a6

##action a0 = forward and right
##action a2 = forward
##action a2 = forward and left

#0 forward right
#1 rotate right
#2 forward
#3 stop
#4 forward left
#5 rotate left

nodes = []

for i in range(len(value)):
    if value[i] != -1:
        nodes.append(i) #get inidices of nodes to be used later in loop to check for crash at each node

# print(nodes)

# Determine which leaf nodes have bounds that will or will not result in a crash
for node in nodes:
    print("Checking Node " + str(node) + "...\n")
    print("Action from Node " + str(node) + ":")
    print(act[value[node]])
    print("\n")
#        A.append(act[value[leaf]]) #don't do this until I am running final function
#    print("Upper Bound of Node " + str(node) + "...\n")
#    print(all_state_bounds[node].sbound_high)
#    print("\n")
#    print("Lower Bound of Node " + str(node) + "...\n")
#    print(all_state_bounds[node].sbound_low)
#    print("\n")
    test(all_state_bounds[node].sbound_high, all_state_bounds[node].sbound_low, act[value[node]], node)
    print("\n \n \n \n \n \n")
