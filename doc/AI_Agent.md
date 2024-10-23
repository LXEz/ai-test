# 基于 auto-gpt 的 agent 以什么样的形式存在

## auto-gpt 有什么

- auto-gpt 的基本元素——block

在 auto-gpt 中，系统具备的基本能力被抽象成一个一个的 block，这些 block 根据能力的不同被划分到不同的类别。

![](http://192.168.99.63:3000/uploads/upload_c16f9039967bb72d16f128d8ba0cecd9.png)

- graph（Agent）

基于这些 block，我们可以将它们拖放到画布上，形成一个个相互连接的 node，这被称做 graph，一个 graph 可以看作一个 Agent

> 一个根据提示词创建图片的 Agent

![](http://192.168.99.63:3000/uploads/upload_75fc7a212ea0b1f2abac685daaa9e163.png)

> 一个复杂点的 Agent（用于生成一个 python 文件，这个 python 文件是一个 auto-gpt 的 block 类）

![](http://192.168.99.63:3000/uploads/upload_9d8e3e2d7bc5f21430c841dae843b350.png)

在上图左侧是 agent 的输入部分，主要从 github 上拉取相应的示例代码，md 说明文档作为上下文，然后传递给 ai node：

![](http://192.168.99.63:3000/uploads/upload_bc68a90400f442078c580f56775d76e9.png)

这个 Agent 的核心是 ai 生成块，将左侧的输入合成为一个完整的提示词传递给 Ai：

![](http://192.168.99.63:3000/uploads/upload_a92f0c462b4355570793bce6fdd22035.png)

最后，将 ai 生成的内容，做一些处理，作为 agent 的输出

![](http://192.168.99.63:3000/uploads/upload_b50db675f1001fe525c0626a03d986c3.png)

## auto-gpt 的特点

- 将 agent 以 graph 的形式组织，基本能力以 block 作为载体，如果系统不具备某种能力，则需要自行编写相应的 block

- 在 auto-gpt 中，将 Ai 的能力看成是一个黑盒，用户在 ai 之外对功能编排，不侵入 ai 内部，将 ai 作为一个第三方供应商来调用。
