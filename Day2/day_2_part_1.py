

def compute_destination(input_filename: str):
    horizontal = 0
    depth = 0
    with open(input_filename) as file:
        while direction:=file.readline():
            (keyword, amount) = direction.split(" ")
            amount = int(amount)
            if keyword == 'forward':
                horizontal += amount
            elif keyword == 'down':
                depth += amount
            elif keyword == 'up':
                depth -= amount
        return (horizontal, depth)


print(compute_destination('day_2_small_input.txt') == (15, 10))

(horiz, dep) = compute_destination('day_2_input.txt')
print(horiz * dep)