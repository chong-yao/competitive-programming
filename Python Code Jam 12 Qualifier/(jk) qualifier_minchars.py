from __future__ import annotations

from node import Node

# this piece of code below is made for giggles and laughs, not to be taken seriously

def query_selector_all(node: "Node", selector: str) -> list["Node"]:
    """
    Given a node, the function will return all nodes, including children,
    that match the given selector.
    
    This is a version that focuses on "as few characters as possible".
    Made with Gemini 2.5 Pro, then DeepSeek R1, then Qwen Coder.
    """
    return [n for n in (lambda f:f(f,node))(lambda f,n:[n]+[i for c in n.children for i in f(f,c)]) if any((not(t:=next((x for x in p if x[0].isalnum()),''))or n.tag==t)and(not(i:=next((x[1:]for x in p if x[0]=='#'),''))or n.attributes.get('id','')==i)and all(k in n.attributes.get('class','').split()for k in[x[1:]for x in p if x[0]=='.'])for p in[q.strip().replace('#',' #').replace('.',' .').split()for q in selector.split(',')if q.strip()])]