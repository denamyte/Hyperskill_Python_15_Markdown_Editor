from abc import ABC, abstractmethod
from typing import List


class MDBase(ABC):
    @abstractmethod
    def render(self) -> str:
        ...


class Plain(MDBase):
    def __init__(self, text: str):
        self._text = text

    def render(self) -> str:
        return self._text


class InlineModifier(Plain):
    F_STR = '{0}{1}{0}'

    def __init__(self, text: str, modifier: str):
        super().__init__(text)
        self._modifier = modifier

    def render(self) -> str:
        return self.F_STR.format(self._modifier, self._text)


class Bold(InlineModifier):
    def __init__(self, text: str):
        super().__init__(text, '**')


class Italic(InlineModifier):
    def __init__(self, text: str):
        super().__init__(text, '*')


class InlineCode(InlineModifier):
    def __init__(self, text: str):
        super().__init__(text, '`')


class Header(Plain):
    F_STR = '{} {}\n'

    def __init__(self, text: str, level: int):
        super().__init__(self.F_STR.format('#' * level, text))
        self._level = level


class NewLine(Plain):
    def __init__(self):
        super().__init__('\n')


class Link(MDBase):
    F_STR = '[{label}]({url})'

    def __init__(self, label: str, url: str):
        self._label = label
        self._url = url

    def render(self) -> str:
        return self.F_STR.format(label=self._label, url=self._url)


class MDList(MDBase):
    def __init__(self, ordered: bool, rows: List[str]):
        self._ordered = ordered
        self._rows = rows[:]

    def render(self) -> str:
        rows_gen = (f'{i + 1}. {self._rows[i]}' for i in range(len(self._rows)))\
            if self._ordered\
            else (f'* {self._rows[i]}' for i in range(len(self._rows)))
        return '\n'.join(rows_gen) + '\n'


class Document(MDBase):
    def __init__(self):
        self._parts: List[MDBase] = []

    def append(self, md: MDBase):
        match md:
            case Header():
                if len(self._parts):
                    self._parts.append(NewLine())
                self._parts.append(md)
            case _:
                self._parts.append(md)

    def render(self) -> str:
        return ''.join(p.render() for p in self._parts)

    def __str__(self):
        return self.render()
