class TodoList:
    def __init__(self):
        self.todo_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        
        return self.todo_list.append(todo)
      
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_list = []
        for i in self.todo_list:
            if i.complete == False:
                incomplete_list.append(i)
        return incomplete_list


    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_list = []
        for i in self.todo_list:
            if i.complete == True:
                complete_list.append(i)
        return complete_list

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for i in self.todo_list:
            i.complete = True