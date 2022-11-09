from enum import Enum, auto
from typing import Dict

from state_transition import StateTransition
from editor_menus import EditorMenus


class State(Enum):
    CHOOSE_FORMATTER = auto()
    UNKNOWN_FORMATTING_TYPE = auto()
    EXECUTE_COMMAND = auto()
    PRINT_HELP = auto()
    INPUT_HEADER_LEVEL = auto()
    INPUT_HEADER_LEVEL_ERROR = auto()
    INPUT_HEADER_TEXT = auto()
    INPUT_BOLD = auto()
    INPUT_ITALIC = auto()
    INPUT_PLAIN = auto()
    INPUT_INLINE_CODE = auto()
    INPUT_NEW_LINE = auto()
    INPUT_LINK = auto()

    EXIT = auto()


class StateMachineFactory:

    def __init__(self, menus: EditorMenus):
        self._menus = menus

    def get_state_dict(self) -> Dict[str, StateTransition]:
        trans_list = [
            StateTransition(State.CHOOSE_FORMATTER.name,
                            {0: State.UNKNOWN_FORMATTING_TYPE.name,
                             1: State.EXECUTE_COMMAND.name},
                            self._menus.choose_formatter),

            StateTransition(State.UNKNOWN_FORMATTING_TYPE.name,
                            {0: State.CHOOSE_FORMATTER.name},
                            self._menus.unknown_formatting_type),

            StateTransition(State.EXECUTE_COMMAND.name,
                            {0: State.EXIT.name,
                             1: State.PRINT_HELP.name,
                             2: State.INPUT_HEADER_LEVEL.name,
                             3: State.INPUT_BOLD.name,
                             4: State.INPUT_ITALIC.name,
                             5: State.INPUT_PLAIN.name,
                             6: State.INPUT_INLINE_CODE.name,
                             7: State.INPUT_NEW_LINE.name,
                             8: State.INPUT_LINK.name,
                             },
                            self._menus.execute_command),

            StateTransition(State.PRINT_HELP.name,
                            {0: State.CHOOSE_FORMATTER.name},
                            self._menus.print_help),

            StateTransition(State.INPUT_HEADER_LEVEL.name,
                            {0: State.INPUT_HEADER_LEVEL_ERROR.name,
                             1: State.INPUT_HEADER_TEXT.name},
                            self._menus.input_header_level),

            StateTransition(State.INPUT_HEADER_LEVEL_ERROR.name,
                            {0: State.INPUT_HEADER_LEVEL.name},
                            self._menus.input_header_level_error),

            StateTransition(State.INPUT_HEADER_TEXT.name,
                            {0: State.CHOOSE_FORMATTER.name},
                            self._menus.input_header_text),

            StateTransition(State.INPUT_BOLD.name,
                            {0: State.CHOOSE_FORMATTER.name},
                            self._menus.input_bold),

            StateTransition(State.INPUT_ITALIC.name,
                            {0: State.CHOOSE_FORMATTER.name},
                            self._menus.input_italic),

            StateTransition(State.INPUT_PLAIN.name,
                            {0: State.CHOOSE_FORMATTER.name},
                            self._menus.input_plain),

            StateTransition(State.INPUT_INLINE_CODE.name,
                            {0: State.CHOOSE_FORMATTER.name},
                            self._menus.input_inline_code),

            StateTransition(State.INPUT_NEW_LINE.name,
                            {0: State.CHOOSE_FORMATTER.name},
                            self._menus.input_new_line),

            StateTransition(State.INPUT_LINK.name,
                            {0: State.CHOOSE_FORMATTER.name},
                            self._menus.input_link),

            StateTransition(State.EXIT.name,
                            {0: ''},
                            lambda: 0)

        ]
        return {st.state_name: st for st in trans_list}

