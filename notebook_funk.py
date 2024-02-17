import os.path

def show_notes(file: str):
    if os.path.exists(file):
        print('*'*25)
        with open(file, encoding = 'utf-8') as f:
            for line in f:
                data = eval(line)
                num = list(data.keys())
                data = list(data.values())
            
                print(f'Название: {data[0][0]}, Заметка: {data[0][1]}')
        print('*'*25)
    else: print('file not found')
    
def add_note(file: str):
    n_note = input("Введите название заметки: ")
    note = input("Введите заметку: ")
    new_dict = {count_lines(file): [n_note, note]}
    with open(file,'a',encoding='UTF-8') as f:
        f.write(f'{new_dict}\n')
    print('*'*25)
    print(f"Заметка {n_note} добавлена")
    print('*'*25)
    
def count_lines(file: str):
    if os.path.exists(file):
        with open(file) as f:
            try:
                for i, _ in enumerate(f):
                    pass
                return i + 1
            except:
                pass
                #return 0
    else: return 0
    
def find_note(file: str):
    user_str = input('Введите запрос: ')
    tmp_list = list()
    with open(file, encoding='UTF-8') as f:
        for line in f:
            if user_str in line:
                tmp_list.append(line)
                decorate_str(line)
        if len(tmp_list) > 1:
            #decorate_str(finder(tmp_list)[0])
            tmp_list = finder(tmp_list)
    if not tmp_list is None:
        print('> Для того, чтобы изменить заметку нажмите (с), для удаления (d)')
        print('> для отмены (x)')
        user_answer = input('>>>: ')
        if user_answer == "c":
            change_note(file, tmp_list)   
        elif user_answer == "d":
            delete_note(file, tmp_list)       
        elif user_answer == "x":
            print("> Работа программы завершена!")      
    else:
        print("> Работа программы завершена!")
        
def change_note(file: str, tmp_list: list):
    num_key = list(eval(tmp_list[0]).keys())
    old_data = list(eval(tmp_list[0]).values())
    new_data = old_data.copy()

    print('Для внесения изменений в запись, введите пожалуйста что вы хотите изменить: название - 0, содержание - 1')
    print('для измения записи полностью, введите Enter')
    user_answer = input(">>>: ")
    if user_answer == '0':
        new_data[0][int(user_answer)] = input("Введите название: ")
    elif user_answer == '1':
        new_data[0][int(user_answer)] = input("Введите заметку: ")
    elif user_answer == '':
        # new_data[0][int(user_answer)] = input("Введите название: ")
        # new_data[0][int(user_answer)] = input("Введите заметку: ")
        new_data[0][0] = input("Введите название: ")
        new_data[0][1] = input("Введите заметку: ")
    new_list = [new_data[0][0], new_data[0][1]]
    new_dict = {num_key[0]: new_list}

    with open(file, 'r',encoding='utf-8') as f:
        data = f.readlines()
        i = data.index(tmp_list[0])
        data[i] = (f'{new_dict}\n')

    with open(file, 'w',encoding='utf-8') as f:
        f.writelines(data)
    print('*'*25)
    print('Заметка изменена!')       
    print('*'*25)
# d - удалить контакт
def delete_note(file: str, tmp_list: list):
    with open(file, encoding='utf-8') as f:
        data = f.readlines()
        data.remove(str(tmp_list[0]))
    with open(file, 'w',encoding='utf-8') as f:
        f.writelines(data)
    print('*'*25)
    print('Заметка удалена!')
    print('*'*25)
# вспомогательная функция для find_contact
def finder(notes: list):
    if len(notes) > 1:
        result = list()
        print('> Для внесения изменений, удаления')
        print('> Уточните данные или передайте порядковый номер строки')
        print('> Для отмены нажмите X')
        user_answer = input('>>>: ')
        if user_answer != 'x':
            try:
                user_answer = int(user_answer)
                result.append(notes[user_answer - 1])
            except:
                for el in notes:
                    if user_answer in el: result.append(el)
        else: 
            result.append("> Поиск завершен!")     
        return result
    else: return notes
    
# преобразователь
def decorate_str(line: str):
    try:
        data = eval(line)
        num = list(data.keys())
        data = list(data.values())
        print(f'Название: {data[0][0]}, Содержание: {data[0][1]}')
    except:
        print(line)