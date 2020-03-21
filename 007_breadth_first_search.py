from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(p):
    return p[-1] == "m"

def breadth_first_search(name):
    l = deque()
    l.extend(graph[name])
    searched = []
    while l:
        p = l.popleft()
        if p not in searched:
            if person_is_seller(p):
                print(p, "is a mango seller!")
                return True
            else:
                l.extend(graph[p])
                searched.append(p)
    return False

assert breadth_first_search("you") == True