"""Contains fixed function to sum the values in a time"""

import pytest

# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.


# [TODO]: fix the function
def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    list_of_nums_str = time_str.split(":")

    # checks list contains hour, minute, and second
    if len(list_of_nums_str) != 3:
        raise ValueError("Must be a time")

    # converts the list[str] to list[int]
    list_of_nums = [int(number) for number in list_of_nums_str]
    return sum(list_of_nums)


def test_sum_current_time():
    """tests output of sum_current_time with valid input"""
    assert sum_current_time("12:02:03") == 17


def test_sum_current_time_type():
    """tests output type of sum_current_time with valid input"""
    assert isinstance(sum_current_time("12:02:03"), int)


def test_sum_current_time_empty():
    """tests invalid input to sum_current_time raises an error"""
    with pytest.raises(Exception):
        sum_current_time("")
