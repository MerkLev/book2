import csv


def file_export(file_name):
    with open('book.txt', 'r', encoding='utf-8') as book:
        buffer_export = []
        for line in book:
            buffer_export.append(line)
    with open(f'{file_name}', 'a', encoding='utf-8') as exportBook:
        for i in buffer_export:
            exportBook.write(i)


def export_byData(search_element):
    with open('book.txt', 'r', encoding='utf-8') as book:
        buffer_export2 = []
        for line in book:
            buffer_export2.append(line)
        filtered = list(filter(lambda x: search_element in x, buffer_export2))
    file_name = input('Введите имя файла для экспорта данных = ')
    with open(f'{file_name}.txt', 'a', encoding='utf-8') as exportBook:
        for i in filtered:
            exportBook.write(i)


def csv_file_export(file_Name1):
    with open("book.csv", 'r', encoding='utf-8') as read_file:
        file_reader = csv.reader(read_file, delimiter=",")
        row_buffer = [row for row in file_reader]
    with open(f"{file_Name1}.csv", mode="a", encoding='utf-8') as book:
        file_writer = csv.writer(book, delimiter=",", lineterminator="\r")
        for i in range(0, len(row_buffer)):
            file_writer.writerow([row_buffer[i]])


def csv_export_byData(search_element):
    with open('book.csv', 'r', encoding='utf-8') as book:
        buffer_export2 = []
        for line in book:
            buffer_export2.append(line)
    filtered = list(filter(lambda x: search_element in x, buffer_export2))
    file_name = input('Введите имя файла для экспорта данных = ')
    with open(f'{file_name}.csv', 'a', encoding='utf-8') as exportBook:
        file_writer = csv.writer(exportBook, delimiter=",")
        for i in filtered:
            file_writer.writerow([i])


