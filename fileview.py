def whole_view(data):
    if data is True:
        with open('book.txt', 'r', encoding='utf-8') as book:
            for lines in book:
                print(lines)


def search_view(data):
    if (data is True):
        with open('book.txt', 'r', encoding='utf-8') as book:
            buffer = []
            search_element = input('Введите атрибут для поиска = ')
            for line in book:
                buffer.append(line)
            filtered = list(filter(lambda x: search_element in x, buffer))
            for i in filtered:
                print(i)
