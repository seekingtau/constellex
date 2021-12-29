import random
import pandas as pd
from random import randint, seed
import numpy as np

# Seed random
seed(randint(0,1000))

# Planet varieties
planetTypesLivable = ['rocky', 'ocean', 'green', 'gas']
planetTypesCold = ['rocky', 'icy', 'gas']
planetTypesHot = ['rocky', 'ocean', 'gas']

# Name list
planetNameSyllables = ['ari', 'ek', 'hyp', 'or', 'our', 'bor', 'sto', 'lo',
                       'lor', 'nor', 'dah', 'dor', 'bo', 'to', 'nor', 'et',
                       'eth', 'ut', 'uth', 'st', 'ah', 'tah', 'ler', 'lar',
                       'it', 'ot', 'oto', 'oth', 'tob', 'xy', 'ter', 'ata',
                       'bar', 'tar', 'car', 'blu', 'iq', 'utu', 'ut', 'at',
                       'fu', 'tog', 'xqi', 'mu', 'qi', 'del', 'oth', 'onu',
                       'pro', 'xi', 'ma', 'mus', 'em', 'plu', 'tun', 'cen',
                       'ven', 'tau', 'ri', 'du', 'dun', 'une', 'no', 'qua',
                       'sti', 'qu', 'kis', 'ara', 'he', 'li', 'ohm', 'eon',
                       'cor', 'ron', 'di', 'dov', 'les', 'ro', 'rio', 'si',
                       'aur', 'el', 'xo', 'ox', 'hua', 'del', 'pho', 'tor']

solarNameSyllables = ['qu', 'ox', 'xo', 'q', 'i', 'set', 'to', 'oto',
                      'alph', 'bet', 'a', 'u', 'ri', 'cen', 'aleph',
                      'lot', 'lote', 'ote', 'oa', 'ti', 's', 'o', 'on',
                      'hi', 'hyp', 'erion', 'eri', 'tethy', 'thi', 'sys',
                      'sis', 'promethy', 'sius', 'ion', 'ius', 'hat',
                      'shep', 'sut', 'miner', 'va', 'vu', 'plut', 'x',
                      'z']

# Element lists
abundantElements = ['Carbon', 'Sulphur', 'Iron', 'Hydrogen', 'Helium', 'Oxygen', 'Nitrogen', 'Silicon', 'Magnesium', 'Neon']
commonElements = ['Aluminium', 'Calcium', 'Nickel', 'Argon', 'Chromium', 'Potassium', 'Vanadium', 'Tin', 'Lead', 'Manganese']
uncommonElements = ['Titanium', 'Copper', 'Mercury', 'Cobalt', 'Neodymium', 'Rhenium', 'Phosphorous', 'Radium']
scarceElements = ['Gold', 'Cadmium', 'Uranium', 'Palladium', 'Osmium', 'Silver', 'Lanthanum', 'Scandium']
rareElements = ['Rhodium', 'Iridium', 'Plutonium', 'Rhenium', 'Tellerium', 'Platinum']

# Element count dictionary
elementCountDict = {'Carbon': 0, 'Sulphur': 0, 'Iron': 0, 'Hydrogen': 0, 'Helium': 0, 'Oxygen': 0,
                    'Nitrogen': 0, 'Silicon': 0, 'Magnesium': 0, 'Neon': 0, 'Aluminium': 0, 'Calcium': 0,
                    'Nickel': 0, 'Argon': 0, 'Chromium': 0, 'Potassium': 0, 'Vanadium': 0, 'Tin': 0,
                    'Lead': 0, 'Manganese': 0, 'Titanium': 0, 'Copper': 0, 'Mercury': 0, 'Cobalt': 0, 
                    'Neodymium': 0, 'Rhenium': 0, 'Phosphorous': 0, 'Radium': 0, 'Gold': 0, 'Cadmium': 0, 
                    'Uranium': 0, 'Palladium': 0, 'Osmium': 0, 'Silver': 0, 'Lanthanum': 0, 'Scandium': 0,
                    'Rhodium': 0, 'Iridium': 0, 'Plutonium': 0, 'Rhenium': 0, 'Tellerium': 0, 'Platinum': 0}


