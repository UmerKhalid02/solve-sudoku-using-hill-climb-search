import numpy as np
import copy

#4x4 grid
def makeGrid():
    grid = []

    # initializing grid
    for i in range(1,5):
        row = []
        for j in range(1,5):
            row.append(j)
        grid.append(row)
    
    grid = np.array(grid)
    return grid


def conflictsInBox(grid, rstart, rend, cstart, cend):
    sum = 0
    for i in range(rstart, rend):
        for j in range(cstart, cend):
            if(i == rstart and j == cstart):
                if(grid[i][j] == grid[i][j+1]):
                    sum+=1
                if(grid[i][j] == grid[i+1][j]):
                    sum+=1
                if(grid[i][j] == grid[i+1][j+1]):
                    sum+=1
            elif(i == rstart and j == cstart + 1):
                if(grid[i][j] == grid[i+1][j]):
                    sum+=1
                if(grid[i][j] == grid[i+1][j-1]):
                    sum+=1
            elif(i == rstart+1 and j == cstart):
                if(grid[i][j] == grid[i][j+1]):
                    sum+=1
    return sum


def objectiveFunction(grid):
    sum = 0

    #conflicts in each column
    for col in range(4):
        for row in range(4):
            if(row < 3):
                for i in range(row+1, 4):
                    if(grid[row][col] == grid[i][col]):
                        sum += 1

    #conflicts in each row
    for row in range(4):
        for col in range(4):
            if(col < 3):
                for i in range(col+1, 4):
                    if(grid[row][col] == grid[row][i]):
                        sum += 1
    
    #conflicts in each box (4 boxes)
    sum += conflictsInBox(grid, 0, 2, 0, 2) #box 1
    sum += conflictsInBox(grid, 0, 2, 2, 4) #box 2
    sum += conflictsInBox(grid, 2, 4, 0, 2) #box 3
    sum += conflictsInBox(grid, 2, 4, 2, 4) #box 4
    
    return sum


def NextPossibleState(current_grid):
    minCost = 1000
    nextState = []

    for row in range(4):
        for col in range(4):
            if(col < 3):
                for i in range(col+1,4):
                    state = copy.copy(current_grid)
                    temp = state[row][col]
                    state[row][col] = state[row][i]
                    state[row][i] = temp

                    cost = objectiveFunction(state)
                    if(minCost > cost):
                        minCost = copy.copy(cost)
                        nextState = copy.copy(state)
    return minCost, nextState

def Solution(grid):

    current = copy.copy(grid)
    cost = 100

    while(cost != 0):
        cost, current = NextPossibleState(current)
        print("\n", current)
    
    return current


def main():
    grid = makeGrid()
    print("Grid: \n", grid)
    result = Solution(grid)

    print("\n\nSolution: \n", result)

main()