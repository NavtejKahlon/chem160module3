from random import choice
from drawgridlib import drawgrid
npart=300
side=75  #Should be an odd number
steps = [(1,0),(-1,0),(0,1),(0,-1)]
grid=[[0 for x in range(side)] for y in range(side)]
grid[side//2][side//2]=1 # set's the location of the initial particle
for ipart in range(npart): # looping over particles
    x,y = 0,0 # varibles for grid indices; every particle will start at 0,0
    while 1:
        grid[x][y] = 0 # Removes particle from current possition
        sx,sy = choice(steps)
        x += sx
        y += sy
        # Enforce periodic boundaries
        if x < 0: x = side - 1
        if y < 0: y = side - 1
        if x == side: x = 0
        if y == side: y = 0
        grid[x][y] = 1   # Places particle in new position

        # Stop if you are next to a particle
        if (grid[(x+1)%side][y]+grid[x][(y+1)%side]+
            grid[(x+side-1)%side][y]+grid[x][(y+side-1)%side])>0:
            break
drawgrid(grid,side)