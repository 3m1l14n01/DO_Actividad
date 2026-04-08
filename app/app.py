from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# archivo donde se guardaran las tareas
TASKS_FILE = "tareas.json"

# Funcion cargar tareas
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# Funcion guardar tareas
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

@app.route('/tareas', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks), 200

@app.route('/tareas', methods=['POST'])
def create_task():
    data = request.get_json()
    tasks = load_tasks()

    # tarea con id incremental
    new_task = {
        "id": len(tasks) + 1,
        "titulo": data["titulo"],
        "descripcion": data["descripcion"]
    }
    tasks.append(new_task)
    save_tasks(tasks)

    return jsonify({"message": "Tarea creada correctamente", "tarea": new_task}), 201

@app.route('/tareas/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["titulo"] = data.get("titulo", task["titulo"])
            task["descripcion"] = data.get("descripcion", task["descripcion"])
            save_tasks(tasks)
            return jsonify({"message": "Tarea actualizada", "tarea": task}), 200

    return jsonify({"error": "Tarea no encontrada"}), 404

@app.route('/tareas/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return jsonify({"message": "Tarea eliminada"}), 200

    return jsonify({"error": "Tarea no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
