def start():
    print('\n *** Список учеников*** \n' +
        '-------------------------------------\n' +
        'введите 1,2,3 или 4:\n' +
        '1 для добавления ученика\n' +
        '2 для поиска ученика\n' +
        '3 для удаления ученика\n' +
        '4 для выхода\n')
    choice = input('введите число от 1 до 4: ')
    return choice

def print_message(data):
    print(data)

def insert_data(message):
    return input(message)