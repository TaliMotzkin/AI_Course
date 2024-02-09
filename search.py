import heapq

from search_node import search_node


def create_open_set():
    return [], {}


def create_closed_set():
    return {}


def add_to_open(vn, open_set):
    heapq.heappush(open_set[0], vn)
    open_set[1][vn.state] = [vn.g, vn]

def open_not_empty(open_set):
    return len(open_set[0]) != 0


def get_best(open_set):
    while open_set[0]:
        item = heapq.heappop(open_set[0])
        if item.valid:
            return item
    return None



def add_to_closed(vn, closed_set):
    closed_set[vn.state] = vn.g


# returns False if curr_neighbor state not in open_set or has a lower g from the node in open_set
# remove the node with the higher g from open_set (if exists)


def duplicate_in_open(vn, open_set):
    existing_node = open_set[1].get(vn.state)
    if existing_node:
        if existing_node[0] >= vn.g:
            existing_node[1].valid = False # Mark the existing node as invalid
            return False
        else:
            return True
    return False


def duplicate_in_closed(vn, closed_set):
    if vn.state in closed_set:
        closed_set[vn.state] = vn.g
        return True
    return False


def print_path(path):
    for i in range(len(path) - 1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    print(path[-1].state.state_str)


def search(start_state, heuristic, goal_state):

    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):

        current = get_best(open_set)

        if current.state.get_state_str() == goal_state:
            path = []
            goal_val = 0
            while current:
                path.append(current)
                goal_val += current.g
                current = current.prev
            path.reverse()
            ###OF nodes and not states!
           # print(f'goal_val{goal_val}')
            return path, goal_val

        add_to_closed(current, closed_set)

        ##neighboor is a state
        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None
