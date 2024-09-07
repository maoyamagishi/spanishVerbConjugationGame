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
        
        self.pblmrange = inputarg["tenserange"]#list
        self.gametypemaster(self)
                
    def gametypemaster(self)-> None:
        _pblmproplst = []
        _vrblst = []
        _tenselst = []
        self.qaset = []
        if self.gametype == 0:#日本語出題6×n問
            self.pblmwrdlst = self.modedict["pblmwrds"]#list
            _pblmproplst= self.filllst({"pbtype":0},6*len(self.pblmwrdlst)*len(self.pblmrange)).copy()
            #print(f"_pblmprolst={_pblmproplst}")
            for ii in range(len(self.pblmwrdlst)): 
                _verb = self.modedict["pblmwrds"][ii]
                for jj in range(6*len(self.pblmrange)):
                    _vrblst.append(_verb)
            _adhoc = []
            for ii in range(len(self.pblmrange)):
                _tense = self.modedict["tenserange"][ii]
                for jj in range(6):
                    _adhoc.append(_tense)#000000or111111
            for ii in range(len(self.pblmwrdlst)):
                for jj in range(len(_adhoc)):
                    _tenselst.append(_adhoc[jj])
            for ii in range(6*len(self.pblmwrdlst)*len(self.pblmrange)): 
                _pblmproplst[ii]["personint"] = 0
            for ii in range(6*len(self.pblmwrdlst)*len(self.pblmrange)): 
                _pblmproplst[ii]["verb"]=(_vrblst[ii])
                _pblmproplst[ii]["tense"]=(_tenselst[ii])
                _pblmproplst[ii]["personint"] = ii%6
            
        elif self.gametype == 1:#変換する問題
            _verbset =[]
            _verblst1 = self.modedict["verb1"]
            _verblst2 = self.modedict["verb2"]
            for ii in range(len(_verblst1)):
                for jj in range(len(_verblst2)):
                    if _verblst1[ii] == _verblst2[jj]:
                        pass
                    else:
                        _verbset.append([_verblst1[ii],_verblst2[jj]])
                        
            print(_verbset)
            _pblmproplst= self.filllst({"pbtype":1},6*len(_verbset)*len(self.pblmrange)).copy()
            #print(_pblmproplst)
            for ii in range(len(_verbset)): 
                _verb = _verbset[ii]
                for jj in range(6*len(self.pblmrange)):
                    _vrblst.append(_verb)
            _adhoc = []
            for ii in range(len(self.pblmrange)):
                _tense = self.modedict["tenserange"][ii]
                for jj in range(6):
                    _adhoc.append(_tense)#000000or111111
            for ii in range(len(_verbset)):
                for jj in range(len(_adhoc)):
                    _tenselst.append(_adhoc[jj])
            for ii in range(6*len(_verbset)*len(self.pblmrange)): 
                #print(_pblmproplst)
                _pblmproplst[ii]["personint"] = 0
            for ii in range(6*len(_verbset)*len(self.pblmrange)): 
                _pblmproplst[ii]["verb"]=(_vrblst[ii])
                _pblmproplst[ii]["tense"]=(_tenselst[ii])
                _pblmproplst[ii]["personint"] = ii%6

        
        elif self.gametype == 2:#gametype1の逆問題
            self.pblmwrdlst = self.modedict["pblmwrds"]#list
            _pblmproplst= self.filllst({"pbtype":2},6*len(self.pblmwrdlst)*len(self.pblmrange)).copy()
            #print(f"_pblmprolst={_pblmproplst}")
            for ii in range(len(self.pblmwrdlst)): 
                _verb = self.modedict["pblmwrds"][ii]
                for jj in range(6*len(self.pblmrange)):
                    _vrblst.append(_verb)
            _adhoc = []
            for ii in range(len(self.pblmrange)):
                _tense = self.modedict["tenserange"][ii]
                for jj in range(6):
                    _adhoc.append(_tense)#000000or111111
            for ii in range(len(self.pblmwrdlst)):
                for jj in range(len(_adhoc)):
                    _tenselst.append(_adhoc[jj])
            for ii in range(6*len(self.pblmwrdlst)*len(self.pblmrange)): 
                _pblmproplst[ii]["personint"] = 0
            for ii in range(6*len(self.pblmwrdlst)*len(self.pblmrange)): 
                _pblmproplst[ii]["verb"]=(_vrblst[ii])
                _pblmproplst[ii]["tense"]=(_tenselst[ii])
                _pblmproplst[ii]["personint"] = ii%6
        _sampledpblmlst = sample(_pblmproplst,len(_pblmproplst))
        #print(f"sampled{_sampledpblmlst}")
        print(_sampledpblmlst)
        self.qaset = db.lst2qa(_sampledpblmlst)
                
    def filllst(arg:any,quantity:int):
        lst = []
        for ii in range(quantity):
            lst.append(arg.copy())#copyしないとアドレスが全て同じになる
        return lst
    
    def shuffle(lst:list)->list:
        outlst = sample(lst,len(lst))
        return outlst