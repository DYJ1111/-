class Trie:
    """
    字典树，Trie树，单词查找树，键树
    
    优点：
    最大限度地减少无谓的字符串比较，查询效率高于哈希表

    基本性质
    1 根节点不包含字符，除根节点外每个节点都包含一个字符
    2 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串
    3 每个节点的所有子节点路径代表的字符都不相同

    核心思想：
    1 空间换时间
    2 利用字符串的公共前缀来降低查询时间的开销，以达到提高效率的目的

    典型应用：
    用于统计和排序大量的字符串（不限于字符串），例如被搜索引擎用于文本词频统计
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = '#'

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node[self.end_of_word] = self.end_of_word  # 单词结束标志

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return self.end_of_word in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True