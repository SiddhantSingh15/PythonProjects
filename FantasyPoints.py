class Driver:
    def __init__(self):
        self.name = None
        self.qualiSesh = None
        self.beatTeammateQuali = None
        self.DNQ = None
        self.qualiPos = None
        self.racePos = None
        self.finishRace = None
        self.beatTeammate = None
        self.DNF = None
        self.fastestLap = None
        self.streaks = None
        self.qualiPoints = None
        self.racePoints = None

    def calculateQuali(self):
        points = 0
        if self.DNQ:
            points = -5

        if self.qualiSesh == 'Q1':
            points = 1
        elif self.qualiSesh == 'Q2':
            points = 2
        elif self.qualiSesh == 'Q3':
            points = 3

        if self.beatTeammateQuali:
            points += 2

        if self.qualiPos < 11:
            points += 11-self.qualiPos

        self.qualiPoints = points
        print(self.name, ' quali - ', self.qualiPoints)

    def calculateRace(self):
        points = 0

        if self.DNF:
            points += -15

        if self.finishRace:
            points += 1
            quali = self.qualiPos
            race = self.racePos
            if quali == race:
                points += 0
            elif quali >= 10:
                if quali > race:
                    overtakeP = (quali - race) * 2
                    if overtakeP >= 10:
                        points += 10
                    else:
                        points += overtakeP
                if quali < race:
                    overtakeP = (quali - race)
                    if overtakeP <= -5:
                        points += -5
                    else:
                        points += overtakeP
            elif quali <= 10:
                if quali > race:
                    overtakeP = (quali - race) * 2
                    if overtakeP >= 10:
                        points += 10
                    else:
                        points += overtakeP
                if quali < race:
                    overtakeP = (quali - race) * 2
                    if overtakeP <= -10:
                        points += -10
                    else:
                        points += overtakeP

        if self.beatTeammate:
            points += 3

        if self.fastestLap:
            points += 5

        if self.racePos == 1:
            points += 25
        elif self.racePos == 2:
            points += 18
        elif self.racePos == 3:
            points += 15
        elif self.racePos == 4:
            points += 12
        elif self.racePos == 5:
            points += 10
        elif self.racePos == 6:
            points += 8
        elif self.racePos == 7:
            points += 6
        elif self.racePos == 8:
            points += 4
        elif self.racePos == 9:
            points += 2
        elif self.racePos == 10:
            points += 1

        points += self.streaks
        self.racePoints = points

        print(self.name, ' race - ', self.racePoints)

    def calculateTotal(self):
        totalP = self.qualiPoints + self.racePoints
        print(self.name, '  -- TOTAL: ', totalP)

from collections import Counter

HAM = Driver()
HAM.name = 'HAM'
HAM.qualiSesh = 'Q3'
HAM.beatTeammateQuali = False
HAM.qualiPos = 3
HAM.racePos = 3
HAM.finishRace = True
HAM.beatTeammate = False
HAM.fastestLap = False
HAM.streaks = 0
HAM.calculateQuali()
HAM.calculateRace()
HAM.calculateTotal()


BOT = Driver()
BOT.name = 'BOT'
BOT.qualiSesh = 'Q3'
BOT.beatTeammateQuali = True
BOT.qualiPos = 2
BOT.racePos = 2
BOT.finishRace = True
BOT.beatTeammate = True
BOT.fastestLap = False
BOT.streaks = 0
BOT.calculateQuali()
BOT.calculateRace()
BOT.calculateTotal()


VER = Driver()
VER.name = 'VER'
VER.qualiSesh = 'Q3'
VER.beatTeammateQuali = True
VER.qualiPos = 1
VER.racePos = 1
VER.finishRace = True
VER.beatTeammate = True
VER.fastestLap = False
VER.streaks = 0
VER.calculateQuali()
VER.calculateRace()
VER.calculateTotal()


ALB = Driver()
ALB.name = 'ALB'
ALB.qualiSesh = 'Q3'
ALB.beatTeammateQuali = False
ALB.qualiPos = 5
ALB.racePos = 4
ALB.finishRace = True
ALB.beatTeammate = False
ALB.fastestLap = False
ALB.streaks = 0
ALB.calculateQuali()
ALB.calculateRace()
ALB.calculateTotal()


STR = Driver()
STR.name = 'STR'
STR.qualiSesh = 'Q3'
STR.beatTeammateQuali = True
STR.qualiPos = 8
STR.racePos = 10
STR.finishRace = True
STR.beatTeammate = True
STR.fastestLap = False
STR.streaks = 0
STR.calculateQuali()
STR.calculateRace()
STR.calculateTotal()


PER = Driver()
PER.name = 'PER'
PER.qualiSesh = 'Q2'
PER.beatTeammateQuali = False
PER.qualiPos = 19
PER.DNF = True
PER.finishRace = False
PER.beatTeammate = False
PER.fastestLap = False
PER.streaks = 0
PER.calculateQuali()
PER.calculateRace()
PER.calculateTotal()


NOR = Driver()
NOR.name = 'NOR'
NOR.qualiSesh = 'Q3'
NOR.beatTeammateQuali = True
NOR.qualiPos = 4
NOR.racePos = 5
NOR.finishRace = True
NOR.beatTeammate = True
NOR.fastestLap = False
NOR.streaks = 0
NOR.calculateQuali()
NOR.calculateRace()
NOR.calculateTotal()


