
def format_input(filename):
    with open(filename) as file:
        lines = file.readlines()
        return [int(line.rstrip()) for line in lines]