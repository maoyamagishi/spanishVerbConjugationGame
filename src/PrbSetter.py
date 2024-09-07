class PrbSetter():
    personword = ["1人称","2人称","3人称"]
    sinpluword = ["単数","複数"]
    tenseword = ["現在形","点過去形","未来形"]
    def __init__(self) -> None:
        pass
        
    @classmethod
    def inf2IF(self,num,mode):
        psn = self.personword[num%3]
        sp = self.sinpluword[num//3]
        tns = self.tenseword[mode["tense"]]
        vrb = mode["verb"] 
        print(f"{vrb}を{psn}{sp}{tns}にしてください")        
        
    @classmethod
    def conj2conjIF(self,pres,mode): #argは呼び出し側のselfを受ける
        tns = self.tenseword[mode["tense2"]]
        print(f"{pres}を{tns}にしてください")