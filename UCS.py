def ucs(graph, start, goal):
    frontier = [(0, [start])]  # Priority queue with cost and path
    explored = set()

    while frontier:
        cost, path = frontier.pop(0)
        current_node = path[-1]

        if current_node == goal:
            return path, cost  # Return the path and total cost

        explored.add(current_node)

        for neighbor, step_cost in graph.get(current_node, []):
            if neighbor not in explored:
                new_cost = cost + step_cost
                new_path = path + [neighbor]
                frontier.append((new_cost, new_path))
                frontier.sort()  # Sort by total cost for UCS

    return None, None  # Goal is not reachable

# Example usage:
graph = {
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 3)],
    'C': [('E', 4)],
    'D': [('F', 5)],
    'E': [('F', 1)],
    'F': []
}

start_node = 'A'
goal_node = 'F'

result_path, result_cost = ucs(graph, start_node, goal_node)

if result_path:
    print("Path found:", result_path)
    print("Total cost:", result_cost)
else:
    print("Goal is not reachable.")
