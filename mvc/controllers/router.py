__all__ = ['start_router_loop']

from ..controllers.controller_copy_to_clipboard import controller_copy_to_clipboard
from ..views.view_utils import clear_terminal
from .types import *


_loop_running: bool = True

def _stop_loop():
    global _loop_running
    _loop_running = False

_routers: routers_t = {
    'exit': (_stop_loop, 'Завершение работы приложения',),
    'copy_to_clipboard': (controller_copy_to_clipboard, 'Сохранить последнюю генерацию паролей в буфер обмена'),
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
