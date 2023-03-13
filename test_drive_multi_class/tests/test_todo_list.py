from lib.todo_list import TodoList


"""
Initially
Todo list is empty
"""
def test_todo_list_initially_empty():
    todo_list = TodoList()
    assert todo_list.todo_list == []

"""
Initially
Return an empty list of incomplete todos
"""
def test_return_list_of_empty_incomplete_todos():
    todo_list = TodoList()
    assert todo_list.incomplete() == []

"""
Initially
Return an empty list of complete todos
"""
def test_return_list_of_empty_complete_todos():
    todo_list = TodoList()
    assert todo_list.complete() == []