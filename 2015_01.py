from puzzle.input import get_puzzle_input


if __name__ == '__main__':
    floor = 0
    up = '('
    down = ')'
    base_entry_idx = 0

    # Test Data
    # instructions = '(())'
    # instructions = '))((((('
    instructions = get_puzzle_input(2015, 1)

    for idx, i in enumerate(instructions):
        if base_entry_idx == 0 and floor == -1:
            base_entry_idx = idx
        if i == up:
            floor += 1
        elif i == down:
            floor -= 1

    print(f'part 1:\n{floor}')
    print(f'part 2:\n{base_entry_idx}')
