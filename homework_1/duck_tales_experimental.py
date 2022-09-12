def boolean_question_on_step(options_map):
    option = ''
    while option not in options_map:
        print('Выберите: {}/{}'.format(*options_map))
        option = input().lower()
    return options_map[option]


def step1(decisions_state):
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар.\n'
        'Взять ей зонтик? ☂️'
    )
    choice_result = boolean_question_on_step({'да': True, 'нет': False})
    decisions_state['have_umbrella'] = choice_result
    return step2(decisions_state)


def step2(decisions_state):
    print('Уточка топает к бару... Поднимает свой любопытный клюв к небу.')
    if decisions_state['have_umbrella']:
        print(
            'И видит - собрались тучи.. Но при уточке оказался удачно взятый зонтик.\n'
            'Порадуется ли уточка?'
        )
        choice_result = boolean_question_on_step({'да': True, 'нет': False})
        decisions_state['have_happy_vibe'] = choice_result
    else:
        print(
            'И видит - как назло собрались тучи.. Зонтик бы пригодился..\n'
            'Расcтроится ли уточка?'
        )
        choice_result = boolean_question_on_step({'да': True, 'нет': False})
        decisions_state['have_upset_vibe'] = choice_result
    return step3(decisions_state)


def step3(decisions_state):
    print('Совсем скоро пошел дождь. ')
    if decisions_state['have_umbrella']:
        print('Утка удачно решила взять с собой зонт. Дошла до бара совсем сухонькой.\n')
        if decisions_state['have_happy_vibe']:
            print(
                'В этот день такое маленькое, почти случайное, но удачное стечение обстоятельств '
                'здорово подняло уточке настроение.\n'
                'На радость себе и назло дождику наша уточка заказала себе тропический коктейль 🍹'
            )
        else:
            print(
                'Это был регулярный поход в бар, уточка по традиции заказала себе бокал пшенички 🍺. '
            )
    else:
        print('Утка не подумала взять зонтик. Конечно же она промокла.\n')
        if decisions_state['have_upset_vibe']:
            print(
                'Мало того, что промокла, так еще и сильно раздосадовалась..\n'
                'По такому поводу наша уточка заказала себе виски со льдом и угрюмо потягивала его из стакана 🥃..'
            )
        else:
            print(
                'Ну промокла и промокла, че бухтеть то.\n'
                'Тем более, что совсем скоро её перышки прогреет добротный кубинский ром 🥃.'
            )


if __name__ == '__main__':
    decisions_state_current = {}
    step1(decisions_state_current)
