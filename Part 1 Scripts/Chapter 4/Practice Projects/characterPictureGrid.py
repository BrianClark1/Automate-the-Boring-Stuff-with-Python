grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# The grid has 0's in a pattern that makes a heart but is tilted 90 degrees
#Really dont under

for j in range(len(grid[0])): # 0 - 5  #Picks that value
 #j = 0
    for i in range(len(grid)): #0 - 8 Goes through the same value of each list Runs through each value before moving on to the next column
        print(grid[i][j],end='')
    print('')

print(len(grid))
print(len(grid[0]))
