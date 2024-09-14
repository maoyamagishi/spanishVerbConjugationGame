class modeSetter():    
    def __init__(self) -> None:
        self.dict = {}
        #問題タイプを選択
        print("問題タイプを選択してください。\n 日本語で出題->0, 同じ動詞の中で時制を変換する問題->1")
        while True:
            ans = int(input())
            if any([ans == 0,ans == 1,ans == 2,ans == 3]):
                self.dict["gametype"] = ans
                break
            else:
                print("invalid input")
                
        if self.dict["gametype"] == 0 or self.dict["gametype"] == 2:
            _tenselst = []
            _verblst = []
            while True:
                print("練習したい時制を追加してください。\n 現在形->0, 点過去形->1, 線過去形->2,未来形->3")
                print(f"現在の設定->{_tenselst}")
                ans = int(input())
                if any([ans == 0,ans == 1,ans == 2,ans == 3,ans == 4,ans == 5,ans == 6]):
                    _tenselst.append(ans)
                    print("さらに追加しますか？ y or n")
                    ans = input()
                    if ans == "y":
                        pass
                    else:
                        self.dict["tenserange"] = _tenselst
                        break
                else:
                    print("invalid input")
                    
            while True:
                print("練習したい動詞を追加してください。\n estar->0, ser->1, tener'->2, ir->3, hablar->4, comer->5, vivir->6")
                print(f"現在の設定->{_verblst}")
                ans = int(input())
                if type(int(ans)) == int:
                    _verblst.append(self.num2verbstr(ans))
                    print("さらに追加しますか？ y or n")
                    ans = input()
                    if ans == "y":
                        pass
                    else:
                        self.dict["pblmwrds"] = _verblst
                        break
                else:
                    print("invalid input")
                    
        else:#gametype =1
            _beforevrb = []
            _aftervrb = []
            _tenselst = []
            while True:
                print("練習したい動詞を追加してください。\n estar->0, ser->1, tener'->2, ir->3, hablar->4, comer->5, vivir->6")
                print(f"現在の設定->{_beforevrb}")
                ans = int(input())
                if type(int(ans)) == int:
                    _beforevrb.append(self.num2verbstr(ans))
                    print("さらに追加しますか？ y or n")
                    ans = input()
                    if ans == "y":
                        pass
                    else:
                        self.dict["verb1"] = _beforevrb
                        break
                else:
                    print("invalid input")
            
            while True:
                print("キーとして使う動詞を追加してください。\n estar->0, ser->1, tener'->2, ir->3, hablar->4, comer->5, vivir->6")
                print(f"現在の設定->{_aftervrb}")
                ans = int(input())
                if type(int(ans)) == int:
                    _aftervrb.append(self.num2verbstr(ans))
                    print("さらに追加しますか？ y or n")
                    ans = input()
                    if ans == "y":
                        pass
                    else:
                        self.dict["verb2"] = _aftervrb
                        break
                else:
                    print("invalid input")
                
            while True:
                print("練習したい時制を追加してください。\n 現在形->0, 点過去形->1, 線過去形->2,未来形->3")
                print(f"現在の設定->{_tenselst}")
                ans = int(input())
                if any([ans == 0,ans == 1,ans == 2,ans == 3,ans == 4,ans == 5,ans == 6]):
                    _tenselst.append(ans)
                    print("さらに追加しますか？ y or n")
                    ans = input()
                    if ans == "y":
                        pass
                    else:
                        self.dict["tenserange"] = _tenselst
                        break
                else:
                    print("invalid input")
                

    
    def num2verbstr(arg,num):
        vp = ("estar","ser","tener","ir","hablar","comer","vivir")
        return vp[num]
    
#md = modeSetter()