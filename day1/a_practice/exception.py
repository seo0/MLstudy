#day1과는 상관x
#장점 : 원래는 error가 나면 그시점부터 코드가 멈춘다. 이렇게 예외처리를 하면 코드가 안멈춘다. 어디서 문제가 생겼는지 쉽게 알수있고 디버깅 가능하다. 프로그램의 안정성을 높이기 위해 사용된다.
#4/0
try:
    4/0
except ZeroDivisionError as e: #이쪽 에러들은 실제 에러가 났을때 나오는 메세지들이다.
    print(e)
print("hello world1")

try :
    f=open("foo.txt",'r')
except FileNotFoundError as e:
    print(e)
else:
    data = f.read()
    print("hello world2")
finally: #에러에 상관없이 실행한다.
    f.close()
    print("hello world3")

try:
    f=open("없는 파일",'r')
except FileNotFoundError:
    if __name__ == '__main__':
        pass #일부러 에러를 회피한다

# 오류를 일부러 발생시키기 raise
# 코드의 안정성을 높이는게ㅔ 중요하다 예를들어 1만줄짜리 코드가 있으면, 어디가 에러인지 잡기가 쉽지 않다. / 남의 코드 볼때 / 협업할때

class Bird:
    def fly(self):
        pass
        #raise NotImplementedError
#상속받아서 반드시 fly라는 함수를 구현해라! 아니면 error가 뜬다.
class Eagle(Bird):
    pass

eagle =Eagle()
eagle.fly()
