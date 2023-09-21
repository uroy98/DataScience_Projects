import csv

class System:
    def __init__(self):
        self.sensors_list = list()
        self.sensor_mapping_list = list()
        self.master_node_list = list()
        
    def config_system(self, file):
        data_file = open(file, 'r')
        reader = csv.DictReader(data_file)
        for row in reader:
            node_id = row['Node ID']
            type = row['Type']
            master_node_id = row['Master Node ID']
            
            if type == 'Master':
                self.master_node_list.append(int(master_node_id))
            elif type == "Sensor":
                self.sensors_list.append(int(node_id))
                self.sensor_mapping_list.append(int(master_node_id))
                
        
    def SensorAssignedCount(self, mapping_list, l, r, OverloadSensor):
        count = 0
        for i in range(l, r+1):
            if (mapping_list[i] == OverloadSensor): 
                count +=  1
        return count
    
    def OverloadNodeHelper(self,l, r):
        frequency = {} #initialising a dictionary to store frequency of sensors for each master node
    
        if (l+r+1) > 1:
            
            # Finding the mid of the array
            mid = (l+r+1)//2
  
            # Dividing the array elements into 2 halves
    
            #First Half
            L = self.sensor_mapping_list[l:mid]
            
            #Second Half
            R = self.sensor_mapping_list[mid:r]
  
            # Dividing the first half
            self.OverloadNodeHelper(0, len(L)-1)
  
            # Dividing the second half
            self.OverloadNodeHelper(0, len(R)-1)
        
            i = j = 0
            
        
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                
                if L[i] < R[j]:
                    
                    if L[i] in frequency:
                        # incrementing the count
                        frequency[L[i]] += 1 #Storing frequency of a sensor in the dictionary
                        if frequency[L[i]] >=len(self.sensor_mapping_list)//2: #checking if the master node is overloaded
                            return L[i] #returning the overloaded master node
                        i += 1
                    else:
                        # initializing the count
                        frequency[L[i]] = 1
                        if frequency[L[i]] >=len(self.sensor_mapping_list)//2: #checking if the master node is overloaded
                            return L[i] #returning the overloaded master node
                        
                else:
                
                    if R[j] in frequency:
                        # incrementing the count
                        frequency[R[j]] += 1 #Storing frequency of a sensor in the dictionary
                        if frequency[R[j]] >=len(self.sensor_mapping_list)//2: #checking if the master node is overloaded
                            return R[j] #returning the overloaded master node
                        j += 1
                    else:
                        # initializing the count
                        frequency[R[j]] = 1  
                        if frequency[R[j]] >=len(self.sensor_mapping_list)//2: #checking if the master node is overloaded
                            return R[j] #returning the overloaded master node
                        
                
  
            # Checking if any element was left
            while i < len(L):
            
                if L[i] in frequency:
                    # incrementing the count
                    frequency[L[i]] += 1 #Storing frequency of a sensor in the dictionary
                    if frequency[L[i]] >=len(self.sensor_mapping_list)//2: #checking if the master node is overloaded
                            return L[i] #returning the overloaded master node
                    i += 1
                else:
                    # initializing the count
                    frequency[L[i]] = 1
                    if frequency[L[i]] >=len(self.sensor_mapping_list)//2: #checking if the master node is overloaded
                            return L[i] #returning the overloaded master node
                    
                
                
                
  
            while j < len(R):
               
                if R[j] in frequency:
                    # incrementing the count
                    frequency[R[j]] += 1 #Storing frequency of a sensor in the dictionary
                    if frequency[R[j]] >=len(self.sensor_mapping_list)//2: #checking if the master node is overloaded
                            return R[j] #returning the overloaded master node
                    j += 1
                else:
                    # initializing the count
                    frequency[R[j]] = 1
                    if frequency[R[j]] >=len(self.sensor_mapping_list)//2: #checking if the master node is overloaded
                            return R[j] #returning the overloaded master node
                    
                
      
        pass
        
    def getOverloadedNode(self):
        return self.OverloadNodeHelper(0, len(self.sensor_mapping_list)-1)
    
    def getPotentialOverloadNode(self):
        
        frequency = {} #initialising a dictionary to store frequency of sensors for each master node
        for item in self.sensor_mapping_list: #iterating through the list "sensor_mapping_list" to find frequency of sensors for each master node 
            # checking the sensor in dictionary
            if item in frequency:
                # incrementing the count
                frequency[item] += 1
            else:
                # initializing the count
                frequency[item] = 1
                
        for item in frequency: #iterating through the dictionary keys to find the  master node that is potentially overloaded
                if (frequency[item] >=len(self.sensor_mapping_list)//3) and (frequency[item] <len(self.sensor_mapping_list)//2):
                    return item #returns the potentially overloaded master node
        return -1 #returns -1 if there are no potentially overloaded master nodes
        
        pass
    
if __name__ == "__main__":
    test_system1 = System()
    
    test_system1.config_system('app_data1.csv')
    
    print("Overloded Master Node : ", test_system1.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system1.getPotentialOverloadNode())

    test_system2 = System()
    
    test_system2.config_system('app_data2.csv')
    
    print("Overloded Master Node : ", test_system2.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system2.getPotentialOverloadNode())

    test_system3 = System()

    test_system3.config_system('app_data3.csv')
    
    print("Overloded Master Node : ", test_system3.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system3.getPotentialOverloadNode())

    test_system4 = System()

    test_system4.config_system('app_data4.csv')
    
    print("Overloded Master Node : ", test_system4.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system4.getPotentialOverloadNode())
