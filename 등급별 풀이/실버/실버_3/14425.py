# Trie 알고리즘 활용 풀이
# class Node(object):
#     def __init__(self, key, data=None):
#         self.data = data
#         self.key = key
#         self.children = {}
        
# class Trie(object):
#     def __init__(self):
#         self.root = Node(None)
        
#     def insert(self, str):
#         cur_node = self.root
        
#         for s in str:
#             if s not in cur_node.children:
#                 cur_node.children[s] = Node(s)
#             cur_node = cur_node.children[s]
            
#         cur_node.data = str
    
#     def search(self, str):
#         cur = self.root
        
#         for s in str:
#             if s in cur.children:
#                 cur = cur.children[s]
#             else:
#                 return False
#         if cur.data == str:
#             return True
#         return False
    
# N, M = map(int, input().split())
# trie = Trie()
# result = 0

# for _ in range(N):
#     trie.insert(input())
    
# for _ in range(M):
#     s = input()
#     if trie.search(s):
#         result += 1
# print(result)

# 일반적인 풀이
N, M = map(int, input().split())
result = 0
dictionary = set([input() for _ in range(N)])
for _ in range(M):
    string = input()
    if string in dictionary:
        result += 1
print(result)