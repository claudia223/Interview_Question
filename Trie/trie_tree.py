import json
from graphviz import Digraph
import Levenshtein

"""

A data structure approach. The key idea behind a Trie is to store a set of strings in a way that shares 
common prefixes among them. This makes Trie trees highly efficient for tasks like searching for strings with 
a given prefix, finding all strings that match a specific pattern. However, given it concentrated on prefixes, 
it doesn't work very well with the given json. However, this approach allowed us to visualize the data in a tree
as can be seen png.

"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def print_trie(self, node=None, prefix=""):
        if node is None:
            node = self.root

        if node.is_end_of_word:
            print(prefix)

        for char, child_node in node.children.items():
            self.print_trie(child_node, prefix + char)

    def generate_dot(self, node=None, prefix="", dot=None):
        if dot is None:
            dot = Digraph(format='png', engine='dot', graph_attr={'dpi': '300'})

        if node is None:
            node = self.root

        if node.is_end_of_word:
            dot.node(prefix)

        for char, child_node in node.children.items():
            dot.edge(prefix, prefix + char)
            self.generate_dot(child_node, prefix + char, dot)

        return dot

            
def find_related_pairs(trie, max_levels=100, threshold=2):
    similar_pairs = set()

    def dfs(node, prefix, level):
        pairs = []
        if node.is_end_of_word:
            pairs.append((prefix, level))
        if level > 0:
            for char, child_node in node.children.items():
                pairs.extend(dfs(child_node, prefix + char, level - 1))
        return pairs
    
    def compare_words(word1, word2):
      return Levenshtein.distance(word1, word2) <= threshold
    
    for char, child_node in trie.root.children.items():
        similar_words = dfs(child_node, char, max_levels)
        for i, (word1,level1) in enumerate(similar_words):
            for j, (word2,level2) in enumerate(similar_words):
                if i != j and compare_words(word1, word2):
                    similar_pairs.add((min(word1, word2), max(word1, word2)))
    
    return similar_pairs

def main():
  # Load the JSON file containing the list of names
  with open("../org_names.json", "r") as file:
      data = json.load(file)
  
  trie = Trie()
  for name in data:
      name = name.strip().lower().replace(" ", "")
      trie.insert(name)
  
  # Generate the DOT representation and render the visualization
  # dot = trie.generate_dot()
  # dot.render("trie_visualization", format="png", cleanup=True)

  #trie.print_trie()

  related_pairs = find_related_pairs(trie)
  for pair in related_pairs:
      print(pair)
  print(len(related_pairs))

if __name__ == "__main__":
      main()