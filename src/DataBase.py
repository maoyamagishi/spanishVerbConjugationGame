import json
class DataBase():
    personword = ["1人称","2人称","3人称"]
    sinpluword = ["単数","複数"]
    tenseword = ["現在形","点過去形","未来形"]
    tensetpl = ("present","preterite","future")
    def __init__(self) -> None:
        pass
    
    def jsnreader(wrd)->dict:
        print(wrd)
        with open(r"C:\mywrks\verbConjugation\src\json\path.json","r",encoding="utf-8") as jsnfl1:
            js1 = json.load(jsnfl1)
            pth = js1[wrd]["path"]
        with open(pth,"r",encoding="utf-8")as jsnfl2:
            js2 = json.load(jsnfl2)
        return js2
    
    def lst2qa(inputlst:list)->list:
        out = []
        for ii in range(len(inputlst)):
            if inputlst[ii]["pbtype"] == 0: #日本語で出題
                tense = DataBase.tenseword[inputlst[ii]["tense"]]  #時制typeの取得
                person = inputlst[ii]["personint"]
                js = DataBase.jsnreader(inputlst[ii]["verb"])#1つの動詞を抜き出し
                vrb = js["infinitive"]
                psn = DataBase.personword[person%3]
                sp = DataBase.sinpluword[person//3]
                question = str(vrb+"を"+psn+sp+tense+"にしてください")
                answer = js[DataBase.tensetpl[inputlst[ii]["tense"]]]["conjugation"][person]

            # for ii in range(6):
            #     self.verb.append(js[self.tensetpl[tense]]["conjugation"][ii])
            # elif pbtyp["gametype"] == 1:#変換問題
            #     tense1 = pbtyp["tense1"]
            #     tense2 = pbtyp["tense2"]
            #     for ii in range(6):
            #         pair = []
            #         pair.append(js[self.tensetpl[tense1]]["conjugation"][ii])
            #         pair.append(js[self.tensetpl[tense2]]["conjugation"][ii])
            #         self.verb.append(pair)
            out.append([question,answer])
        return out