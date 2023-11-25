'''
Функции для 4ого пункта
Описание рисков по сделке (Автоматическая проверка, заглушки)
'''
def get_info_enforcement(document):
    return {'doc': document, 'risk': 'low'}

def get_info_bankruptcy(document):
    return {'doc': document, 'value': True}

def get_info_mvd(document):
    return {'doc': document, 'risk': 'medium'}

def enforcement_proceedings(person):
    document = person.passport
    info = get_info_enforcement(document)
    return info

def bankruptcy(person):
    document = person.passport
    info = get_info_bankruptcy(document)
    return info

def mvd(person):
    document = person.passport
    info = get_info_mvd(document)
    return info