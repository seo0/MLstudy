#점프 투 파이썬 클래스
class calculator:
    def __init__(self):
        self.first=0
        self.second =0
    def setNum(self,first,second):
        self.first = first
        self.second = second
    def mul(self):
        return self.first+self.second
    def minus(self):
        return self.first-self.second
    def multiple(self):
        return self.first*self.second
    def divide(self):
        if(self.second ==0):
            return "분모가 0"
        else:
            return self.first/self.second
print("hello world in class")