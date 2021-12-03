from typing import List, Union, Literal

BitInt = Literal[0, 1]

# TODO: is there a way to enforce strings over an alphabet?
BitStr = str  # But meant to represent ONLY strings over the alphabet of ['0', '1']


def compute_gamma_rate_binary(input_filename: str, n: int) -> List[BitInt]:
    """
    :param input_filename: file of n-digit binary numbers on each line
    :return: the gamma rate as an n-digit binary number list
    """
    count_scoreboard = [0 for _ in range(n)]
    with open(input_filename) as file:

        #  INVAR @ iteration i: count_scoreboard[j] =
        #   number of 1s in position j of first i binary values
        #   - number of 0s in position j for first i binary values
        while this_bin := file.readline():
            for j in range(n):
                if this_bin[j] == '1':
                    count_scoreboard[j] += 1
                else:
                    count_scoreboard[j] -= 1
    return [int(final_score > 0) for final_score in count_scoreboard]  # type: ignore # Literal Subtype


def compute_power_consumption(input_filename: str, n: int):
    gamma_rate_binary: List[BitInt] = compute_gamma_rate_binary(input_filename, n)
    epsilon_rate_binary: List[BitInt] = [1 - gamma for gamma in gamma_rate_binary]  # type: ignore # Literal Subtype

    gamma_rate_decimal: int = convert_binary_to_decimal(gamma_rate_binary)
    epsilon_rate_decimal: int = convert_binary_to_decimal(epsilon_rate_binary)
    return gamma_rate_decimal * epsilon_rate_decimal


def convert_binary_to_decimal(binary: Union[List[BitInt], BitStr]) -> int:
    """
    Converts a binary of one of two forms into its decimal equivalent
    """
    decimal = 0
    for j in range(1, len(binary) + 1):
        decimal += int(binary[-j]) * 2 ** (j - 1)
    return decimal


print(compute_power_consumption('day_3_small_input.txt', 5) == 198)
print(compute_power_consumption('day_3_input.txt', 12) == 2648450)
