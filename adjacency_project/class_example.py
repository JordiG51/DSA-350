def build_adjacency(data): # data is [("Ann", "Clem"),,,,]
    adj_dict = dict()
    for node in data: # node: ("Ann", "Clem") (tuple)
        a = node[0] #"Ann"
        b = node[1]
        if a in adj_dict:
            adj_dict[a].append(b)
        else:
            adj_dict[a] = [b]

        if b in adj_dict:
            adj_dict[b].append(a)

        else:
            adj_dict[b] = [a]
            
    return adj_dict

def display_adj(adj_dict):
    # itereate over keys and values in the dictionary
    for key, val in adj_dict.tems():
        print(f" {key} : {val}")
if __name__ == '__main__': # tuples are (node1, node2)
    data = [("Dan", "Bob"), ("Bob", "Clem"), ("Clem, Anita"), ("Anita", "Bob")], display_adj(build_adjacency(data))
