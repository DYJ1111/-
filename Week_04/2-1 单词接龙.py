class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bfs
        # time: O(len(wordlist) * len(word)), space: O(queue + wordlist)
        wordsets = set(wordList)
        if endWord not in wordList:
            return 0
        from collections import deque
        queue = deque()
        queue.append((beginWord, 1))
        while queue:
            cur_word, count = queue.popleft()
            if cur_word == endWord:
                return count
            for i in range(len(cur_word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = cur_word[:i] + ch + cur_word[i+1:]
                    if new_word in wordsets:
                        queue.append((new_word, count+1))
                        wordsets.remove(new_word)
        return 0