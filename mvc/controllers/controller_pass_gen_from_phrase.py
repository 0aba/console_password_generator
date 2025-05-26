from ..models.pass_gen_fun import pass_gen_from_phrase
from ..views.main_menu import print_passwords_table

def controller_pass_gen_from_phrase() -> None:
    kwargs_input: dict = {}

    kwargs_input['phrase'] = input('Введите фразу: ').strip()

    try:
        kwargs_input['amount_word'] = int(input('Введите из скольких слов будет состоять пароль (по умолчанию 6): ').strip())
    except ValueError:
        print('Количество слов в пароле по умолчанию')

    try:
        kwargs_input['amount_result'] = int(input('Введите количество генерируемых паролей (по умолчанию 1): ').strip())
    except ValueError:
        print('Количество генерируемых паролей по умолчанию')

    try:
        kwargs_input['separator'] = int(input('Введите символ разделения слов (по умолчанию пробел): ').strip())
    except ValueError:
        print('Символ разделения слов по умолчанию')

    passwords = pass_gen_from_phrase(**kwargs_input)

    print_passwords_table(passwords)
    input('Нажмите `Enter`, чтобы продолжить...')
