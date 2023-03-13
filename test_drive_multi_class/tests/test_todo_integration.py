from lib.todo import Todo
from lib.todo_list import TodoList

"""
Given 1 Todo 
It is added to the list of Todos
"""

def test_add_one_todo_to_todo_list():
    todo = Todo("Test Drive a Multiple Class System")
    todo_list = TodoList()
    todo_list.add(todo)
    assert todo_list.todo_list == [todo]

"""
Given 2 Todos
They are added to the list of Todos
"""

def test_add_multi_todos_to_todo_list():
    todo_1 = Todo("Test Drive a Multiple Class System")
    todo_2 = Todo("Pair up in the afternoon")
    todo_list = TodoList()
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    assert todo_list.todo_list == [todo_1, todo_2]

"""
Given one todo
Return a list of incomplete todos
"""
def test_add_one_todo_return_list_of_incomplete_todos():
    todo_list = TodoList()
    todo_1 = Todo("Learn Test Driven Development")
    todo_list.add(todo_1)
    assert todo_list.incomplete() == [todo_1]

"""
Given multiple todos
Returns a list of incomplete todos
"""
def test_add_multi_todo_return_list_of_incomplete_todos():
    todo_list = TodoList()
    todo_1 = Todo("Learn Test Driven Development")
    todo_2 = Todo("Get better at coding")
    todo_3 = Todo("make Lunch")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.add(todo_3)
    assert todo_list.incomplete() == [todo_1, todo_2, todo_3]

"""
Given one todo that is marked as completed
Return a list of complete todos
"""
def test_add_one_todo_return_list_of_complete_todos():
    todo_list = TodoList()
    todo_1 = Todo("Learn Test Driven Development")
    todo_list.add(todo_1)
    todo_1.mark_complete()
    assert todo_list.complete() == [todo_1]

"""
Given 1 todo
Mark it as complete using give_up() method
"""
def test_one_todo_mark_complete_using_give_up_method():
    todo_list = TodoList()
    todo_1 = Todo("Learn Test Driven Development")
    todo_list.add(todo_1)
    todo_list.give_up()
    assert todo_1.complete == True

"""
Given multi todos
Mark them as complete using give_up() method
"""
def test_multi_todo_mark_complete_using_give_up_method():
    todo_list = TodoList()
    todo_1 = Todo("Learn Test Driven Development")
    todo_list.add(todo_1)
    todo_2 = Todo("Learn coding")
    todo_list.add(todo_2)
    todo_3 = Todo("Wash the dishes")
    todo_list.add(todo_3)
    todo_list.give_up()
    assert todo_1.complete == True
    assert todo_2.complete == True
    assert todo_3.complete == True
