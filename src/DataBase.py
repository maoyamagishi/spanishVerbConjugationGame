import json
class DataBase():
    personword = ["1人称","2人称","3人称"]
    sinpluword = ["単数","複数"]
    tenseword = ["現在形","点過去形","線過去形","未来形"]
    tensetpl = ("present","preterite","imperfect","future")
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
                
            elif inputlst[ii]["pbtype"] == 1:
                tense = DataBase.tenseword[inputlst[ii]["tense"]]  #時制typeの取得
                person = inputlst[ii]["personint"]
                js1 = DataBase.jsnreader(inputlst[ii]["verb"][0])#1つの動詞を抜き出し
                js2 = DataBase.jsnreader(inputlst[ii]["verb"][1])#1つの動詞を抜き出し
                vrbinf = js1["infinitive"]

                question = str(vrbinf+"を"+js2[DataBase.tensetpl[inputlst[ii]["tense"]]]["conjugation"][person]+"と同じ形にしてください")
                answer = js1[DataBase.tensetpl[inputlst[ii]["tense"]]]["conjugation"][person]
                
            elif inputlst[ii]["pbtype"] == 2:#０の逆問題
                tense = DataBase.tenseword[inputlst[ii]["tense"]]  #時制typeの取得
                person = inputlst[ii]["personint"]
                js = DataBase.jsnreader(inputlst[ii]["verb"])#1つの動詞を抜き出し
                vrbinf = js["infinitive"]
                qst = js[DataBase.tensetpl[inputlst[ii]["tense"]]]["conjugation"][person]
                question = str(f"{qst}の不定形は？")
                answer = vrbinf

            out.append([question,answer])
        return out