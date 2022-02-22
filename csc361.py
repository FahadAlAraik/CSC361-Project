import pandas as pd
from collections import deque


citiesForVetrices = pd.read_excel("C:/Users/Fahad/Documents/cities.xlsx", sheet_name="Sheet1")

data = pd.read_excel("C:/Users/Fahad/Documents/cities.xlsx", sheet_name="Sheet2")
cities_dic = {}
var = 0
for i in range(len(data)):
    cities_dic[data.loc[i][0]] = []

for i in range(len(data)):
    cities_dic[data.loc[i][0]].append([data.loc[i][1], float(data.loc[i][2])])


maxSize =0
generatedNodes = 0
def bfs(graph, start, end):
    # maintain a queue of paths
    global maxSize
    global generatedNodes
    queue = []
    visited = []
    # push the first path into the queue
    queue.append([start])
    visited.append(start)
    generatedNodes +=1

    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]

        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a
        # new path and push it into the queue
        for adjacent in graph.get(node, []):
            visited.append(adjacent[0])
            new_path = list(path)
            new_path.append(adjacent[0])
            queue.append(new_path)
            generatedNodes +=1

        maxSize = max(len(queue) , maxSize)


queue = []
path = ['Al Hariq']
for adjacent in cities_dic.get('Al Hariq',[]):
        new_path = list(path)
        new_path.append(adjacent[0])
        queue.append(new_path)
print(bfs(cities_dic,'Riyadh' , 'Dhurma'))
print(maxSize)
print(generatedNodes)



#print(bfsSearch("Riyadh","Marat"))

def path_cost(path):
    total_cost=0
    for (node,cost)in path:
        total_cost+= cost
    return total_cost,path[-1][0]


def ucs(dic,start,goal):
    visit=[]
    queue=[[(start,0)]]
    while queue:
        print(queue)
        queue.sort(key=path_cost, reverse = True)
        path=queue.pop()
        node=path[-1][0]
        if node in visit:
            continue
        visit.append(node)
        if node == goal:
            return path
        else:
            adjecent=dic.get(node,[])
            for(node2,cost) in adjecent:
                new_path=path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)


#print(ucs(cities_dic,'Riyadh' , 'Howtat Bani Tamim'))