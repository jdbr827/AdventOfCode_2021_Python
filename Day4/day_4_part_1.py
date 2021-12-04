
def play_bingo(filename):
    (numbers_called, boards) = read_in_boards(filename)
    found = []
    for b in range(len(boards)):
        found.append([[False for _ in range(5)] for _ in range(5)])
    for number in numbers_called:
        for b in range(len(boards)):
            number_board = boards[b]
            found_board = found[b]
            for i in range(5):
                for j in range(5):
                    if number_board[i][j] == number:
                        found_board[i][j] = True
                        if all([found_board[i][k] for k in range(5)]) or all([found_board[k][j] for k in range(5)]):
                            return number * sum([number_board[k][l] for k in range(5) for l in range(5) if not found_board[k][l]])


def play_bingo_to_lose(filename):
    (numbers_called, boards) = read_in_boards(filename)
    found = []
    for b in range(len(boards)):
        found.append([[0 for j in range(5)] for i in range(5)])
    won = [-1 for _ in range(len(boards))]
    win_idx = 0
    numbers_idx = 0
    while -1 in won:
        number = numbers_called[numbers_idx]
        numbers_idx += 1
        for b in range(len(boards)):
            if won[b] == -1:
                number_board = boards[b]
                found_board = found[b]
                for i in range(5):
                    for j in range(5):
                        if number_board[i][j] == number:
                            found_board[i][j] = 1
                            if all([found_board[i][k] == 1 for k in range(5)]) or all(
                                    [found_board[k][j] == 1 for k in range(5)]):
                                won[b] = win_idx
                                win_idx += 1
    winning_idx = won.index(win_idx - 1)
    winning_board = boards[won.index(win_idx - 1)]
    return number * sum([winning_board[k][l] for k in range(5) for l in range(5) if not found[winning_idx][k][l]])


def read_in_boards(filename):
    with open(filename) as f:
        boards = []
        numbers_called = list(map(int, f.readline().split(",")))
        while (f.readline()):  # this is the blank line between boards
            board = []
            for row_idx in range(5):
                this_row = f.readline().split()
                this_row = list(map(int, this_row))
                board.append(this_row)
            boards.append(board)
        return numbers_called, boards


print(play_bingo('day_4_small_input.txt') == 4512)
print(play_bingo('day_4_input.txt') == 41503)
print(play_bingo_to_lose('day_4_small_input.txt') == 1924)
print(play_bingo_to_lose('day_4_input.txt'))
