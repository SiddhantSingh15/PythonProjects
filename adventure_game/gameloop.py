from classes import *
import time
import pickle

Room1 = Room()
Room2 = Room()
Room3 = Room()
Room4 = Room()
Shed1 = Room()
Garden1 = Outside()
Garden2 = Outside()
Garden3 = Outside()
Dagger1 = Dagger()
Dagger2 = Dagger()
Dagger3 = Dagger()
Bucket1 = Bucket()
Torch1 = Torch()
Character1 = Character()

Dagger1.setItemName('The Heavenly Sword')
Dagger1.setItemDesc('With this dagger, thou shall stab any moving creature and send them to hell')
Dagger1.setDaggerSharpness('Very Sharp')

Dagger2.setItemName('The Excalibur')
Dagger2.setItemDesc('With this dagger, thou shall cut through plants')
Dagger2.setDaggerSharpness('Slightly Sharp')

Dagger3.setItemName('Old Night Owl')
Dagger3.setItemDesc('With this dagger,thou can inflict Blunt Force Trauma')
Dagger3.setDaggerSharpness('Very Blunt')

Bucket1.setItemName('The Mighty Container')
Bucket1.setItemDesc('You shall use this to drain the gardens you may come across')
Bucket1.setVolume(2000)

Torch1.setItemName('The LightBringer')
Torch1.setItemDesc('With this, thou shall bring light to any space you like...')
Torch1.setBrightness(1)

Room1.setRoomName('Kitchen')
Room1.setDesc('Knives, pans, pots, bottles... You are surrounded by walls and the smell of tuna. The smell of tuna is'
              ' playing a trick on your mind. You better get out of there quick.')
Room1.setExit(N=Room2, E=Room4)
Room1.setRoomLuminosity()
Room1.setRoomMap('[   ]\n[   ][   ][   ]\n[      ][     ]\n[   *  ][     ]')
Room1.setItemList(Dagger1)
Room1.setItemList(Torch1)
Room1.setCrisis('A sharp slice of ham')

Room2.setRoomName('Dining Room')
Room2.setDesc('The haunted family stares at you as you potter around the rectangular table with a clueless look'
              ' . They get up!!! You need to leave. NOW...')
Room2.setExit(S=Room1, N=Garden1)
Room2.setRoomLuminosity()
Room2.setRoomMap('[   ]\n[   ][   ][   ]\n[   *  ][     ]\n[      ][     ]')
Room2.setCrisis('A flying knife')

Room3.setRoomName('Living Room')
Room3.setDesc('How ironic that the living room consists of dead people. Here we see the king singing an opera'
              ' piece. I reckon hes a Soprano. Weird. He starts walking towards you. Where are you going?')
Room3.setExit(W=Room2, S=Room4)
Room3.setRoomLuminosity()
Room3.setRoomMap('[   ]\n[   ][   ][   ]\n[      ][  *  ]\n[      ][     ]')
Room3.setCrisis('A skeleton approaches you')

Room4.setRoomName('Study')
Room4.setDesc('You are surrounded by books written by members of this house. The moon shines eerily on the red carpet'
              ' . A book falls of the shelf and you look around but you find nothing. You probably want to leave...')
Room4.setExit(W=Room1, N=Room3)
Room4.setRoomLuminosity()
Room4.setRoomMap('[   ]\n[   ][   ][   ]\n[      ][     ]\n[      ][  *  ]')
Room4.setCrisis('A skin cutting book full of skin cutting paper')

Shed1.setRoomName('Shed')
Shed1.setDesc('Ooh this is a shed. There are various tools here but they\'re gyrating like a hard working heart'
              ' suddenly all the saws fly towards you... DUCK. MOVE MOVE MOVE')
Shed1.setExit(S=Garden1)
Shed1.setRoomLuminosity()
Shed1.setRoomMap('[ * ]\n[   ][   ][   ]\n[      ][     ]\n[      ][     ]')
Shed1.setItemList(Dagger2)
Shed1.setItemList(Bucket1)
Shed1.setCrisis('You trip over a gas pipe')

