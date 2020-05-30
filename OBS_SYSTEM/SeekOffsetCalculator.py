
class SeekOffsetCalculator:

    @staticmethod
    def createRecordFileIndex(recordDictionary, file, lineCount):
        lineCounter = 0
        currentRecordId = 0
        recordOffSetValue = 0

        for line in file:
            recordOffSetValue += len(line)
            
            if lineCounter == 0:
                if line.replace("\n","").isnumeric():
                    currentRecordId = int(line)
                else:
                    currentRecordId = line.replace("\n","")
            lineCounter += 1

            if(lineCounter > lineCount):
                recordDictionary[currentRecordId] = recordOffSetValue
                currentRecordId = 0
                lineCounter = 0
                recordOffSetValue = 0

    @staticmethod    
    def determineSeekValueAndOffset(recordDictionary, id):

        jumpToSeekValue = 0
        currentRecordOffset = 0
        for key, recordOffset in recordDictionary.items():

            if(key == id):
                currentRecordOffset = recordOffset
                break
            
            jumpToSeekValue += recordOffset

        return { "jumpToSeekValue": jumpToSeekValue, "currentRecordOffset": currentRecordOffset }