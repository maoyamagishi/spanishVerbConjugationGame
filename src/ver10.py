#class名とファイル名が一致しているためこう書かないと暗黙的にファイルがimportされる
from problemMaker import ProblemMaker as pm
from modesetDialogue import modeSetter
from time import time
class handler():
    def __init__(self) -> None:
        pass
    
    def initialize(self) -> None:
        self.score = 0
        mdsetter = modeSetter()
        self.gamemode = mdsetter.dict
        print(self.gamemode)
        plbmMake = pm
        plbmMake.IF(plbmMake,self.gamemode)
        self.qa = plbmMake.qaset
        
    def manage(self):
        self.initialize()
        while True:
            starttime = time()
            for ii in range(len(self.qa)):
                print(self.qa[ii][0])
                self.judge(self.qa[ii][1])
            print(f"your score is {self.score} / {len(self.qa)}")
            endtime = time()
            print(f"your time record was {endtime - starttime}")
            print(f"{(endtime-starttime)/len(self.qa)}sec/word")
            handler.finishDialogue()
            ans = input()
            if ans == "y":
                self.qa = pm.shuffle(self.qa)
                self.score =0
            elif ans == "n":
                print("Do you want to leave game?")
                ans = input()
                if ans == "y":
                    handler.cls()
                    break
                elif ans =="n":
                    self.initialize()
                
    def judge(self,ans):
        wrd = input()
        if wrd == ans:
            print("correct!")
            self.score +=1
        else:
            print("wrong!")
            print(f"anser->{ans}")
            
    def cls():
        print("プログラムを終了します")
        
    def finishDialogue():
        print("Do you want to try again?")
            
if __name__=='__main__':
    hd = handler()
    hd.manage()