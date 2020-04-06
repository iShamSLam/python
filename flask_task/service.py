from models import ToDoDB


class ToDoService:
    def __init__(self):
        self.db = ToDoDB()

    def create(self, params):
        return self.db.create(params['title'], params['description'], params['due_date'])

    def update(self, params):
        return self.db.update(params['title'])

    def delete(self, params):
        return self.db.delete(params['title'])

    def index(self):
        return self.db.get_all()
