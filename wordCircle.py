from collections import defaultdict, deque
def evalWordCircle(words: list[str]) -> bool:
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    graph = defaultdict(set)

    for word in words:
        start = word[0]
        end = word[-1]
        out_degree[start] += 1
        in_degree[end] += 1
        graph[start].add(end)
        graph[end]

    for char in set(in_degree.keys()).union(set(out_degree.keys())):
        if in_degree[char] != out_degree[char]:
            return False

    def bfs(start_char):
        visited = set()
        queue = deque([start_char])
        while queue:
            char = queue.popleft()
            if char not in visited:
                visited.add(char)
                for neighbor in graph[char]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return visited

    start_char = next((char for char in out_degree if out_degree[char] > 0), None)
    if start_char is None:
        return True

    visited = bfs(start_char)

    for char in set(in_degree.keys()).union(set(out_degree.keys())):
        if in_degree[char] > 0 or out_degree[char] > 0:
            if char not in visited:
                return False

    return True

def test_evalWordCircle():
    words = ['chair', 'height', 'racket', 'touch', 'tunic']
    assert evalWordCircle(words) == True
