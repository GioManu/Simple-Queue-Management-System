class Translator:
    def __init__(self):
        self.dictionary = {
            "a": "ა",
            "b": "ბ",
            "c": "ც",
            "C": "ჩ",
            "d": "დ",
            "e": "ე",
            "f": "ფ",
            "g": "გ",
            "h": "ჰ",
            "i": "ი",
            "j": "ჯ",
            "J": "ჟ",
            "k": "კ",
            "l": "ლ",
            "m": "მ",
            "n": "ნ",
            "o": "ო",
            "p": "პ",
            "q": "ქ",
            "r": "რ",
            "R": "ღ",
            "s": "ს",
            "S": "შ",
            "t": "ტ",
            "T": "თ",
            "u": "უ",
            "v": "ვ",
            "w": "წ",
            "W": "ჭ",
            "x": "ხ",
            "y": "ყ",
            "z": "ზ",
            "Z": "ძ"
        }
        self.dictionaryRev = {
            "ა": "a",
            "ბ": "b",
            "ც": "c",
            "ჩ": "C",
            "დ": "d",
            "ე": "e",
            "ფ": "f",
            "გ": "g",
            "ჰ": "h",
            "ი": "i",
            "ჯ": "j",
            "ჟ": "J",
            "კ": "k",
            "ლ": "l",
            "მ": "m",
            "ნ": "n",
            "ო": "o",
            "პ": "p",
            "ქ": "q",
            "რ": "r",
            "ღ": "R",
            "ს": "s",
            "შ": "S",
            "ტ": "t",
            "თ": "T",
            "უ": "u",
            "ვ": "v",
            "წ": "w",
            "ჭ": "W",
            "ხ": "x",
            "ყ": "y",
            "ზ": "z",
            "ძ": "Z"
        }

    def toUTF(self, text):
        output = ""
        for c in text:
            if c in self.dictionary:
                output += self.dictionary[c]
            else:
                output += c
        return output

    def toAscii(self, text):
        output = ""
        for c in text:
            if c in self.dictionaryRev:
                output += self.dictionaryRev[c]
            else:
                output += c
        return output