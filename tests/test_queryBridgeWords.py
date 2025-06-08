import pytest
from text_graph import TextGraph

# 用例 1：word1 不存在 out_edges 1 2 8
def test_query_no_out_edges_list():
    g = TextGraph("")
    g.nodes = {"a", "b", "c"}
    g.out_edges = {"a": [("b", 1)]}
    g.in_edges = {"b": [("a", 1)]}  # "c" 缺失 out_edges
    bridge_words, edge1, edge2 = g.queryBridgeWords("c", "a")
    assert bridge_words == []
    assert edge1 == []
    assert edge2 == []

# 用例 2：word2 不存在 in_edges 1 2 3 8
def test_query_no_in_edges_list():
    g = TextGraph("")
    g.nodes = {"a", "b", "c"}
    g.out_edges = {"a": [("b", 1)]}
    g.in_edges = {"b": [("a", 1)]}  # "c" 缺失 in_edges
    bridge_words, edge1, edge2 = g.queryBridgeWords("a", "c")
    assert bridge_words == []
    assert edge1 == []
    assert edge2 == []

# 用例 3：word1 有出边列表但为空 1 2 3 4 8
def test_query_no_outgoing_edges():
    g = TextGraph("")
    g.nodes = {"a", "b", "x"}
    g.out_edges = {"a": []}  # 没有出边
    g.in_edges = {"b": [("x", 1)]}
    bridge_words, edge1, edge2 = g.queryBridgeWords("a", "b")
    assert bridge_words == []
    assert edge1 == []
    assert edge2 == []

# 用例 4：word2 有入边列表但为空 1 2 3 4 5 4 8
def test_query_no_incoming_edges():
    g = TextGraph("")
    g.nodes = {"a", "b", "x"}
    g.out_edges = {"a": [("x", 1)]}
    g.in_edges = {"b": []}  # 没有入边
    bridge_words, edge1, edge2 = g.queryBridgeWords("a", "b")
    assert bridge_words == []
    assert edge1 == []
    assert edge2 == []

# 用例 5：中间节点不匹配 word2 的入边 1 2 3 4 5 6 5 4 8
def test_query_no_matching_bridge():
    g = TextGraph("")
    g.nodes = {"a", "b", "x", "y"}
    g.out_edges = {"a": [("x", 1)]}
    g.in_edges = {"b": [("y", 1)]}  # x ≠ y
    bridge_words, edge1, edge2 = g.queryBridgeWords("a", "b")
    assert bridge_words == []
    assert edge1 == []
    assert edge2 == []

# 用例 6：有一个桥接词 1 2 3 4 5 6 7 8
def test_query_one_bridge_word():
    g = TextGraph("")
    g.nodes = {"a", "b", "x"}
    g.out_edges = {"a": [("x", 1)]}
    g.in_edges = {"b": [("x", 1)]}
    bridge_words, edge1, edge2 = g.queryBridgeWords("a", "b")
    assert bridge_words == ["x"]
    assert edge1 == [{"source": "a", "target": "x", "type": "bridge"}]
    assert edge2 == [{"source": "x", "target": "b", "type": "bridge"}]
