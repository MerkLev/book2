import csv


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


def csv_file_import(file_Name1):
    with open(f"{file_Name1}.csv", encoding='utf-8') as read_file:
        file_reader = csv.reader(read_file, delimiter=",")
        row_buffer = [row for row in file_reader]
    with open("book.csv", mode="a", encoding='utf-8') as book:
        file_writer = csv.writer(book, delimiter=",", lineterminator="\r")
        for i in range(0, 3):
            file_writer.writerow(row_buffer[i])


def csv_manual_import(counts):
    with open("book.csv", mode="a", encoding='utf-8') as book:
        file_writer = csv.writer(book, delimiter=",", lineterminator="\r")
        for i in range(0, 3):
            file_writer.writerow(input('Вводите значения в формате (Фамилия Имя, вн. номер, отдел)='))