class Node:
    def __init__(self, ch):
        self.ch = ch
        self.depth = 0
        self.child = [None, None, None, None, None,
                     None, None, None, None, None,
                     None, None, None, None, None,
                     None, None, None, None, None,
                     None, None, None, None, None,
                     None]
    
    def add_node(self, cNode, ch):
        self.child[ord(ch)-97] = cNode
    
    def add_depth(self):
        self.depth += 1
        
    def find_queries(self, word):
        node = self
        for ch in word:
            if ch == '?':
                return node.depth
            if node.child[ord(ch) - 97] is not None:
                node = node.child[ord(ch) - 97]
            else:
                return 0
        
def make_tree(tree, word):
    for ch in word:
        if tree.child[ord(ch) - 97] is not None:
            tree.add_depth()
            tree = tree.child[ord(ch) - 97]
        else:
            cNode = Node(ch)
            tree.add_node(cNode, ch)
            tree.add_depth()
            tree = cNode
    
def solution(words, queries):
    answer = []
    front_trees = {}
    back_trees = {}
    lengths = []
    for word in words:
        length = len(word)
        if length not in lengths:#front_trees.keys():
            stNode = Node(ch='')
            make_tree(stNode, word)
            front_trees[length] = stNode
            stNode = Node(ch='')
            make_tree(stNode, word[::-1])
            back_trees[length] = stNode
            lengths.append(length)
        else:
            make_tree(front_trees[length], word)
            make_tree(back_trees[length], word[::-1])
    for query in queries:
        length = len(query)
        if length not in lengths:
            answer.append(0)
        elif '?' in query[0]:
            answer.append(back_trees[length].find_queries(query[::-1]))
        else:
            answer.append(front_trees[length].find_queries(query))
    return answer
