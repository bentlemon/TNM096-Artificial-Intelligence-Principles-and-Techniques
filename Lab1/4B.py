import time  # Import time module for time taking

class Node:
    def __init__(self, data, level, fval):
        # Initialize the node with the provided data, level, and fvalue
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        # Generate child nodes by moving the blank space in four directions: up, down, left, right
        x, y = self.find(self.data, '_')
        # Define possible moves for the blank space
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in val_list:
            # Attempt to move the blank space
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                # Create a new node for the moved state
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children

    def shuffle(self, puz, x1, y1, x2, y2):
        # Move the blank space to the specified coordinates and return the resulting state
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            # If the move is within bounds, perform the move
            temp_puz = self.copy(puz)
            h2 = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = h2
            return temp_puz
        else:
            # If the move is out of bounds, return None
            return None

    def copy(self, root):
        # Create a copy of the given puzzle state
        h2 = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            h2.append(t)
        return h2

    def find(self, puz, x):
        # Find the coordinates of a specific element in the puzzle state
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self):
        # Initialize the open and closed lists
        self.open = []
        self.closed = []

    def f(self, start, goal):
        # Calculate the f-value for a given state (f(x) = )
        return self.h(start.data, goal)

    def h(self, start, goal):
            h2 = 0
            goal_positions = {}

            for i in range(3):
                for j in range(3):
                    goal_positions[goal[i][j]] = (i, j)

            for i in range(3):
                for j in range(3):
                    if start[i][j] != goal[i][j] and start[i][j] != '':
                        value = start[i][j]
                        goal_i, goal_j = goal_positions[value]
                        h2 += abs(goal_i - i) + abs(goal_j - j)

            return h2

    def process(self):
        start_time = time.time()  # Record the starting time  
        iteration_count = 0  # Initialize iteration counter
  
        # Define the initial and goal states
        start = [
            ['8', '6', '7'], 
            ['2', '5', '4'], 
            ['3', '_', '1']]
        goal = [
            ['1', '2', '3'], 
            ['4', '5', '6'], 
            ['7', '8', '_']]
        start = Node(start, 0, 0)
        start.fval = self.f(start, goal)
        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            iteration_count += 1  # Increment iteration counter

            print("=====\n")
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")
            print("h2 value:", self.h(cur.data, goal))  # Print h value for the current state
            print("=====\n")
            if self.h(cur.data, goal) == 0:
                break
            for i in cur.generate_child():
                i.fval = self.f(i, goal)
                if self.check_state(i.data) == 1:  # Check if state is already visited
                    continue
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]
            self.open.sort(key=lambda x: x.fval, reverse=False)
            depth_level = cur.level  # Update the depth level for each iteration


        end_time = time.time()  # Record the ending time
        execution_time = end_time - start_time  # Calculate the execution time

        print("Iterations:", iteration_count)  # Print the total number of iterations
        print("Execution Time:", execution_time, "seconds")  # Print the execution time
        print("Depth level:", depth_level)  # Print the depth level of the last iteration

        

    def check_state(self, c):
        # Check if a state has already been visited
        for i in self.closed:
            if i.data == c:
                return 1
        return 0

#Iterations: 153
#Execution Time: 0.35958385467529297 seconds

# Create a Puzzle object and execute the process method
puz = Puzzle()
puz.process()
