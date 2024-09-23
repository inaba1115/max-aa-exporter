label_table = {
    "button": "btn",
    "toggle": "tgl",
    "message": "msg",
    "newobj": "obj",
}


class Node:
    def __init__(self, box: dict):
        self.maxclass = box["box"]["maxclass"]
        self.text = box["box"].get("text")  # nullable

    def to_label(self) -> str:
        xs = [label_table[self.maxclass], self.text]
        return ":".join([x for x in xs if x is not None])


class Edge:
    def __init__(self, line: dict):
        self.source = line["patchline"]["source"][0]
        self.destination = line["patchline"]["destination"][0]

    def to_expr(self, nodes: dict) -> str:
        source = nodes[self.source]
        destination = nodes[self.destination]
        return f"[{source.to_label()}]->[{destination.to_label()}]"
