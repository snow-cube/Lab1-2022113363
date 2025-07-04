# Text Graph：哈工大软件工程课程实验 1 词图可视化

## 目录

- [Text Graph：哈工大软件工程课程实验 1 词图可视化](#text-graph哈工大软件工程课程实验-1-词图可视化)
  - [目录](#目录)
  - [项目简介](#项目简介)
  - [功能特性](#功能特性)
  - [环境要求及运行指南](#环境要求及运行指南)
  - [使用说明](#使用说明)
  - [文件结构](#文件结构)
  - [示例](#示例)
  - [报告问题](#报告问题)
  - [作者](#作者)

## 项目简介

Text Graph 是一个基于 Dash 的词图可视化工具，用于分析文本中的单词关系。通过构建词图，用户可以直观地探索单词之间的连接、桥接词、最短路径等信息，并支持随机游走和 PageRank 计算等功能。

> [!IMPORTANT]
> 程序绝大部分功能由 LLM 编写，可能存在诸多问题。

## 功能特性

- **词图可视化**：展示文本中的单词节点及其关系。
- **桥接词查询**：查找两个单词之间的桥接词。
- **最短路径查询**：计算两个单词之间的最短路径。
- **随机游走**：模拟随机游走以探索词图。
- **PageRank 计算**：分析单词的重要性。
- **文本桥接生成**：自动插入桥接词以生成新的文本。

## 环境要求及运行指南

1. **克隆项目代码**：

   ```bash
   git clone <repository-url>
   cd Text-Graph
   ```

2. **安装依赖**：

   本项目使用 uv 进行项目依赖和环境管理，您可以通过 [uv 官方文档](https://docs.astral.sh/uv/) 或 [uv 官方仓库](https://github.com/astral-sh/uv) 中的指引便捷地安装 uv；之后，可以在项目目录下简单地运行

   ```bash
   uv run app.py <文本文件路径>  # 可选参数：初始加载的文本文件
   ```

   以执行程序。uv 将自动在目录下创建虚拟环境、安装依赖并运行程序。项目环境是通过 `pyproject.toml` 配置的。

## 使用说明

1. **上传文本文件**：
   - 点击页面右上角的“上传文本文件”按钮，选择 `.txt` 文件。
   - 文件上传后，系统会解析文本并生成词图。
   - 或在启动程序时指定文本文件路径参数以初始加载。

2. **可视化**：
   - 通过“显示图形可视化”选项来选择开启/关闭可视化。开启时可查看词图，移动节点、选中节点，并查看桥接词/最短路径/随机游走等功能的可视化结果。
   - 当输入文本较长、图的规模较大时可能会遭遇可视化的性能瓶颈，故节点数达到一定规模时系统将锁定开启可视化功能，可在项目中配置该阈值。

3. **查询功能**：
   - **桥接词/最短路径查询**：输入两个单词，选择查询模式（桥接词或最短路径），点击“查询”按钮；或者在可视化图中只选中两个节点时，自动展示查询结果。当只输入第一个单词，第二个单词留空时将展示该节点到其他所有节点的最短路径。
   - **节点信息查询**：输入单词名称，点击“查询”按钮查看详细信息；或者在可视化图中只选中一个节点时，自动展示查询结果。当开启计算 PageRank 选项时，节点信息查询结果将包括该节点 PageRank 值，且在可视化图中将展示每个节点的 PageRank 值（若开启可视化）。

4. **随机游走**：
   - 点击“开始随机游走”按钮，观察游走路径。
   - 可随时停止游走并保存游走结果。

5. **文本桥接生成**：
   - 输入文本，点击“生成”按钮，系统将自动插入桥接词。

## 文件结构

```text
Text-Graph/
├── app.py                      # 主应用入口
├── register_callbacks          # 注册所有回调
├── text_graph.py               # TextGraph 类定义，提高主要算法
├── callbacks/              # 回调函数目录，主要用于处理程序对各种功能的响应
│   ├── upload.py               # 文件上传相关回调
│   └── ...
├── graph_process_utils/        # 各个功能处理的统一工具接口，被回调函数调用
│   ├── upload.py               # 文件上传相关回调
│   └── ...
├── layouts/                    # 布局组件目录
│   ├── message_templates.py    # 输出消息布局模板
│   └── module_container.py     # 各个功能模块的容器布局模板
├── styles/                     # 样式定义目录
├── test_cases/                 # 测试用例目录
├── pyproject.toml              # 项目配置文件
├── README.md                   # 项目说明文档
└── ...
```

## 示例

待完善

<!-- 运行应用后，上传以下示例文本文件：

```plaintext
To explore strange new worlds,
To seek out new life and new civilizations
```

生成的词图将展示单词之间的连接关系。 -->

## 报告问题

欢迎任何形式的贡献！可以通过 [Issues](https://github.com/<repository-url>/issues) 提交问题。

## 作者

- **工具链选择与项目基本框架构建**：GPT-4
- **后续功能实现/算法**：Copilot + Claude 3.7 Sonnet Thinking、GPT-4（具体版本忘记了，为了修改部分 bug 可能各个版本都试了一下）
- **辅助**：我
