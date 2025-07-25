from __future__ import annotations

from node import Node

def query_selector_all(node: "Node", selector: str) -> list["Node"]:
    """
    Given a node, the function will return all nodes, including children,
    that match the given selector.
    """
    # (1) get every single node in the document into one big list
    all_nodes = []

    # highest, top-level node
    nodes_to_visit = [node]

    while len(nodes_to_visit):
        current_node = nodes_to_visit.pop(0)
        all_nodes.append(current_node)

        for n in current_node.children:
            nodes_to_visit.append(n)

    matching_nodes = []
    
    # (2) handle queries, like "h1, p"
    # need to check each part separately since the selector string can have multiple parts separated by commas
    list_of_queries = selector.split(',')

    for q in list_of_queries:
        query = q.strip()

        # if the query part is empty (e.g., from a trailing comma "h1,"), just skip it
        if not query:
            continue

        # (4) find the tag, class, and id of a single query
        # add spaces before '#' and '.' to make splitting easier
        # e.g. "p.intro#main" becomes "p .intro #main", which splits into ['p', '.intro', '#main']
        query_parts = query.replace('#', ' #').replace('.', ' .').split()

        tag_selector = None
        id_selector = None
        class_selectors = []
        
        for part in query_parts:
            if part.startswith('#'):
                id_selector = part[1:]

            elif part.startswith('.'):
                class_selectors.append(part[1:])

            else:
                tag_selector = part

                
        # (5) check every node from (1) against the query rules from (4)
        for node_to_check in all_nodes:
            # assume current node is a match until we find something that proves it isn't
            match = True

            # check the tag (e.g., is the query for a 'p' and is this node a 'p'?)
            if tag_selector and node_to_check.tag != tag_selector:
                 match = False
            
            # if tag matches...
            # check the ID match (e.g., is the query for '#main'?)
            if match and id_selector and node_to_check.attributes.get('id') != id_selector:
                match = False

            # if ID also matches...
            # check if node has all the required classes (e.g., '.class1.class2')
            if match and len(class_selectors) > 0:
                node_classes_string = node_to_check.attributes.get('class', '')
                node_classes_list = node_classes_string.split()
                
                for required_class in class_selectors:
                    if required_class not in node_classes_list:
                        match = False
                        break
            
            # (6) if it's a match, add it to our results list, but cannot add duplicates
            if match == True and node_to_check not in matching_nodes:
                    matching_nodes.append(node_to_check)

    return matching_nodes