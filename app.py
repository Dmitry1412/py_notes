from notebook_funk import show_notes, add_note, find_note
import datetime

def main():
    file_name = 'note_book.txt'
    flag_exit = False
    while not flag_exit:
        print('s - показать заметки')
        print('f - найти заметку')
        print('a - создать заметку')
        answer = input('Введите операцию или Х для выхода: ')
        if answer == 's':
            show_notes(file_name)
        elif answer == 'f':
            find_note(file_name)
        elif answer == "a":
            add_note(file_name)
        elif answer == "x":
            flag_exit = True
            
main()
# d = datetime.datetime.today()
# d= d.strftime("%Y-%m-%d %H:%M:%S")
# print(d)
