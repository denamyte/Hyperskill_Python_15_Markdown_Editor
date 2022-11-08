
class EditorMenus:
    FORMATTERS = ['plain', 'bold', 'italic',
                  'header', 'link', 'inline-code',
                  'ordered-list', 'unordered-list', 'new-line']
    HELP = '!help'
    DONE = '!done'
    SPECIAL_COMMANDS = [HELP, DONE]

    def __init__(self):
        self._command: str = ''

    def choose_formatter(self) -> int:
        cmd = input('Choose a formatter: ')
        if cmd not in (self.FORMATTERS + self.SPECIAL_COMMANDS):
            return 0
        self._command = cmd
        return 1

    @staticmethod
    def unknown_formatting_type() -> int:
        print('Unknown formatting type or command')
        return 0

    def execute_command(self) -> int:
        match self._command:
            case self.DONE:
                return 0
            case self.HELP:
                print('''\
Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done''')
        return 1
