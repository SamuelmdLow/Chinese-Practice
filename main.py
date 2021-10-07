from random import shuffle
from pathlib import Path

def myFunc(e):
  return e.RankingValue

class Word:
    def __init__(self,Chinese, PinYin, English):
        self.Chinese = Chinese
        self.PinYin  = PinYin
        self.English = English

        self.LastUsed = -100

        self.TimesAnswered = 0
        self.TimesCorrect = 0
        self.Accuracy = 0.5

        self.RankingValue = None

    def updateAccuracy(self):
        self.Accuracy = self.TimesCorrect/self.TimesAnswered

class Words:
    def __init__(self):
        self.List = []

    def getNewWord(self):
        for word in self.List:
            gap = round - word.LastUsed
            if gap > 4:
                word.RankingValue = word.Accuracy / gap
            else:
                word.RankingValue = 100

        self.List.sort(key=myFunc)
        return self.List[0]


p = Path(r'databases').glob('**/*')
i = 1
files = [file.name for file in list(p)]
for file in files:
    print(str(i) + ": " + file)
    i = i +1
CHOICE = int(input("Which file would you like to study: "))

filename = "databases\\" + files[CHOICE - 1]

terms = open(filename, "r", encoding="utf-8").readlines()
ChineseWords = Words()
for term in terms:
    term = term.replace("\n", "")
    row = term.split(",")
    newWord = Word(row[0], row[1], row[2])
    ChineseWords.List.append(newWord)

shuffle(ChineseWords.List)
round = 1

while True:
    thing   = ChineseWords.getNewWord()
    answer  = input(thing.Chinese + ": ")
    if answer.lower() == thing.English.lower():
        thing.TimesCorrect += 1
        print(thing.English + " (" + thing.PinYin + ")")
        print("Correct!")
    else:
        print("Nope sorry the answer is: " + thing.English + " (" + thing.PinYin + ")")

    thing.TimesAnswered += 1
    thing.updateAccuracy()
    thing.LastUsed = round

    round += 1


