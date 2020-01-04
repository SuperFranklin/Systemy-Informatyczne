#Program ma za zadanie zmierzyć czas 10000 sortowań grafu zdefiniowanego w zmiennej graph

# Mapa przechowująca graf skierowany
graph = {0: set([1,3,6]),
         1: set([2,3]),
         2: set([3,4,5]),
         3: set([4,5]),
         4: set([5]),
         5: set(),
         6: set([5])}

#Funkcja sortujaca graf
def topoSort(graph):
    in_degree = dict()
    result = []
    queue = []

#Uzupełnia słownik in_degree zerami dla kluczy ze słownika graph
    for v in graph.keys():
        in_degree[v] = 0

#Zlicza ilość ścieżek prowadzących do wierzchołka v
    for key, value in graph.items():
        for v in value:
            in_degree[v]+=1

    print(in_degree)

#Sprawdza czy istnieje wierzchołek startowy - nie posiadajacy żadnej ścieżki prowadzącej do niego
#Jeżeli jest, to umiesza je w kolejce
    for key, value in in_degree.items():
        if value ==0:
            queue.append(key)

#Dopóki kolejka nie jest pusta
    while queue:
#Wyciaga ostatni wierzchołek z kolejki
#i dodaje go do tablicy wynikowej
        vertex = queue.pop()
        result.append(vertex)
#dla każdego elementu do którego prowadzi wyciagniety wierzchołek
        for child in graph[vertex]:
#jeżli dziecko nie jest jeszcze w tablicy wynikowej
            if child not in result:
                in_degree[child]-=1
                if in_degree[child] == 0:
                    queue.append(child)
    return result

start = time.time()
for x in range (0,10000):
    r = topoSort(graph)
end = time.time()
print(end-start)
print(r)
