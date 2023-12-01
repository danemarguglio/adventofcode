from pathlib import Path



def file_to_grid(input_file):
    grid = []
    with open(input_file, 'r') as f:
        for line in f:
            grid.append([int(i) for i in line.strip()])
    return grid
         

def is_visible(grid, x, y):
    """Check if a cell is visible from the edge of the grid"""
    value = grid[x][y]

    if x == 0 or x == len(grid)-1 or y == 0 or y == len(grid[0])-1:
        return True

    # right
    for i in range(x+1, len(grid)):
        if grid[i][y] >= value:
            return False
    # left
    for i in range(x-1, -1, -1):
        if grid[i][y] >= value:
            return False
    # up
    for j in range(y+1, len(grid[0])):
        if grid[x][j] >= value:
            return False
    # down
    for j in range(y-1, -1, -1):
        if grid[x][j] >= value:
            return False
    
    return True
    

def get_visible(grid):
    """Count the number of visible cells from the edge of the grid"""
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_visible(grid, i, j):
                count += 1
    return count



if __name__ == "__main__":
    input_file = Path("input/input_8.txt")

    result_1 = 0
    result_2 = 0

    grid = file_to_grid(input_file)
    result_1 = get_visible(grid)
    
    print(f"Result 1: {result_1}")
    print(f"Result 2: {result_2}")


