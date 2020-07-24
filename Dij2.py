#python 3.8.1 doesnt work with Pyton 2 
def dijk(dict, Usersource, UserDest ,seen=[], dist={}, former={}): 
    if Usersource == UserDest: #if src and dst are equal the shortest knownPath is created and shown
        prior=UserDest
        knownPath=[]
        while (prior != None):
            knownPath.append(prior)
            prior=former.get(prior,None)
        return knownPath, dist[UserDest]
    else :     
        if not seen: #if first time visiting the node, set the cost is set to 0
            dist[Usersource]=0
        for Neighbour in dict[Usersource] : #loop through its Neighbours
            if Neighbour not in seen:
                nDist = dist[Usersource] + dict[Usersource][Neighbour] #setting distance to new Neighbour
                if nDist < dist.get(Neighbour, float('inf')):
                    dist[Neighbour] = nDist
                    former[Neighbour] = Usersource
        seen.append(Usersource) #becomes part of seen and no longet in not seen
        #Here I am using Djkstras to calc shortest knownPath
        unseen={} #takes lowest dist  with source as x
        for d in dict:
            if d not in seen:
                unseen[d] = dist.get(d,float('inf'))
        MinDist=min(unseen, key = unseen.get)
        return dijk(dict,MinDist,UserDest,seen,dist,former)

dict = {'U': {'V' : 2, 'X' : 1, 'W' : 5},
        'V': {'X' : 2, 'W' : 3, 'U' : 2}, 
        'W':{'U' : 5, 'V' : 3, 'X' : 3,'Y':1, 'Z':5},
        'X':{'U' : 1, 'V' : 2, 'W' : 3,'Y':1},
        'Y':{'X' : 1, 'W' : 1, 'Z' : 2},
        'Z':{'W' : 5, 'Y' : 2}
        } 
print("To     |   Next")
print("----------------------")

ListShortestPath, ShortestPathCost = dijk(dict,'U','X')
#print("{}\nMin total cost = {}".format(list(reversed(ListShortestPath)), ShortestPathCost))
print("X      | {}".format(list(reversed(ListShortestPath))[0:2]))


ListShortestPath, ShortestPathCost = dijk(dict,'U','V')
#print("\nMin total cost = {}".format(list(reversed(ListShortestPath)), ShortestPathCost))
print("V      | {}".format(list(reversed(ListShortestPath))[0:2]))

ListShortestPath, ShortestPathCost = dijk(dict,'U','Y')
##print("Shortest knownPath = {}\nMin total cost = {}".format(list(reversed(ListShortestPath)), ShortestPathCost))
print("Y      | {}".format(list(reversed(ListShortestPath))[0:2]))

ListShortestPath, ShortestPathCost = dijk(dict,'U','W')
#print("Shortest knownPath = {}\nMin total cost = {}".format(list(reversed(ListShortestPath)), ShortestPathCost))
print("W      | {}".format(list(reversed(ListShortestPath))[0:2]))


ListShortestPath, ShortestPathCost = dijk(dict,'U','Z')
#print("Shortest knownPath = {}\nMin total cost = {}".format(list(reversed(ListShortestPath)), ShortestPathCost))
print("Z      | {}".format(list(reversed(ListShortestPath))[0:2]))


ListShortestPath, ShortestPathCost = dijk(dict,'U','U')
#print("Shortest knownPath = {}\nMin total cost = {}".format(list(reversed(ListShortestPath)), ShortestPathCost))
print("U      | {}".format(list(reversed(ListShortestPath))[0:2]))



