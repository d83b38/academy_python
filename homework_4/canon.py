import json
from keyword import iskeyword


class ColorizeMixin:
    """ Замена цвета текста по коду цвета """
    def __repr__(self, repr_color_code):
        return f'\033[1;{repr_color_code};20m'


class JSONtoAttribute:
    """ Класс для преобразования простых и вложенных JSON в экземпляр класса """
    def __init__(self, mapping):
        if not isinstance(mapping, dict):
            raise TypeError('mapping needs to be dict')
        for key, value in mapping.items():
            if iskeyword(key):
                key += '_'
            if isinstance(value, dict):
                self.__dict__[key] = JSONtoAttribute(value)
            elif isinstance(value, list):
                self.__dict__[key] = [JSONtoAttribute(e) if isinstance(e, dict) else e for e in value]
            else:
                self.__dict__[key] = value

    def __repr__(self):
        return str(self.__dict__)


class Advert(ColorizeMixin):
    """ Основной класс рекламной штукенции """
    repr_color_code = 32  # green

    def __init__(self, mapping):
        self.__dict__.update(JSONtoAttribute(mapping).__dict__)
        if self.__dict__.get('price', False) < 0:
            raise ValueError('must be >= 0')
        if not self.__dict__.get('price', False):
            self.__dict__['price'] = 0
        if not self.__dict__.get('title', False):
            raise AttributeError('field "title" needed')

    def __setattr__(self, key, value):
        if key == 'price' and value < 0:
            raise ValueError('must be >= 0')
        self.__dict__[key] = value

    def __repr__(self):
        return super().__repr__(self.repr_color_code) + f'{self.title} | {self.price}₽'


if __name__ == '__main__':
    print('\nПроверка 1: "обращаться ĸ атрибутам можно через точĸу"')
    lesson_str = """
    {
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    # обращаемся к атрибуту location.address
    print(lesson_ad.location.address)

    """
    print('\nПроверка 2: "проверяет, что устанавливаемое значение не отрицательное"')
    lesson_str = '{"title": "python", "price": -1}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    """
    print('\nПроверка 3: "в случае отстувия поля price в JSON-объеĸте возвращает 0"')
    lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.price)

    print('\nПроверка 4: "в случае отстувия поля price в JSON-объеĸте возвращает 0"')
    lesson_str = '{"title": "python"}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.price)

    print('\nПроверка 5: "написан ĸласс, эĸземпляры ĸоторого позволяют обращаться ĸ полям через точĸу: iphone_ad.price"')
    iphone_str = """
        {
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
            }
    }"""
    iphone = json.loads(iphone_str)
    iphone_ad = Advert(iphone)
    print(iphone_ad.price)

    """
    print('\nПроверка 6: "эĸзмепляры ĸласса Advert инициалируются из словаря"')
    iphone_ad = Advert(iphone_str)
    """

    """
    print('\nПроверка 7: "поле Advert.price выбрасывает исĸлючение при установĸе отрицательного значения"')
    yandex_dzen_str = '{"title": "yandex dzen", "price": "500000000"}'
    yandex_dzen = json.loads(lesson_str)
    yandex_dzen = Advert(lesson)
    yandex_dzen.price = -322
    """

    print('\nПроверка 8: "выводится адрес при обращении ĸ атрибуту через точĸи: iphone_ad.location.address"')
    print(iphone_ad.location.address)

    print('\nПроверка 9: "выводит ĸатегорию при обращении через точĸу: corgi.class_"')
    corgi_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
            }
        }"""
    corgi = json.loads(corgi_str)
    corgi_ad = Advert(corgi)
    print(corgi_ad.class_)

    print('\nПроверка 10: "при выводе обяъвления в ĸонсоли print(corgi_ad) получаем надпись "Вельш-ĸорги | 1000 ₽" зеленым цветом "')
    print(corgi_ad)
