"""Програма максимум:
Написати алгоритм, що буде парсити html документ та зберігати його Document Object Model (DOM) у дереві. 
Дерево повинно зберігати тег та текст, обрамлений цим тегом (якщо є такий). 
Додати можливість пошуку тексту за тегом.
Вхідні дані: html документ та тег
Вихідні дані: текст, якщо є."""
from html.parser import HTMLParser
class TreeNode:
    def __init__(self, tag, text=''):
        self.tag = tag
        self.text = text
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def build_tree(element):
        if element.name is None:
            # Це текст між тегами
            return Node("text", element.string.strip() if element.string else "")
    
        node = Node(element.name)
        for child in element.children:
            child_node = build_tree(child)
            if child_node:
                node.children.append(child_node)
        return node
    
    def find_by_tag(self, tag):
        results = []
        if self.tag == tag:
            results.append(self.text)
        for child in self.children:
            results.extend(child.find_by_tag(tag))
        return results
    
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = TreeNode("root")  # умовний корінь
        self.stack = [self.root]      # стек для поточного батька

    def handle_starttag(self, tag, attrs):
        node = TreeNode(tag)
        self.stack[-1].add_child(node)
        self.stack.append(node)

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1].tag == tag:
            self.stack.pop()

    def handle_data(self, data):
        text = data.strip()
        if text:
            self.stack[-1].text += text

def print_tree(node, level=0):
    print("    " * level + f"{node.tag}: {node.text}")
    for child in node.children:
        print_tree(child, level + 1)

if __name__ == "__main__":
    html = "<div><p>Hello</p><span>World</span><p>Another</p></div>"

    parser = MyHTMLParser()
    parser.feed(html)
    root = parser.root

    print("DOM-tree:")
    print_tree(root)

    # Пошук тексту за тегом
    texts_p = root.find_by_tag("p")
    texts_span = root.find_by_tag("span")
    print("\nТексти в <p>:", texts_p)
    print("Тексти в <span>:", texts_span)
