#
#
# dict_data = {}
# # dict_data['department'] = 'А-Сахалинский', 'Анива', 'Долинск', 'Курильск', 'Макаров', 'Невельск', 'Новиково', \
# #                           'Поронайск', 'С-Курильск', 'Томари', 'Тымовское', 'Углегорск', 'Чехов', 'Ю-Курильск', 'Смирных'
# dict_data['А-Сахалинский'] = '46 ПЧ', '47 ПЧ', '48 ПЧ', 'ОП 46 ПЧ Виахту', 'ОП 46 ПЧ Хоэ'
# dict_data['Анива'] = '51 ПЧ', '52 ПЧ', 'ОП 51 ПЧ Огоньки', 'ОП 51 ПЧ Таранай'
# dict_data['Долинск'] = '23 ПЧ', '24 ПЧ', '25 ПЧ', 'ОП 23 ПЧ Взморье', 'ОП 23 ПЧ Сокол', 'ОП 23 ПЧ Стародубское'
# dict_data['Курильск'] = '20 ПЧ', '21 ПЧ'
# dict_data['Макаров'] = '26 ПЧ', 'ОП 26 ПЧ Восточное'
# dict_data['Невельск'] = '12 ПЧ', '13 ПЧ', '14 ПЧ'
# dict_data['Новиково'] = '22 ПЧ', 'ОП 22 ПЧ Озерское', 'ОП 22 ПЧ Охотское', 'ОП 22 ПЧ Соловьевка', 'ОП 22 ПЧ Чапаево'
# dict_data['Поронайск'] = '32 ПЧ', '34 ПЧ', '35 ПЧ'
# dict_data['С-Курильск'] = '53 ПЧ'
# dict_data[
#     'Тымовское'] = '41 ПЧ', '42 ПЧ', '43 ПЧ', '44 ПЧ', '45 ПЧ', '54 ПЧ', 'ОП 41 ПЧ Кировское', 'ОП 41 ПЧ Ныш', 'ОП 45 ПЧ Чир-Унвд', 'ОП 54 ПЧ Вал', 'ОП 54 ПЧ Некрасовка'
# dict_data['Углегорск'] = '15 ПЧ', '17 ПЧ', '18 ПЧ', '19 ПЧ', 'ОП 15 ПЧ Краснополье', 'ОП 15 ПЧ Поречье'
# dict_data['Ю-Курильск'] = '49 ПЧ', '50 ПЧ', 'ОП 49 ПЧ Дубовое'
# dict_data['Смирных'] = '36 ПЧ', '37 ПЧ', '38 ПЧ', '39 ПЧ', '40 ПЧ'
# dict_data['Томари'] = '29 ПЧ', '30 ПЧ', '31 ПЧ'
# dict_data['Чехов'] = '10 ПЧ', '11 ПЧ', 'ОП 10 ПЧ Пионеры', 'ОП 11 ПЧ Правда', 'ОП 11 ПЧ Чапланово'
#
#


