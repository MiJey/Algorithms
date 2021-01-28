import sys

sys.setrecursionlimit(10 ** 6)


# trie 자료구조 사용
# https://blog.ilkyu.kr/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-Trie-%ED%8A%B8%EB%9D%BC%EC%9D%B4-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
class Node(object):
    def __init__(self, key, data=None):
        self.key = key  # 노드가 가지고 있느 ㄴ
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

        curr_node.data = string

    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        if curr_node.data is not None:
            return True

    def query_search(self, curr_node, query):
        if len(query) == 0 and curr_node.data is not None:
            return 1

        next_nodes = []
        char = query[0]

        if char == '?':
            next_nodes += curr_node.children
        if char in curr_node.children:
            next_nodes.append(curr_node.children[char])
        else:
            return 0

        result = 0
        for next_node in next_nodes:
            result += self.query_search(next_node, query[1:])
        return result

    def dfs_count(self, query, curr_node, depth):
        # query 보다 긴 단어는 패스
        if depth > len(query):
            return 0

        if query[depth - 1] == '?' or curr_node.key == query[depth - 1]:
            # 쿼리와 완전히 일치하는 경우
            if depth == len(query) and curr_node.data is not None:
                return 1
        elif depth != 0:
            # 쿼리와 일치하지 않는 순간 패스(depth가 0일 땐 넘어감)
            return 0

        temp = 0
        for child in curr_node.children:
            next_node = curr_node.children[child]
            temp += self.dfs_count(query, next_node, depth + 1)

        return temp


def solution(words, queries):
    answer = []

    trie = Trie()

    for word in words:
        trie.insert(word)

    for query in queries:
        #answer.append(trie.dfs_count(query, trie.head, 0))
        answer.append(trie.query_search(trie.head, query))

    return answer


# 효율성 1, 2, 3은 통과 못하는 방식
def solution_fail(words, queries):
    answer = []

    for query in queries:
        result = 0

        for word in words:
            # 길이가 다르면 Fail
            if len(word) != len(query):
                continue

            flag = True
            for i in range(len(word)):
                if query[i] == '?':
                    continue

                # 중간에 하나라도 다르면 Fail
                if query[i] != word[i]:
                    flag = False
                    break

            # 길이도 같고, ?를 제외한 모든 글자가 같을 때 성공
            if flag:
                result += 1

        answer.append(result)

    return answer


sample_words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
sample_queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(sample_words, sample_queries))
