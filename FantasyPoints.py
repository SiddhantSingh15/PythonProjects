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

    def calculateTotal(self):
        totalP = self.qualiPoints + self.racePoints
        print(self.name, ': ', totalP)


HAM = Driver()
HAM.name = 'HAM'
HAM.qualiSesh = 'Q3'
HAM.beatTeammateQuali = False
HAM.qualiPos = 2
HAM.racePos = 2
HAM.finishRace = True
HAM.beatTeammate = True
HAM.fastestLap = True
HAM.streaks = 15
HAM.calculateQuali()
HAM.calculateRace()
HAM.calculateTotal()


BOT = Driver()
BOT.name = 'BOT'
BOT.qualiSesh = 'Q3'
BOT.beatTeammateQuali = True
BOT.qualiPos = 1
BOT.racePos = 3
BOT.finishRace = True
BOT.beatTeammate = False
BOT.fastestLap = False
BOT.streaks = 5
BOT.calculateQuali()
BOT.calculateRace()
BOT.calculateTotal()


VER = Driver()
VER.name = 'VER'
VER.qualiSesh = 'Q3'
VER.beatTeammateQuali = True
VER.qualiPos = 4
VER.racePos = 1
VER.finishRace = True
VER.beatTeammate = True
VER.fastestLap = False
VER.streaks = 5
VER.calculateQuali()
VER.calculateRace()
VER.calculateTotal()


ALB = Driver()
ALB.name = 'ALB'
ALB.qualiSesh = 'Q3'
ALB.beatTeammateQuali = False
ALB.qualiPos = 9
ALB.racePos = 5
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
STR.beatTeammateQuali = False
STR.qualiPos = 6
STR.racePos = 6
STR.finishRace = True
STR.beatTeammate = True
STR.fastestLap = False
STR.streaks = 0
STR.calculateQuali()
STR.calculateRace()
STR.calculateTotal()


HUL = Driver()
HUL.name = 'HUL'
HUL.qualiSesh = 'Q3'
HUL.beatTeammateQuali = True
HUL.qualiPos = 3
HUL.racePos = 7
HUL.finishRace = True
HUL.beatTeammate = False
HUL.fastestLap = False
HUL.streaks = 0
HUL.calculateQuali()
HUL.calculateRace()
HUL.calculateTotal()


NOR = Driver()
NOR.name = 'NOR'
NOR.qualiSesh = 'Q3'
NOR.beatTeammateQuali = True
NOR.qualiPos = 10
NOR.racePos = 9
NOR.finishRace = True
NOR.beatTeammate = True
NOR.fastestLap = False
NOR.streaks = 5
NOR.calculateQuali()
NOR.calculateRace()
NOR.calculateTotal()


SAI = Driver()
SAI.name = 'SAI'
SAI.qualiSesh = 'Q2'
SAI.beatTeammateQuali = False
SAI.qualiPos = 12
SAI.racePos = 13
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
VET.qualiPos = 11
VET.racePos = 12
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
LEC.qualiPos = 8
LEC.racePos = 4
LEC.finishRace = True
LEC.beatTeammate = True
LEC.fastestLap = False
LEC.streaks = 0
LEC.calculateQuali()
LEC.calculateRace()
LEC.calculateTotal()


RUS = Driver()
RUS.name = 'RUS'
RUS.qualiSesh = 'Q2'
RUS.beatTeammateQuali = True
RUS.qualiPos = 15
RUS.racePos = 18
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
LAT.racePos = 19
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
RAI.qualiPos = 20
RAI.racePos = 15
RAI.finishRace = True
RAI.beatTeammate = True
RAI.fastestLap = False
RAI.streaks = 0
RAI.calculateQuali()
RAI.calculateRace()
RAI.calculateTotal()


GIO = Driver()
GIO.name = 'GIO'
GIO.qualiSesh = 'Q1'
GIO.beatTeammateQuali = True
GIO.qualiPos = 19
GIO.racePos = 17
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
GAS.beatTeammateQuali = True
GAS.qualiPos = 7
GAS.racePos = 11
GAS.finishRace = True
GAS.beatTeammate = False
GAS.fastestLap = False
GAS.streaks = 0
GAS.calculateQuali()
GAS.calculateRace()
GAS.calculateTotal()


KVY = Driver()
KVY.name = 'KVY'
KVY.qualiSesh = 'Q1'
KVY.beatTeammateQuali = False
KVY.qualiPos = 16
KVY.racePos = 10
KVY.finishRace = True
KVY.beatTeammate = True
KVY.fastestLap = False
KVY.streaks = 0
KVY.calculateQuali()
KVY.calculateRace()
KVY.calculateTotal()


MAG = Driver()
MAG.name = 'MAG'
MAG.qualiSesh = 'Q1'
MAG.beatTeammateQuali = False
MAG.qualiPos = 17
MAG.racePos = 0
MAG.finishRace = False
MAG.DNF = True
MAG.beatTeammate = False
MAG.fastestLap = False
MAG.streaks = 0
MAG.calculateQuali()
MAG.calculateRace()
MAG.calculateTotal()


GRO = Driver()
GRO.name = 'GRO'
GRO.qualiSesh = 'Q2'
GRO.beatTeammateQuali = True
GRO.qualiPos = 13
GRO.racePos = 16
GRO.finishRace = True
GRO.beatTeammate = True
GRO.fastestLap = False
GRO.streaks = 0
GRO.calculateQuali()
GRO.calculateRace()
GRO.calculateTotal()


RIC = Driver()
RIC.name = 'RIC'
RIC.qualiSesh = 'Q3'
RIC.beatTeammateQuali = True
RIC.qualiPos = 5
RIC.racePos = 14
RIC.finishRace = True
RIC.beatTeammate = False
RIC.fastestLap = False
RIC.streaks = 0
RIC.calculateQuali()
RIC.calculateRace()
RIC.calculateTotal()


OCO = Driver()
OCO.name = 'OCO'
OCO.qualiSesh = 'Q2'
OCO.beatTeammateQuali = False
OCO.qualiPos = 14
OCO.racePos = 8
OCO.finishRace = True
OCO.beatTeammate = True
OCO.fastestLap = False
OCO.streaks = 0
OCO.calculateQuali()
OCO.calculateRace()
OCO.calculateTotal()


