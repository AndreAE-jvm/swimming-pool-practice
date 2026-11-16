# Задание: консольное приложение для управления задачами.
#
# Требования:
#
# Хранение задач в файле tasks.json (список словарей: {"id": 1, "text": "...", "done": false}).
#
# Функции: add_task(text), list_tasks(), mark_done(id), delete_task(id).
#
# Главное меню: пользователь вводит команду (add, list, done, delete, exit)

import json
import os

FILENAME = "tasks.json"

def load_tasks():
    """Загружает задачи из файла. Если файла нет — возвращает пустой список."""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    """Сохраняет задачи в файл."""
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def add_task(text):
    tasks = load_tasks()
    new_id = max([t["id"] for t in tasks], default=0) + 1
    tasks.append({"id": new_id, "text": text, "done": False})
    save_tasks(tasks)
    print(f"Задача добавлена (id={new_id})")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Список задач пуст.")
        return
    for t in tasks:
        mark = "x" if t["done"] else " "
        print(f"{t['id']}. [{mark}] {t['text']}")

def mark_done(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"Задача {task_id} выполнена")
            return
    print(f"Задача с id={task_id} не найдена")

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Задача с id={task_id} не найдена")
        return
    save_tasks(new_tasks)
    print(f"Задача {task_id} удалена")

def main():
    while True:
        command = input("> ").strip().split(maxsplit=1)
        if not command:
            continue
        cmd = command[0].lower()
        arg = command[1] if len(command) > 1 else ""

        if cmd == "add":
            if arg:
                add_task(arg)
            else:
                print("Использование: add <текст>")
        elif cmd == "list":
            list_tasks()
        elif cmd == "done":
            if arg.isdigit():
                mark_done(int(arg))
            else:
                print("Использование: done <id>")
        elif cmd == "delete":
            if arg.isdigit():
                delete_task(int(arg))
            else:
                print("Использование: delete <id>")
        elif cmd == "exit":
            print("До свидания!")
            break
        else:
            print("Неизвестная команда. Доступно: add, list, done, delete, exit")

if __name__ == "__main__":
    main()

