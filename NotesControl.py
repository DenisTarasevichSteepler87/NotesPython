import json
import datetime

notes = []

def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def load_notes():
    global notes
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

def add_note():
    id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    body = input("Введите описание заметки: ")
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": id,
        "заголовок": title,
        "описание": body,
        "создан в": created_at,
        "обновлено в": created_at
    }
    notes.append(note)
    save_notes()
    print("Заметка успешно сохранена")

def edit_note():
    id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == id:
            note["заголовок"] = input("Введите новый заголовок заметки: ")
            note["описание"] = input("Введите новое описание заметки: ")
            note["обновлено в"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes()
            print("Заметка успешно отредактирована")
            return
    print("Заметка с таким ID не найдена")

def delete_note():
    id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == id:
            notes.remove(note)
            save_notes()
            print("Заметка успешно удалена")
            return
    print("Заметка с таким ID не найдена")

def list_notes():
    for note in notes:
        print(f'ID: {note["id"]}, Заголовок: {note["заголовок"]}, Описание: {note["описание"]}, Дата создания: {note["создан в"]}, Дата последнего редактирования: {note["обновлено в"]}')

def filter_notes_by_date():
    date = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    for note in notes:
        if note["создан в"].split()[0] == date:
            print(f'ID: {note["id"]}, Заголовок: {note["заголовок"]}, Описание: {note["описание"]}, Дата создания: {note["создан в"]}, Дата последнего редактирования: {note["обновлено в"]}')

def main():
    load_notes()
    while True:
        command = input("Введите команду (добавить, редактировать, удалить, список, фильтр, выход): ")
        if command == "добавить":
            add_note()
        elif command == "редактировать":
            edit_note()
        elif command == "удалить":
            delete_note()
        elif command == "список":
            list_notes()
        elif command == "фильтр":
            filter_notes_by_date()
        elif command == "выход":
            break
        else:
            print("Неправильная команда, попробуйте снова")

if __name__ == "__main__":
    main()