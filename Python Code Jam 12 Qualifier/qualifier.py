from __future__ import annotations

from node import Node

# def query_selector_all(node: "Node", selector: str) -> list["Node"]:
#     nodes, q, seen = [], [node], set()
#     while q: n = q.pop(0); nodes.append(n); q.extend(n.children)
    
#     queries = [(lambda p: (next((i for i in p if i[0] not in '.#'), None), next((i[1:] for i in p if i[0] == '#'), None), {i[1:] for i in p if i[0] == '.'}))(s.strip().replace('#', ' #').replace('.', ' .').split()) for s in selector.split(',') if s.strip()]

#     return [seen.add(id(n)) or n for n in nodes if id(n) not in seen and any((not t or n.tag == t) and (not i or n.attributes.get('id') == i) and c.issubset(n.attributes.get('class', '').split()) for t, i, c in queries)][:]

def query_selector_all(node: "Node", selector: str) -> list["Node"]:
    """
    Given a node, the function will return all nodes, including children,
    that match the given selector.
    """
    # --- Part 1: Gather all nodes into a flat list ---
    all_nodes_in_tree = []
    nodes_to_visit = [node]
    while nodes_to_visit:
        current_node = nodes_to_visit.pop(0)
        all_nodes_in_tree.append(current_node)
        for child in current_node.children:
            nodes_to_visit.append(child)

    # --- Part 2: Prepare to store the results ---
    matching_nodes = []

    # --- Part 3: Process each query in the selector ---
    for single_query in selector.split(','):
        query = single_query.strip()
        if not query:
            continue

        # --- Part 4: Parse a single query ---
        parts = query.replace('#', ' #').replace('.', ' .').split()

        tag_selector = None
        id_selector = None
        class_selectors = []
        for part in parts:
            if part.startswith('#'):
                id_selector = part[1:]
            elif part.startswith('.'):
                class_selectors.append(part[1:])
            else:
                tag_selector = part

        # --- Part 5: Check every node against the parsed query ---
        for n in all_nodes_in_tree:
            is_a_match = True

            if tag_selector and n.tag != tag_selector:
                is_a_match = False

            if is_a_match and id_selector and n.attributes.get('id') != id_selector:
                is_a_match = False

            if is_a_match and class_selectors:
                node_classes_str = n.attributes.get('class', '')
                node_classes = node_classes_str.split()
                for required_class in class_selectors:
                    if required_class not in node_classes:
                        is_a_match = False
                        break

            # --- Part 6: If it's a match, add it to our list ---
            if is_a_match:
                if n not in matching_nodes:
                    matching_nodes.append(n)

    # --- Part 7: Return the final list ---
    return matching_nodes