import matplotlib.pyplot as plt
from stack import Stack


# Read maze from maze.txt
maze = []

with open('maze.txt', 'r') as f:
    for line in f.readlines():
        row = [int(x) for x in line.rstrip().split(',')]
        maze.append(row)

#plt.imshow(maze, cmap='jet')
#plt.show()


# Solve maze
direction_list = [(0,1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
position = (1,1) # start from (1,1)
stack = Stack() # stack for tracking path


while maze[position[0]][position[1]] != 4: # stop if reached goal
    
    available = False
    for direction in direction_list: # try 4 directions
        next_position = (position[0] + direction[0], position[1] + direction[1])
        
        # if there is available move in any of 4 directions
        if maze[next_position[0]][next_position[1]] == 0 or maze[next_position[0]][next_position[1]] == 4: 
            stack.push(position)
            maze[position[0]][position[1]] = 2 # grid is on stack
            position = next_position
            available = True
            break
        
        
    # unavailable to move, move backwards
    if available == False:
        maze[position[0]][position[1]] = 3 # grid popped from stack
        position = stack.pop()

stack.push(position) # push goal

# print path
print(" -> ".join([str(x) for x in stack.stack])) 
plt.imshow(maze, cmap='jet')
plt.savefig('solution.png')