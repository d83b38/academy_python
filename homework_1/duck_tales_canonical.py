def boolean_question_on_step(options_map):
    """ Булевый вопрос для использования в шагах"""
    option = ''
    while option not in options_map:
        print('Выберите: {}/{}'.format(*options_map))
        option = input().lower()
    return options_map[option]


def step1():
    """ Инициирующий выбор, шаг 1 """
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    choice_result = boolean_question_on_step({'да': True, 'нет': False})
    print('Уточка топает к бару... Поднимает свой любопытный клюв к небу.')
    if choice_result:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    """ Исход при выборе зонта, шаг 2 """
    print(
        'И видит - собрались тучи.. Но при уточке оказался удачно взятый зонтик.\n'
        'Порадуется ли уточка?'
    )
    choice_result = boolean_question_on_step({'да': True, 'нет': False})
    print('Совсем скоро пошел дождь. ')
    print('Утка удачно решила взять с собой зонт. Дошла до бара совсем сухонькой.')
    if choice_result:
        return step3_umbrella_happy()
    return step3_umbrella_neutral()


def step2_no_umbrella():
    """ Исход без выбора зонта, шаг 2 """
    print(
        'И видит - как назло собрались тучи.. Зонтик бы пригодился..\n'
        'Расcтроится ли уточка?'
    )
    choice_result = boolean_question_on_step({'да': True, 'нет': False})
    print('Совсем скоро пошел дождь. ')
    print('Утка не подумала взять зонтик. Конечно же она промокла.')
    if choice_result:
        return step3_no_umbrella_upset()
    return step3_no_umbrella_neutral()


def step3_umbrella_happy():
    """ Исход при выборе зонта и умении замечать радости жизни, шаг 3 """
    print(
        'В этот день такое маленькое, почти случайное, но удачное стечение обстоятельств '
        'здорово подняло уточке настроение.\n'
        'На радость себе и назло дождику наша уточка заказала себе тропический коктейль 🍹'
    )


def step3_umbrella_neutral():
    """ Исход при выборе зонта и неумении замечать радости жизни, шаг 3 """
    print('Это был регулярный поход в бар, уточка по традиции заказала себе бокал пшенички 🍺. ')


def step3_no_umbrella_upset():
    """ Исход без выбора зонта и пессимизме, шаг 3 """
    print(
        'Мало того, что промокла, так еще и сильно раздосадовалась..\n'
        'По такому поводу наша уточка заказала себе виски со льдом и угрюмо потягивала его из стакана 🥃..'
    )


def step3_no_umbrella_neutral():
    """ Исход без выбора зонта и умеренном оптимизме, шаг 3 """
    print(
        'Ну промокла и промокла, че бухтеть то.\n'
        'Тем более, что совсем скоро её перышки прогреет добротный кубинский ром 🥃.'
    )


if __name__ == '__main__':
    step1()
