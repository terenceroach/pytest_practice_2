from lib.tasklist import *

"""
Initially
TaskList todo_list is an empty list
"""
def test_todo_list_initialise_empty_list():
    tasks = TaskList()
    assert tasks.todo_list == []