from abstract_state_utils import State, StateBounds, StateMapper, TreeInformation
from typing import List
from z3 import * # or should I import bounds file into new Z3 file?

child_left = [1, 3, 5, 7, 9, 11, 13, -1, -1, -1, -1, -1, -1, -1, -1]
child_right = [2, 4, 6, 8, 10, 12, 14, -1, -1, -1, -1, -1, -1, -1, -1]
feature = [0, 2, 7, 10, 25, 39, 60] # , -1, -1, -1, -1, -1, -1, -1, -1]
threshold = [1.0, 0.5, 3, 0.5, 0.5, 0.5, 0.5, -1, -1, -1, -1, -1, -1, -1, -1]
value = [-1, -1, -1, -1, -1, -1, -1, 1, 2, 0, 2, 1, 2, 0, 1]

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

print("State Bounds For Node 0")
print(all_state_bounds[0])
print("State Bounds For Node 8")
print(all_state_bounds[8])

# to access the lower or upper bound of node 8, for example do some something like:
# all_state_bounds[8].sbound_low
# all_state_bounds[8].sbound_high






## EVERYTHING BELOW THIS IS AUSTIN'S CODE

input = [3.14, 4.0, 5.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0,
       1.0,  1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0,1.0, 1.0,
1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0,
1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0]



node = 8


for i in feature: #check in on this
    if input[i] >= all_state_bounds[node].sbound_low[i] and input[i] <= all_state_bounds[node].sbound_high[i]:
        action = value[node]
        
#Node number = index of value array
#So the node tells me the action
# action = value(node)



act = [Int('a%s' % i) for i in range(3)]
print(act)
A = act[action]
#print A #a0,a1,a2

##action a0 = forward
##action a1 = forward and left
##action a2 = forward and right

print(A)

pot_dang = [5,6,7,8,9,10,15,16,17,18,19,20,25,26,27,28,29,30]
occ_dang = []

for j in range(len(pot_dang)):
    if input[pot_dang[j]] >= 0.5:
            occ_dang.append(pot_dang[j])
                
print("Occupied Cells")
print(occ_dang)

C = []
for i in occ_dang:
    checker = Bools('c%d' % i)
    C.append(checker[0]) #these are the dangerous cells that are occupied

print(C)
s = Solver()
c = []

if str(A) == 'a0': #if robot is moving forward
    for i in range(len(C)):
        if str(C[i]) == 'c7' or str(C[i]) == 'c17' or str(C[i]) == 'c27' or str(C[i]) == 'c8' or str(C[i]) == 'c18' or str(C[i]) == 'c28': # if any of the danger cells for the forward scenario are occupied
            crash = False == Or(C[i],Not(C[i]))
            s.add(crash)
            c = C[i]
        else:
            safe = True == Or(C[i],C[i])
            s.add(safe)

    if str(s.check()) == 'unsat':
           print("The robot crashed into an object in cell " + c )
    else:
        print("safe action")



if str(A) == 'a1': #if robot is moving forward and left
    for i in range(len(C)):
        if str(C[i]) == 'c9' or str(C[i]) == 'c19' or str(C[i]) == 'c29' or str(C[i]) == 'c10' or str(C[i]) == 'c10' or str(C[i]) == 'c30': # if any of the danger cells for the forward  and left scenario are occupied
            crash = False == Or(C[i],Not(C[i]))
            s.add(crash)
            c = C[i]
        else:
            safe = True == Or(C[i],C[i])
            s.add(safe)

    if str(s.check()) == 'unsat':
           print("The robot crashed into an object in cell " + c )
    else:
        print("safe action")



if str(A) == 'a2':
    for i in range(len(C)): #if robot is moving forward and right
        if str(C[i]) == 'c5' or str(C[i]) == 'c15' or str(C[i]) == 'c25' or str(C[i]) == 'c6' or str(C[i]) == 'c16' or str(C[i]) == 'c26': # if any of the danger cells for the forward and right scenario are occupied
            crash = False == Or(C[i],Not(C[i]))
            s.add(crash)
            c.append(C[i])
        else:
            safe = True == Or(C[i],C[i])
            s.add(safe)
            
    if str(s.check()) == 'unsat':
           print("The robot crashed into an object in " + str(c[0]) )
    else:
        print("safe action")
        
        
        
#trying to figure out if theres any way to store Boolean Not variables in an array so that I can improve the logic

#Ideally I would like to take the array of c's and Not(c)'s then OR the appropriate pair together and check if there is a pair that fit's the crash theorem, meaning that it would have to have a true and a false input from the exact same variable (i.e. c7 and Not(c7)... don't want it to call a crash for c7 and Not(c5)

# I could have the occ_dang values as an array of Not's then another crash_scen array that consolidates those if's into an array of True boolean values. I could then create a loop that checks the true nature of each value in occ_dang vs the values in crash_scen. If the true natures match, it would do an OR of the true and the false variables therefore returning an unsat denoting a crash, else it would return sat and show no crash
