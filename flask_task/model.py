from datetime import datetime


class ToDoModel:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.due_date = due_date
        self.status = "created"

    def to_json(self):
        return {'title': self.title,
                'description': self.description,
                'created_at': self.created_at,
                'due_date': self.due_date,
                'status': self.status
                }


class ToDoDB:
    def __init__(self):
        self.todos = []

    def get_all(self):
        return self.todos

    def create(self, title, description, due_date):
        todo = ToDoModel(title, description, due_date)
        self.todos.append(todo)
        return todo

    def update(self, title):
        for todo in self.todos:
            if todo.title == title:
                found_todo = todo
                found_todo.status = "_is_done"
                return found_todo

    def delete(self, title):
        for todo in self.todos:
            if todo.title == title:
                found_todo = todo
                found_todo.status = "_is_deleted"
                return found_todo
