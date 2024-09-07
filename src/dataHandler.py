from random import sample
import json
class dat():
    def __init__(self)->None:
        self.verb = []
        self.rawdat = [0,1,2,3,4,5]
        self.tensetpl = ("present","preterite","future")
    
    def readInterface(self,pbtyp):
        js = dat.jsnreader(pbtyp["verb"])
        print(type(pbtyp))
        tense = pbtyp["tense"]  #時制typeの取得
        if pbtyp["type"] == 0: #日本語で出題
            for ii in range(6):
                self.verb.append(js[self.tensetpl[tense]]["conjugation"][ii])
        elif pbtyp["type"] == 1:#現在形->変換問題
            for ii in range(6):
                pair = []
                pair.append(js["present"]["conjugation"][ii])
                pair.append(js[self.tensetpl[tense]]["conjugation"][ii])
                self.verb.append(pair)
                
    def datMaker(self)->list:
        out = sample(self.rawdat,len(self.rawdat))
        return out
    
    def jsnreader(wrd)->dict:
        if wrd == "estar":
            with open(r"C:\mywrks\verbConjugation\src\estar.json","r",encoding="utf-8") as jsnfl:
                js = json.load(jsnfl)
        elif wrd == "ser":
            with open(r"C:\mywrks\verbConjugation\src\ser.json","r",encoding="utf-8") as jsnfl:
                js = json.load(jsnfl)
        return js