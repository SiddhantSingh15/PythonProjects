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


HAM = Driver()
HAM.name = 'HAM'
HAM.qualiSesh = 'Q3'
HAM.beatTeammateQuali = True
HAM.qualiPos = 6
HAM.racePos = 1
HAM.finishRace = True
HAM.beatTeammate = True
HAM.fastestLap = False
HAM.streaks = 0
HAM.calculateQuali()
HAM.calculateRace()
HAM.calculateTotal()


BOT = Driver()
BOT.name = 'BOT'
BOT.qualiSesh = 'Q3'
BOT.beatTeammateQuali = False
BOT.qualiPos = 9
BOT.racePos = 14
BOT.finishRace = True
BOT.beatTeammate = False
BOT.fastestLap = False
BOT.streaks = 0
BOT.calculateQuali()
BOT.calculateRace()
BOT.calculateTotal()


VER = Driver()
VER.name = 'VER'
VER.qualiSesh = 'Q3'
VER.beatTeammateQuali = True
VER.qualiPos = 2
VER.racePos = 5
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
ALB.qualiPos = 4
ALB.racePos = 7
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
STR.qualiPos = 1
STR.racePos = 9
STR.finishRace = True
STR.beatTeammate = False
STR.fastestLap = False
STR.streaks = 0
STR.calculateQuali()
STR.calculateRace()
STR.calculateTotal()


PER = Driver()
PER.name = 'PER'
PER.qualiSesh = 'Q3'
PER.beatTeammateQuali = False
PER.qualiPos = 3
PER.racePos = 2
PER.finishRace = True
PER.beatTeammate = True
PER.fastestLap = False
PER.streaks = 10
PER.calculateQuali()
PER.calculateRace()
PER.calculateTotal()


NOR = Driver()
NOR.name = 'NOR'
NOR.qualiSesh = 'Q2'
NOR.beatTeammateQuali = True
NOR.qualiPos = 11
NOR.racePos = 8
NOR.finishRace = True
NOR.beatTeammate = False
NOR.fastestLap = True
NOR.streaks = 0
NOR.calculateQuali()
NOR.calculateRace()
NOR.calculateTotal()


SAI = Driver()
SAI.name = 'SAI'
SAI.qualiSesh = 'Q2'
SAI.beatTeammateQuali = False
SAI.qualiPos = 13
SAI.racePos = 5
SAI.finishRace = True
SAI.beatTeammate = True
SAI.fastestLap = False
SAI.streaks = 0
SAI.calculateQuali()
SAI.calculateRace()
SAI.calculateTotal()


VET = Driver()
VET.name = 'VET'
VET.qualiSesh = 'Q2'
VET.beatTeammateQuali = True
VET.qualiPos = 12
VET.racePos = 3
VET.finishRace = True
VET.beatTeammate = True
VET.fastestLap = False
VET.streaks = 0
VET.calculateQuali()
VET.calculateRace()
VET.calculateTotal()


LEC = Driver()
LEC.name = 'LEC'
LEC.qualiSesh = 'Q2'
LEC.beatTeammateQuali = False
LEC.qualiPos = 14
LEC.racePos = 4
LEC.finishRace = True
LEC.beatTeammate = False
LEC.fastestLap = False
LEC.streaks = 10
LEC.calculateQuali()
LEC.calculateRace()
LEC.calculateTotal()


RUS = Driver()
RUS.name = 'RUS'
RUS.qualiSesh = 'Q1'
RUS.beatTeammateQuali = True
RUS.qualiPos = 20
RUS.racePos = 16
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
LAT.qualiPos = 19
LAT.DNF = True
LAT.finishRace = False
LAT.beatTeammate = True
LAT.fastestLap = False
LAT.streaks = 0
LAT.calculateQuali()
LAT.calculateRace()
LAT.calculateTotal()


RAI = Driver()
RAI.name = 'RAI'
RAI.qualiSesh = 'Q3'
RAI.beatTeammateQuali = True
RAI.qualiPos = 8
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
GIO.qualiSesh = 'Q3'
GIO.beatTeammateQuali = False
GIO.qualiPos = 10
GIO.DNF = True
GIO.finishRace = False
GIO.beatTeammate = False
GIO.fastestLap = False
GIO.streaks = 0
GIO.calculateQuali()
GIO.calculateRace()
GIO.calculateTotal()


GAS = Driver()
GAS.name = 'GAS'
GAS.qualiSesh = 'Q2'
GAS.beatTeammateQuali = True
GAS.qualiPos = 15
GAS.racePos = 13
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
KVY.qualiPos = 17
KVY.racePos = 12
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
MAG.beatTeammateQuali = True
MAG.qualiPos = 16
MAG.racePos = 17
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
GRO.qualiPos = 18
GRO.racePos = 14
GRO.DNF = True
GRO.beatTeammate = False
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
RIC.racePos = 10
RIC.finishRace = True
RIC.beatTeammate = True
RIC.fastestLap = False
RIC.streaks = 0
RIC.calculateQuali()
RIC.calculateRace()
RIC.calculateTotal()


OCO = Driver()
OCO.name = 'OCO'
OCO.qualiSesh = 'Q2'
OCO.beatTeammateQuali = False
OCO.qualiPos = 7
OCO.racePos = 11
OCO.finishRace = False
OCO.beatTeammate = False
OCO.fastestLap = False
OCO.streaks = 0
OCO.calculateQuali()
OCO.calculateRace()
OCO.calculateTotal()
