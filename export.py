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
