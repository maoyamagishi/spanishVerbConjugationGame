from DataBase import DataBase as db
from random import sample

class ProblemMaker():
    def __init__(self,type) -> None:
        pass
    
    def IF(self,inputarg:dict) ->None:
        """This function will be called only when Manager order 
        new problem. Therefore when instance of ProblemMaker is generated, 
        this function will work.
        
        Args:
            self(obj):The object of ProblemMaker
            inputarg(dict):The type of problems, such as tense, how many problems. 
            are needed. Given by user inputs.
        """
        self.modedict = inputarg
        self.gametype = inputarg["gametype"]
        self.pblmwrdlst = inputarg["pblmwrds"]#list
        self.pblmrange = inputarg["tenserange"]#list
        #print(inputarg)
        self.gametypemaster(self)
                
    def gametypemaster(self)-> None:
        _pblmproplst = []
        _vrblst = []
        _tenselst = []
        self.qaset = []
        if self.gametype == 0:#日本語出題6×n問
            _pblmproplst= self.filllst({"pbtype":0},6*len(self.pblmwrdlst)*len(self.pblmrange)).copy()
            print(f"_pblmprolst={_pblmproplst}")
            for ii in range(len(self.pblmwrdlst)): 
                _verb = self.modedict["pblmwrds"][ii]
                for jj in range(6*len(self.pblmrange)):
                    #for kk in range(6):
                    _vrblst.append(_verb)
            for ii in range(len(self.pblmrange)):
                _tense = self.modedict["tenserange"][ii]
                for jj in range(6*len(self.pblmwrdlst)):
                    _tenselst.append(_tense)
            print(f"_vrblst={_vrblst}")
            print(f"_tenselst={_tenselst}")
            for ii in range(6*len(self.pblmwrdlst)*len(self.pblmrange)): 
                _pblmproplst[ii]["personint"] = 0
            for ii in range(6*len(self.pblmwrdlst)*len(self.pblmrange)): 
                #print(ii)
                _pblmproplst[ii]["verb"]=(_vrblst[ii])
                _pblmproplst[ii]["tense"]=(_tenselst[ii])
                _pblmproplst[ii]["personint"] = ii%6
                #print(_pblmproplst)
            
        # elif self.gametype == 1:#変換する問題
        #     _pblmtypelst.copy(self.filllst(1,6))
        #     _verb1 = self.modedict("verb1")
        #     _verb2 = self.modedict("verb2")
        #     _vrblst.copy(self.filllst(_verb,6))
        #     _tense1 =self.modedict["tense1"]
        #     _tenselst.copy(self.filllst(_tense1,6))
        
        _sampledpblmlst = sample(_pblmproplst,len(_pblmproplst))
        print(f"sampled{_sampledpblmlst}")
        self.qaset = db.lst2qa(_sampledpblmlst)
                
    def filllst(arg:any,quantity:int):
        lst = []
        for ii in range(quantity):
            lst.append(arg.copy())#copyしないとアドレスが全て同じになる
        return lst