# Setting up lists
nameList = []
luminosityList = []
sizeList = []
temperatureList = []
distanceList = []
moonsList = []
typeList = []
classLevelList = []
classTypeList = []
supportsLifeList = []
massList = []
elementCountList = []
elementList = []

# Potential lists
potentialMasses = ['mercury-like', 'mars-like', 'earth-like', 'neptune-like', 'jupiter-like']

# Setting up dictionary
dataDictionary = {'Planet Name': nameList,
                  'Luminosity': luminosityList,
                  'Size': sizeList,
                  'Temperature': temperatureList,
                  'Distance': distanceList,
                  'Moons': moonsList,
                  'Planet Type': typeList,
                  'Class Level': classLevelList,
                  'Class Type': classTypeList,
                  'Supports Life': supportsLifeList,
                  'Mass': massList,
                  'Element Count': elementCountList,
                  'Elements': elementList}

# Planet class
class Planet:
    def __init__(self):
        self.luminosity = round(np.random.normal(5, 3))
        self.size = round(np.random.normal(350, 75))
        self.temperature = round(np.random.normal(50, 50))
        self.distance = randint(12, 30)
        self.moons = round(np.random.normal(2, 1.5))
        
        # Green planet temperature limit
        if self.temperature >= 1 and self.temperature <= 40:
            self.type = random.choice(planetTypesLivable)
            
        if self.temperature < 1:
            self.type = random.choice(planetTypesCold)
            
        if self.temperature > 40:
            self.type = random.choice(planetTypesHot)
            
        # Limiting luminosity
        if self.luminosity < 1:
            self.luminosity = 1
            
        if self.luminosity > 10:
            self.luminosity = 10
            
        # Limit moons
        if self.moons < 1:
            self.moons = 1
            
        if self.moons > 6:
            self.moons = 6
        
        # Incorporates naming engine
        self.name = str.title(''.join([random.choice(planetNameSyllables) for i in range(randint(2,5))]))
    
        # Calculates class level
        self.planetClassLevel = round((((3*int(self.size))/100)+(2*int(self.luminosity))+(2*int(self.moons))) / 7, 2)
        
        # Interprets class level as class type
        if self.planetClassLevel < 3.25:
            self.planetClassType = 'Delta'
            
        if self.planetClassLevel >= 3.25 and self. planetClassLevel < 4.25:
            self.planetClassType = 'Beta'
            
        if self.planetClassLevel >= 4.25 and self.planetClassLevel < 5.25:
            self.planetClassType = 'Alpha'
            
        if self.planetClassLevel >= 5.25 and self.planetClassLevel < 5.75:
            self.planetClassType = 'Omega'
            
        if self.planetClassLevel >= 5.75:
            self.planetClassType = 'Iris'
            
        # Supports life characteristic
        if self.type == 'green':
            self.supportsLife = 'yes'
            
        else:
            chanceLife = randint(1,5)
            
            if chanceLife == 1:
                self.supportsLife = 'yes'
            
            else:
                self.supportsLife = 'no'
                
        # Mass characteristic
        self.mass = random.choice(potentialMasses)
        
        # Distance from star horizontal
        self.distanceStarX = round(np.random.normal(0,50))
        
        # Distance from star vertical
        self.distanceStarY = round(np.random.normal(0,50))
        
        # Element count
        self.elementCount = round(np.random.normal(1,1))
        
        if self.elementCount < 1:
            self.elementCount = 1
        
        # Range
        self.elementCountRange = range(0, self.elementCount)
        
        # Setting up the element list
        self.elements = []
        
        # Generating elements
        for i in self.elementCountRange:
            elementValue = randint(1,100)
            
            if elementValue <= 50:
                self.elements.append(random.choice(abundantElements))
                
            if elementValue > 50 and elementValue <= 75:
                self.elements.append(random.choice(commonElements))
                
            if elementValue > 75 and elementValue <= 90: 
                self.elements.append(random.choice(uncommonElements))
                
            if elementValue > 90 and elementValue <= 98:
                self.elements.append(random.choice(scarceElements))
            
            if elementValue > 98 and elementValue <= 100:
                self.elements.append(random.choice(rareElements))
        
        # Remove repeating elements
        self.elements = list(set(self.elements))
        
        # Add element count
        for x in self.elements:
            if x in elementCountDict:
                elementCountDict[x] += 1
                
        # Position X & Y blanks
        self.positionX = 0
        self.positionY = 0

