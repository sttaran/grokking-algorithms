import collections

graph = {}
# FIRST CHAIN LINK. You are Adam and you search a seller
graph["Adam"] = ["Avram",  "Bollet"]

# CHAIN FROM ADAM
graph["Avram"] = ["Sandra", "Late Seller"]
graph["Bollet"] = ["Valera Seller"]

graph["Sandra"] = []
graph["Late Seller"] = []
graph["Valera Seller"] = []


def is_seller(name):
    return "Seller" in name


def search_of_seller(name):
    search_queue = collections.deque()
    search_queue += graph[name]
    searched_persons = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched_persons:
            if is_seller(person):
                print(f"I got it. {person} is a seller!")
                return True
            else:
                if graph[person]:
                    search_queue += graph[person]
                    print(f'{person} not a seller!')
                    searched_persons.append(person)
                else:
                    continue

    return False


search_of_seller("Adam")
