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
        if pbtyp["gametype"] == 0: #日本語で出題
            tense = pbtyp["tense"]  #時制typeの取得
            for ii in range(6):
                self.verb.append(js[self.tensetpl[tense]]["conjugation"][ii])
        elif pbtyp["gametype"] == 1:#変換問題
            tense1 = pbtyp["tense1"]
            tense2 = pbtyp["tense2"]
            for ii in range(6):
                pair = []
                pair.append(js[self.tensetpl[tense1]]["conjugation"][ii])
                pair.append(js[self.tensetpl[tense2]]["conjugation"][ii])
                self.verb.append(pair)
                
    def datMaker(self)->list:
        out = sample(self.rawdat,len(self.rawdat))
        return out
    
    def jsnreader(wrd)->dict:
        print(wrd)
        with open(r"C:\mywrks\verbConjugation\src\json\path.json","r",encoding="utf-8") as jsnfl1:
            js1 = json.load(jsnfl1)
            pth = js1[wrd]["path"]
        with open(pth,"r",encoding="utf-8")as jsnfl2:
            js2 = json.load(jsnfl2)
            
        return js2