import import_Book as ib
import requests as rq
import export as ep
import fileview as fv


type_Request = input('Введите тип работы со справочником(чтение, изменение данных): ')
Mode = rq.type_of_mode(type_Request)
if (Mode is True):
    type_Request = input('Введите тип просмотра данных(все контакты, по фильтру): ')
    Mode = rq.type_of_view(type_Request)
    if (Mode is True):
        fv.whole_view(Mode)
    else:
        fv.search_view(Mode)
else:
    type_Request = input('Введите тип запроса для работы со справочником (импорт/экспорт): ')
    Import = rq.type_of_usage(type_Request)
    if (Import is True):
        type_Request = input('Введите тип ввода данных (файл/ручной ввод): ')
        ffile = rq.type_Import(type_Request)
        if (ffile is True):
            counts = int(input('Введите количество новых контактов: '))
            ib.manual_import(counts)
        else:
            file_Name1 = input('Введите имя файла для экспорта контактов: ')
            ib.file_import(file_Name1)
    else:
        type_Request = input('Введите тип экспорта данных (файл/фильтр): ')
        ffile = rq.type_export(type_Request)
        if (ffile is True):
            file_name = input('Введите имя файла для экспорта данных = ')
            ep.file_export(ffile)
        else:
            search_element = input('Введите атрибут для поиска = ')
            ep.export_byData(search_element)