Garden1.setRoomName('Plot 1')
Garden1.setDesc('Roses are red, roses are pink, you will be dead, and your blood they will drink')
Garden1.setExit(N=Shed1, E=Garden2)
Garden1.setFlower('Roses')
Garden1.setRoomLuminosity()
Garden1.setGardenWeather()
Garden1.setRoomMap('[   ]\n[ * ][   ][   ]\n[      ][     ]\n[      ][     ]')
Garden1.setWaterVolume(350)
Garden1.setCrisis('The roses has a gun loaded in the horns')

Garden2.setRoomName('Plot 2')
Garden2.setDesc('Lilies look cute but not when they are 60 feet long. Beware! Don\'t get twisted in the stems')
Garden2.setExit(E=Garden3, W=Garden1)
Garden2.setFlower('Lilies')
Garden2.setRoomLuminosity()
Garden2.setGardenWeather()
Garden2.setRoomMap('[   ]\n[   ][ * ][   ]\n[      ][     ]\n[      ][     ]')
Garden2.setWaterVolume(1000)
Garden2.setCrisis('The lilies are trying to strangle you')

Garden3.setRoomName('Plot 3')
Garden3.setDesc('Hydrangea need water... Do not drown. They sometimes flood this room')
Garden3.setExit(W=Garden2, S=Room3)
Garden3.setFlower('Hydrangea')
Garden3.setRoomLuminosity()
Garden3.setGardenWeather()
Garden3.setRoomMap('[   ]\n[   ][   ][ * ]\n[      ][     ]\n[      ][     ]')
Garden3.setItemList(Dagger3)
Garden3.setWaterVolume(700)
Garden3.setCrisis('The water limit is increasing')

playing = True
userChoice = ''
visibleExits = 0


# initialising the save method
def saveGame(saveName, loadRoom, limit, things, rooms=Room.allRooms, allItems=Item.allItems):
    pickleJar = [saveName, loadRoom, limit, things, rooms, allItems]
    fileHandle = open(saveName, 'wb')
    pickle.dump(pickleJar, fileHandle, pickle.HIGHEST_PROTOCOL)
    fileHandle.close()


# initialising the load method
def loadGame(fileName):
    # using the exception handling to prevent the program crashing
    try:
        fileHandle = open(fileName, 'rb')
        username, loadRoom, limit, things, Room.allRooms, Item.allItems = pickle.load(fileHandle)
        fileHandle.close()
        return username, loadRoom, limit, things, Room.allRooms, Item.allItems
    except FileNotFoundError:
        print('This file was not found')
        print('Please restart the program and type the correct file name, or make a new game!')
        quit()


reload = str(input('Do you have saved data (type 1 if YES OR type anything else if NO): '))
if reload == '1':
    userName = ''
    while userName == '':
        userName = input('Please input your name (can\'t be blank): ')
    userName, currentRoom, userLimit, items, Room, Item = loadGame(userName)
    Character1.setCharName(userName)
    Character1.setCharPos(currentRoom)
    Character1.setCharLimit(userLimit)
    for i in items:
        Character1.setCharBag(i)
        if i.getItemName() == 'The LightBringer':
            Torch1 = i
else:
    userName = str(input('Please input your name: '))
    while not userName:
        userName = input('Please input your name (can\'t be blank): ')
    userLimit = str(input('Please input the size of your bag (3 or 5): '))
    while userLimit not in ('3', '5'):
        userLimit = str(input('Please input either a \'3\' or a \'5\': '))
    currentRoom = Room1
    Character1.setCharName(userName)
    Character1.setCharLimit(int(userLimit))

