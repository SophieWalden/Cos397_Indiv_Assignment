# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

"""
This module sorts lists of integers...
"""


def bubble(int_list: list) -> list:
    """
    Runs bubble sort on inputted list, by doing the following
    1: 

    Params:
        int_list <List>: input list

    Returns:
        <List>: Sorted version of input list
    """

    for j in range(len(int_list)):
        for i in range(0, j):

            # Swap value if it is higher then adjacent value
            if int_list[i] > int_list[i + 1]:
                int_list[i], int_list[i + 1] = int_list[i + 1], int_list[i]
    return int_list


def quick(int_list):
    """
    Runs quicksort in inputted list, by doing the following:
    1: Chooses a "pivot" to make comparisons against
    2: Sorts the list into two lists, either less or greater then the pivot
    3: Calls quicksort on those smaller lists recursively
    4: Bubbles back up smaller sorted list to construct the final bigger sorted list

    Params:
        int_list <List>: input list

    Returns:
        <List>: Sorted version of input list
    """

    # Base Case
    if len(int_list) <= 1:
        return int_list

    # Pivot chosen to be element in the middle of the list
    pivot = len(int_list) // 2

    # Sorting values into lower or higher then pivot
    less, greater = [], []
    for i, item in enumerate(int_list):
        if i == pivot:
            continue

        if item < int_list[pivot]:
            less.append(item)
        else:
            greater.append(item)

    # Recursively calling quicksort on the smaller lists
    less, greater = quick(less), quick(greater)

    # Reconstructing the list from sorted sublists
    return less + [int_list[pivot]] + greater


def insertion(int_list):
    """
    insertion docstring
    """
    print("insertion sort")
