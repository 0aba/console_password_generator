from ..models.pass_gen_fun import shuffle_pass
from ..views.main_menu import print_passwords_table


def controller_shuffle_pass() -> None:
    password = input('Введите пароль: ').strip()
    aggressive = input('Усиленное перемешивание (y/n) (по умолчанию n): ').strip() == 'y'

    print_passwords_table([shuffle_pass(password, aggressive=aggressive)])
    input('Нажмите `Enter`, чтобы продолжить...')
