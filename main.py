import import_Book as ib
import requests as rq
import export as ep
import fileview as fv
import csv

type_Request = input('Введите тип работы со справочником(чтение, изменение данных): ')
Mode = rq.type_of_mode(type_Request)
type_Request = input('Введите расширение справочника(txt, csv): ')
extention = rq.type_of_file_extension(type_Request)

if (extention is True):
    if (Mode is True):
        type_Request = input('Введите тип просмотра данных(все контакты, по фильтру): ')
        Mode = rq.type_of_view(type_Request)
        if (Mode is True):
            fv.csv_whole_view(Mode)
        else:
            search_element = input('введите элемент для поиска =')
            fv.csv_search_view(search_element)
    else:
        type_Request = input('Введите тип запроса для работы со справочником (импорт/экспорт): ')
        Import = rq.type_of_usage(type_Request)
        if (Import is True):
            type_Request = input('Введите тип ввода данных (файл/ручной ввод): ')
            ffile = rq.type_Import(type_Request)
            if (ffile is True):
                counts = int(input('Введите количество новых контактов: '))
                ib.csv_manual_import(counts)
            else:
                file_Name1 = input('Введите имя файла для экспорта контактов: ')
                ib.csv_file_import(file_Name1)
        else:
            type_Request = input('Введите тип экспорта данных (файл/фильтр): ')
            ffile = rq.csv_type_export(type_Request)
            if (ffile is True):
                file_name = input('Введите имя файла для экспорта данных = ')
                ep.csv_file_export(file_name)
            else:
                search_element = input('Введите атрибут для поиска = ')
                ep.csv_export_byData(search_element)
else:
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
