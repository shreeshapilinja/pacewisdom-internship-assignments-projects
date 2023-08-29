def convert_to_positive(coordinates):
    min_value = min(min(x, y) for x, y in coordinates)
    offset = abs(min_value)
    new_coordinates = [(x + offset, y + offset) for x, y in coordinates]
    return new_coordinates

coordinates = [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
print(convert_to_positive(coordinates))