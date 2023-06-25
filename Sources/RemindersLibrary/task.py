import random
from dataclasses import dataclass, field
from enum import Enum


class Zone(Enum):
    VEGETABLE = 1
    FRUIT = 2
    DAIRY = 3
    MEAT = 4
    FISH = 5


@dataclass
class Item:
    name: str
    sensitive: bool
    producer: bool
    count: int = 1

@dataclass
class Cell:
    capacity: int
    items: list[Item] = field(default_factory=list)


def has_sensitive(cell):
    return any(i.sensitive for i in cell.items)

def get_producer(cell):
    for i in cell.items:
        if i.producer:
            return i
    return None

def can_place_item(grid, row, col, item):
    cell = grid[row][col]
    enough_capacity = cell.capacity > 0
    if not item.sensitive and not item.producer:
        return enough_capacity

    cells = [cell]
    if 0 < col:
        cells.append(grid[row][col-1])
    if (col + 1) < len(grid[row]):
        cells.append(grid[row][col+1])

    for n in cells:
        producer = get_producer(n)
        if producer and item.name == producer.name:
            continue
        
        if item.sensitive and producer:
            return False
        
        if item.producer and has_sensitive(n):
            return False        
    
    return enough_capacity
    

# def fill_grid(grid, items):
#     # TODO: write an implementation which maximises number of stored items
#     pass

def fill_grid(grid, items):
    # Sort items by descending count
    items.sort(key=lambda i: -i.count)

    # Try to place each item in the grid
    for item in items:
        placed = False
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if can_place_item(grid, row, col, item):
                    grid[row][col].items.append(item)
                    grid[row][col].capacity -= 1
                    item.count -= 1
                    placed = True
                    break
            if placed:
                break
        if not placed and item.count > 0:
            print(f"Could not place all items of type {item.name}")
            
    return grid

m = 3
n = 5
grid = [[Cell(capacity=random.randint(1,9)) for _ in range(n)] for _ in range(m)]


items = [
    Item('A', True, False),
    Item('B', True, True),
    Item('C', False, True, 2),
    Item('C', False, False, 3),
]

fill_grid(grid, items)

for row in grid:
    print(row)
    print('')

# def can_place_object(grid, row, col, obj):
#     if not obj['sensitive'] and not obj['producer']:
#         return True
    

#     for i in range(max(0, row-1), min(len(grid), row+2)):
#         for j in range(max(0, col-1), min(len(grid[0]), col+2)):
#             if i == row and j == col:
#                 continue
#             if 'producer' in grid[i][j] and grid[i][j]['producer'] == 1:
#                 return False
        
#     return True

# def fill_matrix(grid, objects):
#     for obj in sorted(objects, key=lambda x: -x['count']):
#         for row in range(len(grid)):
#             for col in range(len(grid[0])):
#                 if grid[row][col] is None and can_place_object(grid, row, col, obj):
#                     grid[row][col] = obj
#                     obj['count'] -= 1
#                     if obj['count'] == 0:
#                         break
#             if obj['count'] == 0:
#                 break

# m = 2
# n = 5
# grid = [[None for _ in range(n)] for _ in range(m)]
# objects = [
#     {'name': 'A', 'sensitive': 0, 'producer': 0, 'count': 5},
#     {'name': 'B', 'sensitive': 1, 'producer': 0, 'count': 3},
#     {'name': 'C', 'sensitive': 0, 'producer': 1, 'count': 2},
#     {'name': 'D', 'sensitive': 0, 'producer': 0, 'count': 1},
#     {'name': 'E', 'sensitive': 1, 'producer': 0, 'count': 2},
#     {'name': 'F', 'sensitive': 0, 'producer': 0, 'count': 3},
# ]
# fill_matrix(grid, objects)

# for row in grid:
#     print([obj['name'] if obj is not None else ' ' for obj in row])























# def fill_cell(row, col, objects, grid, result):
#     m, n = len(grid), len(grid[0])
#     if row == m:
#         result[:] = [row[:] for row in grid] # make a copy of the current grid
#         return True
#     for obj in objects:
#         if obj['sensitive'] == 0 or not any([result[row][col-1]['producer'] for row in range(m) if col > 0]):
#             # check if the object satisfies the constraints
#             grid[row][col] = obj
#             if fill_cell(row + (col + 1) // n, (col + 1) % n, objects, grid, result):
#                 return True
#             grid[row][col] = 0 # backtrack
#     return False

# # example usage
# grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# objects = [{'name': 'obj1', 'sensitive': 0, 'producer': 1},
#            {'name': 'obj2', 'sensitive': 1, 'producer': 0},
#            {'name': 'obj3', 'sensitive': 0, 'producer': 0}]
# result = [[0] * len(grid[0]) for _ in range(len(grid))]
# fill_cell(0, 0, objects, grid, result)
# print(result)
