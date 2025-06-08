import pytest
from text_graph import TextGraph

@pytest.fixture
def test_graph():
    g = TextGraph("a b b c c d d e")  # a→b→c→d→e
    return g

# ========== 等价类测试 ==========
# 用例 1 有效类：路径存在一条 (1)(4)(7)
def test_path_exists(test_graph):
    path, cost = test_graph.calcShortestPath("a", "e")
    assert path == ["a", "b", "c", "d", "e"]
    assert cost == 4

# 用例 2 有效类：多路径，选最短 (5)
def test_multiple_paths_select_shortest():
    g = TextGraph("a b a b a b a c c b b d")
    path, cost = g.calcShortestPath("a", "d")
    assert path == ["a", "c", "b", "d"]
    assert cost == 3  # a→c→b→d 优于 a→b→d

# 用例 3 有效类：起点等于终点 (8)
def test_same_start_end(test_graph):
    path, cost = test_graph.calcShortestPath("b", "b")
    assert path == ["b"] and cost == 0

# 用例 4 无效类：起点不存在 (2)
def test_invalid_start_node(test_graph):
    path, cost = test_graph.calcShortestPath("x", "c")
    assert path == [] and cost == 0

# 用例 5 无效类：终点不存在 (3)
def test_invalid_end_node(test_graph):
    path, cost = test_graph.calcShortestPath("a", "z")
    assert path == [] and cost == 0

# 用例 6 无效类：无路径存在 (6)
def test_no_path_between_nodes(test_graph):
    path, cost = test_graph.calcShortestPath("e", "a")
    assert path == [] and cost == 0

# ========== 边界值测试 ==========

# 边界：仅两个节点，有边
def test_two_nodes_connected():
    g = TextGraph("x y")
    path, cost = g.calcShortestPath("x", "y")
    assert path == ["x", "y"] and cost == 1

# 边界：仅两个节点，无边
def test_two_nodes_disconnected():
    g = TextGraph("x y")
    path, cost = g.calcShortestPath("y", "x")
    assert path == [] and cost == 0

# 边界：起点为无出边节点
def test_start_node_no_outgoing():
    g = TextGraph("a b c")
    path, cost = g.calcShortestPath("c", "b")
    assert path == [] and cost == 0

# 边界：终点为无入边节点（除非直接连接）
def test_end_node_no_incoming():
    g = TextGraph("a b c")
    path, cost = g.calcShortestPath("b", "a")
    assert path == [] and cost == 0
