
def play_bingo():
    with open('day_4_input.txt') as f:
        boards = []
        numbers_called = list(map(int, f.readline().split(",")))
        while (hasNextBoard := f.readline()): # this is the blank line between boards
            board = []
            for row_idx in range(5):
                this_row = f.readline()[:-1].split()
                this_row = list(map(int, this_row))
                board.append(this_row)
            boards.append(board)

play_bingo()
