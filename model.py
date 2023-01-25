file_name = 'students.csv'
file1 = open(file_name, 'a+')
file1.close()


def search_student(search_name):
    search_name = search_name.title()
    file1 = open(file_name, 'r+')
    file_contents = file1.readlines()
    found = False
    for line in file_contents:
        if search_name in line:
            return line
        found = True
        break
    if found == False:
        return 'Не найден'
    


def delete_student(search_name):
    search_name = search_name.title()
    file1 = open(file_name, 'r+')
    file_contents = file1.readlines()
    found = False
    for line in file_contents:
        if search_name in line:
            print('Ваш ученик: ', end=' ')
            print(line)
            found = True
            file = open('students.csv', 'r')
            f = file.read().replace(line, ' ')
            file2 = open('students.csv', 'w')
            file2.write(f)
            file2.close()
            break
    if found == False:
        return 'Не найден'
      

def add_new_student():
    first = input('Введите имя: ')
    first = first.title()
    last = input('Введите фамилию: ')
    last = last.title()
    DoB = input('Введите дату рождения: ')
    group = input('Введите номер класса: ')
    student = ('[' + first + ' ' + last + '||' + DoB + '||' + group +']\n')
    file1 = open(file_name, 'a+')
    file1.write(student)
    file1.close()