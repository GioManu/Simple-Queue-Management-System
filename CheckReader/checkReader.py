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
                if(len(el) > 0):
                    num,state = el[0].split("|")
                    if(not num in chkDict):
                        chkDict[num] = state
                    else:
                        chkDict.update({num : state})
            if(len(chkDict) > 0 and not (str(self.conf.STATE_IN_PROGRESS) in chkDict.values() or str(self.conf.STATE_DONE) in chkDict.values())):
                raise Exception('CustomException','FileIsSafeToClean')
        except Exception as e:
            open(str(path) + "\\" + self.conf.CHECKS_PATH, 'w').close()

        chkDict = { k:v for k,v in chkDict.items() if v!=str(self.conf.STATE_CLOSED) }

        return chkDict
