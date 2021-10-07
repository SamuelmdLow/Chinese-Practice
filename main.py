from random import shuffle

def myFunc(e):
  return e.RankingValue


class Word:
    def __init__(self,Chinese, English):
        self.Chinese = Chinese
        self.English = English

        self.LastUsed = 0

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
            word.RankingValue = word.Accuracy / (round - word.LastUsed)
        self.List.sort(key=myFunc)
        return self.List[0]

terms = open("terms.csv", "r", encoding="utf-8").readlines()
ChineseWords = Words()
for term in terms:
    term = term.replace("\n", "")
    row = term.split(",")
    newWord = Word(row[0], row[1])
    ChineseWords.List.append(newWord)

for i in ChineseWords.List:
    print(i.Chinese)

shuffle(ChineseWords.List)
round = 1

while True:
    thing   = ChineseWords.getNewWord()
    answer  = input(thing.Chinese + ": ")

    if answer.lower() == thing.English.lower():
        thing.TimesCorrect += 1

    thing.TimesAnswered += 1
    thing.updateAccuracy()
    thing.LastUsed = round

    round += 1

    for i in ChineseWords.List:
        print(i.Accuracy)

