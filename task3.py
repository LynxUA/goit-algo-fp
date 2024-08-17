import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

def dijkstra(graph, start):
    dist = {vertex: float('infinity') for vertex in graph}
    dist[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)
        
        if current_dist > dist[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex]:
            distance = current_dist + weight
            
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return dist

start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

print(f"Найкоротші шляхи від вершини {start_vertex}:")
for vertex, distance in shortest_paths.items():
    print(f"Вершина {vertex}: {distance}")
