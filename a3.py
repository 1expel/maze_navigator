
# --- NAVIGATE MAZE PROBLEM ---

# --- CONSTANTS --- 

ROW = [-1, 0, 1, 0]
COL = [0, 1, 0, -1]

# --- DATA STRUCTURES ---

class Maze:

    def __init__(self, size, start, finish, barriers):
        self.size = size
        self.start = start
        self.finish = finish
        self.barriers = barriers
        return

    def __str__(self):
        s = f"--- MAZE ---\n\n  "
        for i in range(1, self.size[1] + 1):
            s += str(i)
        s += '\n'
        for i in range(1, self.size[0] + 1):
            s += str(i) + ' '
            for j in range(1, self.size[1] + 1):
                coordinate = [i, j]
                if(coordinate in self.barriers):
                    s += 'X'
                elif(coordinate == self.start):
                    s += 'S'
                elif(coordinate == self.finish):
                    s += 'F'
                else:
                    s += ' '
            s += '\n'
        s += "\n------------\n"
        return s

    def _is_valid_coordinate(self, coordinate):
        return 0 < coordinate[0] <= self.size[0] and 0 < coordinate[1] <= self.size[1] and coordinate not in self.barriers

    def generate_moves(self, coordinate):
        moves = []
        for i in range(4):
            move = [
                coordinate[0] + ROW[i],
                coordinate[1] + COL[i]
            ]
            if(self._is_valid_coordinate(move)):
                moves.append(move)
        return moves

    def calc_manhattan_dist(self, coordinate):
        return abs(coordinate[0] - self.finish[0]) + abs(coordinate[1] - self.finish[1])

class PriorityQueue:

    def __init__(self):
        self.pq = []
        return

    def __len__(self):
        return len(self.pq)

    def __iter__(self):
        for node in self.pq:
            yield node
        return

    def insert(self, node):
        self.pq.append(node)
        return

    def remove(self):
        min_index = 0
        for i in range(1, len(self.pq)):
            if(self.pq[i] < self.pq[min_index]):
                min_index = i
        return self.pq.pop(min_index)

    def is_open(self, node):
        for open_node in self.pq:
            if(open_node.coordinate == node.coordinate):
                if(node.is_shorter_path(open_node)):
                    open_node.update_path(node)
                return True
        return False
    
    def is_empty(self):
        return len(self.pq) == 0

class Visited:

    def __init__(self):
        self.visited = []
        return

    def __len__(self):
        return len(self.visited)

    def __iter__(self):
        for node in self.visited:
            yield node
        return

    def append(self, node):
        self.visited.append(node)
        return

    def is_visited(self, node):
        for i in range(len(self.visited)):
            if(self.visited[i].coordinate == node.coordinate):
                if(node.is_shorter_path(self.visited[i])):
                    self.visited.pop(i)
                    return False
                else:
                    return True
        return False
    
    def is_empty(self):
        return len(self.visited) == 0

class Node:

    def __init__(self, parent, coordinate, level, heuristic):
        self.parent = parent
        self.coordinate = coordinate
        self.level = level
        self.heuristic = heuristic
        return  

    def __lt__(self, node):
        return (self.level + self.heuristic) < (node.level + node.heuristic)

    def __str__(self):
        if(self.parent): 
            return f"Node({self.parent.coordinate}, {self.coordinate}, {self.level}, {self.heuristic})"
        else:
            return f"Node(None, {self.coordinate}, {self.level}, {self.heuristic})"

    def is_shorter_path(self, node):
        return self < node

    def update_path(self, node):
        self.parent = node.parent
        self.level = node.level
        return
    
    def print_path(self):
        if(self.parent):
            self.parent.print_path()
        print(self.coordinate)
        return

# --- DRIVER CODE ---

def solve(start, finish):
    maze = Maze(
        [5, 9],
        start,
        finish,
        [[1,8],
        [2,2],
        [2,4],
        [2,5],
        [3,4],
        [3,7],
        [3,9],
        [4,4],
        [4,7],
        [4,9],
        [5,2]]
    )
    print(maze)
    pq = PriorityQueue()
    visited = Visited()
    root = Node(None, start, 0, maze.calc_manhattan_dist(start))
    pq.insert(root)
    while(not pq.is_empty()):
        node = pq.remove()
        visited.append(node)
        if(node.coordinate == finish):
            print("--- PATH ---\n")
            node.print_path()
            print("\n------------\n")
            return 
        moves = maze.generate_moves(node.coordinate)
        for move in moves:
            child_node = Node(node, move, node.level + 1, maze.calc_manhattan_dist(move))
            if(not visited.is_visited(child_node) and not pq.is_open(child_node)):
                pq.insert(child_node)
    print("no solution")
    return

# --- INPUT ---

solve([3,1], [2,6])
solve([3,1], [5,9])
