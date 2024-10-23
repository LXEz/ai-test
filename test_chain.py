class Runnable:
    def __ror__(self, other):
        """
        当使用 | 操作符时，触发此方法。
        如果左边是字典，就调用 invoke 方法处理字典。
        如果不是字典，则继续构建管道。
        """
        if isinstance(other, dict):
            return RunnableSequence(DictAsRunnable(other), self)
        else:
            return RunnableSequence(self, other)

    def invoke(self, inputs):
        """
        处理输入数据的逻辑，如果输入是字典，
        我们递归处理字典的键值对。如果值是一个 Runnable，
        那么我们执行该 Runnable。
        """
        return self._invoke(inputs)

    def run(self, inputs):
        """
        该方法用于运行实际的处理逻辑，
        子类应该覆盖此方法来定义具体的行为。
        """
        raise NotImplementedError("This method should be implemented by subclasses")


class DictAsRunnable(Runnable):
    """
    将字典包装为 Runnable 对象。
    """

    def __init__(self, data):
        self.data = data

    def _invoke(self, inputs=None):
        if isinstance(self.data, dict):
            # 处理字典：递归处理键值对
            return {
                key: (val.invoke(inputs) if isinstance(val, Runnable) else val)
                for key, val in self.data.items()
            }
        else:
            return inputs  # 非字典直接返回


class RunnableSequence(Runnable):
    """
    实现 Runnable 的管道机制，允许链式调用。
    """

    def __init__(self, first, second):
        self.first = first  # 左边的 runnable
        self.second = second  # 右边的 runnable

    def _invoke(self, inputs):
        # 先执行左边的 runnable，然后把结果传递给右边的 runnable
        intermediate_result = self.first._invoke(inputs)
        return self.second.invoke(intermediate_result)


context = {"asd": "asd的上下文", "test": "test的上下文"}


class PromptRunnable(Runnable):
    """
    一个简单的子类，用于模拟 prompt 的行为。
    该类接收 context 和 question 并生成一个简单的回复。
    """

    def _invoke(self, inputs):
        context_key = inputs.get("context", "No context provided")
        question = inputs.get("question", "No question provided")
        return f"Context: {context[context_key]}, Question: {question}"


class RunnablePassthrough(Runnable):
    """
    简单的 Passthrough，不做任何修改，直接返回输入。
    """

    def _invoke(self, inputs=None):
        return inputs


# 测试运行示例
if __name__ == "__main__":
    # 定义几个 runnable
    retriever = RunnablePassthrough()
    prompt = PromptRunnable()

    # 创建一个字典，并通过管道传递给 prompt
    chain = {"context": retriever, "question": RunnablePassthrough()} | prompt

    # 执行管道
    result = chain  # 运行链式操作

    result = result.invoke("asd")
    print(result)
