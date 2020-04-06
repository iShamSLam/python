import json

from flask import Flask
from flask import request
from service import ToDoService

app = Flask(__name__)
service = ToDoService()


@app.route('/todo', methods=["POST"])
def create_todo():
    result = service.create(request.get_json())
    return result.to_json()


@app.route('/todo', methods=["PATCH"])
def update_todo():
    result = service.update(request.get_json())
    return result.to_json()


@app.route('/todo', methods=["DELETE"])
def delete_todo():
    result = service.delete(request.get_json())
    return result.to_json()


@app.route('/todos', methods=["GET"])
def get_todos():
    result = service.index()
    todos = []
    if result is not None:
        for todo in result:
            todos.append(todo.to_json)
        return todos


if __name__ == '__main__':
    app.run(debug="true")
