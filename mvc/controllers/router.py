__all__ = ['start_router_loop']

from .controller_pass_gen_from_phrase import controller_pass_gen_from_phrase
from .controller_check_pass_strength import controller_check_pass_strength
from .controller_copy_to_clipboard import controller_copy_to_clipboard
from .controller_shuffle_pass import controller_shuffle_pass
from .controller_pass_gen import controller_pass_gen
from ..views.view_utils import clear_terminal
from .types import *


_loop_running: bool = True

def _stop_loop():
    global _loop_running
    _loop_running = False

_routers: routers_t = {
    'exit': (_stop_loop, 'Завершение работы приложения',),
    'pass_gen': (controller_pass_gen, 'Генерация паролей',),
    'pass_gen_from_phrase': (controller_pass_gen_from_phrase, 'Сгенерировать пароль на основе фразы',),
    'copy_to_clipboard': (controller_copy_to_clipboard, 'Сохранить последнюю генерацию паролей в буфер обмена'),
    'check_pass_strength': (controller_check_pass_strength, 'Проверить пароль на надежность'),
    'shuffle_pass': (controller_shuffle_pass, 'Перемешать пароль'),
}

def start_router_loop():
    from ..views.main_menu import print_main_menu
    global _loop_running, _routers

    while _loop_running:
        clear_terminal()
        print_main_menu(_routers)
        command = input('> ').strip()
        if data := _routers.get(command):
            data[0]()
        else:
            input('Команда не найдена, нажмите `Enter`, чтобы продолжить...')
