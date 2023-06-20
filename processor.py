import json
import os.path
from os import path
import datetime


all_data = []
note_id = 1
file_base = "My_notes.json"

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_notes():
    global all_data, note_id
    with open(file_base, "r", encoding="utf-8") as f:
        if os.path.getsize(file_base) != 0:
            all_data = json.load(f)
            if all_data:
                note_id = len(all_data) + 1
                return all_data
    return []

def show_all():
    if all_data != []:
        for note in all_data:
            print("{}/ {}/ {}/ {}\n".format(note['id'], note['title'].upper(), note['message'][:50],note['time']))
    else:
        print("Notebook is empty!\n")

def save_note():
    with open(file_base, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=2)

def add_new_note():
    global note_id
    curent_date = str(datetime.now())
    title = input("Enter a title:\n")
    massage = input("Enter a message:\n")
    temp_note = {"id": note_id, "title": title, "message": massage, "time":curent_date}
    all_data.append(temp_note)
    note_id += 1
    save_note()
    print("Note is created!\n")

def change_note():
    if all_data != []:
        choice = get_choice()
        if choice != -1:
            title = input("Change a title:\n")
            massage = input("Change a message:\n")
            curent_date = str(datetime.now())
            temp_note = {"id": choice + 1, "title": title, "message": massage, "time":curent_date}
            all_data.remove(all_data[choice])
            all_data.insert(choice, temp_note)
            save_note()
            print("Note is successfully changed\n")
        else:
            print("Id is not found!\n")
    else:
        print("Notebook is empty!\n")

def search_note():
    if all_data != []:
        play = True
        while play:
            answer = input("Search menu:\n"
                           "1. Search by id\n"
                           "2. Search by title\n"
                           "3. Search by text\n")
            match answer:
                case "1":
                    search_by_id()
                    play = False
                case "2":
                    search_by_title()
                    play = False
                case "3":
                    search_by_text()
                    play = False
                case _:
                    print("Try again!\n")
    else:
        print("Notebook is empty!\n")

def search_by_id():
    choice = get_choice()
    if choice != -1:

        if choice < len(all_data):
            print("{}/ {}/ {}/ {}\n".format(all_data[choice]['id'], all_data[choice]['title'].upper(),
                                            all_data[choice]['message'], all_data[choice]['time']))
        else:
            print("Id is not found!\n")
    else:
        print("Id is not found!\n")

def search_by_title():
    choice = input("Enter a title:\n")
    flag = True
    for note in all_data:
        if note["title"].lower().strip() == choice.lower().strip():
            temp_id = note["id"] - 1
            print("{}. {}\n{}\n{}\n".format(all_data[temp_id]['id'], all_data[temp_id]['title'].upper(),
                                            all_data[temp_id]['message'], all_data[temp_id]['time']))
            flag = False
    if flag:
        print("Title is not found!\n")

def search_by_text():
    choice = input("Enter a text:\n")
    flag = True
    for note in all_data:
        if choice.lower().strip() in note["message"].lower().strip():
            temp_id = note["id"] - 1
            print("{}. {}\n{}\n{}\n".format(all_data[temp_id]['id'], all_data[temp_id]['title'].upper(),
                                            all_data[temp_id]['message'], all_data[temp_id]['time']))
            flag = False
    if flag:
        print("Text is not found!\n")

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def delete_note():
    if all_data != []:
        choice = get_choice()
        if choice != -1:
            last = len(all_data) - 1
            all_data.remove(all_data[choice])
            if choice != last:
                for temp_index in range(choice, len(all_data)):
                    temp_note = all_data[temp_index]
                    all_data[temp_index] = {"id": temp_index + 1, "title": temp_note['title'],
                                             "message": temp_note['message'],"time":temp_note['time']}
                    save_note()
            save_note()
            print("Note is deleted!\n")
        else:
            print("Id is not found!\n")
    else:
        print("Notebook is empty!\n")

def get_choice():
    show_all()
    choice = input("Enter id of the note:\n")
    if is_int(choice):
        if ((int(choice) <= len(all_data)) & (int(choice) > 0)):
            x = int(choice)
            x -= 1
            return x
    return -1
