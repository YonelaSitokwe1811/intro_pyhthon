def push_up (grid):

    """merge grid values upwards"""

    already_merged=[]

    for i in range(5):

        for column_num in (0,1,2,3):

            for row_num in range(3):


                if grid[row_num][column_num]==0:

                    grid[row_num][column_num]=grid[row_num+1][column_num]

                    grid[row_num+1][column_num]=0

                elif column_num in already_merged: 

                    continue

                else:   

                    if grid[row_num][column_num]==grid[row_num+1][column_num]:

                        grid[row_num][column_num]=grid[row_num][column_num]+grid[row_num+1][column_num]

                        grid[row_num+1][column_num]=0

                        already_merged.append(column_num)

                

    



def push_down (grid):

    """merge grid values downwards"""

    already_merged=[]

    for i in range(5):

        for column_num in (0,1,2,3):

            for row_num in range(3, 0, -1):

               

                if grid[row_num][column_num]==0:

                    grid[row_num][column_num]=grid[row_num-1][column_num]

                    grid[row_num-1][column_num]=0

                                

                elif column_num in already_merged: 

                    continue

                else:   

                    if grid[row_num][column_num]==grid[row_num-1][column_num]:

                        grid[row_num][column_num]=grid[row_num][column_num]+grid[row_num-1][column_num]

                        grid[row_num-1][column_num]=0

                        already_merged.append(column_num)

    

def push_left (grid):

    """merge grid values left"""

    already_merged=[]

    for i in range(5):

            for row_num in (0,1,2,3):

                for column_num in range(3):

                   

                    if grid[row_num][column_num]==0:

                        grid[row_num][column_num]=grid[row_num][column_num+1]

                        grid[row_num][column_num+1]=0

                        
                    elif row_num in already_merged: 

                        continue

                    else:

                        if grid[row_num][column_num]==grid[row_num][column_num+1]:

                            grid[row_num][column_num]=grid[row_num][column_num]+grid[row_num][column_num+1]

                            grid[row_num][column_num+1]=0

                            already_merged.append(row_num)

                  

                    

                    

def push_right (grid):

    """merge grid values right"""

    already_merged=[]

    for i in range(5):

            for row_num in (0,1,2,3):

                for column_num in range(3,0,-1):

                   

                    if grid[row_num][column_num]==0:

                        grid[row_num][column_num]=grid[row_num][column_num-1]

                        grid[row_num][column_num-1]=0

                      

                    elif row_num in already_merged: 

                        continue

                    else:

                        if grid[row_num][column_num]==grid[row_num][column_num-1]:

                            grid[row_num][column_num]=grid[row_num][column_num]+grid[row_num][column_num-1]

                            grid[row_num][column_num-1]=0

                            already_merged.append(row_num)