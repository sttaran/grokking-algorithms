# GRAPH
graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["start"]["c"] = 2

graph["a"] = {}
graph["a"]["final"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["final"] = 3

graph["c"] = {}
graph["c"]["a"] = 1
graph["c"]["b"] = 1

graph["final"] = {}

# COSTS GRAPH
# costs from start point to each other point
costs = {}

# we can make variable with infinity value this way
infinity = float("inf")

costs["a"] = 6
costs["b"] = 2
costs["c"] = 3
costs["final"] = infinity

# PARENTS GRAPH
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = "start"
parents["final"] = None

# PROCESSED NODE LIST
processed = []

# FUNCTION FOR SEARCH LOWEST COST


def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# FINNALY FUNCTION FOR SEARCH THE LOWEST COST
def find_lowest_cost(costs):

    # FIND FIRST LOWEST COST
    node = find_lowest_cost_node(costs)
    print('Go to -> ' + node)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours.keys():
            new_cost = cost + neighbours[n]
            if new_cost > costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
        print('Go to -> ' + node if node is not None else 'Go to -> finish')


find_lowest_cost(costs)
