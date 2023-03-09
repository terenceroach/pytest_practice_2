# ToDo Class Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can keep track of my tasks
> I want a program that I can add todo tasks to and see a list of them.

> As a user
> So that I can focus on tasks to complete
> I want to mark tasks as complete and have them disappear from the list.

* May want to add tasks marked as completed and from todo_list to a completed list

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class ToDo():
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   none 
        # Side effects:
        #   Sets up an empty list self.todo_list = []
        pass # No code here yet

    def add_todo(self, todo):
        # Parameters:
        #   todo: string representing a single todo
        # Returns:
        #   Nothing
        # Side-effects
        #   Adds the task to the self.todo_list
        pass # No code here yet

    def view_todos(self):
        # Paramters:
        #   none
        # Returns:
        #   list of todo items
        # Side-effects:
        #   none

    def remove_completed_todo(self, todo):
        # Paramters:
        #   todo: a string representing a single todo
        # Returns:
        #   none
        # Side-effects:
        #   Removes the task from the self.todo_list
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a todo when the todo_list is empty
# add todo to the todo_list
"""
todo = Todo()
todo.add_todo("Walk the dog")
todo.view_todos() # => "1. Walk the dog"

"""
Given a todo when the todo_list already has items
# add todo to the todo_list
"""
todo = Todo()
todo.add_todo("Walk the dog")
todo.add_todo("Do the ironing")
todo.view_todos() # => "1. Walk the dog 2. Do the ironing"

"""
Given a todo when there is only 1 todo present in todo_list
# remove the todo from the todo_list
"""
todo = Todo()
todo.add_todo("Walk the dog")
todo.remove_completed_todo("Walk the dog")
todo.view_todos() # => "No todos"

"""
Given a todo when there is more than 1 todo present in todo_list
# remove the todo from the todo_list
"""
todo = Todo()
todo.add_todo("Walk the dog")
todo.add_todo("Do the ironing")
todo.remove_completed_todo("Walk the dog")
todo.view_todos() # => "1. Do the ironing"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
