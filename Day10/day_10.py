from abc import abstractmethod, ABC
from typing import Optional, Generator, Literal, Union, Sequence, Dict, Tuple

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

CORRUPTED_SCORE: Dict[CloseChar, int] = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

AUTOCOMPLETE_SCORE: Dict[CloseChar, int] = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def read_in_lines(filename: str) -> Generator[NavigationLine, None, None]:
    with open(filename) as f:
        while line := f.readline():
            yield line.strip()


def score_line(line: NavigationLine) -> Tuple[bool, int]:
    """
    Determines the score of the line.
    :param line:
    :return:
        - bool is_corrupted if the line is corrupted or just incomplete
        - int score of the line based on the scoring rules for that line
    """
    open_stack = []

    for ch in line:
        if ch in OPEN_TO_CLOSE_DICT.keys():
            open_stack.append(ch)
        else:
            if OPEN_TO_CLOSE_DICT[open_stack.pop()] != ch:
                return True, CORRUPTED_SCORE[ch]
    # line is now incomplete
    score = 0
    while open_stack:
        score *= 5
        score += AUTOCOMPLETE_SCORE[OPEN_TO_CLOSE_DICT[open_stack.pop()]]
    return False, score


def collect_appropriate_scores(filename: str, desired_is_corrupted: bool):
    """
    returns the scores of all lines in the provided file that are corrupted (if desired_is_corrupted is True) or that
    are NOT corrupted (if is_corrupted is False)
    :return:
    """
    scores = []
    for line in read_in_lines(filename):
        (line_is_corrupted, score) = score_line(line)
        if desired_is_corrupted == line_is_corrupted:
            scores.append(score)
    return scores


def file_autocomplete_score(filename):
    scores = collect_appropriate_scores(filename, False)
    scores.sort()
    return scores[int(len(scores) / 2)]


def file_corrupted_score(filename):
    scores = collect_appropriate_scores(filename, True)
    return sum(scores)


print(file_corrupted_score('day_10_small_input.txt') == 26397)
print(file_corrupted_score('day_10_input.txt') == 166191)

print(file_autocomplete_score('day_10_small_input.txt') == 288957)
print(file_autocomplete_score('day_10_input.txt') == 1152088313)
