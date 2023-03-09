from lib.single_class_program import *

def test_add_todo_to_empty_list():
    todo = Todo()
    todo.add_todo("Walk the dog")
    assert todo.view_todos() == "1. Walk the dog"

def test_add_tomorrow_todo_to_empty_list():
    tomorrow_todo = Todo()
    tomorrow_todo.add_todo("Do the dishes")
    assert tomorrow_todo.view_todos() == "1. Do the dishes"

def test_add_multiple_todos():
    todo = Todo()
    todo.add_todo("Walk the dog")
    todo.add_todo("Do the ironing")
    assert todo.view_todos() == "1. Walk the dog 2. Do the ironing"

def test_remove_only_todo_from_list():
    todo = Todo()
    todo.add_todo("Walk the dog")
    todo.remove_completed_todo("Walk the dog")
    assert todo.view_todos() == "No todos"

def test_remove_todo_when_multiple_in_list():
    todo = Todo()
    todo.add_todo("Walk the dog")
    todo.add_todo("Do the ironing")
    todo.remove_completed_todo("Walk the dog")
    assert todo.view_todos() == "1. Do the ironing"