'''
Program to find the brightest star in the range provided.
This basically aims at finding the star with the lowest magnitude.
'''
class StarCatalog(object):
   
    def __init__(self):      
        pass
    
'''This function loads the  text file into the program with the help of inbuilt split function'''
def loadCatalog(self, starFile=None):            
        if starFile == None:
            raise ValueError("StarCatalog.loadCatalog: Missing parameter")
        if not(isinstance(starFile, str)):
            raise ValueError("StarCatalog.loadCatalog: Non string parameter")
        try:
            myFile = open(starFile,'r')
            for lines in myFile:
                myStarData = lines.split()
                self.catalog.append(myStarData)
        except:
            raise ValueError("StarCatalog.loadCatalog: Bad file or file value")
        
'''  This function is to empty the catalogue '''
def emptyCatalog(self):
        del self.catalog[:]
    
''' This gives the total count of the stars  '''
def getStarCount(self, lowerMagnitude=None, upperMagnitude=None):
        self.count = 0
        if lowerMagnitude == None:
            lowerMagnitude = 0
        if upperMagnitude == None:
            upperMagnitude = 9
        if upperMagnitude <= lowerMagnitude:
            raise ValueError("StarCatalog.getStarCount: upper bound lower than lower bound")
        if upperMagnitude < 0:
            raise ValueError("StarCatalog.getStarCount: bad parameter")
        for SingleStar in self.catalog:
            if SingleStar[1] >= lowerMagnitude and SingleStar[1] <= upperMagnitude:
                self.count += 1
        return self.count
    
def getMagnitude(self, rightAscentionCenterPoint=None, declinationCenterPoint=None, fieldOfView=None):
        self.lowestMagnitude = 9
        for SingleStar in self.catalog:
            rA = SingleStar[2]
            dC = SingleStar[3]
            if rA < (rightAscentionCenterPoint + (0.5 * fieldOfView)) and rA > (rightAscentionCenterPoint - (0.5 * fieldOfView)) and dC < (declinationCenterPoint + (0.5 * fieldOfView)) and dC > (declinationCenterPoint - (0.5 * fieldOfView)):
                if (SingleStar[1] < self.lowestMagnitude):
                    self.lowestMagnitude = SingleStar[1]
        if self.lowestMagnitude == 9:
            return None
        return self.lowestMagnitude
        