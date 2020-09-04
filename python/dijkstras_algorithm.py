# GRAPH
graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["final"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["final"] = 3

graph["final"] = {}

# COSTS GRAPH
# costs from start point to each other point
costs = {}

# we can make variable with infinity value this way
infinity = float("inf")

costs["a"] = 6
costs["b"] = 2
costs["final"] = infinity

# PARENTS GRAPH

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["final"] = None

# PROCESSED NODE LIST

processed = []

