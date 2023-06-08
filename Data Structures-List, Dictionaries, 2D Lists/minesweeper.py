#This program takes in a grid of '-'(mine-free) and '#'(mines) and returns a grid where '-' is replaced by number of mines immediately adjacent to that spot



#The below function takes in input grid and returns the grid where mine-free spot is replaced by number of mines adjacent to that spot
def find_mines(grid):
    # The nested for loops below gets each row initially and then each of the elements in that row(column) by incrementing variables using enumerate function and the if loop checks for the mine-free spot inorder to replace it with the digit
    #'row_index', 'col_index' represents the index position of element, 'row' represents each row in grid, 'col' represnts each element in the row
    for row_index, row in enumerate(grid, start = 0):
        for col_index, col in enumerate(row, start = 0):
            #The below loop checks the current spot is mine-free, initialize 'mine_count' variable with value 0, and checks the index of row for boundaries to setup a starting index position
            #'mine_count' variable is used to store the number of mines adjacent to the mine-free spot; 'start' variable is used store a starting position inorder to check mines in adjacent rows
            if col=='-':
                mine_count=0
                if row_index==0:
                    start=0
                else:
                    start=row_index-1
                #The below loops checks mines in the current and adjacent rows, adjacent columns considering boundaries and increments the 'mine_count' variable
                #'row_p' represents the each adjacent and current row that need to be checked for mines; 'start' and 'row_index+2' decides row boundaries and '0' and 'len(row)' which is then length of the row decides column boundaries
                for row_p in grid[start:row_index+2]:
                    if col_index+1<len(row) and row_p[col_index+1]=='#':
                        mine_count+=1
                    if col_index-1>=0 and row_p[col_index-1]=='#':
                        mine_count+=1
                    if row_p[col_index]=='#':
                        mine_count+=1
                #The below command replaces the current mine-free spot in the grid with the number of mines 
                grid[row_index][col_index]=str(mine_count)
    #The below command returns the output grid
    return grid

# The below function is the main function it stores the input grid in 'grid_input' variable, calls 'find_mines' function and the returned output grid is stored in variable 'output_grid' and displays the input and output grids 
def main():
    grid_input=[ ["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "#", "-"] ]

    
    # The below loop prints the input grid; 'row_in' variable represents each row of the input grid
    print("\nInput Grid")
    for row_in in grid_input:
        print(row_in)
    
    #The below command calls the 'find_mines' function which takes input grid as argument and result is stored in 'output_grid' variable
    output_grid=find_mines(grid_input)
    
    # The below loop prints the output grid; 'row_out' variable represents each row of the output grid
    print("\nOutput Grid")
    for row_out in output_grid:
        print(row_out)

#The below command calls the main function
main()

