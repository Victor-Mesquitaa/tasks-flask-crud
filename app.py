from flask import Flask, request, jsonify
from models.tasks import Task

app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete
# Tabela: Tarefa

tasks = []
task_id_control = 1

# Rota para criar tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json() # Recuperando dado que o cliente inseriu
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description"))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "New task created sucessfuly", "id": new_task.id})

# Rota para listar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)

# Rota para listar tarefa específica
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())

    return jsonify({"message": "Can't found this task"}), 404

# Rota para atualizar tarefa
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t

    if task == None:
        return jsonify({"message": "Can't found this task"}), 404

    data = request.get_json() # Recuperando dado que o cliente inseriu
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    return jsonify({"message": "Task updated succesfuly"})

# Rota para excluir tarefa
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            tasks.remove(task)
            return jsonify({"message": "Task deleted succesfuly"})

    if task == None:
        return jsonify({"message": "Can't found this task"}), 404

if __name__ == "__main__":
    app.run(debug=True)