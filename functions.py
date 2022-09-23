from random import randrange
from datetime import date

LastNames = open("./last-names.txt", mode="r", encoding="utf-8").read().splitlines()
MaleFirstNames = open("./male-first-names.txt", mode="r", encoding="utf-8").read().splitlines()
FemaleFirstNames = open("./female-first-names.txt", mode="r", encoding="utf-8").read().splitlines()
ReadMe = open("./README.md", mode="r", encoding="utf-8").read()

def GetReadMe():
    return ReadMe


def getRandomNumber(start=0, end=1):
    return randrange(start, end + 1)

def Seprator():
    result = "." if getRandomNumber() == 1 else "_"
    return result

def getDate():
    return getRandomNumber(start=1, end=date.today().year)

def getNameOfMales():
    return MaleFirstNames[getRandomNumber(0, len(MaleFirstNames) - 1)]

def getNameOfFemales():
    return FemaleFirstNames[getRandomNumber(0, len(FemaleFirstNames) - 1)]

def getName(flag=0):
    name = None

    if flag == 0:
        num = getRandomNumber(0, 2)
        if num == 0:
            return getNameOfMales()
        elif num == 1:
            return getNameOfFemales()
        else:
            return ""
    elif flag == 1:
        num = getRandomNumber(0, 1)
        if num == 0:
            return getNameOfMales()
        else:
            return ""
    else:
        num = getRandomNumber(0, 1)
        if num == 0:
            return getNameOfFemales()
        else:
            return ""


def getLastName():
    return LastNames[getRandomNumber(0, len(LastNames) - 1)]

# 0 -> both
# 1 -> male
# 2 -> female

def CreateUser(flag=0):
    user = getName(flag=flag)
    user += Seprator()
    user += LastNames[getRandomNumber(0, len(LastNames) - 1)]
    user += str(getDate())
    return user


def CreateSeveralUser(count=1, gender=0):
    users = set()

    while len(users) != count:
        for user in range(count):
            users.add(CreateUser(flag=gender))
    
    return list(users)
