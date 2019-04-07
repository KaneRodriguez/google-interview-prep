from GraphAdjList import GraphAdjList, NodeAdjList
from collections import deque

def visit(node):
	print(node.val)

def DFSAdjList(root):
	if root is None:
		return root
	else:
		visit(root)
		root.visited = True
		for adjN in root.adj:
			if not adjN.visited:
				DFSAdjList(adjN)


def BFSAdjList(root):
	if root is None:
		return root
	else:
		Q = deque()
		Q.insert(0, root)
		root.visited = True
		
		while len(Q) > 0:
			node = Q.pop()
			visit(node)
			node.visited = True
			for adjN in node.adj:
				if not adjN.visited:
					Q.insert(0, adjN)


node2 = NodeAdjList(2, [])
node3 = NodeAdjList(3, [])
node4 = NodeAdjList(4, [node2])
node5 = NodeAdjList(5, [node4])
node6 = NodeAdjList(6, [node4, node5])
node1 = NodeAdjList(1, [node2, node3, node6])

nodes = [node1, node2, node3, node4, node5, node6]
	
graphAdjList = GraphAdjList(nodes)

def clearGraphAdjList(graphAdjList):
	for node in graphAdjList.nodes:
		if node is not None:
			node.visited = False

def testBFSAdjList(graphAdjList):
	BFSAdjList(graphAdjList.nodes[0])
	clearGraphAdjList(graphAdjList)

def testDFSAdjList(graphAdjList):
	DFSAdjList(graphAdjList.nodes[0])
	clearGraphAdjList(graphAdjList)


print("testing dfs...")
testDFSAdjList(graphAdjList)

print("testing bfs...")
testBFSAdjList(graphAdjList)
