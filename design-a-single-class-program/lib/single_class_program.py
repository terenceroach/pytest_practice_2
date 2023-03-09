class Todo():
    def __init__(self):
        self.todo_list = []

    def add_todo(self, todo):
        self.todo_list.append(todo)

    def remove_completed_todo(self, todo):
        if todo in self.todo_list:
            self.todo_list.remove(todo)

    def view_todos(self):
        if self.todo_list == []:
            return "No todos"
        else:
            counter = 1
            list_string = ""
            for i in self.todo_list:
                list_string = list_string + f"{counter}. {i} "
                counter+= 1
            return list_string.rstrip()