
def manual_import(counts):
    with open('book.txt', 'a', encoding='utf-8') as book:
        for i in range(0, counts):
            contact = (input("Введите данные для записи в книгу в формате (Фамилия Имя, вн. номер, отдел)=  "))
            book.writelines(contact + '\n')


def file_import(file_Name1):
    buffer = ''
    with open(f'{file_Name1}', 'r', encoding='utf-8') as file:
        for line in file:
            buffer.append(line)
    with open('book.txt', 'a', encoding='utf-8') as file:
        for line in buffer:
            file.write(line + '\n')
