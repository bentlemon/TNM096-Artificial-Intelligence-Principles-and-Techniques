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
            h1 = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = h1
            return temp_puz
        else:
            # If the move is out of bounds, return None
            return None

    def copy(self, root):
        # Create a copy of the given puzzle state
        h1 = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            h1.append(t)
        return h1

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
        # Calculate the heuristic value (number of misplaced tiles) for a given state
        h1 = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    h1 += 1
        return h1

    def process(self):
        # Define the initial and goal states
        start = [
            ['2', '5', '_'], 
            ['1', '4', '8'], 
            ['7', '3', '6']]
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
            print("=====\n")
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")
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

    def check_state(self, c):
        # Check if a state has already been visited
        for i in self.closed:
            if i.data == c:
                return 1
        return 0


# Create a Puzzle object and execute the process method
puz = Puzzle()
puz.process()