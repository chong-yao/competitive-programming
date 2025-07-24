from __future__ import annotations
from node import Node

def _parse_selector_part(part: str) -> dict:
    """
    Parses a single selector string (e.g., 'tag#id.class') into its components.
    
    This function uses string replacements to easily split the selector part
    into tag, id, and classes.
    """
    # By adding spaces before '#' and '.', we can split the string easily.
    processed_part = part.replace("#", " #").replace(".", " .")
    components = processed_part.split()

    tag = None
    element_id = None
    classes = []

    # The first component is the tag if it doesn't start with '#' or '.'
    if components and not components[0].startswith(("#", ".")):
        tag = components.pop(0)

    # Identify the ID and classes from the remaining components
    for comp in components:
        if comp.startswith("#"):
            element_id = comp[1:]  # Get the ID without the '#'
        elif comp.startswith("."):
            classes.append(comp[1:]) # Get the class name without the '.'

    return {"tag": tag, "id": element_id, "classes": classes}

def _node_matches_part(node: Node, parsed_part: dict) -> bool:
    """
    Checks if a single node matches the rules from a parsed selector part.
    Returns True if it's a match, False otherwise.
    """
    # 1. Check if the tag matches
    if parsed_part["tag"] and node.tag != parsed_part["tag"]:
        return False

    # 2. Check if the ID matches
    if parsed_part["id"] and node.attributes.get("id") != parsed_part["id"]:
        return False

    # 3. Check if all required classes are present
    if parsed_part["classes"]:
        # Get the node's classes as a set for efficient checking.
        node_classes_str = node.attributes.get("class", "")
        node_classes = set(node_classes_str.split())
        required_classes = set(parsed_part["classes"])
        # The node must have all the classes specified in the selector.
        if not required_classes.issubset(node_classes):
            return False

    # If all checks passed, it's a match
    return True

def _traverse_and_collect_all_nodes(node: Node) -> list[Node]:
    """
    Traverses the node tree starting from the given node using Breadth-First Search (BFS)
    and returns a flat list of all nodes in the tree.
    """
    all_nodes = []
    nodes_to_visit = [node]  # Initialize a queue for BFS

    while nodes_to_visit:
        current_node = nodes_to_visit.pop(0) # Get the next node to process
        all_nodes.append(current_node)
        
        # Add all children of the current node to the queue to be visited later
        nodes_to_visit.extend(current_node.children)
        
    return all_nodes

def query_selector_all(node: Node, selector: str) -> list[Node]:
    """
    Given a starting node and a selector string, this function finds all
    nodes in the tree that match the selector's rules.
    """
    # Use a list to store found nodes to avoid the hashing issue with sets.
    # We will manually check for duplicates before adding.
    found_nodes = []

    # Get a flat list of every single node in the document tree.
    all_nodes_in_document = _traverse_and_collect_all_nodes(node)

    # A selector can have multiple parts, like "h1, .button, #main".
    # They are split by the comma to handle each one separately.
    selector_parts = [part.strip() for part in selector.split(',')]

    # Process each selector part individually.
    for part in selector_parts:
        # Turn the text part like "p.important" into understandable rules.
        parsed_part = _parse_selector_part(part)
        
        # Check every node in the document against the current rule.
        for n in all_nodes_in_document:
            # If the node matches the rules and is not already in our list...
            if _node_matches_part(n, parsed_part) and n not in found_nodes:
                # ...add it to our collection of found nodes.
                found_nodes.append(n)

    # Return the list of unique matching nodes.
    return found_nodes