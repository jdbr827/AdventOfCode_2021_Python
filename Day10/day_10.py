from typing import Optional, Generator


def read_in_lines(filename: str) -> Generator[str, None, None]:
    with open(filename) as f:
        while line := f.readline():
            yield line.strip()


def is_line_corrupted(line: str) -> Optional[str]:
    """
    Determines if the inputted line is corrupted.
    If it is, returns the first illegal character in the line.
    Otherwise, returns None
    :param line:
    :return:
    """
    return None


line_generator: Generator[str, None, None] = read_in_lines('day_10_small_input.txt')
for line in line_generator:
    print(line)