suka = {

    "А-Сахалинский": {
        "brigate": ['46 ПЧ', '47 ПЧ', '48 ПЧ', 'ОП 46 ПЧ Виахту', 'ОП 46 ПЧ Хоэ'],
        "auto": ['АЦ(л)-1,0-30(3308)', 'АЦ-3,7-40(531340)', 'АЦ-5,5-40(5557)', 'АЦ-6,0-40(4320)', 'АЦ-7.5-40('
                                                                                                  '4320)',
                 'УАЗ(390995)', 'ГАЗ(66)'],
        'АЦ(л)-1,0-30(3308)': ['К 197 СА'],
        'АЦ-5,5-40(5557)': ['К 170 ХТ', 'К 833 ТК', 'М 433 ОК', 'М 954 ОЕ', 'М 956 ОЕ'],
        'АЦ-3,7-40(531340)': ['К 169 ХТ'],
        'АЦ-6,0-40(4320)': ['М 722 ОН'],
        'АЦ-7.5-40(4320)': ['К 832 ТК'],
        'УАЗ(390995)': ['Н 431 ЕА'],
        'ГАЗ(66)': ['К 294 АА']
    },

    "Анива": {
        "brigate": ['51 ПЧ', '52 ПЧ', 'ОП 51 ПЧ Огоньки', 'ОП 51 ПЧ Таранай'],
        "auto": ['Автобус', 'АЛ-30 (5557)', 'АЛ-50 (Камаз-53229)', 'АНР-40-1,4 (КАМАЗ 43118)', 'АР-2 (5557)',
                 'АЦ-2,5-40 (5313)', 'АЦ-3,0-20 Natisk (5557)', 'АЦ-4,0-40 (43206)', 'АЦ-5-100 (43118)',
                 'АЦ-6,0-70(5557)', 'АЦ-7,5-40 (4320)', 'АЦЛ-4,0-40/17 (43118)', 'Камаз(бортовой)',
                 'Кран-манипулятор', 'ПНС-110 (5557)', 'Погрузчик', 'ПСА 2,0-40/2 (43206)', 'УАЗ(315195)'],
        'Автобус': ['М 541 ТХ', 'М 542 ТХ', 'М 543 ТХ'],
        'АЛ-30 (5557)': ['К 684 НВ'],
        'АЛ-50 (Камаз-53229)': ['М 963 ВЕ'],
        'АНР-40-1,4 (КАМАЗ 43118)': ['М 987 СТ'],
        'АР-2 (5557)': ['М 649 ТХ'],
        'АЦ-2,5-40 (5313)': ['К 028 ТС'],
        'АЦ-3,0-20 Natisk (5557)': ['М 304 ОА'],
        'АЦ-4,0-40 (43206)': ['К 197 МЕ'],
        'АЦ-5-100 (43118)': ['М 195 СТ'],
        'АЦ-6,0-70(5557)': ['Н 542 АМ'],
        'АЦ-7,5-40 (4320)': ['К 128 УС'],
        'АЦЛ-4,0-40/17 (43118)': ['Н 735 ВР'],
        'Камаз(бортовой)': ['К 441 ТХ'],
        'Кран-манипулятор': ['Н 014 АУ'],
        'ПНС-110 (5557)': ['М 768 ТХ'],
        'Погрузчик': ['6326 СМ'],
        'ПСА 2,0-40/2 (43206)': ['М 961 ВЕ'],
        'УАЗ(315195)': ['К 388 ХА']

    },
    "Долиск": {
        "brigate": ['23 ПЧ','24 ПЧ', '25 ПЧ', 'ОП 23 ПЧ Взморье', 'ОП 23 ПЧ Сокол', 'ОП 23 ПЧ Стародубское'],
        "auto": ['HINO','АЛ-30(531320)', 'АР-2(КАМАЗ-5350)', 'АСО-20 (ГАЗ-3308)', 'АЦ-40 (131)137', 'АЦ-6,0 (УРАЛ-4320)',
                 'АЦ-7,5 (КАМАЗ-43118)', 'АШ-7 (ГАЗ-2705)', 'УАЗ(Патриот)',	'АЦ-2,5-40(5313)', 'АЦ-4,0-40 (УРАЛ-43206)',
                 'АНР 40-1,4(КАМАЗ-43118)',	'АЦ-6,0-70(5557)', 'АЦ-6,0-50 (УРАЛ-5557)'],
        'HINO': ['М 014 АО'],
        'АЛ-30(531320)': ['К 986 ХХ'],
        'АР-2(КАМАЗ-5350)': ['М 584 СХ'],
        'АСО-20 (ГАЗ-3308)': ['М 823 СР'],
        'АЦ-40 (131)137': ['М 669 КР'],
        'АЦ-6,0 (УРАЛ-4320)': ['М 926 РЕ'],
        'АЦ-7,5 (КАМАЗ-43118)': ['М 925 РЕ'],
        'АШ-7 (ГАЗ-2705)': ['К 871 ТН'],
        'УАЗ(Патриот)': ['К 300 УВ'],
        'АЦ-2,5-40(5313)': ['К 014 РС', 'К 459 РТ', 'К 013 РС'],
        'АЦ-4,0-40 (УРАЛ-43206)': ['К 352 КС'],
        'АНР 40-1,4(КАМАЗ-43118)': ['М 917 РР'],
        'АЦ-6,0-70(5557)': ['Н 658 ЕВ'],
        'АЦ-6,0-50 (УРАЛ-5557)': ['К 012 РС']

    },

    "Курильск": {
        "brigate": ['20 ПЧ','21 ПЧ'],
        "auto": ['АЦ 3,0-40 (43206)', 'АЦ-2,5-40(5313)', 'АЦ-5,5-40(5557)',	'АЦ-6,0-70(5557)',	'АЦ-7,5-40(43118)',
                 'Погрузчик', 'АЦ 5,8-40(5557)'],
        'АЦ 3,0-40 (43206)': ['В 076 СХ'],
        'АЦ-2,5-40(5313)': ['К 627 ТМ'],
        'АЦ-5,5-40(5557)': ['М 600 НР'],
        'АЦ-6,0-70(5557)': ['Н 664 ВМ'],
        'АЦ-7,5-40(43118)': ['М 650 НР'],
        'Погрузчик': ['7295 СМ'],
        'АЦ 5,8-40(5557)': ['В 075 СХ']

    },

    "Макаров": {
        "brigate": ['26 ПЧ','ОП 26 ПЧ Восточное'],
        "auto": ['АЦ-2,5-40 (5313)', 'АЦ-5,5-40 (5557)', 'АЦ-7,5-40 (4320)', 'АЦЛ-3,0-40-17(КАМАЗ 43118)',
                'Снегоболотоход', 'УАЗ(390995)', 'АМУР(531382)'],
        'АЦ-2,5-40 (5313)': ['К 441 РТ'],
        'АЦ-5,5-40 (5557)': ['М 063 НХ', 'М 355 НЕ'],
        'АЦ-7,5-40 (4320)': ['К 136 ТК'],
        'АЦЛ-3,0-40-17(КАМАЗ 43118)': ['М 368 ТК'],
        'Снегоболотоход': ['4827 СМ'],
        'УАЗ(390995)': ['М 736 ВМ'],
        'АМУР(531382)': ['М 910 МЕ']

    },


}






######################################################

brigate = ['А-Сахалинский', 'Анива', 'Долинск', 'Курильск', 'Макаров', 'Невельск', 'Новиково', 'Поронайск', \
           'С-Курильск', 'Томари', 'Тымовское', 'Углегорск', 'Чехов', 'Ю-Курильск', 'Смирных']

machine = ['АЦ(л)-1,0-30(3308)', 'АЦ-3,7-40(531340)', 'АЦ-5,5-40(5557)', 'АЦ-6,0-40(4320)', 'АЦ-7.5-40(4320)',
           'ГАЗ(66)', 'УАЗ(390995)']
