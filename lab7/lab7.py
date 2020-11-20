from collections import Counter

class Node: # Node used in BinaryTree
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree: # Simple Binary Tree, no specific implementation of Huffman Coding
    def __init__(self, root):
        self.root = root # BinaryTree class only stores root node

    # We can actually express binary trees using only class Node, but class BinaryTree exists to implement some helper functions, and diffrentiate between Node and Tree
    @staticmethod
    def insert_left(parent, child):
        parent.left = child
    
    @staticmethod
    def insert_right(parent, child):
        parent.right = child
    
    @staticmethod
    def delete_left(parent):
        parent.left = None
    
    @staticmethod
    def delete_right(parent):
        parent.right = None
    
    @staticmethod
    def merge(left_tree, right_tree, root_data): # attach(merge) two trees
        root = Node(root_data)
        parent_tree = BinaryTree(root)
        
        BinaryTree.insert_left(parent_tree.root, left_tree.root)
        BinaryTree.insert_right(parent_tree.root, right_tree.root)
        
        return parent_tree
        
def construct_huffman_tree(original_string): # construct huffman tree from original string
    count = Counter(original_string)
    tree_list = []
    
    for char, freq in count.items(): # make a tree for each characters, with node data of character and frequency
        node = Node((char, freq))
        tree = BinaryTree(node)
        tree_list.append(tree)

    while len(tree_list) > 1: # merge 2 minimum value trees while we have only 1 tree left

        min1_idx, min1 = min(enumerate(tree_list), key=lambda x: x[1].root.data[1]) # get min freq count tree
        tree_list.pop(min1_idx)

        min2_idx, min2 = min(enumerate(tree_list), key=lambda x: x[1].root.data[1]) # get min freq count tree
        tree_list.pop(min2_idx)

        new_root_data = (None, min1.root.data[1] + min2.root.data[1])

        if min1.root.data[1] < min2.root.data[1]:
            merged_tree = BinaryTree.merge(min1, min2, new_root_data)
        else:
            merged_tree = BinaryTree.merge(min2, min1, new_root_data)

        tree_list.append(merged_tree)
    
    huffman_tree = tree_list[0]
    return huffman_tree

def extract_huffman_code(huffman_tree): # extract code by traversing huffman tree recursively
    code_dict = {}
    def traverse_huffman_tree(root, code = ""):
        if root.data[0] != None: # leaf node
            code_dict[root.data[0]] = code
        else:
            traverse_huffman_tree(root.left, code + "0")
            traverse_huffman_tree(root.right, code + "1")
    
    traverse_huffman_tree(huffman_tree.root)
    return code_dict

def decode_huffman(huffman_tree, encoded_string): # decode string by searching huffman tree
    decoded_string = ""
    current_node = huffman_tree.root
    
    for char in encoded_string:
        
        if char == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.data[0] != None: # leaf node
            decoded_string += current_node.data[0]
            current_node = huffman_tree.root
    
    return decoded_string



# Huffman Coding
if __name__=="__main__":
    original_string = "AAAABBCDDEEFFFFFFFF"
    example_string = "ABBCCCDDDDEEEEEFFFFFF"
    
    ## Construct Huffman Tree
    huffman_tree = construct_huffman_tree(original_string)
    huffman_tree_example = construct_huffman_tree(example_string)
   
    ## Extract Characters from Huffman Tree
    code_dict = extract_huffman_code(huffman_tree)
    print("huffman code with string", original_string, code_dict)
    code_dict_example = extract_huffman_code(huffman_tree_example)
    print("huffman code with example string",example_string, code_dict_example)
    
    ## Encode Characters with Huffman Coding
    encoded_string = ""
    for char in original_string:
        encoded_string += code_dict[char]
    print("huffman encoded string", original_string, encoded_string)
    encoded_string_example = ""
    for char in example_string:
        encoded_string_example += code_dict_example[char]
    print("huffman encoded example string", example_string, encoded_string_example)
    
    assert(encoded_string_example == "100010011001101101101000000000101010101111111111111") # test example string with lab pdf answer
    
    ## Decompress Compressed Code into Original String
    decoded_string = decode_huffman(huffman_tree, encoded_string)
    decoded_string_example = decode_huffman(huffman_tree_example, encoded_string_example)
    
    print("huffman decoded string", decoded_string)
    print("huffman decoded example string", decoded_string_example)
    
    assert(decoded_string == original_string) # test decoded string is same with original
    assert(decoded_string_example == example_string) 
    