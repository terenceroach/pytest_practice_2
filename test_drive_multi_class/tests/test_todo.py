from lib.todo import Todo

"""
Given 1 todo
Task is added as per string value passed and complete property is False
"""
def test_one_todo_added_task_and_complete_properties_set_false():
    todo = Todo("Do the washing")
    assert todo.task == "Do the washing"
    assert todo.complete == False

"""
Given 1 task is added
Task is marked as complete and complete property is updated to True
"""
def test_one_todo_added_and_updated_to_complete_true():
    todo = Todo("Learn to code")
    todo.mark_complete()
    assert todo.complete == True

    """
Given multiple todos
Tasks are added as per string value passed and complete property is False
"""
def test_multi_todo_added_task_and_complete_properties_set_false():
    todo_1 = Todo("Do the washing")
    todo_2 = Todo("Make lunch")
    todo_3 = Todo("Watch the match")
    assert todo_1.complete == False
    assert todo_2.complete == False
    assert todo_3.complete == False

"""
Given multi todos
Tasks are marked as complete and complete property is updated to True
"""
def test_multi_todo_added_and_updated_to_complete_true():
    todo_1 = Todo("Do the washing")
    todo_1.mark_complete()
    todo_2 = Todo("Make lunch")
    todo_2.mark_complete()
    todo_3 = Todo("Watch the match")
    todo_3.mark_complete()
    assert todo_1.complete == True
    assert todo_2.complete == True
    assert todo_3.complete == True