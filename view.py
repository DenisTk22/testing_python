import processor

def main_menu():
    play = True
    while play:
        processor.read_notes()
        answer = input("Choose the command bellow:\n"
                       "1. Show all notes\n"
                       "2. Add a note\n"
                       "3. Search a note\n"
                       "4. Change a note\n"
                       "5. Delete a note\n"
                       "6. Exit\n")
        match answer:
            case "1":
                processor.show_all()
            case "2":
                processor.add_new_note()
            case "3":
                processor.search_note()
            case "4":
                processor.change_note()
            case "5":
                processor.delete_note()
            case "6":
                play = False
            case _:
                print("Try again!\n")