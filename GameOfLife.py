import pygame 
import numpy as np

pygame.init()

width,height = 300,300
screen = pygame.display.set_mode((width,height))

# Set the number of cells in each row and column
n_cells_x, n_cells_y = width // 20, height// 20

cell_width = width // n_cells_x
cell_height = height // n_cells_y

grid = [[0] * n_cells_x for _ in range(n_cells_y)]

# Define the colors
bg_color = pygame.Color('gray20')
alive_color = pygame.Color('gray86')

# Function to update the grid based on the Game of Life rules
def update_grid():
    def countNeighbours(r,c):
        n = 0
        for i in range(r-1,r+2):
            for j in range(c-1,c+2):
                #edge cases or out of bounds we will disregard 
                if ((i==r and j==c) or i<0 or j<0 or i==n_cells_x or j==n_cells_y):
                    continue
                if grid[i][j] in [1,3]:  # the value is either 1 or 3: then it was originally 1 as state col in the table below
                    n+=1
        return n
  

    for r in range(n_cells_x):
        for c in range(n_cells_y):
            neighbours = countNeighbours(r,c)

            if grid[r][c]:
                if neighbours in [2,3]: 
                    grid[r][c] = 3
            elif neighbours == 3:
                        grid[r][c] = 2

    for r in range(n_cells_x):
        for c in range(n_cells_y):
            if grid[r][c] == 1:
                grid[r][c] = 0
            elif grid[r][c] in [2,3]:
                grid[r][c] = 1 



# Function to draw the grid on the screen
def draw_grid():
    screen.fill(bg_color)
    
    # Loop over each cell
    for x in range(n_cells_x):
        for y in range(n_cells_y):
            # Calculate the position of the cell on the screen
            cell_x = x * cell_width
            cell_y = y * cell_height
            
            # Draw the cell
            if grid[x][y] == 1:
                pygame.draw.rect(screen, alive_color, (cell_x, cell_y, cell_width, cell_height))

    # Draw the grid lines
    for x in range(0, width, cell_width):
        pygame.draw.line(screen, pygame.Color('green'), (x, 0), (x, height))
    for y in range(0, height, cell_height):
        pygame.draw.line(screen, pygame.Color('red'), (0, y), (width, y))
    
    # Update the display
    pygame.display.flip()

running = True
paused = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Get the cell position based on the mouse click
                mouse_x, mouse_y = pygame.mouse.get_pos()
                cell_x = mouse_x // cell_width
                cell_y = mouse_y // cell_height
                
                # Toggle the cell state
                grid[cell_x][cell_y] = not grid[cell_x][cell_y]
        
    if not paused:
        update_grid()
    
    draw_grid()


pygame.quit()