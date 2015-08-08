import threading
import Queue
from ThreadClass import myThread
from Input import GetInput
from Writer import writeFile


class ThreadMotor():
    def __init__(self, threadNumber, listTask):
        self.result = []
        self.done = 0
        self.threadList = range(0,threadNumber)
        self.queueLock = threading.Lock()
        self.workQueue = Queue.Queue()
        self.threads = []
        self.threadID = 1
        self.exitFlag = 0
        #Add element into Queue Object
        self.queueLock.acquire()
        for element in listTask:
            self.workQueue.put(element)
        self.queueLock.release()
        self.error = 0
    
    def addElement(self, element):
        self.queueLock.acquire()
        self.workQueue.put(element)
        self.queueLock.release()
    
        
    def launch(self):
        for tName in self.threadList:
            thread = myThread(self.threadID, tName, self.workQueue, self)
            thread.start()
            self.threads.append(thread)
            self.threadID += 1
                
        while (not self.workQueue.empty()) and self.exitFlag == 0:
            pass
               
        # Notify threads it's time to exit
        self.exitFlag = 1
        
        for t in self.threads:
            t.join()

inputFile = "scrape2.xlsx"

try:
    liste = GetInput(inputFile)
except Exception as e:
    print 'Error with reading input'
    print e

motor = ThreadMotor(20, liste)

try:
    motor.launch()
except:
    pass
finally:
    writeFile(inputFile, motor.result)