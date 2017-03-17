#make the relationship class
#관계형 클래스 구축
class fruitSeller:

    def __init__(self, apple, money, price):
        self._numberOfApple = apple
        self._money = money
        self._price = price

    def SaleApple(self,payment):
        payment == BuyApple[payment]

        pass
        #예외처리하기, 가진개수보다 더 많이 살때는 가진것만 다팔기. 거스름돈 반환

    def printApple(self):
        print("==========판매자==================")
        print("남은 사과 개수",int(self._numberOfApple))
        print("금일 판매 수익 : ",int(self._money))



class fruitBuyer:
    def __init__(self,money):
        self.myMoney = money
        self.numberOfApple = 0

    def BuyApple(self,FruitSeller,payment):

        pass
        #BUYAPPLE만 호출해서 판매자의 사과개수도 줄이기

    def printResult(self):
        print("==========구매자==================")
        print("현재 잔액 : ",int(self.myMoney))
        print("사과 개수 : ",int(self.numberOfApple))

if __name__ == '__main__':
    a = fruitSeller(100,0,10)
    b = fruitBuyer(10000)
    b.BuyApple(a,500)
    a.printApple()
    b.printResult()