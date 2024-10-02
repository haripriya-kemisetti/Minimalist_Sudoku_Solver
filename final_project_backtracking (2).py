import random

def printing(arr):
    for row in arr:
        print(*row)

def isSafe(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    startRow, startCol = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def solveSudoku(grid, row, col, count):
    if row == 8 and col == 9:
        count[0] += 1
        return count[0] > 1
    if col == 9:
        row, col = row + 1, 0
    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1, count)
    for num in range(1, 10):
        if isSafe(grid, row, col, num):
            grid[row][col] = num
            if solveSudoku(grid, row, col + 1, count):
                return True
        grid[row][col] = 0
    return False

def truth(grid):
    count = [0]
    solveSudoku(grid, 0, 0, count)
    return count[0]

def makeZeroSystematically(grid):
    while True:
        positions = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(positions)
        temp_grid = [row[:] for row in grid]
        for row, col in positions:
            if temp_grid[row][col] != 0:
                temp = temp_grid[row][col]
                temp_grid[row][col] = 0
                if truth(temp_grid) != 1:
                    temp_grid[row][col] = temp
        if truth(temp_grid) == 1:
            return sum(1 for row in temp_grid for cell in row if cell != 0)
        
#makeZeroSystematically(completed_grid)
#truth(g)
        
grids =[[
    [2,3,4,9,5,6,8,1,7],
    [9,5,7,8,1,4,2,6,3],
    [1,8,6,3,7,2,4,5,9],
    [5,4,9,6,8,1,7,3,2],
    [6,1,8,7,2,3,5,9,4],
    [7,2,3,4,9,5,6,8,1],
    [3,9,2,5,6,7,1,4,8],
    [4,7,5,1,3,8,9,2,6],
    [8,6,1,2,4,9,3,7,5]],
        
    [[4,3,5,2,6,9,7,8,1],
    [6,8,2,5,7,1,4,9,3],
    [1,9,7,8,3,4,5,6,2],
    [8,2,6,1,9,5,3,4,7],
    [3,7,4,6,8,2,9,1,5],
    [9,5,1,7,4,3,6,2,8],
    [5,1,9,3,2,6,8,7,4],
    [2,4,8,9,5,7,1,3,6],
    [7,6,3,4,1,8,2,5,9]],
        
    [[2,6,3,5,7,4,8,9,1],
     [7,1,8,6,9,2,3,4,5],
     [5,9,4,8,1,3,2,7,6],
     [3,4,5,1,6,7,9,8,2],
     [1,2,6,3,8,9,4,5,7],
     [8,7,9,2,4,5,6,1,3],
     [6,3,1,4,5,8,7,2,9],
     [9,8,2,7,3,1,5,6,4],
     [4,5,7,9,2,6,1,3,8]],

    [[2,3,7,8,4,1,5,6,9],
     [1,8,6,7,9,5,2,4,3],
     [5,9,4,3,2,6,7,1,8],
     [3,1,5,6,7,4,8,9,2],
     [4,6,9,5,8,2,1,3,7],
     [7,2,8,1,3,9,4,5,6],
     [6,4,2,9,1,8,3,7,5],
     [8,5,3,4,6,7,9,2,1],
     [9,7,1,2,5,3,6,8,4]]]

gri = [[2,3,7,8,4,1,5,6,9],
     [1,8,6,7,9,5,2,4,3],
     [5,9,4,3,2,6,7,1,8],
     [3,1,5,6,7,4,8,9,2],
     [4,6,9,5,8,2,1,3,7],
     [7,2,8,1,3,9,4,5,6],
     [6,4,2,9,1,8,3,7,5],
     [8,5,3,4,6,7,9,2,1],
     [9,7,1,2,5,3,6,8,4]]

for g in grids:
    minimum = float('inf')
    for i in range(100):
        num_clues = makeZeroSystematically(g)
        minimum = min(minimum, num_clues)
    print(minimum)


