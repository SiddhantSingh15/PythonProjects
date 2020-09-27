import random
# testing

class Room:

    allRooms = []

    def __init__(self):
        self.__roomName = None
        self.__roomDesc = None
        self.__roomExits = {}
        self.__roomLuminosity = None
        self.__roomMap = None
        self.__itemList = []
        self.__roomCrisis = None
        Room.allRooms.append(self)

    def setRoomName(self, roomName):
        self.__roomName = roomName

    def getRoomName(self):
        return self.__roomName

    def setDesc(self, description):
        self.__roomDesc = description

    def getDesc(self):
        return self.__roomDesc

    def setExit(self, **kwargs):
        self.__roomExits = kwargs

    def getExit(self):
        return self.__roomExits

    def setRoomLuminosity(self):
        randomVariable1 = random.randint(1, 4)
        self.__roomLuminosity = randomVariable1

    def getRoomLuminosity(self):
        return self.__roomLuminosity

    def setRoomMap(self, drawing):
        self.__roomMap = drawing

    def getRoomMap(self):
        return self.__roomMap

    def setItemList(self, item):
        self.__itemList.append(item)

    def getItemList(self):
        return self.__itemList

    def removeItem(self, item):
        self.__itemList.remove(item)

    def setCrisis(self, crisis):
        self.__roomCrisis = crisis

    def getCrisis(self):
        return self.__roomCrisis


class Outside(Room):

    allOutside = []

    def __init__(self):
        Room.__init__(self)
        self.__gardenWeather = None
        self.__gardenFlowers = None
        self.__waterVolume = None
        Outside.allOutside.append(self)

    def setGardenWeather(self):
        randomVariable2 = random.randint(1, 4)
        self.__gardenWeather = randomVariable2

    def getGardenWeather(self):
        return self.__gardenWeather

    def setFlower(self, gardenFlowers):
        self.__gardenFlowers = gardenFlowers

    def getGardenFlowers(self):
        return self.__gardenFlowers

    def setWaterVolume(self, volume):
        self.__waterVolume = volume

    def getWaterVolume(self):
        return self.__waterVolume


class Item:

    allItems = []

    def __init__(self):
        self.__itemName = None
        self.__itemDesc = None
        Item.allItems.append(self)

    def setItemName(self, itemName):
        self.__itemName = itemName

    def getItemName(self):
        return self.__itemName

    def setItemDesc(self, itemDesc):
        self.__itemDesc = itemDesc

    def getItemDesc(self):
        return self.__itemDesc


class Dagger(Item):
    def __init__(self):
        Item.__init__(self)
        self.__sharpness = None

    def setDaggerSharpness(self, sharpness):
        self.__sharpness = sharpness

    def getDaggerSharpness(self):
        return self.__sharpness


class Bucket(Item):
    def __init__(self):
        Item.__init__(self)
        self.__volume = None

    def setVolume(self, volume):
        self.__volume = volume

    def getVolume(self):
        return self.__volume


class Torch(Item):
    def __init__(self):
        Item.__init__(self)
        self.__brightness = None

    def setBrightness(self, light):
        self.__brightness = light

    def getBrightness(self):
        return self.__brightness


class Character:

    allCharacters = []

    def __init__(self):
        self.__charName = None
        self.__charPos = None
        self.__charLimit = None
        self.__charBag = []
        Character.allCharacters.append(self)

    def setCharName(self, name):
        self.__charName = name

    def getCharName(self):
        return self.__charName

    def setCharPos(self, position):
        self.__charPos = position

    def getCharPos(self):
        return self.__charPos

    def removeCharItem(self, item):
        self.__charBag.remove(item)

    def setCharLimit(self, limit):
        self.__charLimit = limit

    def getCharLimit(self):
        return self.__charLimit

    def setCharBag(self, item):
        self.__charBag.append(item)

    def getCharBag(self):
        return self.__charBag

    def removeBagItem(self, item):
        self.__charBag.pop(item)

    def emptyBag(self):
        self.__charBag.clear()
