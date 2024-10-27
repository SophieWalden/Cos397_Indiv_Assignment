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
    Runs bubble sort on inputted list

    Params:
        int_list <List>: input list

    Returns:
        <List>: Sorted version of input list
    """

    for j in range(len(int_list)):
        for i in range(0, j):

            # Swap value if it is higher then the value after it
            if int_list[i] > int_list[i + 1]:
                int_list[i], int_list[i + 1] = int_list[i + 1], int_list[i]
    return int_list


def quick(int_list):
    """
    qsort docstring
    """
    print("quick sort")


def insertion(int_list):
    """
    insertion docstring
    """
    print("insertion sort")
