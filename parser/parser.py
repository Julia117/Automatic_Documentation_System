import os
from tree_sitter import Language, Parser
import tree_sitter_python as tspython


def read_file(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def walk_files(root, extensions=None):
    for dirpath, _, filenames in os.walk(root):
        for file in filenames:
            if extensions is None or any(file.endswith(ext) for ext in extensions):
                yield os.path.join(dirpath, file)


def get_node_text(node, code):
    return code[node.start_byte:node.end_byte].decode("utf-8", errors="ignore")


def extract_python_symbols(tree, code):
    """
    Returns a list of dicts:
      - type: 'function' | 'class'
      - name
      - code
      - docstring
      - imports
      - start_line, end_line
    """
    root = tree.root_node
    symbols = []

    def extract_docstring(node):
        try:
            if node.child_count > 0:
                first = node.children[0]
                if first.type == "expression_statement" and first.children and first.children[0].type == "string":
                    return get_node_text(first, code)
        except Exception:
            pass
        return ""

    stack = [root]
    while stack:
        node = stack.pop()
        if node.type in ("function_definition", "class_definition"):
            name_node = None
            for child in node.children:
                if child.type == "identifier":
                    name_node = child
                    break

            name = get_node_text(name_node, code) if name_node else "<unknown>"
            chunk_code = get_node_text(node, code)

            docstring = extract_docstring(node)

            symbols.append({
                "type": "function" if node.type == "function_definition" else "class",
                "name": name,
                "code": chunk_code,
                "docstring": docstring,
                "start_line": node.start_point[0],
                "end_line": node.end_point[0],
            })

        # Continue traversal
        for child in node.children:
            stack.append(child)

    return symbols


def extract_imports(tree, code):
    imports = []
    root = tree.root_node

    for node in root.children:
        if node.type in ("import_statement", "import_from_statement"):
            imports.append(get_node_text(node, code))
    return imports


def parse_codebase(root_folder, extensions=[".py"]):
    from tree_sitter import Parser

    PY_LANGUAGE = Language(tspython.language())
    parser = Parser(PY_LANGUAGE)

    all_chunks = []

    for path in walk_files(root_folder, extensions):
        raw = read_file(path)
        try:
            tree = parser.parse(bytes(raw.encode("utf-8")))
        except Exception as e:
            print(f"Skipping {path} due to parse error: {e}")
            continue

        symbols = extract_python_symbols(tree, raw.encode("utf-8"))
        imports = extract_imports(tree, raw.encode("utf-8"))

        for s in symbols:
            chunk = {
                "file": path,
                "type": s["type"],
                "name": s["name"],
                "code": s["code"],
                "docstring": s["docstring"],
                "imports": imports,
                "start_line": s["start_line"],
                "end_line": s["end_line"],
            }
            all_chunks.append(chunk)

    return all_chunks
