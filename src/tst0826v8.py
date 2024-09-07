#class名とファイル名が一致しているためこう書かないと暗黙的にファイルがimportされる
from problemMaker import ProblemMaker as pm
#from dataHandler import dat
from modesetDialogue import modeSetter
class handler():
    def __init__(self) -> None:
        pass
    
    def initialize(self) -> None:
        #self.dt = dat()
        #self.order = dt.datMaker()
        mdsetter = modeSetter()
        self.gamemode = mdsetter.dict
        print(self.gamemode)
        plbmMake = pm
        plbmMake.IF(plbmMake,self.gamemode)
        self.qa = plbmMake.qaset
        
    def manage(self):
        self.initialize()
        while True:
            for ii in range(len(self.qa)):
                print(self.qa[ii][0])
                self.judge(self.qa[ii][1])
            handler.finishDialogue()
            ans = input()
            if ans == "y":
                pass
            elif ans == "n":
                handler.cls()
                break
                
    def judge(self,ans):
        wrd = input()
        if wrd == ans:
            print("correct!")
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