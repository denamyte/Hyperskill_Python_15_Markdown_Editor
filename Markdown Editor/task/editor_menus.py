import md


class EditorMenus:
    FORMATTERS = ['plain', 'bold', 'italic',
                  'header', 'link', 'inline-code',
                  'ordered-list', 'unordered-list',
                  'new-line']
    SPECIAL_COMMANDS = ['!help', '!done']

    def __init__(self):
        self._command: str = ''
        self._document = md.Document()
        self._header_level = 0
        self._text = ''
        self._rows_number = 0
        self._ordered_list = False

    def print_document(self) -> int:
        print(self._document)
        return 0

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
            case '!done':
                return 0
            case '!help':
                return 1
            case 'header':
                return 2
            case 'bold':
                return 3
            case 'italic':
                return 4
            case 'plain':
                return 5
            case 'inline-code':
                return 6
            case 'new-line':
                return 7
            case 'link':
                return 8
            case 'ordered-list' | 'unordered-list' as lst:
                self._ordered_list = lst == 'ordered-list'
                return 9
        return 0

    @staticmethod
    def print_help() -> int:
        print('''\
Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done''')
        return 0

    def input_header_level(self) -> int:
        raw = input('Level: ')
        try:
            level = int(raw)
            if level < 1 or level > 6:
                return 0
        except ValueError:
            return 0
        self._header_level = level
        return 1

    @staticmethod
    def input_header_level_error() -> int:
        print('The level should be within the range of 1 to 6')
        return 0

    def input_header_text(self) -> int:
        text = input('Text: ')
        self._document.append(md.Header(text, self._header_level))
        return self.print_document()

    def input_bold(self) -> int:
        text = input('Text: ')
        self._document.append(md.Bold(text))
        return self.print_document()

    def input_italic(self) -> int:
        text = input('Text: ')
        self._document.append(md.Italic(text))
        return self.print_document()

    def input_plain(self) -> int:
        text = input('Text: ')
        self._document.append(md.Plain(text))
        return self.print_document()

    def input_inline_code(self) -> int:
        text = input('Text: ')
        self._document.append(md.InlineCode(text))
        return self.print_document()

    def input_new_line(self) -> int:
        self._document.append(md.NewLine())
        return self.print_document()

    def input_link(self) -> int:
        self._document.append(md.Link(input('Label: '), input('URL: ')))
        return self.print_document()

    def input_list_number_of_rows(self) -> int:
        try:
            self._rows_number = int(input('Number of rows: '))
            return 0 if self._rows_number <= 0 else 1
        except ValueError:
            return 0

    @staticmethod
    def input_list_number_of_rows_error() -> int:
        print('The number of rows should be greater than zero')
        return 0

    def input_list_rows(self) -> int:
        rows = [input(f'Row #{i + 1}: ') for i in range(self._rows_number)]
        self._document.append(md.MDList(self._ordered_list, rows))
        return self.print_document()
