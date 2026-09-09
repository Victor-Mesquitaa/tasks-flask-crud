from flask import Flask, request, jsonify
from models.tasks import Task

app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete
# Tabela: Tarefa

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description"))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "New task created sucessfuly",})

if __name__ == "__main__":
    app.run(debug=True)