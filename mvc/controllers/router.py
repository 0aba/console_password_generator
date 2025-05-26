__all__ = ['start_router_loop']

from ..views.view_utils import clear_terminal
from .controller_pass_gen import controller_pass_gen
from .types import *


_loop_running: bool = True

def _stop_loop():
    global _loop_running
    _loop_running = False

_routers: routers_t = {
    'exit': (_stop_loop, 'Завершение работы приложения',),
    'pass_gen': (controller_pass_gen, 'Генерация паролей',),
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