SAI = Driver()
SAI.name = 'SAI'
SAI.qualiSesh = 'Q3'
SAI.beatTeammateQuali = False
SAI.qualiPos = 6
SAI.racePos = 6
SAI.finishRace = True
SAI.beatTeammate = False
SAI.fastestLap = False
SAI.streaks = 0
SAI.calculateQuali()
SAI.calculateRace()
SAI.calculateTotal()


VET = Driver()
VET.name = 'VET'
VET.qualiSesh = 'Q2'
VET.beatTeammateQuali = False
VET.qualiPos = 13
VET.racePos = 14
VET.finishRace = True
VET.beatTeammate = False
VET.fastestLap = False
VET.streaks = 0
VET.calculateQuali()
VET.calculateRace()
VET.calculateTotal()


LEC = Driver()
LEC.name = 'LEC'
LEC.qualiSesh = 'Q3'
LEC.beatTeammateQuali = True
LEC.qualiPos = 12
LEC.racePos = 13
LEC.finishRace = True
LEC.beatTeammate = True
LEC.fastestLap = False
LEC.streaks = 0
LEC.calculateQuali()
LEC.calculateRace()
LEC.calculateTotal()


RUS = Driver()
RUS.name = 'RUS'
RUS.qualiSesh = 'Q1'
RUS.beatTeammateQuali = True
RUS.qualiPos = 16
RUS.racePos = 15
RUS.finishRace = True
RUS.beatTeammate = True
RUS.fastestLap = False
RUS.streaks = 0
RUS.calculateQuali()
RUS.calculateRace()
RUS.calculateTotal()


LAT = Driver()
LAT.name = 'LAT'
LAT.qualiSesh = 'Q1'
LAT.beatTeammateQuali = False
LAT.qualiPos = 18
LAT.racePos = 17
LAT.finishRace = True
LAT.beatTeammate = False
LAT.fastestLap = False
LAT.streaks = 0
LAT.calculateQuali()
LAT.calculateRace()
LAT.calculateTotal()


RAI = Driver()
RAI.name = 'RAI'
RAI.qualiSesh = 'Q1'
RAI.beatTeammateQuali = False
RAI.qualiPos = 15
RAI.racePos = 12
RAI.finishRace = True
RAI.beatTeammate = True
RAI.fastestLap = False
RAI.streaks = 0
RAI.calculateQuali()
RAI.calculateRace()
RAI.calculateTotal()


GIO = Driver()
GIO.name = 'GIO'
GIO.qualiSesh = 'Q2'
GIO.beatTeammateQuali = True
GIO.qualiPos = 14
GIO.racePos = 16
GIO.finishRace = True
GIO.beatTeammate = False
GIO.fastestLap = False
GIO.streaks = 0
GIO.calculateQuali()
GIO.calculateRace()
GIO.calculateTotal()


GAS = Driver()
GAS.name = 'GAS'
GAS.qualiSesh = 'Q3'
GAS.beatTeammateQuali = False
GAS.qualiPos = 9
GAS.racePos = 8
GAS.finishRace = True
GAS.beatTeammate = True
GAS.fastestLap = False
GAS.streaks = 0
GAS.calculateQuali()
GAS.calculateRace()
GAS.calculateTotal()


KVY = Driver()
KVY.name = 'KVY'
KVY.qualiSesh = 'Q3'
KVY.beatTeammateQuali = True
KVY.qualiPos = 7
KVY.racePos = 11
KVY.finishRace = True
KVY.beatTeammate = False
KVY.fastestLap = False
KVY.streaks = 0
KVY.calculateQuali()
KVY.calculateRace()
KVY.calculateTotal()


MAG = Driver()
MAG.name = 'MAG'
MAG.qualiSesh = 'Q1'
MAG.beatTeammateQuali = True
MAG.qualiPos = 20
MAG.racePos = 18
MAG.finishRace = True
MAG.beatTeammate = True
MAG.fastestLap = False
MAG.streaks = 0
MAG.calculateQuali()
MAG.calculateRace()
MAG.calculateTotal()


GRO = Driver()
GRO.name = 'GRO'
GRO.qualiSesh = 'Q1'
GRO.beatTeammateQuali = False
GRO.qualiPos = 17
GRO.racePos = 19
GRO.finishRace = True
GRO.beatTeammate = False
GRO.fastestLap = False
GRO.streaks = 0
GRO.calculateQuali()
GRO.calculateRace()
GRO.calculateTotal()


RIC = Driver()
RIC.name = 'RIC'
RIC.qualiSesh = 'Q2'
RIC.beatTeammateQuali = False
RIC.qualiPos = 11
RIC.racePos = 7
RIC.finishRace = True
RIC.beatTeammate = True
RIC.fastestLap = True
RIC.streaks = 0
RIC.calculateQuali()
RIC.calculateRace()
RIC.calculateTotal()


OCO = Driver()
OCO.name = 'OCO'
OCO.qualiSesh = 'Q2'
OCO.beatTeammateQuali = True
OCO.qualiPos = 10
OCO.racePos = 9
OCO.finishRace = True
OCO.beatTeammate = False
OCO.fastestLap = False
OCO.streaks = 0
OCO.calculateQuali()
OCO.calculateRace()
OCO.calculateTotal()
