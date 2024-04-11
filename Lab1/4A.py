import time

class Node:
    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        x, y = self.find(self.data, '_')
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children

    def shuffle(self, puz, x1, y1, x2, y2):
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = self.copy(puz)
            h1 = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = h1
            return temp_puz
        else:
            return None

    def copy(self, root):
        h1 = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            h1.append(t)
        return h1

    def find(self, puz, x):
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self):
        self.open = []
        self.closed = []

    def f(self, start, goal, depth_level):
        return self.h(start.data, goal) + depth_level  # Incorporate depth level into the f function

    def h(self, start, goal):
        h1 = 0
        for i in range(0, 3):
                for j in range(0, 3):
                    if start[i][j] != goal[i][j] and start[i][j] != '_':
                        h1 += 1 
        return h1

    def process(self):
        start_time = time.time()
        iteration_count = 0
        depth_levels = []

        start = [
            ['8', '6', '7'], 
            ['2', '5', '4'], 
            ['3', '_', '1']]
        goal = [
            ['1', '2', '3'], 
            ['4', '5', '6'], 
            ['7', '8', '_']]
        start = Node(start, 0, 0)
        start.fval = self.f(start, goal, 0)  # Pass depth level as 0 initially
        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            iteration_count += 1 
            print("=====\n")
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")
            print("h1 value:", self.h(cur.data, goal))
            print("Depth level:", cur.level)  # Print depth level for the current node
            print("=====\n")
            if self.h(cur.data, goal) == 0:
                break
            for i in cur.generate_child():
                i.fval = self.f(i, goal, i.level)  # Pass depth level for each child
                if self.check_state(i.data) == 1:
                    continue
                self.open.append(i)
            self.closed.append(cur)
            print("F:", cur.fval)
            del self.open[0]
            self.open.sort(key=lambda x: x.fval, reverse=False)
            depth_levels.append(cur.level)

        end_time = time.time()
        execution_time = end_time - start_time

        print("Iterations:", iteration_count)
        print("Execution Time:", execution_time, "seconds")
        print("Depth levels:", depth_levels)
        return depth_levels

    def check_state(self, c):
        for i in self.closed:
            if i.data == c:
                return 1
        return 0

# Create a Puzzle object and execute the process method
puz = Puzzle()
depth_levels = puz.process()
