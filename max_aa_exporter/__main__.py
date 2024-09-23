import json

from .lib import Edge, Node

HEADER = "graph{flow:south;}"


with open("testdata/hello.maxpat") as f:
    j = json.loads(f.read())


boxes = j["patcher"]["boxes"]
lines = j["patcher"]["lines"]

nodes = {}
for box in boxes:
    nodes[box["box"]["id"]] = Node(box)

edges = []
for line in lines:
    edges.append(Edge(line))

expr = "".join([edge.to_expr(nodes) for edge in edges])

print(f"{HEADER}{expr}")
