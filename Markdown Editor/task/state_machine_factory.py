from enum import Enum, auto
from typing import Dict

from state_transition import StateTransition
from editor_menus import EditorMenus


class State(Enum):
    CHOOSE_FORMATTER = auto()
    UNKNOWN_FORMATTING_TYPE = auto()
    EXECUTE_COMMAND = auto()

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
                             1: State.CHOOSE_FORMATTER.name},
                            self._menus.execute_command),

            StateTransition(State.EXIT.name,
                            {0: ''},
                            lambda: 0)

        ]
        return {st.state_name: st for st in trans_list}

