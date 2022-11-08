from state_machine_factory import StateMachineFactory, State
from state_machine import StateMachineRunner
from editor_menus import EditorMenus


menus = EditorMenus()
state_dict = StateMachineFactory(menus).get_state_dict()
smr = StateMachineRunner(state_dict, State.CHOOSE_FORMATTER.name)

smr.run()
