import csv

#Method to find indexes of nodes to traverse from source to destination for find_route()

def rec(source,destination,visited =[]):
  visited.append(source)
  t = test_system1.get_neighbours(source[0],source[1])
  if( destination in t):
    return source,destination
  if(len(t) == 0 ):
    return
  a=[x for x in t if x not in visited]
  for i in a:
    x = rec(i,destination,visited)
    if x is not None:
      return source,x

#Method to find indexes of nodes to traverse from source to destination for Bluevalley_to_Smallville_route()

def rec1(source,destination,visited =[]):
  visited.append(source)
  t = test_system1.get_neighbours(source[0],source[1])
  if( destination in t):
    return source,destination
  if(len(t) == 0 ):
    return
  a=[x for x in t if x not in visited]
  for i in a:
    x = rec1(i,destination,visited)
    if x is not None:
      return source,x
      


class System:
    steps = [   
        [-1,0], # Top Step
        [0,1],  # Right Step
        [1,0], # Bottom Step
        [0,-1] # Left Step
    ]
    
    def __init__(self):
        self.star_city = list()
        self.star_city_rows = 0
        self.star_city_cols = 0
        
    def config_system(self, file):
        data_file = open(file, 'r')
        reader = csv.reader(data_file)
        self.star_city=list()
        for row in reader:
            self.star_city.append(row)
        self.star_city_rows=len(self.star_city)
        self.star_city_cols=len(self.star_city[0])

    def check_limits(self,row_num, col_num):
        if 0 <= row_num < self.star_city_rows and 0 <= col_num < self.star_city_cols:
            return True
        return False

    def get_neighbours(self,row,col):
        neighbours=[]
        #loop through top, right, bottom and left adjacent nodes to get the neighbor
        # only if the altitude of adjacent node is lower or equal to the current node 
        # and is not already present in neighbors list
        for i in System.steps:
            if self.check_limits(row+i[0], col+i[1]):
                if self.star_city[row+i[0]][col+i[1]] <= self.star_city[row][col] and (row+i[0],col+i[1]) not in neighbours:
                    neighbours.append((row+i[0],col+i[1]))
        return neighbours
    
    def find_route(self,source,destination):
        path = rec(source,destination) #path from source to destination
        t = path
        a = []
        while True  :
            a.append(path[0])
            path = path[1]
            if(destination==path):
                break
            else:
                if (type(path[1]) != tuple):
                    a.append(path)
                    break
                    
        if path != None: #returning path and 1 if path is found
            return a,1

    def Bluevalley_to_Smallville_route(self):
        s = []
        s1 = {}
        
        d = []
        d1 = {}
        #Storing border nodes and indexes for city Smallville and Bluevalley in dictionaries s1 and d1 
        for i in range(self.star_city_rows):
            s.append(self.star_city[i][0])
            s1[self.star_city[i][0]] = (i,0)
            
            d.append(self.star_city[i][self.star_city_cols-1])
            d1[self.star_city[i][self.star_city_cols-1]] = (i,self.star_city_cols-1)
    
        #picked source node 
        s = max(s)
        s_index = s1[s]
        
        #picked destination node
        d = min(d)
        d_index = d1[d]
        
        path1 = rec1(s_index,d_index) #path from source to destination
        t = path1
        a = []
        while True  :
            a.append(path1[0])
            path1 = path1[1]
            if (type(path1[1]) != tuple):
                a.append(path1)
                break
        print(f"\n\nTo reach from Node Bluevalley{s_index} from Node Smallville{d_index} the nodes traversed are-")
        
        #printing the path from source to destination
        x = len(a)
        c = 0
        for node in a:
            c=c+1
            if c!= (len(a)):
                print(f"({node[0]},{node[1]}) ---->", end=" ")
            else:
                print(f"({node[0]},{node[1]})", end=" ")



if __name__ == "__main__":
    test_system1 = System()
    
    #Getting data in 2D matrix
    test_system1.config_system('city_data.csv')
    
    #Finding path between Source node to Destination node
    route,_ = test_system1.find_route((3,0),(4,2))
    print(f"\n\nTo reach Node (4,2) from Node (3,0) the nodes traversed are-")
    for node in route:
        print(f"({node[0]},{node[1]}) ---->", end=" ")
    print((4,2))
    
    #Finding path between Bluevalley to Smallville   
    test_system1.Bluevalley_to_Smallville_route()
    