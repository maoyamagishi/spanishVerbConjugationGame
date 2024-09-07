import json
class modeSetter():    
    def __init__(self) -> None:
        with open(r"C:\mywrks\verbConjugation\src\json\dialogue.json","r",encoding="utf-8") as jfle:
            js = json.load(jfle)
        
        self.gamemode = []
        self.props = []
        self.dict = {}
        routename = "route0"
        pos = 0
        while True:
            try:
                print(js[routename][str(pos)]["text"])
                self.props.append(js[routename][str(pos)]["prop"])
            except KeyError:
                pass
                
            ac = int(input())
            self.gamemode.append(ac)
            if ac == 0:
                try:
                    hoge = js[routename][str(pos)]["brs"]
                    break
                except KeyError:
                    pass
                pos += 1
            else:
                try:
                    hoge = js[routename][str(pos)]["brs"]
                    break
                except KeyError:
                    pass
                key = "to" + str(ac) 
                routename = js[str(routename)][str(pos)][str(key)]
                # print(routename)
                pos = 0
        print(js["end"])
        ac = int(input())
        self.gamemode.append(ac)
        print(self.gamemode)
        print(self.props)
        self.tuplMaker()
        print(self.dict)
    
    def num2verbstr(arg,num):
        vp = ("estar","ser")
        return [vp[num]]
    
    def tuplMaker(self):
        for ii in range(len(self.props)):
            self.dict[str(self.props[ii])] = self.gamemode[ii]
        self.dict["pblmwrds"] = self.num2verbstr(self.gamemode[len(self.gamemode) -1])
        self.dict["tenserange"] = [self.dict["tenserange"]]
        print(self.dict)
    
#md = modeSetter()