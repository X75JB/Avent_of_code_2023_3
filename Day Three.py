def read_engine_schematic(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]

def is_valid_coordinate(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def get_adjacent_numbers(engine_schematic, x, y):
    rows, cols = len(engine_schematic), len(engine_schematic[0])
    directions = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2)]

    adjacent_numbers = []
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid_coordinate(new_x, new_y, rows, cols):
            current_char = engine_schematic[new_x][new_y]
            if current_char.isdigit():
                adjacent_numbers.append(int(current_char))

    return adjacent_numbers

def sum_of_part_numbers(engine_schematic):
    part_numbers_sum = 0

    for i in range(len(engine_schematic)):
        for j in range(len(engine_schematic[i])):
            current_char = engine_schematic[i][j]
            if current_char.isdigit():
                adjacent_numbers = get_adjacent_numbers(engine_schematic, i, j)
                part_numbers_sum += sum(adjacent_numbers)

    return part_numbers_sum

if __name__ == "__main__":
    file_path = "values.txt"  # Replace with the actual file path
    engine_schematic = read_engine_schematic(file_path)
    result = sum_of_part_numbers(engine_schematic)
    print("Sum of all part numbers:", result)
