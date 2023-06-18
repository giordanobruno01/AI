import time
class AI:
    def __init__(self):
        self.negList = []
        self.posList = []
        self.neutList = []

    def loadWords(self):
        neg = open("negativeSenti.csv", "r")
        neut = open("neutralSenti.csv", "r")
        pos = open("positiveSenti.txt", "r")

        l = neg.readline()
        while(l!=""):
            l = l.split(",")
            l = l[1].lower().strip()
            self.negList.append(l)
            l = neg.readline()

        l = neut.readline()
        while(l!=""):
            l = l.split(",")
            l = l[1].strip().lower()
            
            self.neutList.append(l)
            l = neut.readline()
        
        self.posList = pos.readline().split()
        
        
    def checkMood(self, wordList):
        negCount = 0
        posCount = 0
        neutCount = 0
        print(" ".join(wordList))
        for i in range(len(wordList)):
            if wordList[i] in self.negList:
                negCount += 1
            if wordList[i] in self.posList:
                posCount += 1
            if wordList[i] in self.neutList:
                neutCount += 1
        posScore = posCount*100/len(wordList)
        negScore = negCount*100/len(wordList)
        neutScore = neutCount*100/len(wordList)
        print("negative score ",round(negScore,2))
        print("positive score ", round(posScore,2))
        print("neutral score ", round(neutScore,2))
        if(negCount==posCount and posCount==neutCount):
            print("cannot determine mood")
            
        elif(negCount>posCount and negCount>neutCount):
            print("text mood is negative")
        elif(negCount<posCount and posCount>neutCount):
            print("text mood is positive")
        else:
            print("text mood is neutral")
            

    def convertSplit(self, l):
        lis = l.split(",")
        phrase = lis[2:]
        phrase = (" ".join(phrase)).lower()
        converted = ""
        for i in range(len(phrase)):
            if(phrase[i] == " "):
                converted = converted +phrase[i]
            if(phrase[i].isalpha()):
                converted = converted +phrase[i]
            
        return converted.split()    

                

        
        
ai = AI()
ai.loadWords()

reader = open("gioTexts.csv", "r")
l = reader.readline()
l = reader.readline()
while(l!=""):
    l = ai.convertSplit(l)
    ai.checkMood(l)
    print("\n")
    time.sleep(10)
    l = reader.readline()
