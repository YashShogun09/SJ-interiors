import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue for UCS (min-heap based on cost)
    pq = [(0, start, [])]  # (cost, current_node, path)
    visited = {}
    
    while pq:
        cost, node, path = heapq.heappop(pq)
        
        if node in visited and visited[node] <= cost:
            continue  # Skip if we've already found a cheaper path to this node
        
        # Mark node as visited with the current lowest cost
        visited[node] = cost
        path = path + [node]
        
        # Goal check
        if node == goal:
            return cost, path
        
        # Expand neighbors
        for neighbor, weight in graph.get(node, []):
            heapq.heappush(pq, (cost + weight, neighbor, path))
    
    return float("inf"), []  # If goal is not reachable

# Graph representation as an adjacency list with weighted edges
graph = {
    'S': [('a', 2), ('b', 1), ('d', 3), ('p', 1)],
    'a': [('c', 8)],
    'b': [('d', 1)],
    'd': [('e', 2)],
    'c': [],
    'e': [('c', 9), ('h', 8)],
    'h': [('f', 2)],
    'f': [('G', 2), ('r', 1)],
    'r': [],
    'p': [('q', 15)],
    'q': []
}

# Running UCS
start_node = 'S'
goal_node = 'G'
cost, path = uniform_cost_search(graph, start_node, goal_node)
print(f"Shortest Path: {' -> '.join(path)} with cost {cost}")
