import json
import unittest

from max_aa_exporter import lib


class TestNode(unittest.TestCase):
    def test_to_label(self):
        obj = lib.Node(json.loads("""{"box": {"id": "obj-2", "maxclass": "newobj", "text": "print"}}"""))
        msg = lib.Node(json.loads("""{"box": {"id": "obj-2", "maxclass": "message", "text": "hello"}}"""))
        btn = lib.Node(json.loads("""{"box": {"id": "obj-2", "maxclass": "button"}}"""))
        tgl = lib.Node(json.loads("""{"box": {"id": "obj-2", "maxclass": "toggle"}}"""))
        self.assertEqual(obj.to_label(), "obj:print")
        self.assertEqual(msg.to_label(), "msg:hello")
        self.assertEqual(btn.to_label(), "btn")
        self.assertEqual(tgl.to_label(), "tgl")


class TestEdge(unittest.TestCase):
    def test_to_expr(self):
        btn = lib.Node(json.loads("""{"box": {"id": "obj-2", "maxclass": "button"}}"""))
        msg = lib.Node(json.loads("""{"box": {"id": "obj-3", "maxclass": "message", "text": "hello"}}"""))
        nodes = {"obj-2": btn, "obj-3": msg}
        edge = lib.Edge(json.loads("""{"patchline": {"source": ["obj-2", 0], "destination": ["obj-3", 0]}}"""))
        self.assertEqual(edge.to_expr(nodes), "[btn]->[msg:hello]")