class solarSystem:
    def __init__(self):
        # Generates local name
        self.solarSystemName = str.title(''.join([random.choice(solarNameSyllables) for i in range(randint(2,3))]))
        
        # Generates solar distance
        self.solarDistanceX = randint(-10000, 10000)
        self.solarDistanceY = randint(-10000, 10000)
        
        # Creates local lists
        self.nameList = []
        self.luminosityList = []
        self.sizeList = []
        self.temperatureList = []
        self.distanceList = []
        self.moonsList = []
        self.typeList = []
        self.classLevelList = []
        self.classTypeList = []
        self.supportsLifeList = []
        self.massList = []
        self.elementCountList = []
        self.elementList = []
        self.solarSystemNameList = []
        self.distanceStarXList = []
        self.distanceStarYList = []
        self.positionXList = []
        self.positionYList = []
        
        # Sets up local dictionary
        self.dataDictionary = {'System Name': self.solarSystemNameList,
                               'Planet Name': self.nameList,
                               'Luminosity': self.luminosityList,
                               'Size': self.sizeList,
                               'Temperature': self.temperatureList,
                               'Distance': self.distanceList,
                               'Moons': self.moonsList,
                               'Planet Type': self.typeList,
                               'Class Level': self.classLevelList,
                               'Class Type': self.classTypeList,
                               'Supports Life': self.supportsLifeList,
                               'Mass': self.massList,
                               'Element Count': self.elementCountList,
                               'Elements': self.elementList,
                               'Dist. Horiz.': self.distanceStarXList,
                               'Dist. Verti.': self.distanceStarYList,
                               'Pos. X': self.positionXList,
                               'Pos. Y': self.positionYList}
        
        # Number of planets
        numPlanets = round(np.random.normal(6,8))
        
        if numPlanets < 1:
            numPlanets = 1
        
        # Adds planets to the Solar System
        for x in range(0, numPlanets):
            planet = Planet()
            
            # Appends planets to local lists
            self.solarSystemNameList.append(self.solarSystemName)
            self.nameList.append(planet.name)
            self.luminosityList.append(planet.luminosity)
            self.sizeList.append(planet.size)
            self.temperatureList.append(planet.temperature)
            self.distanceList.append(planet.distance)
            self.moonsList.append(planet.moons)
            self.typeList.append(planet.type)
            self.classLevelList.append(planet.planetClassLevel)
            self.classTypeList.append(planet.planetClassType)
            self.supportsLifeList.append(planet.supportsLife)
            self.massList.append(planet.mass)
            self.elementCountList.append(planet.elementCount)
            self.elementList.append(planet.elements)
            self.distanceStarXList.append(planet.distanceStarX)
            self.distanceStarYList.append(planet.distanceStarY)
            
            # Calculates true distance & appends it
            planet.positionX = self.solarDistanceX + planet.distanceStarX
            planet.positionY = self.solarDistanceY + planet.distanceStarY
            
            self.positionXList.append(planet.positionX)
            self.positionYList.append(planet.positionY)
            
# Big dataframe
largeDF = pd.DataFrame(data = dataDictionary)

# Combining dataframes
for x in range (0, 501):
    solarSystemOne = solarSystem()
    tempDF = pd.DataFrame(data = solarSystemOne.dataDictionary)
    
    largeDF = largeDF.append(tempDF)

# Adds index
largeDF = largeDF.reset_index()

# Print DF
print(largeDF.to_string())

# Allows for export
def exportXLSX():
    exportPreference = input('Do you want to export to XLSX? (Y/N) ')
    proceed = 'Y'
    
    if exportPreference == proceed:
        largeDF.to_excel('planetList.xlsx')
        
    else:
        print('Thank you. Export to XLSX will not proceed.')

# Calls export function
exportXLSX()
