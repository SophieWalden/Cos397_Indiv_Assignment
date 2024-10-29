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
import pytest
import numpy as np

import int_sort  # noqa: E402


def is_sorted(int_list):
    """
    Checks whether a given list is sorted

    Params:
        int_list <List>: input list

    Returns:
        <Boolean>: True/False on whether int_list is sorted

    """
    return int_list == sorted(int_list)


@pytest.fixture
def int_lists():
    # fixture which creates testing data for all tests
    return [[3, 2, 1], [1, 1, 1], np.random.randint(low=-10, high=200, size=5)]


def test_bubble(int_lists):
    bubble_List = [
        int_sort.bubble(int_lists[0]),
        int_sort.bubble(int_lists[1]),
        int_sort.bubble(int_lists[2]),
    ]

    for list in bubble_List:
        if is_sorted(list) == 0:
            assert False
    assert True


def test_quick(int_lists):
    quick_List = [
        int_sort.quick(int_lists[0]),
        int_sort.quick(int_lists[1]),
        int_sort.quick(int_lists[2]),
    ]

    for list in quick_List:
        if is_sorted(list) == 0:
            assert False
    assert True


def test_insertion(int_lists):
    insert_List = [
        int_sort.insertion(int_lists[0]),
        int_sort.insertion(int_lists[1]),
        int_sort.insertion(int_lists[2]),
    ]

    for list in insert_List:
        if is_sorted(list) == 0:
            assert False
    assert True
