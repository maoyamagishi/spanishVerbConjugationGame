#class名とファイル名が一致しているためこう書かないと暗黙的にファイルがimportされる
from PrbSetter import PrbSetter 
from dataHandler import dat
from modesetDialogue import modeSetter
class handler():
    def __init__(self) -> None:
        dt = dat()
        self.order = dt.datMaker()
        mdsetter = modeSetter()
        self.gamemode = mdsetter.dict
        print(self.gamemode)
        dt.readInterface(self.gamemode)
        self.lst = dt.verb
        self.pbsetter = PrbSetter
        
    def manage(self):
        while True:
            print(self.lst)
            print(self.gamemode)
            if self.gamemode["gametype"] == 0:
                for ii in range(len(self.lst)):
                    self.pbsetter.inf2IF(self.order[ii],self.gamemode)
                    handler.judge(self.lst[self.order[ii]])
            elif self.gamemode["gametype"] == 1:
                for ii in range(len(self.lst)):
                    self.pbsetter.conj2conjIF(self.lst[self.order[ii]][0],self.gamemode)
                    handler.judge(self.lst[self.order[ii]][1])
            handler.finishDialogue()
            ans = input()
            if ans == "y":
                handler.__init__(self)
            elif ans == "n":
                handler.cls()
                break
                    
    def judge(ans):
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