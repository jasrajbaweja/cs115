'''
CS 115, Lab 12, Inheritance

Author: Jasraj Baweja
Pledge: I pledge my honor that I have abided by the Stevens Honor System. -Jasraj Baweja
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 1 
' Implement missing sections of the Car class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Car(object):
    '''Write the constructor. It should take in four arguments:
       - make (a string, the company name, a.k.a. brand)
       - model (a string)
       - mpg (miles per gallon, a float)
       - tank_capacity (capacity of the gas tank in gallons, a float)
       These should all be assigned to corresponding private fields, i.e., with
       names that start with '__'.  Use the names in the 'str' method provided below.
       '''
    def __init__(self, make, model, mpg, tank_capacity):
        '''This function is the constructor method for class Car which takes in 4 different arguments'''
        self.__make = make
        self.__model = model
        self.__mpg = mpg
        self.__tank_capacity = tank_capacity
        
    '''Write getters for make, model, mpg, and tank_capacity.'''
    def get_make(self):
        '''This function returns the string of make'''
        return self.__make
    def get_model(self):
        '''This function returns the string of model'''
        return self.__model
    def get_mpg(self):
        '''This function returns the float of mpg'''
        return self.__mpg
    def get_tank_capacity(self):
        '''This function returns the float of tank_capacity'''
        return self.__tank_capacity
    
    '''Write setters for mpg and tank_capacity.'''
    def set_mpg(self,mpg):
        '''This function changes the value of the mpg in self'''
        self.__mpg = mpg
    def set_tank_capacity(self, tank_capacity):
        '''This function changes the value of tank_capacity in self'''
        self.__tank_capacity = tank_capacity
    
    '''Write a method called get_total_range.
       It returns the total distance the car can travel on a full tank of
       gas.'''
    def get_total_range(self):
        '''This function returns the total distance the car can
        travel on a full tank of gas'''
        gallon = self.get_mpg()
        tank = self.get_tank_capacity()
        total_distance = gallon * tank
        return total_distance

    def __str__(self):
        '''A string for printing information about a car.'''
        return self.__make + ' ' + self.__model + ', MPG: ' + str(self.__mpg) \
            + ', tank capacity: ' + str(self.__tank_capacity)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 2 
' Implement missing sections of the HybridCar class. 
' Make HybridCar be a subclass of Car.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class HybridCar(Car):  
    '''Write the constructor. It should take in 6 arguments:
    - the first four are the same as in the Car constructor
    - battery_kWh (battery power in kilowatt-hours, a float)
    - miles_per_kWh (miles per kilowatt-hours, a float)
    The additional fields must be private.
    '''
    def __init__(self, make, model, mpg, tank_capacity,battery_kWh, miles_per_kWh):
        '''This function is the constructor method for the hybrid car class'''
        Car.__init__(self,make, model, mpg, tank_capacity)
        self.__battery_kWh = battery_kWh
        self.__miles_per_kWh = miles_per_kWh
    def get_battery_kWh(self):
        '''This function returns the float of battery_kWh'''
        return self.__battery_kWh
    def get_miles_per_kWh(self):
        '''This function returns the float of miles_per_kWh'''
        return self.__miles_per_kWh
    '''Implement the following method.'''
    def get_battery_range(self):
        '''This function returns the total distance the car can
        travel on a fully charged battery'''
        power = self.get_battery_kWh()
        mpkWh = self.get_miles_per_kWh()
        distance = power*mpkWh
        return distance 
 
    '''Override the method get_total_range.
    Returns the total distance the car can travel on a full tank of
    gas and a fully charged battery.
    Do not do any math here except a single +. To get credit, you must call
    the methods you have already written.
    '''

    def get_total_range(self):
        '''This function returns the total distance the car can travel on
        a full tank of gas and a fully charged battery'''
        gasMaxDistance = Car.get_total_range(self)
        batteryMaxDistance = self.get_battery_range()
        return batteryMaxDistance + gasMaxDistance

    def __str__(self):
        '''A string for printing information about a car.'''
        return super().__str__() + ', battery kWh: ' + \
            str(self.__battery_kWh) + ', miles/kWh: ' + \
            str(self.__miles_per_kWh)
