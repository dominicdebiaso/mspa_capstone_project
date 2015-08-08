import threading
from GoogleCode import GetGoogleSearchResult

class myThread (threading.Thread):
    def __init__(self, threadID, name, q, multiThreadMotor):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
        self.multiThreadMotor = multiThreadMotor

    def run(self):
        self.process_data(self.name, self.q)

    def process_data(self,threadName, q):
        while not self.multiThreadMotor.exitFlag:
            self.multiThreadMotor.queueLock.acquire()
    
            if not self.multiThreadMotor.workQueue.empty():
                self.element = self.q.get()
                self.multiThreadMotor.queueLock.release()
                self.multiThreadMotor.done = self.multiThreadMotor.done + 1
                print self.multiThreadMotor.done
                self.treat()

            else:
                self.multiThreadMotor.queueLock.release()
    
    def treat(self):
        try:
            if not self.multiThreadMotor.exitFlag == 1:
                res= GetGoogleSearchResult(self.element)
                if res == 0:
                    raise Exception
                self.multiThreadMotor.result.append(res)
        except Exception as e:
            print e
            self.multiThreadMotor.result.append(0)
            self.multiThreadMotor.error  = self.multiThreadMotor.error + 1
            
            if self.multiThreadMotor.error > 20:
                print "Quitting the program"
                self.multiThreadMotor.exitFlag = 1
                