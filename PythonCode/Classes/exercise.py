class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print (self.time)

clock = Clock('5:30')
clock.print_time()

class Weird(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getX(self):
        return x
    def getY(self):
        return y
class Wild(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def setBirthday(self,month,day,year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year,month,day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's ame is lexicographically
           less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """return self's name"""
        return self.name
    
