// GRAPH
const graph = {};

graph["start"] = {};
graph["start"]["a"] = 6;
graph["start"]["b"] = 2;
graph["start"]["c"] = 2;

graph["a"] = {};
graph["a"]["final"] = 1;

graph["b"] = {};
graph["b"]["a"] = 3;
graph["b"]["final"] = 3;

graph["c"] = {};
graph["c"]["a"] = 1;
graph["c"]["b"] = 1;

graph["final"] = {};

// COSTS GRAPH
// costs from start point to each other point
const costs = {};

// we can use the global property Infinity is a numeric value representing infinity.
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Infinity
costs["a"] = 6;
costs["b"] = 2;
costs["c"] = 3;
costs["final"] = Infinity;

// PARENTS GRAPH
parents = {};
parents["a"] = "start";
parents["b"] = "start";
parents["c"] = "start";
parents["final"] = null;

// PROCESSED NODE LIST
processed = [];

// FUNCTION FOR SEARCH LOWEST COST
const findLowestCostNode = (costs) => {
  let lowestCost = Infinity;
  let lowestCostNode = null;

  for (node in costs) {
    const cost = costs[node];
    if (cost < lowestCost && processed.indexOf(node) == -1) {
      lowestCost = cost;
      lowestCostNode = node;
    }
  }
  return lowestCostNode;
};

// FINNALY FUNCTION FOR SEARCH THE LOWEST COST

const findLowestCost = (costs) => {
  let node = findLowestCostNode(costs);
  console.log(`Go to -> ${node}`);
  while (node !== null) {
    //undefined
    let cost = costs[node];
    const neighbours = graph[node];
    for (n in Object.keys(neighbours)) {
      const newCost = cost + neighbours[n];
      if (newCost > cost[n]) {
        cost[n] = newCost;
        parents[n] = node;
      }
    }
    processed.push(node);
    node = findLowestCostNode(costs);
    console.log(`Go to ->  ${node !== null ? node : "finish"}`);
  }
};

findLowestCost(costs);
