def create_grid(grid):

    

    for i in range (4):

        grid.append([])

        for j in range (4):

            grid[i].append(0)

    

   

def print_grid (grid):

    

    for m in range(4):

        for l in range(4):

            if grid[m][l] == 0:

                grid[m][l] = " "

        

    

    print("+--------------------+")

    

    for i in range (4):

            print("|" + (str(grid[i][0])) + " " * (5 - len(str(grid[i][0]))) + (str(grid[i][1])) + " " * (5 - len(str(grid[i][1]))) + (str(grid[i][2])) + " " * (5 - len(str(grid[i][2]))) + (str(grid[i][3])) + " " * (5 - len(str(grid[i][3]))) + "|")

    

    

    print("+--------------------+")

    

def check_lost (grid):

    

    lost = True

    for j in range (4):

        if grid[j][0] != grid[j][1] and grid [j][1] != grid[j][2] and grid[j][2] != grid[j][3]:

            

            for l in range (4):

                if grid[j][l] == 0:

                    

                    lost = False

       

        for m in range(3):

            for c in range(4):

                if grid[m][c] == grid[m+1][c]:

                    lost = False

    

    return lost

            

def check_won (grid):

    test = False

    for i in range (4):

        for j in range (4):

            if eval(str(grid[i][j])) >= 32:

                test = True

                

    return test



def copy_grid(grid):

    copy = [[0 for x in range(4)] for x in range (4)]

    for i in range (4):

        for j in range(4):

            copy[i][j] = grid[i][j]

            

    return copy



def grid_equal(grid1, grid2):

    

    test2 = True

    

    for x in range (4):

        for y in range(4):

            if grid1[x][y] != grid2[x][y]:

                test2 = False

    

    return test2
