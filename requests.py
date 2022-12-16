
def type_of_usage(Data):
    if Data == 'импорт':
        Data = True
    elif Data == 'экспорт':
        Data = False
    else:
        while Data != 'импорт' and Data != 'экспорт':
            Data = input('некорректный тип запроса, ввод типа строго маске (импорт/экспорт):')
        if Data == 'импорт':
            Data = True
        else:
            Data = False
    return (Data)


def type_Import(Data):
    if Data == 'ручной ввод':
        ffile = True
    elif Data == 'файл':
        ffile = False
    else:
        while Data != 'файл' and Data != 'ручной ввод':
            Data = input('некорректный тип запроса, ввод типа строго маске (файл/ручной ввод):')
    return (ffile)


def type_export(Data):
    if Data == 'Файл':
        ffile = True
    elif Data == 'фильтр':
        ffile = False
    else:
        while Data != 'файл' and Data != 'фильтр':
            Data = input('некорректный тип запроса, ввод типа строго маске (файл/фильтр):')
    return (ffile)


def type_of_mode(Data):
    if Data == 'чтение':
        Data = True
    elif Data == 'изменение данных':
        Data = False
    else:
        while Data != 'чтение' and Data != 'изменение данных':
            Data = input('некорректный тип запроса, ввод типа строго маске (чтение/изменение данных):')
        if Data == 'чтение':
            Data = True
        else:
            Data = False
    return (Data)


def type_of_view(Data):
    if Data == 'все контакты':
        Data = True
    elif Data == 'по фильтру':
        Data = False
    else:
        while Data != 'все контакты' and Data != 'по фильтру':
            Data = input('некорректный тип запроса, ввод типа строго маске (все контакты/по фильтру):')
        if Data == 'все контакты':
            Data = True
        else:
            Data = False
    return (Data)
