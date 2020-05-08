from abstract_state_utils import State, StateBounds, StateMapper, TreeInformation
from typing import List
from z3 import * # or should I import bounds file into new Z3 file?

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

input = [3.14, 4.0, 5.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0,
       1.0,  1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0,1.0, 1.0,
1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0,
1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 1.0]


#Node number = index of value array
#So the node tells me the action
# action = value(node)


actions = []
#get all actions from tree policy
for i in range(len(value)):
    if value[i] != -1:
        actions.append(value[i])
        
print("\n")
#print("Actions from policy")
#print(actions)



action = actions[1] #currently running for a single leaf node & action



act = [Int('a%s' % i) for i in range(6)] #need to do range 6
A = act[action]

#print A #a0,a1,a2

##action a0 = forward
##action a1 = forward and left
##action a2 = forward and right

#0 forward right
#1 rotate right
#2 forward
#3 stop
#4 forward left
#5 rotate left

print("Action from Node 8:")
print(A)
print("\n")

pot_dang = [5,6,7,8,9,10,15,16,17,18,19,20,25,26,27,28,29,30]
occ_dang = []
occupied = []

input.pop(0)
input.pop(0)
input.pop(0)
#doing this so I can focus just on the cells indexes without the goal or angle, keeping the true indexes of the cells

for j in range(len(input)):
    if input[j] >= 0.5:
        occupied.append(j)
        

print("All occupied cells")
print(occupied)
print("\n")

# [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 41, 42, 43, 45, 46, 48, 50, 51, 53, 54, 55, 57, 58, 60, 61, 62, 63, 65, 67, 69, 70]



for j in range(len(pot_dang)):
    if input[pot_dang[j]] >= 0.5:
            occ_dang.append(pot_dang[j])
            
act_0 = [5,15,25,6,16,26]
act_2 = [7,17,27,8,18,28]
act_4 = [9,19,29,10,20,30]
occ_0 = []
occ_2 = []
occ_4 = []

# #check these elements of input, if they are occupied then store as c_ else store as Not(c_)

#build an array of those potentially dangerous as all true for each action... Done

danger_forward = [7,17,27,8,18,28]
danger_for_left = [9,19,29,10,20,30]
danger_for_right = [5,15,25,6,16,26]

crash_0 = [] # forward right crash
not_0 = []
crash_2 = [] # forward crash
not_2 = []
crash_4 = [] # forward left crash
not_4 = []

for i in danger_for_right:
    a = Bools('c%d' % i)
    crash_0.append(a[0])

for i in danger_forward:
    b = Bools('c%d' % i)
    crash_2.append(b[0])

for i in danger_for_left:
    c = Bools('c%d' % i)
    crash_4.append(c[0])



def filler(act,occ):
    
    for i in act:
        if input[i] >= 0.5:
            checker = Bools('c%d' % i)
            occ.append(checker[0])
        else:
            filled = Bools('c%d' % i)
            occ.append(Not(filled[0]))
            
    print(occ)
    
    return occ
    

def prove(f):
    s = Solver() # if I remove I get an interesting result
    s.add(Not(f))
    if str(s.check()) == 'unsat': #determine sat or unsat
        print("The robot will crash into an object")
    else:
        print("safe action")

    return str(s.check())
    
def crash_check(act,occ,crash):
    

    s = Solver()
    
    x = Bools('x')
        

    for i in range(len(crash)):
        s.push()
        crashing = And(occ[i],crash[i]) == Or(And(occ[i],crash[i]), crash[i])
        prove(crashing)
        
        s.pop()

# now to stop on first crash


        
#        if str(s.check()) == 'sat': #determine sat or unsat
#            print("The robot crashed into an object in " + str(crash[i]))
#        else:
#                print("safe action")

    return s.check()


# "Potentially dangerous occupied" means cells in immediate range of causing a crash for a specific action, given the described constraints, any cell outside of this range would be far enough that the robot would be able to recalibrate and make a "safer" decision

    
if str(A) == 'a0':
    print("Cells that will cause a crash if Action 0")
    print(crash_0)
    print("\n")
    print("Currently occupied potentially dangerous cells if action = 0")
    filler(act_0,occ_0) #action 0
    print("\n")
    crash_check(act_0,occ_0,crash_0)

elif str(A) == 'a2':
    print("Cells that will cause a crash if Action 2")
    print(crash_2)
    print("\n")
    print("Currently occupied potentially dangerous cells if action = 2")
    filler(act_2,occ_2) #action 2
    print("\n")
    crash_check(act_2,occ_2,crash_2)

elif str(A) == 'a4':
    print("Cells that will cause a crash if Action 4")
    print(crash_4)
    print("\n")
    print("Currently occupied potentially dangerous cells if action = 4")
    filler(act_4,occ_4) #action 4
    print("\n")
    crash_check(act_4,occ_4,crash_4)

else:
    print("safe action")




    
    



#[c5, c6, c7, c9, c10, c15, c16, c17, c19, c20, c25, c26, c27, c28, c29, c30]
#these are the dangerous cells that are occupied as Z3 expressions


#[c5, c15, c25, c6, c16, c26]
#[5,15,25,6,16,26] check these elements of input, if they are occupied then store as c_ else store as Not(filled)
#[c7, c17, c27, c8, c18, c28]
#[c9, c19, c29, c10, c20, c30]


#build an array of those potentially dangerous as all true for each action... Done

#have another array that is a combination of trues and falses but same length as previous array
#in a loop do NAND by index, if check returns unsat at any point, that's a crash
#make a filler variable that's true, fill in appropriate values for each crash scenario then

#Filled is bad, not filled is good, so make crash cells be filled (True)

#THink I want a NAND




        
#trying to figure out if theres any way to store Boolean Not variables in an array so that I can improve the logic

#Ideally I would like to take the array of c's and Not(c)'s then OR the appropriate pair together and check if there is a pair that fit's the crash theorem, meaning that it would have to have a true and a false input from the exact same variable (i.e. c7 and Not(c7)... don't want it to call a crash for c7 and Not(c5)

# I could have the occ_dang values as an array of Trues then another crash_scen array that consolidates those if's into an array of False boolean values. I could then create a loop that checks the true nature of each value in occ_dang vs the values in crash_scen. If the true natures match, it would do an OR of the true and the false variables therefore returning an unsat denoting a crash, else it would return sat and show no crash



