import sys
import view
import model 

def show_main_menu():
    while True:
        menu_num = view.start()
        if menu_num == '1': 
            result1 = model.add_new_student()
            view.print_message(result1)
        elif menu_num == '2': 
            data = view.insert_data('Поиск ученика по фамилии:')
            result2 = model.search_student(data)
            view.print_message(result2)
        elif menu_num == '3': 
            data = view.insert_data('Поиск ученика для удаления:')
            result3 = model.delete_student(data)
            view.print_message(result3)
        elif menu_num == '4': 
            sys.exit
        else:
            print('Ошибка. Введите число от 1 до 4 \n')
            show_main_menu()