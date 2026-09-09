import pytest
import requests

# CRUD

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
    new_task_data = {
        "title": "Test Task",
        "description": "This is a test task.",
        "done": False
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data) # Envia uma requisição POST para criar uma nova tarefa
    assert response.status_code == 200 # Verifica se a requisição foi bem sucedida
    response_json = response.json() # Recuperando dado que o cliente inseriu
    assert "message" in response_json # Verifica se a resposta contém a chave "message"
    assert "id" in response_json # Verifica se a resposta contém a chave "id"
    tasks.append(response_json["id"]) # Adiciona o ID da tarefa criada à lista de tarefas

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json # Verifica se a resposta contém a chave "tasks"
    assert "total_tasks" in response_json # Verifica se a resposta contém a chave "total_tasks"

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response__json = response.json()
        assert task_id == response__json['id'] # Verifica se o ID da tarefa retornada é igual ao ID da tarefa solicitada

def test_update_task():
    if tasks:
        task_id = tasks[0]
        updated_task_data = {
            "title": "Updated Test Task",
            "description": "This is an updated test task.",
            "completed": True
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=updated_task_data) # Envia uma requisição PUT para atualizar a tarefa com o ID especificado
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json # Verifica se a resposta contém a chave "message"

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}") # Envia uma requisição DELETE para remover a tarefa com o ID especificado
        assert response.status_code == 200
        response_json = response.json()

        response = requests.get(f"{BASE_URL}/tasks/{task_id}") # Verifica se a tarefa foi realmente removida
        assert response.status_code == 404 # Verifica se a resposta da requisição GET