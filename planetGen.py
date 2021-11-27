import random
import pandas as pd
from random import randint, seed, choice
import numpy as np

# Seed random
seed(randint(0,1000))

# Planet varieties
planetTypesLivable = ['rocky', 'ocean', 'green', 'gas']
planetTypesUnlivable = ['rocky', 'icy', 'ocean', 'gas']

# Name list
nameSyllables = ['ari', 'ek', 'hyp', 'or', 'our', 'bor', 'sto', 'lo',
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

# Setting up dictionary
dataDictionary = {'Names': nameList,
                  'Luminosity': luminosityList,
                  'Size': sizeList,
                  'Temperature': temperatureList,
                  'Distance': distanceList,
                  'Moons': moonsList,
                  'Planet Type': typeList,
                  'Class Level': classLevelList,
                  'Class Type': classTypeList}

# Planet class
class Planet:
    def __init__(self):
        self.luminosity = round(np.random.normal(5, 3))
        self.size = round(np.random.normal(350, 75))
        self.temperature = round(np.random.normal(50, 50))
        self.distance = randint(12, 30)
        self.moons = round(np.random.normal(2, 2))
        
        # Green planet temperature limit
        if self.temperature >= 1 and self.temperature <= 40:
            self.type = random.choice(planetTypesLivable)
            
        else:
            self.type = random.choice(planetTypesUnlivable)
            
        # Limiting luminosity
        if self.luminosity < 1:
            self.luminosity = 1
            
        if self.luminosity > 10:
            self.luminosity = 10
            
        # Limit moons
        if self.moons < 1:
            self.moons = 1
            
        if self.moons > 7:
            self.moons = 7
        
        # Incorporates naming engine
        self.name = str.title(''.join([random.choice(nameSyllables) for i in range(randint(2,5))]))
    
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
    
    # I don't really know what this does
    def __str__(self):
        return 'Planet % s has luminosity: % s, size: % s, temperature: % s, distance % s, moons % s, and type % s, for a class level of % s and a class of % s' % (
            self.name,
            self.luminosity,
            self.size,
            self.temperature,
            self.distance,
            self.moons,
            self.type,
            self.planetClassLevel,
            self.planetClassType)
        
# Generates planets and appends list
for x in range(0, 2500):
    planet = Planet()
    
    # Appends planets to the list
    nameList.append(planet.name)
    luminosityList.append(planet.luminosity)
    sizeList.append(planet.size)
    temperatureList.append(planet.temperature)
    distanceList.append(planet.distance)
    moonsList.append(planet.moons)
    typeList.append(planet.type)
    classLevelList.append(planet.planetClassLevel)
    classTypeList.append(planet.planetClassType)
    
# Loads dataframe
df = pd.DataFrame(data = dataDictionary)

# Renders the whole dataframe
print(df.to_string())

# Counts each class, then prints it
def countClassType():
    classTypeCount = df['Class Type'].value_counts()
    
    print(classTypeCount)

# Counts each planet type, then prints it
def countPlanetType():
    planetTypeCount = df['Planet Type'].value_counts()
    
    print(planetTypeCount)
    
# Counts luminosity, then prints it
def countLuminosity():
    luminosityCount = df['Luminosity'].value_counts()
    
    print(luminosityCount)
    
# Counts everything
def countAll():
    countLuminosity()
    countPlanetType()
    countClassType()
    
# Calls count function
countAll()

# Allows for export
def exportXLSX():
    exportPreference = input('Do you want to export to XLSX? (Y/N) ')
    proceed = 'Y'
    
    if exportPreference == proceed:
        df.to_excel('planetList.xlsx')
        
    else:
        print('Thank you.')

# Calls export function
exportXLSX()
