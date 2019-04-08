from enum import Enum
from collections import deque

class NodeState(Enum):
  UNVISITED = 0
  VISITING = 1
  VISITED = 2

class GraphNode:
  def __init__(self, val):
    self.val = val
    self.adj = []
    self.state = NodeState.UNVISITED

graph = {}

for i in range(5):
  graph[i] = GraphNode(i)

graph[0].adj = [graph[1], graph[2]]
graph[1].adj = [graph[1], graph[2]]
graph[2].adj = [graph[3]]
graph[3].adj = [graph[4]]

def search(start, end):
  if start is None or end is None:
    return False

  q = deque()
  start.state = NodeState.VISITING
  q.append(start)
  
  while len(q) > 0:
    node = q.pop()

    if node is not None:
      for neighbor in node.adj:
        if neighbor is end:
          return True
        elif neighbor.state == NodeState.UNVISITED:
          neighbor.state = NodeState.VISITING
          q.append(neighbor)
      node.state = NodeState.VISITED
    
  return False

print(search(graph[0], graph[4]))
print(search(graph[2], graph[4]))
print(search(graph[2], graph[1]))
print(search(graph[4], graph[0]))
