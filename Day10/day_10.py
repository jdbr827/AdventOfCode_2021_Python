from typing import Optional, Generator, Literal, Union, Sequence, Dict

OpenChar = Literal['(', '[', '{', '<']
CloseChar = Literal[')', ']', '}', '>']
NavigationChar = Union[OpenChar, CloseChar]
NavigationLine = Sequence[NavigationChar]

OPEN_TO_CLOSE_DICT: Dict[OpenChar, CloseChar] = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def read_in_lines(filename: str) -> Generator[NavigationLine, None, None]:
    with open(filename) as f:
        while line := f.readline():
            yield line.strip()


def is_line_corrupted(line: NavigationLine) -> Optional[NavigationChar]:
    """
    Determines if the inputted line is corrupted.
    If it is, returns the first illegal character in the line.
    Otherwise, returns None
    :param line:
    :return:
    """
    open_stack = []

    for ch in line:
        if ch in OPEN_TO_CLOSE_DICT.keys():
            open_stack.append(ch)
        else:
            if OPEN_TO_CLOSE_DICT[open_stack.pop()] != ch:
                return ch
    return None


SCORE: Dict[CloseChar, int] = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    None: 0
}


def score_line(line: NavigationLine) -> int:
    """
    returns the score of the first illegal character in line, or 0 if no such char exists
    :param line:
    :return:
    """
    return SCORE[is_line_corrupted(line)]

print(sum([score_line(line) for line in read_in_lines('day_10_small_input.txt')]) == 26397)
print(sum([score_line(line) for line in read_in_lines('day_10_input.txt')]))
