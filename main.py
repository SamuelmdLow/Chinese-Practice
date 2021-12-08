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

    def aveAccuracy(self):
        sumAccuracy = 0
        for word in self.List:
            sumAccuracy = sumAccuracy + word.Accuracy
        return sumAccuracy / len(self.List)

    def getNewWord(self):
        for word in self.List:
            gap = round - word.LastUsed
            if gap > 4:
                word.RankingValue = word.Accuracy / gap
            else:
                word.RankingValue = 100

        self.List.sort(key=myFunc)
        return self.List[0]


while True:
    p = Path(r'C:\Users\tubbd\PycharmProjects\Chinese-Practice\databases').glob('**/*')
    i = 1
    files = [file for file in p]
    for file in files:
        print(str(i) + ": " + file.name.replace(".csv", ""))
        i = i + 1
    CHOICE = int(input("Which file would you like to study: "))

    # filename = "databases" + x + files[CHOICE - 1]
    print("opening " + files[CHOICE - 1].name + "...")
    filename = files[CHOICE - 1]

    terms = open(filename, "r", encoding="utf-8").readlines()
    ChineseWords = Words()
    for term in terms:
        term = term.replace("\n", "")
        row = term.split(",")
        newWord = Word(row[0], row[1], row[2])
        ChineseWords.List.append(newWord)

    shuffle(ChineseWords.List)
    round = 1

    isEnglish = input("Practice english meaning (1) or pinyin/character (2)?") == "1"

    while ChineseWords.aveAccuracy() < 0.95:
        thing = ChineseWords.getNewWord()
        answer = input(thing.Chinese + ": ")
        print(thing.English + " (" + thing.PinYin + ")")
        if isEnglish == True:
            realAnswer = thing.English.lower()
        else:
            realAnswer = thing.Chinese.lower()

        if answer.lower() == realAnswer:
            thing.TimesCorrect += 1
            print("Correct! You are at " + str(ChineseWords.aveAccuracy() * 100) + "% accuracy!")
        else:
            print("Nope sorry!")

        thing.TimesAnswered += 1
        thing.updateAccuracy()
        thing.LastUsed = round

        round += 1

    print("Good job! You reached a 95% accuracy!")
