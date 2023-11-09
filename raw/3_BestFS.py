import heapq

class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.parent = parent
        self.cost = cost

    def __lt__(self, other):
        # Modify the comparison based on your heuristic function
        return self.cost < other.cost

def best_first_search(problem):
    start_node = Node(problem.initial_state)
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if problem.is_goal(current_node.state):
            return build_path(current_node)

        closed_set.add(current_node.state)

        for action, successor, step_cost in problem.get_successors(current_node.state):
            if successor not in closed_set:
                child = Node(successor, current_node, step_cost)
                heapq.heappush(open_list, child)

    return None

def build_path(node):
    path = []
    while node:
        path.insert(0, node.state)
        node = node.parent
    return path

class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def is_goal(self, state):
        raise NotImplementedError("Subclasses must implement is_goal")

    def get_successors(self, state):
        raise NotImplementedError("Subclasses must implement get_successors")

class EightPuzzleProblem(Problem):
    def is_goal(self, state):
        goal_state = (1, 2, 3, 8, 0, 4, 7, 6, 5)  # New goal state
        return state == goal_state

    def get_successors(self, state):
        successors = []
        blank_index = state.index(0)  # Find the index of the blank tile (represented as 0)

        # Define possible moves: up, down, left, right
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for move in moves:
            new_x = blank_index % 3 + move[0]
            new_y = blank_index // 3 + move[1]

            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = list(state)
                new_index = new_x + new_y * 3
                new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
                successors.append(("Move", tuple(new_state), 1))  # Cost of 1 for each move

        return successors

if __name__ == "__main__":
    initial_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)  # New initial state
    problem = EightPuzzleProblem(initial_state)

    solution_path = best_first_search(problem)
    if solution_path:
        print("Solution Found:")
        for state in solution_path:
            print(state)
    else:
        print("Solution doesn't Exist")
