__all__ = ['print_main_menu', 'print_passwords_table']

from ..controllers.types import *
from ..models.types import *
from textwrap import fill


WIDTH: int = 100

def print_main_menu(routers: routers_t) -> None:
    size_colum_command: int = int(WIDTH * 0.25) - 1
    size_colum_about: int = int(WIDTH * 0.75) - 2

    print(f'╔{'═' * (WIDTH - 2)}╗')
    print(f'║{'ГЛАВНОЕ МЕНЮ':^{WIDTH - 2}}║')
    print(f'╠{'═' * size_colum_command}╦{'═' * size_colum_about}╣')
    print(f'║{'КОМАНДА':^{size_colum_command}}║{'ОПИСАНИЕ':^{size_colum_about}}║')
    print(f'╠{"═" * size_colum_command}╬{"═" * size_colum_about}╣')

    for command, (_, about) in routers.items():
        cmd_lines = fill(command, width=size_colum_command).split('\n')
        about_lines = fill(about, width=size_colum_about).split('\n')
        max_lines: int = max(len(cmd_lines), len(about_lines))

        for i in range(max_lines):
            cmd_part = cmd_lines[i] if i < len(cmd_lines) else ''
            about_part = about_lines[i] if i < len(about_lines) else ''
            print(f'║{cmd_part:{size_colum_command}}║{about_part:{size_colum_about}}║')

        if command != list(routers.keys())[-1]:
            print(f'╠{'═' * size_colum_command}╬{'═' * size_colum_about}╣')

    print(f'╚{'═' * size_colum_command}╩{'═' * size_colum_about}╝')

def _print_exist_passwords_table(passwords: passwords_t) -> None:
    size_column_number: int = int(WIDTH * 0.1)
    size_column_password: int = int(WIDTH * 0.9) - 3

    print(f'╔{"═" * (WIDTH - 2)}╗')
    print(f'║{"СГЕНЕРИРОВАННЫЕ ПАРОЛИ":^{WIDTH - 2}}║')
    print(f'╠{"═" * size_column_number}╦{"═" * size_column_password}╣')
    print(f'║{"№":^{size_column_number}}║{"ПАРОЛЬ":^{size_column_password}}║')
    print(f'╠{"═" * size_column_number}╬{"═" * size_column_password}╣')

    for i, password in enumerate(passwords, 1):
        num_lines = fill(str(i), width=size_column_number).split('\n')
        pass_lines = fill(password, width=size_column_password, break_on_hyphens=False).split('\n')
        max_lines: int = max(len(num_lines), len(pass_lines))

        for line in range(max_lines):
            num_part = num_lines[line] if line < len(num_lines) else ''
            pass_part = pass_lines[line] if line < len(pass_lines) else ''
            print(f'║{num_part:^{size_column_number}}║{pass_part:<{size_column_password}}║')

        if i != len(passwords):
            print(f'╠{"═" * size_column_number}╬{"═" * size_column_password}╣')

    print(f'╚{"═" * size_column_number}╩{"═" * size_column_password}╝')

def _print_empty_passwords_table() -> None:
    print('''
╔══════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                             ПАРОЛЕЙ НЕТ                                          ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════╝
║
║　　　　 ／\\____ / フ
║　　　　| 　_　 _ l  Котик не смог отобразить пароли,
║ 　　　／` ミ＿x ノ  потому что он получил пустой список!
║　 　 /　　　　 |    🔒
║　　 /　 ヽ　　 ﾉ    (P.S котику еще не нравиться граница справа по этому, я ее снес) ))
║ 　 │　　 |　|　| 
║／￣|　　 |　|　|
║| (￣ヽ＿_ヽ_)__)
║＼二つ
╚══════════════════════════════════════════════════════════════════════════════════════════════════╡
'''
    )

def print_passwords_table(passwords: passwords_t) -> None:
    if len(passwords) == 0: _print_empty_passwords_table()
    else: _print_exist_passwords_table(passwords)
