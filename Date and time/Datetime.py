import random 
import time
def getRandomDate(startDate , endDate):
    print("Printing random date between",startDate," and",endDate)
    randomGenerator=random.random()
    dateformat='%d-%m-%Y'
    starttime=time.mktime(time.strptime(startDate,dateformat))
    endtime=time.mktime(time.strptime(endDate,dateformat))
    randomTime=starttime+randomGenerator * (endtime-starttime)
    randomDate=time.strftime(dateformat,time.localtime(randomTime))
    return randomDate
print("Random Date = ", getRandomDate('1-1-2024','12-12-2024'))
