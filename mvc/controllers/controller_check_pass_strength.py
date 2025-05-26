from ..models.pass_utils import MAX_SCORE_PASS, check_pass_strength


def controller_check_pass_strength() -> None:
    password = input('Введите пароль: ').strip()

    print(f'Оценка пароля: {check_pass_strength(password)}/{MAX_SCORE_PASS} баллов')
    input('Нажмите `Enter`, чтобы продолжить...')
