import pytest
from text_graph import TextGraph

@pytest.fixture
def sample_graph():
    text = "the quick brown fox jumps over the lazy dog"
    return TextGraph(text)

# TC1: 存在桥接词
def test_bridge_word_exists(sample_graph):
    bridges, edges1, edges2 = sample_graph.queryBridgeWords("quick", "fox")
    assert bridges == ["brown"]
    assert edges1 == [{"source": "quick", "target": "brown", "type": "bridge"}]
    assert edges2 == [{"source": "brown", "target": "fox", "type": "bridge"}]

# TC2: 不存在桥接词
def test_no_bridge_word(sample_graph):
    bridges, edges1, edges2 = sample_graph.queryBridgeWords("the", "fox")
    assert bridges == []
    assert edges1 == []
    assert edges2 == []

# TC3: word1 不存在
def test_word1_not_in_graph(sample_graph):
    bridges, edges1, edges2 = sample_graph.queryBridgeWords("hello", "fox")
    assert bridges == []
    assert edges1 == []
    assert edges2 == []

# TC4: word2 不存在
def test_word2_not_in_graph(sample_graph):
    bridges, edges1, edges2 = sample_graph.queryBridgeWords("quick", "unicorn")
    assert bridges == []
    assert edges1 == []
    assert edges2 == []

# TC5: word1 与 word2 相同
def test_same_word_input(sample_graph):
    bridges, edges1, edges2 = sample_graph.queryBridgeWords("dog", "dog")
    assert bridges == []
    assert edges1 == []
    assert edges2 == []

# TC6: 空字符串输入
def test_empty_input(sample_graph):
    bridges, edges1, edges2 = sample_graph.queryBridgeWords("", "")
    assert bridges == []
    assert edges1 == []
    assert edges2 == []

# TC7: 边界条件 - word1 是句尾词
def test_word1_is_last_word(sample_graph):
    bridges, edges1, edges2 = sample_graph.queryBridgeWords("dog", "fox")
    assert bridges == []
    assert edges1 == []
    assert edges2 == []

# TC8: 大小写混合输入
def test_case_insensitive_input(sample_graph):
    bridges1, _, _ = sample_graph.queryBridgeWords("QUICK", "FOX")
    bridges2, _, _ = sample_graph.queryBridgeWords("quick", "fox")
    assert bridges1 == bridges2 == ["brown"]
