import csv


def whole_view(data):
    if data is True:
        with open('book.txt', 'r', encoding='utf-8') as book:
            for lines in book:
                print(lines)


def search_view(data):
        with open('book.txt', 'r', encoding='utf-8') as book:
            buffer = []
            search_element = input('Введите атрибут для поиска = ')
            for line in book:
                buffer.append(line)
            filtered = list(filter(lambda x: search_element in x, buffer))
            for i in filtered:
                print(i)


def csv_whole_view(file_Name1):
    with open("book.csv", 'r', encoding='utf-8') as read_file:
        file_reader = csv.reader(read_file, delimiter=",")
        row_buffer = [row for row in file_reader]
        for i in row_buffer:
            print(i)


def csv_search_view(search_element):
    with open('book.csv', 'r', encoding='utf-8') as book:
        buffer_export2 = []
        for line in book:
            buffer_export2.append(str(line))
    filtered = list(filter(lambda x: str(search_element) in x, buffer_export2))
    for i in filtered:
        print(i)