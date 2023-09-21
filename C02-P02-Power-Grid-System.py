import csv

class House:
    def __init__(self, number, power):
        self.house_no = number
        self.power_required = power
        self.assigned_propagator_no = -1
        
    def assign_propagtor(self, number):
        self.assigned_propagator_no = number
    
    def __str__(self):
        return f"house_no: {self.house_no} power_required: {self.power_required}"
    
class Propagator:
    def __init__(self, number, max_power):
        self.propagator_no = number
        self.maximum_power = max_power
        self.power_remaining = max_power
        self.houses_connected = list()
        
    def __str__(self):
        return f"no : {self.propagator_no} max_power: {self.maximum_power} power_remaining: {self.power_remaining}"
    
    def connected_houses_info(self):
        
        for house in self.houses_connected:
            print(house)
    
    # check if the house is connected part of the list or not.           
    def is_house_present(self, house_no):
        
        #Iterating each element of the list of houses to find out if the house is present in the propagator or not
        for x in self.houses_connected: 
            if house_no == x.house_no:
                return True #Returns True if house is present in the propagator
            else:
                return False
        pass
    
    # Add the house in the list.
    # Before adding check if the house is already connected
    def add_house(self, house:House):
        
        if self.is_house_present(house.house_no): #Checking if house to be added is already present in the propagtor
            return False
        else:
            if(self.power_remaining >= house.power_required):
                self.power_remaining = self.power_remaining - house.power_required #When house is added, remaining power of propagator reduces by the amount of power required by the house
                self.houses_connected.append(house) #Adding house to a propagator
                
        pass
    
    # Remove the house from the list, before removing need to check
    # if the house is in the assigned propoagtor list. 
    def remove_house(self, house_no:int):
        
        for x in self.houses_connected:
            if house_no == x.house_no: #Checking if house number is present in the propagator or not
                if self.propagator_no == x.assigned_propagator_no: #Checking if the house is in the assigned propagator list
                    self.power_remaining = self.power_remaining + x.power_required #When a house is removed, power used by that house is restored back to the propagator
                    self.houses_connected.remove(x)
                    return True
        else:
            return False
        
    pass
                
                        
class PowerGrid:
    def __init__(self):
        self.propagators = dict()
        
    # Adding the propagtor into in the dictionary. 
    # Check if the propagator is not part of the dictioary already
    # It will not posess any value in the beginning. 
    def add_propagator(self, propagator:Propagator):
        if propagator.propagator_no not in self.propagators.keys(): #Checking if the propagator is part of the dictionary or not 
            self.propagators[propagator.propagator_no] = propagator #Adding a propagator to the dictionary
            return True
        else:
            return False
        
        #self.propagators[propagator.propagator_no] = propagator #Adding a propagator to the dictionary
        
        pass
        
    
    # Removing the propagtor into in the dictionary. 
    # Check if the propagator is part of the dictioary or not    
    def remove_propagator(self, propagator_no):
        
        if propagator_no in self.propagators.keys(): #Checking if the propagator is part of the dictioary or not  
            del self.propagators[propagator_no] #Removing the propagator from the dictionary 
            return True
        else:
            print("Propagator does not exist") #Prints this message if propagator to be deleted is not found in the dictionary
            return False
        
        pass
    
    def add_house(self, house:House, propagator_no:int):
        if propagator_no in self.propagators:
            return self.propagators[propagator_no].add_house(house)
        else:
            return False
        
    def remove_house(self, house_no:int, propagator_no:int):
        if propagator_no in self.propagators:
            return self.propagators[propagator_no].remove_house(house_no)
        else:
            return False

def create_power_grid():
    power_grid = PowerGrid()
    
    with open('app.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            
            entity_type = row['Type']
            
            if entity_type == "propagator":
                propagator = Propagator(int(row['Entity_Number']), int(row['Power']))
                power_grid.add_propagator(propagator)
            
            elif entity_type == "house":
                
                house = House(int(row['Entity_Number']), int(row['Power']))
                house.assigned_propagator_no = int(row['Assigned_Propagator'])
                
                power_grid.add_house(house, int(row['Assigned_Propagator']))
          
    return power_grid

if __name__ == "__main__":
    power_grid = create_power_grid()
    
    for _, propagator in power_grid.propagators.items():
        
        #Printing the propagator information
        print(f"Propagator No : {propagator.propagator_no}")
        print("------------Propagator Information-----------------")
        print(propagator)
        print("------------Connected Houses Information-----------------")
        propagator.connected_houses_info()
        print("\n")
        
    print("----Removing House 1014 from Propagator 1002----")
    if power_grid.remove_house(1014, 1002):
        print("House 1014 is successfully removed from Propagator 1002")
    else:
        print("House 1014 is not connected with Propagator 1002")
        
    
    print("\n----Removing House 1024 from Propagator 1003----")
    if power_grid.remove_house(1024, 1003):
        print("House 1024 is successfully removed from Propagator 1003")
    else:
        print("House 1024 is not connected with Propagator 1003")


    print("\n----Removing Propagator 1005----\n")
        
    if power_grid.remove_propagator(1005):
        print("Propagator 1005 and houses allocated removed successfully")
    else:
        print("Propagator 1005 is not present to be deleted")


    print("\n------Displaying propagator and houses connected after removing the houses above----\n")
        
    for _, propagator in power_grid.propagators.items():
        
        #Printing the propagator information
        print(f"Propagator No : {propagator.propagator_no}")
        print("------------Propagator Information-----------------")
        print(propagator)
        print("------------Connected Houses Information-----------------")
        propagator.connected_houses_info()
        print("\n")