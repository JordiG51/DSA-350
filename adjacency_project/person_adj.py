import random

class Person:

    def __init__(self,first_name, last_name,):
        self.first_name = first_name
        self.last_name = last_name
        self.num_of_friends = 0
        self.id = random.randint(1000,9999)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f" {self.full_name()} ({self.id})"

    def update(self):
        self.num_of_friends += 1
    

        
def build_adjacency(data): # data is [("Ann", "Clem"),,,,]
    adj_dict = dict()
    for node in data: # node: ("Ann", "Clem") (tuple)
        a = node[0] #"Ann"
        b = node[1]
        if a in adj_dict:
            adj_dict[a].append(b)
        else:
            adj_dict[a] = [b]
        a.update()
        if b in adj_dict:
            adj_dict[b].append(a)

        else:
            adj_dict[b] = [a]
        b.update()
    return adj_dict

def display_adj(adj_dict):
    # itereate over keys and values in the dictionary
    for person, friends_list in adj_dict.items():
        print(f"{person.id}: {person.full_name()}, number of friends: {person.num_of_friends}")

        for friend in friends_list:
            print(f" {friend}")

if __name__ == '__main__':
    p1 = Person("Anita", "Racinez")
    p2 = Person("Clem", "Jameson")
    p3 = Person("Lars", "Eriksson")
    p4 = Person("Jed", "Jones")
    data = [(p1, p2), (p2, p3), (p1, p4), (p2, p4)]
    display_adj(build_adjacency(data))
