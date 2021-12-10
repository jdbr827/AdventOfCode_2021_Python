from typing import Optional, Generator, Literal, Union, Sequence

OpenChar = Literal['(', '[', '{', '<']
CloseChar = Literal[')', ']', '}', '>']
NavigationLine = Sequence[Union[OpenChar, CloseChar]]


def read_in_lines(filename: str) -> Generator[NavigationLine, None, None]:
    with open(filename) as f:
        while line := f.readline():
            yield line.strip()


def is_line_corrupted(line: NavigationLine) -> Optional[str]:
    """
    Determines if the inputted line is corrupted.
    If it is, returns the first illegal character in the line.
    Otherwise, returns None
    :param line:
    :return:
    """
    return None


line_generator: Generator[NavigationLine, None, None] = read_in_lines('day_10_small_input.txt')
for line in line_generator:
    print(line)