# start of game loop
while playing:
    print('\n*************LOCATION*************')
    print(currentRoom.getRoomMap())
    print('You are in the ', currentRoom.getRoomName())
    print(currentRoom.getDesc())

    print('\n*************CURRENT BAG*************')
    if len(Character1.getCharBag()) > 0:
        for i in Character1.getCharBag():
            print(i.getItemName())
    else:
        print('Your bag is empty.')

    print('\n*************ITEMS*************')
    # looping through the room's item list to print the items to the list
    if len(currentRoom.getItemList()) > 0:
        for thing in currentRoom.getItemList():
            print('You come across ', thing.getItemName())
            print(thing.getItemDesc())
            userChoice = str(input('Type 1 if you want to pick this item up? : '))
            if userChoice == '1':
                # adding the item to the character's bag
                if len(Character1.getCharBag()) < Character1.getCharLimit():
                    Character1.setCharBag(thing)
                else:
                    print('You do not have enough space in your bag!')
                    dropChoice = str(input('Type 1 if you want to drop an item: '))
                    if dropChoice == '1':
                        try:
                            itemNumber = str(input('Please type the index of the item you want to drop: '))
                            itemIndex = int(itemNumber) - 1
                            while itemIndex < 0 or itemIndex > len(Character1.getCharBag()):
                                itemNumber = str(
                                    input('The number you entered is invalid (Please choose between 0 and : '))
                                itemIndex = int(itemNumber) - 1
                            removedItem = Character1.getCharBag()[itemIndex]
                            print(removedItem.getItemName(), 'has been replaced with ', thing.getItemName())
                            currentRoom.setItemList(Character1.getCharBag()[itemIndex])
                            Character1.removeBagItem(itemIndex)
                            Character1.setCharBag(thing)
                            break
                        except ValueError:
                            print('Your input format was invalid, you cannot drop the item...')
                            break
                    else:
                        print('Wrong input. ', thing.getItemName(), ' could not be added.')
            else:
                print('Not added')
    else:
        print('No items found...')

    # Removing items from the room
    for chosenItem in Character1.getCharBag():
        if chosenItem in currentRoom.getItemList():
            currentRoom.removeItem(chosenItem)

    print('\n*************LUMINOSITY*************')
    visibleExits = len(currentRoom.getExit())
    luminosity = currentRoom.getRoomLuminosity()
    # calling the random variable, and assigning the value
    if luminosity == 1:
        print('It is very bright')
    elif luminosity == 2:
        print('It is bright enough for you to see')
    elif luminosity == 3:
        print('it is dim, you are having difficulty seeing')
    else:
        print('You cannot see, it is too dark. Use The LightBringer if you have one!')

    if luminosity == 4:
        if Torch1 in Character1.getCharBag():
            userChoice = str(input('Type 1 to switch on your torch: '))
            if userChoice == '1':
                print('You can see!')
                visibleExits = len(currentRoom.getExit())
            else:
                visibleExits = 0
                print('Torch not switched on...')
        else:
            visibleExits = 0

    print('\n*************EXITS*************')
    # checking for all the exits in the room
    # if exit found, then exit is printed
    if visibleExits > 0:
        for door in currentRoom.getExit():
            print(door, '-', currentRoom.getExit()[door].getRoomName())

    print('There are', visibleExits, 'visible exits in this room.')
    print(currentRoom.getCrisis() + ', 20 SECONDS START NOW... LEAVE')

    startTime = time.time()
    userChoice = str(input('Please choose wisely!  :  '))
    currentTime = time.time()
    if currentTime - startTime < 20:
        if userChoice.upper() in currentRoom.getExit():
            currentRoom = currentRoom.getExit()[userChoice.upper()]
            Character1.setCharPos(currentRoom)
        else:
            print("------WRONG------")
            print('TRY AGAIN')
            continue
    else:
        print('Sorry ', Character1.getCharName(), ', you ran out of time :(')
        print('Your location and bag has been reset')
        currentRoom = Room1
        Character1.emptyBag()
        continue

    continueGame = str(input('Type YES if you want to save the game and quit, NO if you want to continue:'))
    while continueGame.upper() not in ('YES', 'NO'):
        continueGame = str(input('Please input either YES or NO: '))
    if continueGame.upper() == 'YES':
        saveGame(userName, currentRoom, Character1.getCharLimit(), Character1.getCharBag())
        print('GAME SAVED!')
        break
    elif continueGame.upper() == 'NO':
        print('Continuing...')
    else:
        print('Wrong choice, you shall continue!')
        continue
