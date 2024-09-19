import pytest
import task
from unittest.mock import patch

#------------------------------------------------------------------#
#------------------------------task_1------------------------------#
#------------------------------------------------------------------#

def test_task_1_case_1():
    test_list = [3, 4, 9]
    multiplier = 3
    expected = [9, -2, 15]
    assert task.task_1(test_list, multiplier) == expected

def test_task_1_case_2():
    test_list = [0, 0, 0]
    multiplier = 10
    expected = [-20, -20, -20]
    assert task.task_1(test_list, multiplier) == expected

def test_task_1_case_3():
    test_list = [1, 2, 3]
    multiplier = 1
    expected = [3, 0, 5]
    assert task.task_1(test_list, multiplier) == expected

#------------------------------------------------------------------#
#------------------------------task_2------------------------------#
#------------------------------------------------------------------#

def test_describe_num_13():
    assert task.task_2(13) == "The most brilliant number is 13!"

def test_describe_num_4():
    assert task.task_2(4) == "The most brilliant exciting virtuous number is 4!"

def test_describe_num_21():
    assert task.task_2(21) == "The most brilliant fantastic beautiful number is 21!"

def test_describe_num_60():
    assert task.task_2(60) == "The most brilliant exciting fantastic virtuous heart-warming tear-jerking inspiring number is 60!"

#------------------------------------------------------------------#
#------------------------------task_3------------------------------#
#------------------------------------------------------------------#

def test_addition():
    assert task.task_3("12 + 12") == 24

def test_subtraction():
    assert task.task_3("12 - 12") == 0

def test_multiplication():
    assert task.task_3("12 * 12") == 144

def test_division_by_non_zero():
    assert task.task_3("144 // 12") == 12

def test_division_by_zero():
    assert task.task_3("12 // 0") == -1
