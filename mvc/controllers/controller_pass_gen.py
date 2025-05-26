from ..views.main_menu import print_passwords_table
from ..models.pass_gen_fun import pass_gen


def controller_pass_gen() -> None:
    kwargs_input: dict = {}

    try:
        kwargs_input['length_pass'] = int(input('Введите длину пароля (по умолчанию 8): ').strip())
    except ValueError:
        print('Длина пароля была установлена по умолчанию')

    chars_input = input('Введите символы для генерации (по умолчанию `a-zA-Z-_0-9`): ').strip()

    if chars_input:
        kwargs_input['by_chars'] = chars_input
    else:
        print('Используется набор символов по умолчанию')

    try:
        kwargs_input['amount_result'] = int(input('Введите количество генерируемых паролей (по умолчанию 1): ').strip())
    except ValueError:
        print('Количество генерируемых паролей по умолчанию')

    passwords = pass_gen(**kwargs_input)

    print_passwords_table(passwords)
    input('Нажмите `Enter`, чтобы продолжить...')
