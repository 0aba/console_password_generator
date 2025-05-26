from typing import Callable


type command_t            = str
type about_t              = str
type handler_controller_t = Callable[[], None]
type data_command_t       = tuple[handler_controller_t, about_t]
type routers_t            = dict[command_t, data_command_t]
