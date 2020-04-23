from abstract_state_utils import State, StateBounds, StateMapper, TreeInformation
from typing import List

child_left = [1, 3, 5, 7, 9, 11, 13, -1, -1, -1, -1, -1, -1, -1, -1]
child_right = [2, 4, 6, 8, 10, 12, 14, -1, -1, -1, -1, -1, -1, -1, -1]
feature = [0, 2, 7, 10, 25, 39, 60, -1, -1, -1, -1, -1, -1, -1, -1]
threshold = [1.0, 0.5, 3, 0.5, 0.5, 0.5, 0.5, -1, -1, -1, -1, -1, -1, -1, -1]
value = [-1, -1, -1, -1, -1, -1, -1, 1, 3, 0, 7, 5, 2, 4, 3]

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

print("State Bounds For Node 0")
print(all_state_bounds[0])
print("State Bounds For Node 8")
print(all_state_bounds[8])

# to access the lower or upper bound of node 8, for example do some something like:
# all_state_bounds[8].sbound_low
# all_state_bounds[8].sbound_high
