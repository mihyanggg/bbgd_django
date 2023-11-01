from pyTraning05 import 냉장고정리업무

class 업무() :
    아침업무유무 = False
    
    def 아침업무체크(self):
        self.아침업무유무 = True
    
    def 아침업무(self, 상자):
        냉장고정리업무(상자)
        self.아침업무체크()

출근 = True
if 출근 : 
    상자 = ["콩", "사과", "배", "아이스크림", "황도", "두부"]
    mimi_업무 = 업무() # for check
    print(mimi_업무.아침업무유무)
    mimi_업무.아침업무(상자) # for check
    print(mimi_업무.아침업무유무)