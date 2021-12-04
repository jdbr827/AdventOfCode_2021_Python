
def play_bingo(filename):
    (numbers_called, boards) = read_in_boards(filename)
    found = []
    for b in range(len(boards)):
        found.append([[0 for j in range(5)] for i in range(5)])
    for number in numbers_called:
        for b in range(len(boards)):
            number_board = boards[b]
            found_board = found[b]
            for i in range(5):
                for j in range(5):
                    if number_board[i][j] == number:
                        found_row = found_board[i]
                        found_val = found_row[j]
                        found_board[i][j] = 1
                        if all([found_board[i][k] == 1 for k in range(5)]) or all([found_board[k][j] == 1 for k in range(5)]):
                            return number * sum([number_board[k][l] for k in range(5) for l in range(5) if not found_board[k][l]])




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
