from PrbSetter import PrbSetter #class名とファイル名が一致しているためこう書かないと暗黙的にファイルがimportされる
from dataHandler import dat
class handler():
    def __init__(self) -> None:
        dt = dat()
        self.order = dt.datMaker()
        mdsetter = modeSetter()
        self.gamemode = mdsetter.mode
        print(self.gamemode)
        dt.readInterface(self.gamemode)
        self.lst = dt.verb
        
    def manage(self):
        while True:
            print(self.lst)
            print(self.gamemode)
            if self.gamemode["type"] == 0:
                for ii in range(len(self.lst)):
                    PrbSetter.inf2IF(self.order[ii],self.gamemode)
                    handler.judge(self.lst[self.order[ii]])
            elif self.gamemode["type"] == 1:
                for ii in range(len(self.lst)):
                    PrbSetter.conj2conjIF(self.lst[self.order[ii]][0],self.gamemode)
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
            

class modeSetter():
    def __init__(self) :
        print("select verb 0.estar 1.ser")
        __verbnum = int(input())
        print("select problem type")
        print("現在形->0, 現在形２過去形->1")
        __innum = int(input())
        self.mode = modeSetter.modeMap(__innum)
        self.mode["verb"] = self.num2verbstr(__verbnum)
        
    def modeMap(input):
        mp = ({"type":0,"tense":0},{"type":0,"tense":1},{"type":0,"tense":2},{"type":1,"tense":1},{"type":1,"tense":2})
        return mp[input]
    
    def num2verbstr(arg,num):
        vp = ("estar","ser")
        return vp[num]
    
if __name__=='__main__':
    hd = handler()
    hd.manage()