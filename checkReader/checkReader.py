import os
from pathlib import Path

class CheckReader:

    def __init__(self, configuration):
        self.conf = configuration

    def readChecks(self):

        chkDict = dict()
        data = list()

        path = Path().absolute()

        try:
            with open(str(path) + "\\" + self.conf.CHECKS_PATH,'r') as f:
                data = [x.split() for x in f.readlines()]

            for el in data:
                num,state = el[0].split("|")
                if(not num in chkDict):
                    chkDict[num] = state
                else:
                    chkDict.update({num : state})
            print(chkDict)

        except Exception as e:
            print(e)

        return chkDict