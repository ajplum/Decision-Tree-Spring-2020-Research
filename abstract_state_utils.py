from typing import Tuple, List, Union, Dict, TypeVar
import numpy as np
from copy import deepcopy

# LICENSE INFORMATION:  ALL RIGHTS RESERVED BY AARON ROTH 2020


State = List[float]

BinaryStateBounds = List[Union[int, Tuple[float, float]]]
T = TypeVar('T')


class StateBounds(object):

    def __init__(self, state_bound_low: List[float], state_bound_high: List[float]):
        self.sbound_low: List[float] = state_bound_low
        self.sbound_high: List[float] = state_bound_high

    def __str__(self):
        return "low: %s\nhigh: %s" % (str(self.sbound_low), str(self.sbound_high))


class TreeInformation(object):
    def __init__(self,
                 root_state_bounds: StateBounds,
                 child_left: List[int],
                 child_right: List[int],
                 feature: List[int],
                 threshold: List[float],
                 value: List[int]
                 ):
        self.sbound_low: List[float] = root_state_bounds.sbound_low
        self.sbound_high: List[float] = root_state_bounds.sbound_high
        self.child_left = child_left
        self.child_right = child_right
        self.feature = feature
        self.threshold = threshold
        self.value = value

    def _validate(self):
        if len(self.sbound_low) != len(self.sbound_high):
            raise ValueError("High and Low Bounds Must be of Equal Length")
        if len(np.unique([len(self.child_right), len(self.child_left), len(self.feature),
                          len(self.threshold), len(self.value)])):
            raise ValueError("All tree information arrays must be same length.")


class StateMapper(object):

    def __init__(self, tree_information: TreeInformation):
        self.t = tree_information
        # noinspection PyTypeChecker
        self.states: List[StateBounds] = None

    def map_abstract_states(self) -> List[StateBounds]:
        if self.states is None:
            self.states: List[Union[StateBounds, None]] = [None] * len(self.t.value)
            self.states[0] = StateBounds(self.t.sbound_low, self.t.sbound_high)
            if self.t.child_left[0] and self.t.child_left[0] > -1:  # b/c convention of non-children being -1
                self._calc_abstract_state(self.t.child_left[0], is_left_child=True, parent=0)
            if self.t.child_right[0] and self.t.child_right[0] > -1:  # b/c convention of non-children being -1
                self._calc_abstract_state(self.t.child_right[0], is_left_child=False, parent=0)
        return self.states

    def _calc_abstract_state(self, node: int, is_left_child: bool, parent: int) -> None:
        parent_bounds_copy: StateBounds = deepcopy(self.states[parent])
        feature = self.t.feature[parent]
        thresh = self.t.threshold[parent]
        if is_left_child:
            parent_bounds_copy.sbound_high[feature] = thresh
        else:
            parent_bounds_copy.sbound_low[feature] = thresh
        self.states[node] = parent_bounds_copy
        if self.t.child_left[node] > -1:
            self._calc_abstract_state(self.t.child_left[node], is_left_child=True, parent=node)
        if self.t.child_right[node] > -1:
            self._calc_abstract_state(self.t.child_right[node], is_left_child=False, parent=node)


# Take a StateBounds, and transform *segment* portion of it by assuming
# everything should be code as either a 0, a 1, or both. Both represented by both_value
# which defaults to None
def statebounds_to_binary_na_format(abstract_state: StateBounds, segment: Tuple[int] = (3, 212),
                                    both_value=None) -> BinaryStateBounds:
    state: BinaryStateBounds = []
    for e in range(0, segment[0]):
        state.append((abstract_state.sbound_low[e], abstract_state.sbound_high[e]))  # add as tuple
    for e in range(segment[0], segment[1]+1):
        if abstract_state.sbound_low[e] <= 0 and abstract_state.sbound_high[e] >= 1:
            state.append(both_value)
        elif abstract_state.sbound_low[e] > 0 and abstract_state.sbound_high[e] >= 1:
            state.append(1)
        elif abstract_state.sbound_low[e] <= 0 and abstract_state.sbound_high[e] < 1:
            state.append(0)
        else:
            raise TypeError("Expected element %d to be 0 or 1 or both" % e)
    for e in range(segment[1]+1, len(abstract_state.sbound_high)):
        state.append((abstract_state.sbound_low[e], abstract_state.sbound_high[e]))  # add as tuple
    return state


def count_occurences_in_array(arr: List[T]) -> Dict[T, int]:
    unique, counts = np.unique(arr, return_counts=True)
    return dict(zip(unique, counts))
