def compute_destination_2(input_filename: str):
    aim = 0
    horizontal = 0
    depth = 0
    with open(input_filename) as file:
        while direction := file.readline():
            (keyword, amount) = direction.split(" ")
            amount = int(amount)
            if keyword == 'forward':
                horizontal += amount
                depth += amount * aim
            elif keyword == 'down':
                aim += amount
            elif keyword == 'up':
                aim -= amount
        return (horizontal, depth)


print(compute_destination_2('day_2_small_input.txt') == (15, 60))

(horiz, dep) = compute_destination_2('day_2_input.txt')
print(horiz * dep) # 1599311480
