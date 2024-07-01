"""
File: mazeGenerator.py
Last Modified: 7/1/1014

Logic for generating a random maze
"""

import random

class Cell():
    """
    Cells are maze units, which store a location and connecting cells (which can be any four adjacent cells)
    """
    
    def __init__(self, x, y):
        """
        Initialize a cell
        
        x - The x coordinate, or column number
        y - The y coordinate, or row number
        """
        self.x = x
        self.y = y
        self.connections = []
        self.has_treasure = False
        
        
    def add_connection(self, c):
        """
        Add a connection
        
        c - The connecting cell location (x, y)
        """
        self.connections.append(c)
        
        
    def remove_connection(self, c):
        """
        Remove a connection
        
        c - The connecting cell location (x, y)
        """
        self.connections.remove(c)
        
        
    def has_connection(self, c):
        """
        Determine if the cell has connection c
        
        c - The connection to check for
        Returns true if the connection exists or false otherwise
        """
        if c in self.connections:
            return True
        else:
            return False
        
        
    def has_left_connection(self):
        """
        Returns true if there is a connection left of the cell
        """
        return self.has_connection((self.x - 1, self.y))
    
    
    def has_right_connection(self):
        """
        eturns true if there is a connection right of the cell
        """
        return self.has_connection((self.x + 1, self.y))
    
    
    def has_top_connection(self):
        """
        Returns true if there is a connection above the cell
        """
        return self.has_connection((self.x, self.y - 1))
    
    
    def has_bottom_connection(self):
        """
        Returns true if there is a connection below the cell
        """
        return self.has_connection((self.x, self.y + 1))


class MazeGenerator():
    """
    Generates and stores the maze
    """
    
    def __init__(self, size):
        """
        Initialize the 2D list maze matrix
        """
        self.size = size
        self.maze = [[0 for i in range(self.size)] for j in range(self.size)] 

    
    def create_graph(self):
        """
        Create the maze graph
        """
        for x in range(self.size):
            for y in range(self.size):
                self.maze[x][y] = Cell(x, y)
                
        
    def draw_maze(self):
        """
        Draw a text version of the maze to the screen, for debugging purposes
        """
        print("________________")
        for y in range(self.size):
            print("|", end="")
            for x in range(self.size):
                if not self.maze[x][y].has_connection((x, y + 1)):
                    print("_", end="")
                else:
                    print(" ", end="")
                    
                if not self.maze[x][y].has_connection((x + 1, y)):
                    print("|", end="")
                else:
                    print(" ", end="")
            print()
            
            
    def __generate_treasure(self):
        """
        Randomly generate 3 pieces of treasure in the maze
        """
        values = []
        
        for i in range(self.size):
            for j in range(self.size):
                values.append(i + (j * 10))
                
        # We do not want to start/end locs to have treasure
        values.remove(7)
        values.remove(70)
        
        r1 = random.choice(values)
        values.remove(r1)
        r2 = random.choice(values)
        values.remove(r2)
        r3 = random.choice(values)
        
        # Split the values into two terms, access the maze, and add treasure
        self.maze[r1%10][(r1//10) % 100].has_treasure = True
        self.maze[r2%10][(r2//10) % 100].has_treasure = True
        self.maze[r3%10][(r3//10) % 100].has_treasure = True
        
        
    def __get_neighbors(self, x, y):
        """
        Get all possible neighbors of some cell location
        
        x - The x coord of the cell to get neighbors for
        y - The y coord of the cell to get neighbors for
        Returns the neighbor list
        """
        neighbors = []
        
        if x < self.size - 1:
            neighbors.append((x + 1, y))
        if y < self.size - 1:
            neighbors.append((x, y + 1))
        if x > 0:
            neighbors.append((x - 1, y))
        if y > 0:
            neighbors.append((x, y - 1))
            
        return neighbors

    
    def __get_in_maze_rand_neighbor(self, x, y, explored):
        """
        Get a random neighbor of some cell that has already been explored
        
        x - The x coord of the cell to get a neighbor for
        y - The y coord of the cell to get a neighbor for
        explored - The list of explored cells
        Returns a random explored neighbor
        """
        neighbors = []
        
        if (x + 1, y) in explored:
            neighbors.append((x + 1, y))
        if (x, y + 1) in explored:
            neighbors.append((x, y + 1))
        if (x - 1, y) in explored:
            neighbors.append((x - 1, y))
        if (x, y - 1) in explored:
            neighbors.append((x, y - 1))
        
        return random.choice(neighbors)
            
    
    def generate_maze(self):
        """
        Using Prim's algorithm, generate a random maze
        """
        init = True
        
        #Select some random cell to begin
        init_x = random.randrange(0, self.size)
        init_y = random.randrange(0, self.size)

        #Add that random cell to the maze 
        explored = []
        explored.append((init_x, init_y))
        
        #The cells adjacent to the already explored ones, to be explored next, at random
        frontier = []
        
        while init or len(frontier) > 0:
            init = False
            
            #Select some random cell from the explored list
            rand_cell = random.choice(explored)
            
            #Add the neighboring cells to the frontier, that are not already in the frontier or part of the maze
            for n in self.__get_neighbors(rand_cell[0], rand_cell[1]):
                if n not in explored and n not in frontier:
                    frontier.append(n)
            
            #Choose a random frontier cell
            new_connection = random.choice(frontier)
            #Get a cell that is adjacent to that frontier cell, that is already in the maze
            adjacent = self.__get_in_maze_rand_neighbor(new_connection[0], new_connection[1], explored)
            
            # Connect those cells
            self.maze[new_connection[0]][new_connection[1]].add_connection(adjacent)
            self.maze[adjacent[0]][adjacent[1]].add_connection(new_connection)
            
            # From the new cell, add cells to the frontier
            for n in self.__get_neighbors(new_connection[0], new_connection[1]):
                if n not in explored and n not in frontier:
                    frontier.append(n)
            
            #Mark the new cell as part of the maze now that it is connected
            explored.append(new_connection)
            frontier.remove(new_connection)
        
        self.__generate_treasure()
         
