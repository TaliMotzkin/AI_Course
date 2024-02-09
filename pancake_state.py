class pancake_state:
    neighbor_dict = {}
    heuristics_dict = {}

    def __init__(self, state_str):
        self.state_str = state_str
        self.state_list = state_str.split(',')
        self.N = len(self.state_list)
        # self.hashing = (self.state_str, tuple(self.state_list))

    '''
    returns an array of tuples of neighbor states and the cost to reach them: [(pancake_state1, cost1),
    (pancake _state2, cost2)...]
    '''
    def get_neighbors(self):
        temp_self = self.state_list
        num_pancakes = self.N
        neighbors_list = []

        for i in range(num_pancakes - 1):
            new_neighbor = temp_self[:i] + temp_self[i:][::-1]
            price = sum(map(int,temp_self[i:]))
            new_neighbor_str = ','.join(new_neighbor)
            neighbors_list.append((pancake_state(new_neighbor_str), price))

        return neighbors_list


    # you can change the body of the function if you want
    def __hash__(self):
        return hash(self.state_str)

    # you can change the body of the function if you want
    def __eq__(self, other):
        return self.state_str == other.state_str

    def get_state_str(self):
        return self.state_str
