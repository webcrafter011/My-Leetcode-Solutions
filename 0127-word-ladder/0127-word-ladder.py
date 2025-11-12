class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pattern_dict = defaultdict(list)

        # building a graph of all the corresponding patterns 
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                pattern_dict[pattern].append(word)
        
        # start bfs 
        q = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)

        
        while q:
            word, curr_seq = q.popleft()
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                for similar_word in pattern_dict[pattern]:
                    if similar_word == endWord:
                        return curr_seq + 1
                    elif similar_word not in visited:
                        visited.add(similar_word)
                        q.append((similar_word, curr_seq + 1))

        return 0


        
            