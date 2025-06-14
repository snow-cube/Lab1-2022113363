from text_graph import TextGraph


def process_bridge_words(
    word1, word2, text_graph, style_state, is_graph_displayed=True
):
    """处理桥接词的通用函数

    Args:
        word1: 第一个单词
        word2: 第二个单词
        text_graph: TextGraph 实例或原始文本
        elements: 图的元素列表
        style_state: 当前样式状态字典
        is_graph_displayed: 图形是否显示

    Returns:
        tuple: (桥接词列表, 信息消息, 更新后的样式状态)
    """
    if isinstance(text_graph, str):
        tg = TextGraph(text_graph or "")
    else:
        tg = text_graph

    if not word1 or not word2 or word1 == word2:
        return [], f"请提供两个不同的单词", style_state

    word1 = word1.lower()
    word2 = word2.lower()
    # 检查单词是否存在于图中
    word1_exists = word1 in tg.nodes
    word2_exists = word2 in tg.nodes

    if not word1_exists and not word2_exists:
        return [], f"单词 '{word1}' 和 '{word2}' 都不存在于图中", style_state
    elif not word1_exists:
        return [], f"单词 '{word1}' 不存在于图中", style_state
    elif not word2_exists:
        return [], f"单词 '{word2}' 不存在于图中", style_state

    # Always calculate the bridge words result and get edge information directly
    bridges, word1_to_bridge_edges, bridge_to_word2_edges = tg.queryBridgeWords(
        word1, word2
    )

    # Only update the visual style if the graph is displayed
    if is_graph_displayed:
        style_state["shortest_path"] = []
        style_state["bridge_words"] = bridges

        selected_nodes = []
        selected_nodes.append(word1)
        selected_nodes.append(word2)
        style_state["selected_nodes"] = selected_nodes

        # 合并从 TextGraph 实例获取的边信息
        highlighted_edges = word1_to_bridge_edges + bridge_to_word2_edges
        style_state["highlighted_edges"] = highlighted_edges

    if bridges:
        msg = f"桥接词 ({word1} → ? → {word2}): " + ", ".join(bridges)
    else:
        msg = f"未找到 {word1} → ? → {word2} 的桥接词"

    return bridges, msg, style_state
