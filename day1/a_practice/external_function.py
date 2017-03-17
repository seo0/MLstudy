#jump to python 빈출 외부 라이브러리
#전 세계의 파이썬 사용자들이 만든 유용한 프로그램들을 모아 놓은 것이 파이썬 라이브러리이다. 원하는 정보를 찾아보는 곳.
#모든 라이브러리를 다 알 필요는 없고 어떤 일을 할 때 어떤 라이브러리를 사용해야 한다는 정도만 알면 된다.
#그러기 위해서 어떤 라이브러리들이 존재하고 어떻게 사용되는지 알아야 할 필요가 있다.

"""
sys
시스템 입출력 관련되어있는 라이브러리

pickle 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈

os
환경변수나 디렉토리, 파일등의 os자원을 제어 가능하게 한다.
"""
"""
#데이터 처리할때 편하다. 내가 쓰던 자료형을 그대로 다시 옮겨서 사용하고 싶을때.
import pickle
f=open("test.txt","rb")
data = {1:'python',2:"you need"}
pickle.dump(data,f)
f.close()

f=open("test.txt",'rb')
data = pickle.load(f)
print(data)
f.close()
찾아보고 써보기.
"""


"""
shutil 파일 복사해주는
shutil.copy("src.txt","Dst.txt")

glob
특정 디렉토리에 있는 파일 이름을 모두 알아야 할때
import glob
glob.glob("C:/Python/q")
#제목들을 리스트에 넣어서 한꺼번에 처리가능
"""


"""
time함수
time.time() ->1970년 1월 1일 0시 0분 0초 기준으로 지난 초단위로 리턴
time.localtime(time.time()) #년 월 일 시 분 초로 반환해준다.

time.strftime('출력할 형식 포맷 코드', time.location(time.time()))
여러가지 포맷코드를 제공한다. 맞는 코드로 바꿔서 필요할때 찾아서 보면 될듯
time.strftime('%x',time.localtime(time.time()))
time.sleep(10)
"""
"""
import calendar
print(calendar.calendar(2015))

print(calendar.prcal(2015))
print(calendar.prmonth(2015,12))
print(calendar.weekday(2015.12.31)
#0 월 1 화 2 수 3 목 4 금 5 토 6 일
print(calendar.monthrange(2015,12)
#몇일까지 있는지를 (1,31)이렇게 반환
"""

"""
#random
#난수 발생시 많이 쓰인다.
import random
#(0에서 1사이 실수 반환)
print(random.random())
prinit(random.randomint(1,10))

"""
"""
import random
def random_pop(data):
    number = random.randint(0,len(data)-1)
    if __name__ == '__main__':
        return data.pop(number)#pop 은 반환하고 list에서 없앤다
def random_pop2(data):
    number = random.choice(data) #임의로 한개를 고른다.
    data.remove(number)
    return number

data=list(range(1,6))
while data: # []는 false이다.
    print(random_pop(data))
"""
"""
import random
data = [1,2,3,4,5]
random.shuffle(data)
print(data)
#랜덤으로 섞어준다. 데이터 처리할때 유용할듯 test 데이터 만들때
"""
"""
#웹관련 코드
import webbrowser
webbrowser.open("http://google.com")
"""