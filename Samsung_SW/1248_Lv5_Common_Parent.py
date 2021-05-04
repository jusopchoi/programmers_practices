class Node:
    def __init__(self, value, parent = None):
        self.value = value
        self.parent = parent
        if parent is not None:
	        self.parent.inc_size()
        self.size = 1
        
    def set_parent(self, parent):
        self.parent = parent
        tmp_parent = parent
        while tmp_parent != None:
            tmp_parent.inc_size(self.size)
            tmp_parent = tmp_parent.parent
    
    def inc_size(self, inc_size_value=1):
        self.size += inc_size_value
        
    def inc_size_recur(self):
        tmp_parent = self.parent
        while tmp_parent != None:
            tmp_parent.inc_size()
            tmp_parent = tmp_parent.parent

T = int(input())
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    V, E, node1, node2 = map(int, input().split())
    line = input().split()
    node_dic = {}
    for idx in range(0, len(line), 2):
        parent = int(line[idx])
        child = int(line[idx + 1])
        if parent not in node_dic:
            parent_node = Node(parent)
            node_dic[parent] = parent_node
        else:
            parent_node = node_dic[parent]
        if child not in node_dic:
            child_node = Node(child, parent_node)
            node_dic[child] = child_node
            parent_node.inc_size_recur()
        else:
            node_dic[child].set_parent(parent_node)
    parent = node_dic[node1].parent
    parent_list = []
    while parent is not None:
        parent_list.append(parent.value)
        parent = parent.parent
    parent = node_dic[node2].parent
    while parent is not None:
        if parent.value in parent_list:
            break
        parent = parent.parent
    print('#%d %d %d' % (test_case, parent.value, parent.size))
    # ///////////////////////////////////////////////////////////////////////////////////

