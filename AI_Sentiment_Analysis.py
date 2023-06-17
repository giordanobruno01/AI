class AI:


    def checkMood():
        pass
    def processing(phrase):
        pass
    def convertFile():
        reader = open("gioTexts.csv", "r")
        l = reader.readline()
        l = reader.readline()
        while(l!=""):
            
            lis = l.split(",")
            phrase = lis[2]

            l = reader.readline()

ai = AI()
ai.convertFile()