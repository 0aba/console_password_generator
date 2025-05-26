from ..models.pass_gen_fun import last_result_is_empty, copy_to_clipboard
import pyperclip


def controller_copy_to_clipboard() -> None:
    if last_result_is_empty():
        print('Список генерируемых паролей пуст')
        input('Нажмите `Enter`, чтобы продолжить...')
        return

    try:
        copy_to_clipboard()
    except pyperclip.PyperclipException as e:
        print(f'Ошибка буфера обмена: {e}')
        input('Нажмите `Enter`, чтобы продолжить...')
        return

    print('Успешно пароли сохранены в буфер обмена')
    input('Нажмите `Enter`, чтобы продолжить...')
